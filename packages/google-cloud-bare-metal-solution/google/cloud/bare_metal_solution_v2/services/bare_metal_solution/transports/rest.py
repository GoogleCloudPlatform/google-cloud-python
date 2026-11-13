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

from google.cloud.bare_metal_solution_v2._compat import transcode_request
from google.cloud.bare_metal_solution_v2.types import (
    instance,
    lun,
    network,
    nfs_share,
    osimage,
    provisioning,
    ssh_key,
    volume,
    volume_snapshot,
)
from google.cloud.bare_metal_solution_v2.types import instance as gcb_instance
from google.cloud.bare_metal_solution_v2.types import network as gcb_network
from google.cloud.bare_metal_solution_v2.types import nfs_share as gcb_nfs_share
from google.cloud.bare_metal_solution_v2.types import ssh_key as gcb_ssh_key
from google.cloud.bare_metal_solution_v2.types import volume as gcb_volume
from google.cloud.bare_metal_solution_v2.types import (
    volume_snapshot as gcb_volume_snapshot,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBareMetalSolutionRestTransport

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


class BareMetalSolutionRestInterceptor:
    """Interceptor for BareMetalSolution.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BareMetalSolutionRestTransport.

    .. code-block:: python
        class MyCustomBareMetalSolutionInterceptor(BareMetalSolutionRestInterceptor):
            def pre_create_nfs_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_nfs_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_provisioning_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_provisioning_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_ssh_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ssh_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_volume_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_volume_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_nfs_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_nfs_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_ssh_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_volume_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_detach_lun(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_detach_lun(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_disable_interactive_serial_console(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_interactive_serial_console(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_interactive_serial_console(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_interactive_serial_console(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_evict_lun(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_evict_lun(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_evict_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_evict_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_lun(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_lun(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_nfs_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_nfs_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_provisioning_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_provisioning_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_volume_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_volume_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_luns(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_luns(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_networks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_networks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_network_usage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_network_usage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_nfs_shares(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_nfs_shares(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_os_images(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_os_images(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_provisioning_quotas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_provisioning_quotas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ssh_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ssh_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_volumes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_volumes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_volume_snapshots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_volume_snapshots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rename_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rename_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rename_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rename_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rename_nfs_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rename_nfs_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rename_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rename_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resize_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resize_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_volume_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_volume_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_submit_provisioning_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_submit_provisioning_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_nfs_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_nfs_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_provisioning_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_provisioning_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BareMetalSolutionRestTransport(interceptor=MyCustomBareMetalSolutionInterceptor())
        client = BareMetalSolutionClient(transport=transport)


    """

    def pre_create_nfs_share(
        self,
        request: gcb_nfs_share.CreateNfsShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_nfs_share.CreateNfsShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_nfs_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_create_nfs_share(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_nfs_share

        DEPRECATED. Please use the `post_create_nfs_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_create_nfs_share` interceptor runs
        before the `post_create_nfs_share_with_metadata` interceptor.
        """
        return response

    def post_create_nfs_share_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_nfs_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_create_nfs_share_with_metadata`
        interceptor in new development instead of the `post_create_nfs_share` interceptor.
        When both interceptors are used, this `post_create_nfs_share_with_metadata` interceptor runs after the
        `post_create_nfs_share` interceptor. The (possibly modified) response returned by
        `post_create_nfs_share` will be passed to
        `post_create_nfs_share_with_metadata`.
        """
        return response, metadata

    def pre_create_provisioning_config(
        self,
        request: provisioning.CreateProvisioningConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.CreateProvisioningConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_provisioning_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_create_provisioning_config(
        self, response: provisioning.ProvisioningConfig
    ) -> provisioning.ProvisioningConfig:
        """Post-rpc interceptor for create_provisioning_config

        DEPRECATED. Please use the `post_create_provisioning_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_create_provisioning_config` interceptor runs
        before the `post_create_provisioning_config_with_metadata` interceptor.
        """
        return response

    def post_create_provisioning_config_with_metadata(
        self,
        response: provisioning.ProvisioningConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.ProvisioningConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_provisioning_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_create_provisioning_config_with_metadata`
        interceptor in new development instead of the `post_create_provisioning_config` interceptor.
        When both interceptors are used, this `post_create_provisioning_config_with_metadata` interceptor runs after the
        `post_create_provisioning_config` interceptor. The (possibly modified) response returned by
        `post_create_provisioning_config` will be passed to
        `post_create_provisioning_config_with_metadata`.
        """
        return response, metadata

    def pre_create_ssh_key(
        self,
        request: gcb_ssh_key.CreateSSHKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_ssh_key.CreateSSHKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_ssh_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_create_ssh_key(self, response: gcb_ssh_key.SSHKey) -> gcb_ssh_key.SSHKey:
        """Post-rpc interceptor for create_ssh_key

        DEPRECATED. Please use the `post_create_ssh_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_create_ssh_key` interceptor runs
        before the `post_create_ssh_key_with_metadata` interceptor.
        """
        return response

    def post_create_ssh_key_with_metadata(
        self,
        response: gcb_ssh_key.SSHKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcb_ssh_key.SSHKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ssh_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_create_ssh_key_with_metadata`
        interceptor in new development instead of the `post_create_ssh_key` interceptor.
        When both interceptors are used, this `post_create_ssh_key_with_metadata` interceptor runs after the
        `post_create_ssh_key` interceptor. The (possibly modified) response returned by
        `post_create_ssh_key` will be passed to
        `post_create_ssh_key_with_metadata`.
        """
        return response, metadata

    def pre_create_volume_snapshot(
        self,
        request: gcb_volume_snapshot.CreateVolumeSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_volume_snapshot.CreateVolumeSnapshotRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_volume_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_create_volume_snapshot(
        self, response: gcb_volume_snapshot.VolumeSnapshot
    ) -> gcb_volume_snapshot.VolumeSnapshot:
        """Post-rpc interceptor for create_volume_snapshot

        DEPRECATED. Please use the `post_create_volume_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_create_volume_snapshot` interceptor runs
        before the `post_create_volume_snapshot_with_metadata` interceptor.
        """
        return response

    def post_create_volume_snapshot_with_metadata(
        self,
        response: gcb_volume_snapshot.VolumeSnapshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_volume_snapshot.VolumeSnapshot, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_volume_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_create_volume_snapshot_with_metadata`
        interceptor in new development instead of the `post_create_volume_snapshot` interceptor.
        When both interceptors are used, this `post_create_volume_snapshot_with_metadata` interceptor runs after the
        `post_create_volume_snapshot` interceptor. The (possibly modified) response returned by
        `post_create_volume_snapshot` will be passed to
        `post_create_volume_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_delete_nfs_share(
        self,
        request: nfs_share.DeleteNfsShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        nfs_share.DeleteNfsShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_nfs_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_delete_nfs_share(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_nfs_share

        DEPRECATED. Please use the `post_delete_nfs_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_delete_nfs_share` interceptor runs
        before the `post_delete_nfs_share_with_metadata` interceptor.
        """
        return response

    def post_delete_nfs_share_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_nfs_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_delete_nfs_share_with_metadata`
        interceptor in new development instead of the `post_delete_nfs_share` interceptor.
        When both interceptors are used, this `post_delete_nfs_share_with_metadata` interceptor runs after the
        `post_delete_nfs_share` interceptor. The (possibly modified) response returned by
        `post_delete_nfs_share` will be passed to
        `post_delete_nfs_share_with_metadata`.
        """
        return response, metadata

    def pre_delete_ssh_key(
        self,
        request: ssh_key.DeleteSSHKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ssh_key.DeleteSSHKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_ssh_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def pre_delete_volume_snapshot(
        self,
        request: volume_snapshot.DeleteVolumeSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume_snapshot.DeleteVolumeSnapshotRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_volume_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def pre_detach_lun(
        self,
        request: gcb_instance.DetachLunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcb_instance.DetachLunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for detach_lun

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_detach_lun(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for detach_lun

        DEPRECATED. Please use the `post_detach_lun_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_detach_lun` interceptor runs
        before the `post_detach_lun_with_metadata` interceptor.
        """
        return response

    def post_detach_lun_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for detach_lun

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_detach_lun_with_metadata`
        interceptor in new development instead of the `post_detach_lun` interceptor.
        When both interceptors are used, this `post_detach_lun_with_metadata` interceptor runs after the
        `post_detach_lun` interceptor. The (possibly modified) response returned by
        `post_detach_lun` will be passed to
        `post_detach_lun_with_metadata`.
        """
        return response, metadata

    def pre_disable_interactive_serial_console(
        self,
        request: instance.DisableInteractiveSerialConsoleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        instance.DisableInteractiveSerialConsoleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for disable_interactive_serial_console

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_disable_interactive_serial_console(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for disable_interactive_serial_console

        DEPRECATED. Please use the `post_disable_interactive_serial_console_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_disable_interactive_serial_console` interceptor runs
        before the `post_disable_interactive_serial_console_with_metadata` interceptor.
        """
        return response

    def post_disable_interactive_serial_console_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_interactive_serial_console

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_disable_interactive_serial_console_with_metadata`
        interceptor in new development instead of the `post_disable_interactive_serial_console` interceptor.
        When both interceptors are used, this `post_disable_interactive_serial_console_with_metadata` interceptor runs after the
        `post_disable_interactive_serial_console` interceptor. The (possibly modified) response returned by
        `post_disable_interactive_serial_console` will be passed to
        `post_disable_interactive_serial_console_with_metadata`.
        """
        return response, metadata

    def pre_enable_interactive_serial_console(
        self,
        request: instance.EnableInteractiveSerialConsoleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        instance.EnableInteractiveSerialConsoleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for enable_interactive_serial_console

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_enable_interactive_serial_console(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for enable_interactive_serial_console

        DEPRECATED. Please use the `post_enable_interactive_serial_console_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_enable_interactive_serial_console` interceptor runs
        before the `post_enable_interactive_serial_console_with_metadata` interceptor.
        """
        return response

    def post_enable_interactive_serial_console_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_interactive_serial_console

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_enable_interactive_serial_console_with_metadata`
        interceptor in new development instead of the `post_enable_interactive_serial_console` interceptor.
        When both interceptors are used, this `post_enable_interactive_serial_console_with_metadata` interceptor runs after the
        `post_enable_interactive_serial_console` interceptor. The (possibly modified) response returned by
        `post_enable_interactive_serial_console` will be passed to
        `post_enable_interactive_serial_console_with_metadata`.
        """
        return response, metadata

    def pre_evict_lun(
        self,
        request: lun.EvictLunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lun.EvictLunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for evict_lun

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_evict_lun(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for evict_lun

        DEPRECATED. Please use the `post_evict_lun_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_evict_lun` interceptor runs
        before the `post_evict_lun_with_metadata` interceptor.
        """
        return response

    def post_evict_lun_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for evict_lun

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_evict_lun_with_metadata`
        interceptor in new development instead of the `post_evict_lun` interceptor.
        When both interceptors are used, this `post_evict_lun_with_metadata` interceptor runs after the
        `post_evict_lun` interceptor. The (possibly modified) response returned by
        `post_evict_lun` will be passed to
        `post_evict_lun_with_metadata`.
        """
        return response, metadata

    def pre_evict_volume(
        self,
        request: volume.EvictVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.EvictVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for evict_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_evict_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for evict_volume

        DEPRECATED. Please use the `post_evict_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_evict_volume` interceptor runs
        before the `post_evict_volume_with_metadata` interceptor.
        """
        return response

    def post_evict_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for evict_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_evict_volume_with_metadata`
        interceptor in new development instead of the `post_evict_volume` interceptor.
        When both interceptors are used, this `post_evict_volume_with_metadata` interceptor runs after the
        `post_evict_volume` interceptor. The (possibly modified) response returned by
        `post_evict_volume` will be passed to
        `post_evict_volume_with_metadata`.
        """
        return response, metadata

    def pre_get_instance(
        self,
        request: instance.GetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.GetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_instance(self, response: instance.Instance) -> instance.Instance:
        """Post-rpc interceptor for get_instance

        DEPRECATED. Please use the `post_get_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_instance` interceptor runs
        before the `post_get_instance_with_metadata` interceptor.
        """
        return response

    def post_get_instance_with_metadata(
        self,
        response: instance.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_instance_with_metadata`
        interceptor in new development instead of the `post_get_instance` interceptor.
        When both interceptors are used, this `post_get_instance_with_metadata` interceptor runs after the
        `post_get_instance` interceptor. The (possibly modified) response returned by
        `post_get_instance` will be passed to
        `post_get_instance_with_metadata`.
        """
        return response, metadata

    def pre_get_lun(
        self,
        request: lun.GetLunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lun.GetLunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_lun

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_lun(self, response: lun.Lun) -> lun.Lun:
        """Post-rpc interceptor for get_lun

        DEPRECATED. Please use the `post_get_lun_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_lun` interceptor runs
        before the `post_get_lun_with_metadata` interceptor.
        """
        return response

    def post_get_lun_with_metadata(
        self, response: lun.Lun, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[lun.Lun, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_lun

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_lun_with_metadata`
        interceptor in new development instead of the `post_get_lun` interceptor.
        When both interceptors are used, this `post_get_lun_with_metadata` interceptor runs after the
        `post_get_lun` interceptor. The (possibly modified) response returned by
        `post_get_lun` will be passed to
        `post_get_lun_with_metadata`.
        """
        return response, metadata

    def pre_get_network(
        self,
        request: network.GetNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network.GetNetworkRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_network(self, response: network.Network) -> network.Network:
        """Post-rpc interceptor for get_network

        DEPRECATED. Please use the `post_get_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_network` interceptor runs
        before the `post_get_network_with_metadata` interceptor.
        """
        return response

    def post_get_network_with_metadata(
        self,
        response: network.Network,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network.Network, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_network_with_metadata`
        interceptor in new development instead of the `post_get_network` interceptor.
        When both interceptors are used, this `post_get_network_with_metadata` interceptor runs after the
        `post_get_network` interceptor. The (possibly modified) response returned by
        `post_get_network` will be passed to
        `post_get_network_with_metadata`.
        """
        return response, metadata

    def pre_get_nfs_share(
        self,
        request: nfs_share.GetNfsShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[nfs_share.GetNfsShareRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_nfs_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_nfs_share(self, response: nfs_share.NfsShare) -> nfs_share.NfsShare:
        """Post-rpc interceptor for get_nfs_share

        DEPRECATED. Please use the `post_get_nfs_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_nfs_share` interceptor runs
        before the `post_get_nfs_share_with_metadata` interceptor.
        """
        return response

    def post_get_nfs_share_with_metadata(
        self,
        response: nfs_share.NfsShare,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[nfs_share.NfsShare, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_nfs_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_nfs_share_with_metadata`
        interceptor in new development instead of the `post_get_nfs_share` interceptor.
        When both interceptors are used, this `post_get_nfs_share_with_metadata` interceptor runs after the
        `post_get_nfs_share` interceptor. The (possibly modified) response returned by
        `post_get_nfs_share` will be passed to
        `post_get_nfs_share_with_metadata`.
        """
        return response, metadata

    def pre_get_provisioning_config(
        self,
        request: provisioning.GetProvisioningConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.GetProvisioningConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_provisioning_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_provisioning_config(
        self, response: provisioning.ProvisioningConfig
    ) -> provisioning.ProvisioningConfig:
        """Post-rpc interceptor for get_provisioning_config

        DEPRECATED. Please use the `post_get_provisioning_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_provisioning_config` interceptor runs
        before the `post_get_provisioning_config_with_metadata` interceptor.
        """
        return response

    def post_get_provisioning_config_with_metadata(
        self,
        response: provisioning.ProvisioningConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.ProvisioningConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_provisioning_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_provisioning_config_with_metadata`
        interceptor in new development instead of the `post_get_provisioning_config` interceptor.
        When both interceptors are used, this `post_get_provisioning_config_with_metadata` interceptor runs after the
        `post_get_provisioning_config` interceptor. The (possibly modified) response returned by
        `post_get_provisioning_config` will be passed to
        `post_get_provisioning_config_with_metadata`.
        """
        return response, metadata

    def pre_get_volume(
        self,
        request: volume.GetVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.GetVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_volume(self, response: volume.Volume) -> volume.Volume:
        """Post-rpc interceptor for get_volume

        DEPRECATED. Please use the `post_get_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_volume` interceptor runs
        before the `post_get_volume_with_metadata` interceptor.
        """
        return response

    def post_get_volume_with_metadata(
        self, response: volume.Volume, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[volume.Volume, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_volume_with_metadata`
        interceptor in new development instead of the `post_get_volume` interceptor.
        When both interceptors are used, this `post_get_volume_with_metadata` interceptor runs after the
        `post_get_volume` interceptor. The (possibly modified) response returned by
        `post_get_volume` will be passed to
        `post_get_volume_with_metadata`.
        """
        return response, metadata

    def pre_get_volume_snapshot(
        self,
        request: volume_snapshot.GetVolumeSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume_snapshot.GetVolumeSnapshotRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_volume_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_volume_snapshot(
        self, response: volume_snapshot.VolumeSnapshot
    ) -> volume_snapshot.VolumeSnapshot:
        """Post-rpc interceptor for get_volume_snapshot

        DEPRECATED. Please use the `post_get_volume_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_get_volume_snapshot` interceptor runs
        before the `post_get_volume_snapshot_with_metadata` interceptor.
        """
        return response

    def post_get_volume_snapshot_with_metadata(
        self,
        response: volume_snapshot.VolumeSnapshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume_snapshot.VolumeSnapshot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_volume_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_get_volume_snapshot_with_metadata`
        interceptor in new development instead of the `post_get_volume_snapshot` interceptor.
        When both interceptors are used, this `post_get_volume_snapshot_with_metadata` interceptor runs after the
        `post_get_volume_snapshot` interceptor. The (possibly modified) response returned by
        `post_get_volume_snapshot` will be passed to
        `post_get_volume_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_list_instances(
        self,
        request: instance.ListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.ListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_instances(
        self, response: instance.ListInstancesResponse
    ) -> instance.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        DEPRECATED. Please use the `post_list_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_instances` interceptor runs
        before the `post_list_instances_with_metadata` interceptor.
        """
        return response

    def post_list_instances_with_metadata(
        self,
        response: instance.ListInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.ListInstancesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_instances_with_metadata`
        interceptor in new development instead of the `post_list_instances` interceptor.
        When both interceptors are used, this `post_list_instances_with_metadata` interceptor runs after the
        `post_list_instances` interceptor. The (possibly modified) response returned by
        `post_list_instances` will be passed to
        `post_list_instances_with_metadata`.
        """
        return response, metadata

    def pre_list_luns(
        self,
        request: lun.ListLunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lun.ListLunsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_luns

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_luns(self, response: lun.ListLunsResponse) -> lun.ListLunsResponse:
        """Post-rpc interceptor for list_luns

        DEPRECATED. Please use the `post_list_luns_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_luns` interceptor runs
        before the `post_list_luns_with_metadata` interceptor.
        """
        return response

    def post_list_luns_with_metadata(
        self,
        response: lun.ListLunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lun.ListLunsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_luns

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_luns_with_metadata`
        interceptor in new development instead of the `post_list_luns` interceptor.
        When both interceptors are used, this `post_list_luns_with_metadata` interceptor runs after the
        `post_list_luns` interceptor. The (possibly modified) response returned by
        `post_list_luns` will be passed to
        `post_list_luns_with_metadata`.
        """
        return response, metadata

    def pre_list_networks(
        self,
        request: network.ListNetworksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network.ListNetworksRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_networks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_networks(
        self, response: network.ListNetworksResponse
    ) -> network.ListNetworksResponse:
        """Post-rpc interceptor for list_networks

        DEPRECATED. Please use the `post_list_networks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_networks` interceptor runs
        before the `post_list_networks_with_metadata` interceptor.
        """
        return response

    def post_list_networks_with_metadata(
        self,
        response: network.ListNetworksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network.ListNetworksResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_networks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_networks_with_metadata`
        interceptor in new development instead of the `post_list_networks` interceptor.
        When both interceptors are used, this `post_list_networks_with_metadata` interceptor runs after the
        `post_list_networks` interceptor. The (possibly modified) response returned by
        `post_list_networks` will be passed to
        `post_list_networks_with_metadata`.
        """
        return response, metadata

    def pre_list_network_usage(
        self,
        request: network.ListNetworkUsageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network.ListNetworkUsageRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_network_usage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_network_usage(
        self, response: network.ListNetworkUsageResponse
    ) -> network.ListNetworkUsageResponse:
        """Post-rpc interceptor for list_network_usage

        DEPRECATED. Please use the `post_list_network_usage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_network_usage` interceptor runs
        before the `post_list_network_usage_with_metadata` interceptor.
        """
        return response

    def post_list_network_usage_with_metadata(
        self,
        response: network.ListNetworkUsageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network.ListNetworkUsageResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_network_usage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_network_usage_with_metadata`
        interceptor in new development instead of the `post_list_network_usage` interceptor.
        When both interceptors are used, this `post_list_network_usage_with_metadata` interceptor runs after the
        `post_list_network_usage` interceptor. The (possibly modified) response returned by
        `post_list_network_usage` will be passed to
        `post_list_network_usage_with_metadata`.
        """
        return response, metadata

    def pre_list_nfs_shares(
        self,
        request: nfs_share.ListNfsSharesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[nfs_share.ListNfsSharesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_nfs_shares

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_nfs_shares(
        self, response: nfs_share.ListNfsSharesResponse
    ) -> nfs_share.ListNfsSharesResponse:
        """Post-rpc interceptor for list_nfs_shares

        DEPRECATED. Please use the `post_list_nfs_shares_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_nfs_shares` interceptor runs
        before the `post_list_nfs_shares_with_metadata` interceptor.
        """
        return response

    def post_list_nfs_shares_with_metadata(
        self,
        response: nfs_share.ListNfsSharesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        nfs_share.ListNfsSharesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_nfs_shares

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_nfs_shares_with_metadata`
        interceptor in new development instead of the `post_list_nfs_shares` interceptor.
        When both interceptors are used, this `post_list_nfs_shares_with_metadata` interceptor runs after the
        `post_list_nfs_shares` interceptor. The (possibly modified) response returned by
        `post_list_nfs_shares` will be passed to
        `post_list_nfs_shares_with_metadata`.
        """
        return response, metadata

    def pre_list_os_images(
        self,
        request: osimage.ListOSImagesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[osimage.ListOSImagesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_os_images

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_os_images(
        self, response: osimage.ListOSImagesResponse
    ) -> osimage.ListOSImagesResponse:
        """Post-rpc interceptor for list_os_images

        DEPRECATED. Please use the `post_list_os_images_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_os_images` interceptor runs
        before the `post_list_os_images_with_metadata` interceptor.
        """
        return response

    def post_list_os_images_with_metadata(
        self,
        response: osimage.ListOSImagesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[osimage.ListOSImagesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_os_images

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_os_images_with_metadata`
        interceptor in new development instead of the `post_list_os_images` interceptor.
        When both interceptors are used, this `post_list_os_images_with_metadata` interceptor runs after the
        `post_list_os_images` interceptor. The (possibly modified) response returned by
        `post_list_os_images` will be passed to
        `post_list_os_images_with_metadata`.
        """
        return response, metadata

    def pre_list_provisioning_quotas(
        self,
        request: provisioning.ListProvisioningQuotasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.ListProvisioningQuotasRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_provisioning_quotas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_provisioning_quotas(
        self, response: provisioning.ListProvisioningQuotasResponse
    ) -> provisioning.ListProvisioningQuotasResponse:
        """Post-rpc interceptor for list_provisioning_quotas

        DEPRECATED. Please use the `post_list_provisioning_quotas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_provisioning_quotas` interceptor runs
        before the `post_list_provisioning_quotas_with_metadata` interceptor.
        """
        return response

    def post_list_provisioning_quotas_with_metadata(
        self,
        response: provisioning.ListProvisioningQuotasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.ListProvisioningQuotasResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_provisioning_quotas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_provisioning_quotas_with_metadata`
        interceptor in new development instead of the `post_list_provisioning_quotas` interceptor.
        When both interceptors are used, this `post_list_provisioning_quotas_with_metadata` interceptor runs after the
        `post_list_provisioning_quotas` interceptor. The (possibly modified) response returned by
        `post_list_provisioning_quotas` will be passed to
        `post_list_provisioning_quotas_with_metadata`.
        """
        return response, metadata

    def pre_list_ssh_keys(
        self,
        request: ssh_key.ListSSHKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ssh_key.ListSSHKeysRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_ssh_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_ssh_keys(
        self, response: ssh_key.ListSSHKeysResponse
    ) -> ssh_key.ListSSHKeysResponse:
        """Post-rpc interceptor for list_ssh_keys

        DEPRECATED. Please use the `post_list_ssh_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_ssh_keys` interceptor runs
        before the `post_list_ssh_keys_with_metadata` interceptor.
        """
        return response

    def post_list_ssh_keys_with_metadata(
        self,
        response: ssh_key.ListSSHKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ssh_key.ListSSHKeysResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_ssh_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_ssh_keys_with_metadata`
        interceptor in new development instead of the `post_list_ssh_keys` interceptor.
        When both interceptors are used, this `post_list_ssh_keys_with_metadata` interceptor runs after the
        `post_list_ssh_keys` interceptor. The (possibly modified) response returned by
        `post_list_ssh_keys` will be passed to
        `post_list_ssh_keys_with_metadata`.
        """
        return response, metadata

    def pre_list_volumes(
        self,
        request: volume.ListVolumesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.ListVolumesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_volumes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_volumes(
        self, response: volume.ListVolumesResponse
    ) -> volume.ListVolumesResponse:
        """Post-rpc interceptor for list_volumes

        DEPRECATED. Please use the `post_list_volumes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
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
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_volumes_with_metadata`
        interceptor in new development instead of the `post_list_volumes` interceptor.
        When both interceptors are used, this `post_list_volumes_with_metadata` interceptor runs after the
        `post_list_volumes` interceptor. The (possibly modified) response returned by
        `post_list_volumes` will be passed to
        `post_list_volumes_with_metadata`.
        """
        return response, metadata

    def pre_list_volume_snapshots(
        self,
        request: volume_snapshot.ListVolumeSnapshotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume_snapshot.ListVolumeSnapshotsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_volume_snapshots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_volume_snapshots(
        self, response: volume_snapshot.ListVolumeSnapshotsResponse
    ) -> volume_snapshot.ListVolumeSnapshotsResponse:
        """Post-rpc interceptor for list_volume_snapshots

        DEPRECATED. Please use the `post_list_volume_snapshots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_list_volume_snapshots` interceptor runs
        before the `post_list_volume_snapshots_with_metadata` interceptor.
        """
        return response

    def post_list_volume_snapshots_with_metadata(
        self,
        response: volume_snapshot.ListVolumeSnapshotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume_snapshot.ListVolumeSnapshotsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_volume_snapshots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_list_volume_snapshots_with_metadata`
        interceptor in new development instead of the `post_list_volume_snapshots` interceptor.
        When both interceptors are used, this `post_list_volume_snapshots_with_metadata` interceptor runs after the
        `post_list_volume_snapshots` interceptor. The (possibly modified) response returned by
        `post_list_volume_snapshots` will be passed to
        `post_list_volume_snapshots_with_metadata`.
        """
        return response, metadata

    def pre_rename_instance(
        self,
        request: instance.RenameInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.RenameInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for rename_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_rename_instance(self, response: instance.Instance) -> instance.Instance:
        """Post-rpc interceptor for rename_instance

        DEPRECATED. Please use the `post_rename_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_rename_instance` interceptor runs
        before the `post_rename_instance_with_metadata` interceptor.
        """
        return response

    def post_rename_instance_with_metadata(
        self,
        response: instance.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rename_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_rename_instance_with_metadata`
        interceptor in new development instead of the `post_rename_instance` interceptor.
        When both interceptors are used, this `post_rename_instance_with_metadata` interceptor runs after the
        `post_rename_instance` interceptor. The (possibly modified) response returned by
        `post_rename_instance` will be passed to
        `post_rename_instance_with_metadata`.
        """
        return response, metadata

    def pre_rename_network(
        self,
        request: network.RenameNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network.RenameNetworkRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for rename_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_rename_network(self, response: network.Network) -> network.Network:
        """Post-rpc interceptor for rename_network

        DEPRECATED. Please use the `post_rename_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_rename_network` interceptor runs
        before the `post_rename_network_with_metadata` interceptor.
        """
        return response

    def post_rename_network_with_metadata(
        self,
        response: network.Network,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network.Network, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rename_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_rename_network_with_metadata`
        interceptor in new development instead of the `post_rename_network` interceptor.
        When both interceptors are used, this `post_rename_network_with_metadata` interceptor runs after the
        `post_rename_network` interceptor. The (possibly modified) response returned by
        `post_rename_network` will be passed to
        `post_rename_network_with_metadata`.
        """
        return response, metadata

    def pre_rename_nfs_share(
        self,
        request: nfs_share.RenameNfsShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        nfs_share.RenameNfsShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for rename_nfs_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_rename_nfs_share(self, response: nfs_share.NfsShare) -> nfs_share.NfsShare:
        """Post-rpc interceptor for rename_nfs_share

        DEPRECATED. Please use the `post_rename_nfs_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_rename_nfs_share` interceptor runs
        before the `post_rename_nfs_share_with_metadata` interceptor.
        """
        return response

    def post_rename_nfs_share_with_metadata(
        self,
        response: nfs_share.NfsShare,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[nfs_share.NfsShare, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rename_nfs_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_rename_nfs_share_with_metadata`
        interceptor in new development instead of the `post_rename_nfs_share` interceptor.
        When both interceptors are used, this `post_rename_nfs_share_with_metadata` interceptor runs after the
        `post_rename_nfs_share` interceptor. The (possibly modified) response returned by
        `post_rename_nfs_share` will be passed to
        `post_rename_nfs_share_with_metadata`.
        """
        return response, metadata

    def pre_rename_volume(
        self,
        request: volume.RenameVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.RenameVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for rename_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_rename_volume(self, response: volume.Volume) -> volume.Volume:
        """Post-rpc interceptor for rename_volume

        DEPRECATED. Please use the `post_rename_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_rename_volume` interceptor runs
        before the `post_rename_volume_with_metadata` interceptor.
        """
        return response

    def post_rename_volume_with_metadata(
        self, response: volume.Volume, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[volume.Volume, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rename_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_rename_volume_with_metadata`
        interceptor in new development instead of the `post_rename_volume` interceptor.
        When both interceptors are used, this `post_rename_volume_with_metadata` interceptor runs after the
        `post_rename_volume` interceptor. The (possibly modified) response returned by
        `post_rename_volume` will be passed to
        `post_rename_volume_with_metadata`.
        """
        return response, metadata

    def pre_reset_instance(
        self,
        request: instance.ResetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.ResetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for reset_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_reset_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reset_instance

        DEPRECATED. Please use the `post_reset_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_reset_instance` interceptor runs
        before the `post_reset_instance_with_metadata` interceptor.
        """
        return response

    def post_reset_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_reset_instance_with_metadata`
        interceptor in new development instead of the `post_reset_instance` interceptor.
        When both interceptors are used, this `post_reset_instance_with_metadata` interceptor runs after the
        `post_reset_instance` interceptor. The (possibly modified) response returned by
        `post_reset_instance` will be passed to
        `post_reset_instance_with_metadata`.
        """
        return response, metadata

    def pre_resize_volume(
        self,
        request: gcb_volume.ResizeVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcb_volume.ResizeVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for resize_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_resize_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for resize_volume

        DEPRECATED. Please use the `post_resize_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_resize_volume` interceptor runs
        before the `post_resize_volume_with_metadata` interceptor.
        """
        return response

    def post_resize_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resize_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_resize_volume_with_metadata`
        interceptor in new development instead of the `post_resize_volume` interceptor.
        When both interceptors are used, this `post_resize_volume_with_metadata` interceptor runs after the
        `post_resize_volume` interceptor. The (possibly modified) response returned by
        `post_resize_volume` will be passed to
        `post_resize_volume_with_metadata`.
        """
        return response, metadata

    def pre_restore_volume_snapshot(
        self,
        request: gcb_volume_snapshot.RestoreVolumeSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_volume_snapshot.RestoreVolumeSnapshotRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for restore_volume_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_restore_volume_snapshot(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_volume_snapshot

        DEPRECATED. Please use the `post_restore_volume_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_restore_volume_snapshot` interceptor runs
        before the `post_restore_volume_snapshot_with_metadata` interceptor.
        """
        return response

    def post_restore_volume_snapshot_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_volume_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_restore_volume_snapshot_with_metadata`
        interceptor in new development instead of the `post_restore_volume_snapshot` interceptor.
        When both interceptors are used, this `post_restore_volume_snapshot_with_metadata` interceptor runs after the
        `post_restore_volume_snapshot` interceptor. The (possibly modified) response returned by
        `post_restore_volume_snapshot` will be passed to
        `post_restore_volume_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_start_instance(
        self,
        request: instance.StartInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.StartInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for start_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_start_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_instance

        DEPRECATED. Please use the `post_start_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_start_instance` interceptor runs
        before the `post_start_instance_with_metadata` interceptor.
        """
        return response

    def post_start_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_start_instance_with_metadata`
        interceptor in new development instead of the `post_start_instance` interceptor.
        When both interceptors are used, this `post_start_instance_with_metadata` interceptor runs after the
        `post_start_instance` interceptor. The (possibly modified) response returned by
        `post_start_instance` will be passed to
        `post_start_instance_with_metadata`.
        """
        return response, metadata

    def pre_stop_instance(
        self,
        request: instance.StopInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[instance.StopInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for stop_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_stop_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_instance

        DEPRECATED. Please use the `post_stop_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_stop_instance` interceptor runs
        before the `post_stop_instance_with_metadata` interceptor.
        """
        return response

    def post_stop_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_stop_instance_with_metadata`
        interceptor in new development instead of the `post_stop_instance` interceptor.
        When both interceptors are used, this `post_stop_instance_with_metadata` interceptor runs after the
        `post_stop_instance` interceptor. The (possibly modified) response returned by
        `post_stop_instance` will be passed to
        `post_stop_instance_with_metadata`.
        """
        return response, metadata

    def pre_submit_provisioning_config(
        self,
        request: provisioning.SubmitProvisioningConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.SubmitProvisioningConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for submit_provisioning_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_submit_provisioning_config(
        self, response: provisioning.SubmitProvisioningConfigResponse
    ) -> provisioning.SubmitProvisioningConfigResponse:
        """Post-rpc interceptor for submit_provisioning_config

        DEPRECATED. Please use the `post_submit_provisioning_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_submit_provisioning_config` interceptor runs
        before the `post_submit_provisioning_config_with_metadata` interceptor.
        """
        return response

    def post_submit_provisioning_config_with_metadata(
        self,
        response: provisioning.SubmitProvisioningConfigResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.SubmitProvisioningConfigResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for submit_provisioning_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_submit_provisioning_config_with_metadata`
        interceptor in new development instead of the `post_submit_provisioning_config` interceptor.
        When both interceptors are used, this `post_submit_provisioning_config_with_metadata` interceptor runs after the
        `post_submit_provisioning_config` interceptor. The (possibly modified) response returned by
        `post_submit_provisioning_config` will be passed to
        `post_submit_provisioning_config_with_metadata`.
        """
        return response, metadata

    def pre_update_instance(
        self,
        request: gcb_instance.UpdateInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_instance.UpdateInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_update_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_instance

        DEPRECATED. Please use the `post_update_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
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
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_update_instance_with_metadata`
        interceptor in new development instead of the `post_update_instance` interceptor.
        When both interceptors are used, this `post_update_instance_with_metadata` interceptor runs after the
        `post_update_instance` interceptor. The (possibly modified) response returned by
        `post_update_instance` will be passed to
        `post_update_instance_with_metadata`.
        """
        return response, metadata

    def pre_update_network(
        self,
        request: gcb_network.UpdateNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_network.UpdateNetworkRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_update_network(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_network

        DEPRECATED. Please use the `post_update_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_update_network` interceptor runs
        before the `post_update_network_with_metadata` interceptor.
        """
        return response

    def post_update_network_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_update_network_with_metadata`
        interceptor in new development instead of the `post_update_network` interceptor.
        When both interceptors are used, this `post_update_network_with_metadata` interceptor runs after the
        `post_update_network` interceptor. The (possibly modified) response returned by
        `post_update_network` will be passed to
        `post_update_network_with_metadata`.
        """
        return response, metadata

    def pre_update_nfs_share(
        self,
        request: gcb_nfs_share.UpdateNfsShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcb_nfs_share.UpdateNfsShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_nfs_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_update_nfs_share(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_nfs_share

        DEPRECATED. Please use the `post_update_nfs_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_update_nfs_share` interceptor runs
        before the `post_update_nfs_share_with_metadata` interceptor.
        """
        return response

    def post_update_nfs_share_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_nfs_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_update_nfs_share_with_metadata`
        interceptor in new development instead of the `post_update_nfs_share` interceptor.
        When both interceptors are used, this `post_update_nfs_share_with_metadata` interceptor runs after the
        `post_update_nfs_share` interceptor. The (possibly modified) response returned by
        `post_update_nfs_share` will be passed to
        `post_update_nfs_share_with_metadata`.
        """
        return response, metadata

    def pre_update_provisioning_config(
        self,
        request: provisioning.UpdateProvisioningConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.UpdateProvisioningConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_provisioning_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_update_provisioning_config(
        self, response: provisioning.ProvisioningConfig
    ) -> provisioning.ProvisioningConfig:
        """Post-rpc interceptor for update_provisioning_config

        DEPRECATED. Please use the `post_update_provisioning_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code. This `post_update_provisioning_config` interceptor runs
        before the `post_update_provisioning_config_with_metadata` interceptor.
        """
        return response

    def post_update_provisioning_config_with_metadata(
        self,
        response: provisioning.ProvisioningConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        provisioning.ProvisioningConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_provisioning_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_update_provisioning_config_with_metadata`
        interceptor in new development instead of the `post_update_provisioning_config` interceptor.
        When both interceptors are used, this `post_update_provisioning_config_with_metadata` interceptor runs after the
        `post_update_provisioning_config` interceptor. The (possibly modified) response returned by
        `post_update_provisioning_config` will be passed to
        `post_update_provisioning_config_with_metadata`.
        """
        return response, metadata

    def pre_update_volume(
        self,
        request: gcb_volume.UpdateVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcb_volume.UpdateVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_update_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_volume

        DEPRECATED. Please use the `post_update_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BareMetalSolution server but before
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
        is returned by the BareMetalSolution server but before it is returned to user code.

        We recommend only using this `post_update_volume_with_metadata`
        interceptor in new development instead of the `post_update_volume` interceptor.
        When both interceptors are used, this `post_update_volume_with_metadata` interceptor runs after the
        `post_update_volume` interceptor. The (possibly modified) response returned by
        `post_update_volume` will be passed to
        `post_update_volume_with_metadata`.
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
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the BareMetalSolution server but before
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
        before they are sent to the BareMetalSolution server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the BareMetalSolution server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class BareMetalSolutionRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BareMetalSolutionRestInterceptor


class BareMetalSolutionRestTransport(_BaseBareMetalSolutionRestTransport):
    """REST backend synchronous transport for BareMetalSolution.

    Performs management operations on Bare Metal Solution servers.

    The ``baremetalsolution.googleapis.com`` service provides management
    capabilities for Bare Metal Solution servers. To access the API
    methods, you must assign Bare Metal Solution IAM roles containing
    the desired permissions to your staff in your Google Cloud project.
    You must also enable the Bare Metal Solution API. Once enabled, the
    methods act upon specific servers in your Bare Metal Solution
    environment.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "baremetalsolution.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BareMetalSolutionRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'baremetalsolution.googleapis.com').
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
            interceptor (Optional[BareMetalSolutionRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or BareMetalSolutionRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {}

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateNfsShare(
        _BaseBareMetalSolutionRestTransport._BaseCreateNfsShare,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.CreateNfsShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_nfs_share.CreateNfsShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create nfs share method over HTTP.

            Args:
                request (~.gcb_nfs_share.CreateNfsShareRequest):
                    The request object. Message for creating an NFS share.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseCreateNfsShare._get_http_options()
            request, metadata = self._interceptor.pre_create_nfs_share(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseCreateNfsShare,
                    "_BaseCreateNfsShare__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.CreateNfsShare",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateNfsShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._CreateNfsShare._get_response(
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

            resp = self._interceptor.post_create_nfs_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_nfs_share_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.create_nfs_share",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateNfsShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProvisioningConfig(
        _BaseBareMetalSolutionRestTransport._BaseCreateProvisioningConfig,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.CreateProvisioningConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: provisioning.CreateProvisioningConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> provisioning.ProvisioningConfig:
            r"""Call the create provisioning
            config method over HTTP.

                Args:
                    request (~.provisioning.CreateProvisioningConfigRequest):
                        The request object. Request for CreateProvisioningConfig.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.provisioning.ProvisioningConfig:
                        A provisioning configuration.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseCreateProvisioningConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_provisioning_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseCreateProvisioningConfig,
                    "_BaseCreateProvisioningConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.CreateProvisioningConfig",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateProvisioningConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._CreateProvisioningConfig._get_response(
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
            resp = provisioning.ProvisioningConfig()
            pb_resp = provisioning.ProvisioningConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_provisioning_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_provisioning_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = provisioning.ProvisioningConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.create_provisioning_config",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateProvisioningConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSSHKey(
        _BaseBareMetalSolutionRestTransport._BaseCreateSSHKey, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.CreateSSHKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_ssh_key.CreateSSHKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcb_ssh_key.SSHKey:
            r"""Call the create ssh key method over HTTP.

            Args:
                request (~.gcb_ssh_key.CreateSSHKeyRequest):
                    The request object. Message for registering a public SSH
                key in a project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcb_ssh_key.SSHKey:
                    An SSH key, used for authorizing with
                the interactive serial console feature.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseCreateSSHKey._get_http_options()
            request, metadata = self._interceptor.pre_create_ssh_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseCreateSSHKey,
                    "_BaseCreateSSHKey__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.CreateSSHKey",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateSSHKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._CreateSSHKey._get_response(
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
            resp = gcb_ssh_key.SSHKey()
            pb_resp = gcb_ssh_key.SSHKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ssh_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ssh_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcb_ssh_key.SSHKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.create_ssh_key",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateSSHKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVolumeSnapshot(
        _BaseBareMetalSolutionRestTransport._BaseCreateVolumeSnapshot,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.CreateVolumeSnapshot")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_volume_snapshot.CreateVolumeSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcb_volume_snapshot.VolumeSnapshot:
            r"""Call the create volume snapshot method over HTTP.

            Args:
                request (~.gcb_volume_snapshot.CreateVolumeSnapshotRequest):
                    The request object. Message for creating a volume
                snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcb_volume_snapshot.VolumeSnapshot:
                    A snapshot of a volume. Only boot
                volumes can have snapshots.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseCreateVolumeSnapshot._get_http_options()
            request, metadata = self._interceptor.pre_create_volume_snapshot(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseCreateVolumeSnapshot,
                    "_BaseCreateVolumeSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.CreateVolumeSnapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateVolumeSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._CreateVolumeSnapshot._get_response(
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
            resp = gcb_volume_snapshot.VolumeSnapshot()
            pb_resp = gcb_volume_snapshot.VolumeSnapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_volume_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_volume_snapshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcb_volume_snapshot.VolumeSnapshot.to_json(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.create_volume_snapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "CreateVolumeSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNfsShare(
        _BaseBareMetalSolutionRestTransport._BaseDeleteNfsShare,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.DeleteNfsShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: nfs_share.DeleteNfsShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete nfs share method over HTTP.

            Args:
                request (~.nfs_share.DeleteNfsShareRequest):
                    The request object. Message for deleting an NFS share.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseDeleteNfsShare._get_http_options()
            request, metadata = self._interceptor.pre_delete_nfs_share(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseDeleteNfsShare,
                    "_BaseDeleteNfsShare__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.DeleteNfsShare",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DeleteNfsShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._DeleteNfsShare._get_response(
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

            resp = self._interceptor.post_delete_nfs_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_nfs_share_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.delete_nfs_share",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DeleteNfsShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSSHKey(
        _BaseBareMetalSolutionRestTransport._BaseDeleteSSHKey, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.DeleteSSHKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: ssh_key.DeleteSSHKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete ssh key method over HTTP.

            Args:
                request (~.ssh_key.DeleteSSHKeyRequest):
                    The request object. Message for deleting an SSH key from
                a project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseDeleteSSHKey._get_http_options()
            request, metadata = self._interceptor.pre_delete_ssh_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseDeleteSSHKey,
                    "_BaseDeleteSSHKey__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.DeleteSSHKey",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DeleteSSHKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._DeleteSSHKey._get_response(
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

    class _DeleteVolumeSnapshot(
        _BaseBareMetalSolutionRestTransport._BaseDeleteVolumeSnapshot,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.DeleteVolumeSnapshot")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: volume_snapshot.DeleteVolumeSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete volume snapshot method over HTTP.

            Args:
                request (~.volume_snapshot.DeleteVolumeSnapshotRequest):
                    The request object. Message for deleting named Volume
                snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseDeleteVolumeSnapshot._get_http_options()
            request, metadata = self._interceptor.pre_delete_volume_snapshot(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseDeleteVolumeSnapshot,
                    "_BaseDeleteVolumeSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.DeleteVolumeSnapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DeleteVolumeSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._DeleteVolumeSnapshot._get_response(
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

    class _DetachLun(
        _BaseBareMetalSolutionRestTransport._BaseDetachLun, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.DetachLun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_instance.DetachLunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the detach lun method over HTTP.

            Args:
                request (~.gcb_instance.DetachLunRequest):
                    The request object. Message for detach specific LUN from
                an Instance.
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
                _BaseBareMetalSolutionRestTransport._BaseDetachLun._get_http_options()
            )
            request, metadata = self._interceptor.pre_detach_lun(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseDetachLun,
                    "_BaseDetachLun__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.DetachLun",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DetachLun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._DetachLun._get_response(
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

            resp = self._interceptor.post_detach_lun(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_detach_lun_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.detach_lun",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DetachLun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DisableInteractiveSerialConsole(
        _BaseBareMetalSolutionRestTransport._BaseDisableInteractiveSerialConsole,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash(
                "BareMetalSolutionRestTransport.DisableInteractiveSerialConsole"
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
                data=body,
            )
            return response

        def __call__(
            self,
            request: instance.DisableInteractiveSerialConsoleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the disable interactive
            serial console method over HTTP.

                Args:
                    request (~.instance.DisableInteractiveSerialConsoleRequest):
                        The request object. Message for disabling the interactive
                    serial console on an instance.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseDisableInteractiveSerialConsole._get_http_options()
            request, metadata = (
                self._interceptor.pre_disable_interactive_serial_console(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseDisableInteractiveSerialConsole,
                    "_BaseDisableInteractiveSerialConsole__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.DisableInteractiveSerialConsole",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DisableInteractiveSerialConsole",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._DisableInteractiveSerialConsole._get_response(
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

            resp = self._interceptor.post_disable_interactive_serial_console(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_disable_interactive_serial_console_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.disable_interactive_serial_console",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "DisableInteractiveSerialConsole",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableInteractiveSerialConsole(
        _BaseBareMetalSolutionRestTransport._BaseEnableInteractiveSerialConsole,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.EnableInteractiveSerialConsole")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.EnableInteractiveSerialConsoleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the enable interactive serial
            console method over HTTP.

                Args:
                    request (~.instance.EnableInteractiveSerialConsoleRequest):
                        The request object. Message for enabling the interactive
                    serial console on an instance.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseEnableInteractiveSerialConsole._get_http_options()
            request, metadata = self._interceptor.pre_enable_interactive_serial_console(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseEnableInteractiveSerialConsole,
                    "_BaseEnableInteractiveSerialConsole__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.EnableInteractiveSerialConsole",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "EnableInteractiveSerialConsole",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._EnableInteractiveSerialConsole._get_response(
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

            resp = self._interceptor.post_enable_interactive_serial_console(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_enable_interactive_serial_console_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.enable_interactive_serial_console",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "EnableInteractiveSerialConsole",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EvictLun(
        _BaseBareMetalSolutionRestTransport._BaseEvictLun, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.EvictLun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: lun.EvictLunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the evict lun method over HTTP.

            Args:
                request (~.lun.EvictLunRequest):
                    The request object. Request for skip lun cooloff and
                delete it.
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
                _BaseBareMetalSolutionRestTransport._BaseEvictLun._get_http_options()
            )
            request, metadata = self._interceptor.pre_evict_lun(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseEvictLun,
                    "_BaseEvictLun__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.EvictLun",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "EvictLun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._EvictLun._get_response(
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

            resp = self._interceptor.post_evict_lun(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_evict_lun_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.evict_lun",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "EvictLun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EvictVolume(
        _BaseBareMetalSolutionRestTransport._BaseEvictVolume, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.EvictVolume")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: volume.EvictVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the evict volume method over HTTP.

            Args:
                request (~.volume.EvictVolumeRequest):
                    The request object. Request for skip volume cooloff and
                delete it.
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
                _BaseBareMetalSolutionRestTransport._BaseEvictVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_evict_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseEvictVolume,
                    "_BaseEvictVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.EvictVolume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "EvictVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._EvictVolume._get_response(
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

            resp = self._interceptor.post_evict_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_evict_volume_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.evict_volume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "EvictVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstance(
        _BaseBareMetalSolutionRestTransport._BaseGetInstance, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.GetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> instance.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.instance.GetInstanceRequest):
                    The request object. Message for requesting server
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.instance.Instance:
                    A server.
            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseGetInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetInstance,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetInstance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetInstance._get_response(
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
            resp = instance.Instance()
            pb_resp = instance.Instance.pb(resp)

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
                    response_payload = instance.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_instance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLun(
        _BaseBareMetalSolutionRestTransport._BaseGetLun, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetLun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: lun.GetLunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lun.Lun:
            r"""Call the get lun method over HTTP.

            Args:
                request (~.lun.GetLunRequest):
                    The request object. Message for requesting storage lun
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lun.Lun:
                    A storage volume logical unit number
                (LUN).

            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseGetLun._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_lun(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetLun,
                    "_BaseGetLun__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetLun",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetLun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetLun._get_response(
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
            resp = lun.Lun()
            pb_resp = lun.Lun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_lun(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_lun_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lun.Lun.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_lun",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetLun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNetwork(
        _BaseBareMetalSolutionRestTransport._BaseGetNetwork, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetNetwork")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: network.GetNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network.Network:
            r"""Call the get network method over HTTP.

            Args:
                request (~.network.GetNetworkRequest):
                    The request object. Message for requesting network
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network.Network:
                    A Network.
            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseGetNetwork._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_network(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetNetwork,
                    "_BaseGetNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetNetwork",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetNetwork._get_response(
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
            resp = network.Network()
            pb_resp = network.Network.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_network_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network.Network.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_network",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNfsShare(
        _BaseBareMetalSolutionRestTransport._BaseGetNfsShare, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetNfsShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: nfs_share.GetNfsShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> nfs_share.NfsShare:
            r"""Call the get nfs share method over HTTP.

            Args:
                request (~.nfs_share.GetNfsShareRequest):
                    The request object. Message for requesting NFS share
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.nfs_share.NfsShare:
                    An NFS share.
            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseGetNfsShare._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_nfs_share(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetNfsShare,
                    "_BaseGetNfsShare__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetNfsShare",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetNfsShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetNfsShare._get_response(
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
            resp = nfs_share.NfsShare()
            pb_resp = nfs_share.NfsShare.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_nfs_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_nfs_share_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = nfs_share.NfsShare.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_nfs_share",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetNfsShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProvisioningConfig(
        _BaseBareMetalSolutionRestTransport._BaseGetProvisioningConfig,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetProvisioningConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: provisioning.GetProvisioningConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> provisioning.ProvisioningConfig:
            r"""Call the get provisioning config method over HTTP.

            Args:
                request (~.provisioning.GetProvisioningConfigRequest):
                    The request object. Request for GetProvisioningConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.provisioning.ProvisioningConfig:
                    A provisioning configuration.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseGetProvisioningConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_provisioning_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetProvisioningConfig,
                    "_BaseGetProvisioningConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetProvisioningConfig",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetProvisioningConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._GetProvisioningConfig._get_response(
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
            resp = provisioning.ProvisioningConfig()
            pb_resp = provisioning.ProvisioningConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_provisioning_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_provisioning_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = provisioning.ProvisioningConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_provisioning_config",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetProvisioningConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVolume(
        _BaseBareMetalSolutionRestTransport._BaseGetVolume, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetVolume")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                    The request object. Message for requesting storage volume
                information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.Volume:
                    A storage volume.
            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseGetVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetVolume,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetVolume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetVolume._get_response(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_volume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVolumeSnapshot(
        _BaseBareMetalSolutionRestTransport._BaseGetVolumeSnapshot,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetVolumeSnapshot")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: volume_snapshot.GetVolumeSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume_snapshot.VolumeSnapshot:
            r"""Call the get volume snapshot method over HTTP.

            Args:
                request (~.volume_snapshot.GetVolumeSnapshotRequest):
                    The request object. Message for requesting volume
                snapshot information.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume_snapshot.VolumeSnapshot:
                    A snapshot of a volume. Only boot
                volumes can have snapshots.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseGetVolumeSnapshot._get_http_options()
            request, metadata = self._interceptor.pre_get_volume_snapshot(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetVolumeSnapshot,
                    "_BaseGetVolumeSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetVolumeSnapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetVolumeSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetVolumeSnapshot._get_response(
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
            resp = volume_snapshot.VolumeSnapshot()
            pb_resp = volume_snapshot.VolumeSnapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_volume_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_volume_snapshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume_snapshot.VolumeSnapshot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.get_volume_snapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetVolumeSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInstances(
        _BaseBareMetalSolutionRestTransport._BaseListInstances,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListInstances")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.ListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> instance.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.instance.ListInstancesRequest):
                    The request object. Message for requesting the list of
                servers.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.instance.ListInstancesResponse:
                    Response message for the list of
                servers.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListInstances._get_http_options()
            request, metadata = self._interceptor.pre_list_instances(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListInstances,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListInstances",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListInstances._get_response(
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
            resp = instance.ListInstancesResponse()
            pb_resp = instance.ListInstancesResponse.pb(resp)

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
                    response_payload = instance.ListInstancesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_instances",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLuns(
        _BaseBareMetalSolutionRestTransport._BaseListLuns, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListLuns")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: lun.ListLunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lun.ListLunsResponse:
            r"""Call the list luns method over HTTP.

            Args:
                request (~.lun.ListLunsRequest):
                    The request object. Message for requesting a list of
                storage volume luns.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lun.ListLunsResponse:
                    Response message containing the list
                of storage volume luns.

            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseListLuns._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_luns(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListLuns,
                    "_BaseListLuns__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListLuns",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListLuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListLuns._get_response(
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
            resp = lun.ListLunsResponse()
            pb_resp = lun.ListLunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_luns(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_luns_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lun.ListLunsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_luns",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListLuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNetworks(
        _BaseBareMetalSolutionRestTransport._BaseListNetworks, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListNetworks")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: network.ListNetworksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network.ListNetworksResponse:
            r"""Call the list networks method over HTTP.

            Args:
                request (~.network.ListNetworksRequest):
                    The request object. Message for requesting a list of
                networks.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network.ListNetworksResponse:
                    Response message containing the list
                of networks.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListNetworks._get_http_options()
            request, metadata = self._interceptor.pre_list_networks(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListNetworks,
                    "_BaseListNetworks__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListNetworks",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListNetworks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListNetworks._get_response(
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
            resp = network.ListNetworksResponse()
            pb_resp = network.ListNetworksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_networks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_networks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network.ListNetworksResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_networks",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListNetworks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNetworkUsage(
        _BaseBareMetalSolutionRestTransport._BaseListNetworkUsage,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListNetworkUsage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: network.ListNetworkUsageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network.ListNetworkUsageResponse:
            r"""Call the list network usage method over HTTP.

            Args:
                request (~.network.ListNetworkUsageRequest):
                    The request object. Request to get networks with IPs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network.ListNetworkUsageResponse:
                    Response with Networks with IPs
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListNetworkUsage._get_http_options()
            request, metadata = self._interceptor.pre_list_network_usage(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListNetworkUsage,
                    "_BaseListNetworkUsage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListNetworkUsage",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListNetworkUsage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListNetworkUsage._get_response(
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
            resp = network.ListNetworkUsageResponse()
            pb_resp = network.ListNetworkUsageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_network_usage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_network_usage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network.ListNetworkUsageResponse.to_json(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_network_usage",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListNetworkUsage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNfsShares(
        _BaseBareMetalSolutionRestTransport._BaseListNfsShares,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListNfsShares")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: nfs_share.ListNfsSharesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> nfs_share.ListNfsSharesResponse:
            r"""Call the list nfs shares method over HTTP.

            Args:
                request (~.nfs_share.ListNfsSharesRequest):
                    The request object. Message for requesting a list of NFS
                shares.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.nfs_share.ListNfsSharesResponse:
                    Response message containing the list
                of NFS shares.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListNfsShares._get_http_options()
            request, metadata = self._interceptor.pre_list_nfs_shares(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListNfsShares,
                    "_BaseListNfsShares__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListNfsShares",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListNfsShares",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListNfsShares._get_response(
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
            resp = nfs_share.ListNfsSharesResponse()
            pb_resp = nfs_share.ListNfsSharesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_nfs_shares(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_nfs_shares_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = nfs_share.ListNfsSharesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_nfs_shares",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListNfsShares",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOSImages(
        _BaseBareMetalSolutionRestTransport._BaseListOSImages, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListOSImages")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: osimage.ListOSImagesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> osimage.ListOSImagesResponse:
            r"""Call the list os images method over HTTP.

            Args:
                request (~.osimage.ListOSImagesRequest):
                    The request object. Request for getting all available OS
                images.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.osimage.ListOSImagesResponse:
                    Request for getting all available OS
                images.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListOSImages._get_http_options()
            request, metadata = self._interceptor.pre_list_os_images(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListOSImages,
                    "_BaseListOSImages__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListOSImages",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListOSImages",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListOSImages._get_response(
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
            resp = osimage.ListOSImagesResponse()
            pb_resp = osimage.ListOSImagesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_os_images(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_os_images_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = osimage.ListOSImagesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_os_images",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListOSImages",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProvisioningQuotas(
        _BaseBareMetalSolutionRestTransport._BaseListProvisioningQuotas,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListProvisioningQuotas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: provisioning.ListProvisioningQuotasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> provisioning.ListProvisioningQuotasResponse:
            r"""Call the list provisioning quotas method over HTTP.

            Args:
                request (~.provisioning.ListProvisioningQuotasRequest):
                    The request object. Message for requesting the list of
                provisioning quotas.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.provisioning.ListProvisioningQuotasResponse:
                    Response message for the list of
                provisioning quotas.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListProvisioningQuotas._get_http_options()
            request, metadata = self._interceptor.pre_list_provisioning_quotas(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListProvisioningQuotas,
                    "_BaseListProvisioningQuotas__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListProvisioningQuotas",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListProvisioningQuotas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._ListProvisioningQuotas._get_response(
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
            resp = provisioning.ListProvisioningQuotasResponse()
            pb_resp = provisioning.ListProvisioningQuotasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_provisioning_quotas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_provisioning_quotas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        provisioning.ListProvisioningQuotasResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_provisioning_quotas",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListProvisioningQuotas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSSHKeys(
        _BaseBareMetalSolutionRestTransport._BaseListSSHKeys, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListSSHKeys")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: ssh_key.ListSSHKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ssh_key.ListSSHKeysResponse:
            r"""Call the list ssh keys method over HTTP.

            Args:
                request (~.ssh_key.ListSSHKeysRequest):
                    The request object. Message for listing the public SSH
                keys in a project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ssh_key.ListSSHKeysResponse:
                    Message for response of ListSSHKeys.
            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseListSSHKeys._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ssh_keys(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListSSHKeys,
                    "_BaseListSSHKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListSSHKeys",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListSSHKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListSSHKeys._get_response(
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
            resp = ssh_key.ListSSHKeysResponse()
            pb_resp = ssh_key.ListSSHKeysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ssh_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ssh_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ssh_key.ListSSHKeysResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_ssh_keys",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListSSHKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVolumes(
        _BaseBareMetalSolutionRestTransport._BaseListVolumes, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListVolumes")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                    The request object. Message for requesting a list of
                storage volumes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.ListVolumesResponse:
                    Response message containing the list
                of storage volumes.

            """

            http_options = (
                _BaseBareMetalSolutionRestTransport._BaseListVolumes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_volumes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListVolumes,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListVolumes",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListVolumes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListVolumes._get_response(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_volumes",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListVolumes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVolumeSnapshots(
        _BaseBareMetalSolutionRestTransport._BaseListVolumeSnapshots,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListVolumeSnapshots")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: volume_snapshot.ListVolumeSnapshotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume_snapshot.ListVolumeSnapshotsResponse:
            r"""Call the list volume snapshots method over HTTP.

            Args:
                request (~.volume_snapshot.ListVolumeSnapshotsRequest):
                    The request object. Message for requesting a list of
                volume snapshots.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume_snapshot.ListVolumeSnapshotsResponse:
                    Response message containing the list
                of volume snapshots.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseListVolumeSnapshots._get_http_options()
            request, metadata = self._interceptor.pre_list_volume_snapshots(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListVolumeSnapshots,
                    "_BaseListVolumeSnapshots__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListVolumeSnapshots",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListVolumeSnapshots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._ListVolumeSnapshots._get_response(
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
            resp = volume_snapshot.ListVolumeSnapshotsResponse()
            pb_resp = volume_snapshot.ListVolumeSnapshotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_volume_snapshots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_volume_snapshots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        volume_snapshot.ListVolumeSnapshotsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.list_volume_snapshots",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListVolumeSnapshots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenameInstance(
        _BaseBareMetalSolutionRestTransport._BaseRenameInstance,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.RenameInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.RenameInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> instance.Instance:
            r"""Call the rename instance method over HTTP.

            Args:
                request (~.instance.RenameInstanceRequest):
                    The request object. Message requesting rename of a
                server.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.instance.Instance:
                    A server.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseRenameInstance._get_http_options()
            request, metadata = self._interceptor.pre_rename_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseRenameInstance,
                    "_BaseRenameInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.RenameInstance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._RenameInstance._get_response(
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
            resp = instance.Instance()
            pb_resp = instance.Instance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rename_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rename_instance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = instance.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.rename_instance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenameNetwork(
        _BaseBareMetalSolutionRestTransport._BaseRenameNetwork,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.RenameNetwork")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: network.RenameNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network.Network:
            r"""Call the rename network method over HTTP.

            Args:
                request (~.network.RenameNetworkRequest):
                    The request object. Message requesting rename of a
                server.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network.Network:
                    A Network.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseRenameNetwork._get_http_options()
            request, metadata = self._interceptor.pre_rename_network(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseRenameNetwork,
                    "_BaseRenameNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.RenameNetwork",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._RenameNetwork._get_response(
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
            resp = network.Network()
            pb_resp = network.Network.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rename_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rename_network_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network.Network.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.rename_network",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenameNfsShare(
        _BaseBareMetalSolutionRestTransport._BaseRenameNfsShare,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.RenameNfsShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: nfs_share.RenameNfsShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> nfs_share.NfsShare:
            r"""Call the rename nfs share method over HTTP.

            Args:
                request (~.nfs_share.RenameNfsShareRequest):
                    The request object. Message requesting rename of a
                server.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.nfs_share.NfsShare:
                    An NFS share.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseRenameNfsShare._get_http_options()
            request, metadata = self._interceptor.pre_rename_nfs_share(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseRenameNfsShare,
                    "_BaseRenameNfsShare__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.RenameNfsShare",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameNfsShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._RenameNfsShare._get_response(
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
            resp = nfs_share.NfsShare()
            pb_resp = nfs_share.NfsShare.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rename_nfs_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rename_nfs_share_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = nfs_share.NfsShare.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.rename_nfs_share",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameNfsShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenameVolume(
        _BaseBareMetalSolutionRestTransport._BaseRenameVolume, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.RenameVolume")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: volume.RenameVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.Volume:
            r"""Call the rename volume method over HTTP.

            Args:
                request (~.volume.RenameVolumeRequest):
                    The request object. Message requesting rename of a
                server.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.Volume:
                    A storage volume.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseRenameVolume._get_http_options()
            request, metadata = self._interceptor.pre_rename_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseRenameVolume,
                    "_BaseRenameVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.RenameVolume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._RenameVolume._get_response(
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
            resp = volume.Volume()
            pb_resp = volume.Volume.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rename_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rename_volume_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.rename_volume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RenameVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetInstance(
        _BaseBareMetalSolutionRestTransport._BaseResetInstance,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ResetInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.ResetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reset instance method over HTTP.

            Args:
                request (~.instance.ResetInstanceRequest):
                    The request object. Message requesting to reset a server.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseResetInstance._get_http_options()
            request, metadata = self._interceptor.pre_reset_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseResetInstance,
                    "_BaseResetInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ResetInstance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ResetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ResetInstance._get_response(
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

            resp = self._interceptor.post_reset_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_instance_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.reset_instance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ResetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResizeVolume(
        _BaseBareMetalSolutionRestTransport._BaseResizeVolume, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ResizeVolume")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_volume.ResizeVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the resize volume method over HTTP.

            Args:
                request (~.gcb_volume.ResizeVolumeRequest):
                    The request object. Request for emergency resize Volume.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseResizeVolume._get_http_options()
            request, metadata = self._interceptor.pre_resize_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseResizeVolume,
                    "_BaseResizeVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ResizeVolume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ResizeVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ResizeVolume._get_response(
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

            resp = self._interceptor.post_resize_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resize_volume_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.resize_volume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ResizeVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreVolumeSnapshot(
        _BaseBareMetalSolutionRestTransport._BaseRestoreVolumeSnapshot,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.RestoreVolumeSnapshot")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_volume_snapshot.RestoreVolumeSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore volume snapshot method over HTTP.

            Args:
                request (~.gcb_volume_snapshot.RestoreVolumeSnapshotRequest):
                    The request object. Message for restoring a volume
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseRestoreVolumeSnapshot._get_http_options()
            request, metadata = self._interceptor.pre_restore_volume_snapshot(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseRestoreVolumeSnapshot,
                    "_BaseRestoreVolumeSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.RestoreVolumeSnapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RestoreVolumeSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._RestoreVolumeSnapshot._get_response(
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

            resp = self._interceptor.post_restore_volume_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_volume_snapshot_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.restore_volume_snapshot",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "RestoreVolumeSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartInstance(
        _BaseBareMetalSolutionRestTransport._BaseStartInstance,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.StartInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.StartInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start instance method over HTTP.

            Args:
                request (~.instance.StartInstanceRequest):
                    The request object. Message requesting to start a server.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseStartInstance._get_http_options()
            request, metadata = self._interceptor.pre_start_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseStartInstance,
                    "_BaseStartInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.StartInstance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "StartInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._StartInstance._get_response(
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

            resp = self._interceptor.post_start_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_instance_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.start_instance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "StartInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopInstance(
        _BaseBareMetalSolutionRestTransport._BaseStopInstance, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.StopInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: instance.StopInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop instance method over HTTP.

            Args:
                request (~.instance.StopInstanceRequest):
                    The request object. Message requesting to stop a server.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseStopInstance._get_http_options()
            request, metadata = self._interceptor.pre_stop_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseStopInstance,
                    "_BaseStopInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.StopInstance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "StopInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._StopInstance._get_response(
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

            resp = self._interceptor.post_stop_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_instance_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.stop_instance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "StopInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SubmitProvisioningConfig(
        _BaseBareMetalSolutionRestTransport._BaseSubmitProvisioningConfig,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.SubmitProvisioningConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: provisioning.SubmitProvisioningConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> provisioning.SubmitProvisioningConfigResponse:
            r"""Call the submit provisioning
            config method over HTTP.

                Args:
                    request (~.provisioning.SubmitProvisioningConfigRequest):
                        The request object. Request for SubmitProvisioningConfig.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.provisioning.SubmitProvisioningConfigResponse:
                        Response for
                    SubmitProvisioningConfig.

            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseSubmitProvisioningConfig._get_http_options()
            request, metadata = self._interceptor.pre_submit_provisioning_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseSubmitProvisioningConfig,
                    "_BaseSubmitProvisioningConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.SubmitProvisioningConfig",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "SubmitProvisioningConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._SubmitProvisioningConfig._get_response(
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
            resp = provisioning.SubmitProvisioningConfigResponse()
            pb_resp = provisioning.SubmitProvisioningConfigResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_submit_provisioning_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_submit_provisioning_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        provisioning.SubmitProvisioningConfigResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.submit_provisioning_config",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "SubmitProvisioningConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInstance(
        _BaseBareMetalSolutionRestTransport._BaseUpdateInstance,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.UpdateInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_instance.UpdateInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update instance method over HTTP.

            Args:
                request (~.gcb_instance.UpdateInstanceRequest):
                    The request object. Message requesting to updating a
                server.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseUpdateInstance._get_http_options()
            request, metadata = self._interceptor.pre_update_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseUpdateInstance,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.UpdateInstance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._UpdateInstance._get_response(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.update_instance",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNetwork(
        _BaseBareMetalSolutionRestTransport._BaseUpdateNetwork,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.UpdateNetwork")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_network.UpdateNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update network method over HTTP.

            Args:
                request (~.gcb_network.UpdateNetworkRequest):
                    The request object. Message requesting to updating a
                network.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseUpdateNetwork._get_http_options()
            request, metadata = self._interceptor.pre_update_network(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseUpdateNetwork,
                    "_BaseUpdateNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.UpdateNetwork",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._UpdateNetwork._get_response(
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

            resp = self._interceptor.post_update_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_network_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.update_network",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNfsShare(
        _BaseBareMetalSolutionRestTransport._BaseUpdateNfsShare,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.UpdateNfsShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_nfs_share.UpdateNfsShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update nfs share method over HTTP.

            Args:
                request (~.gcb_nfs_share.UpdateNfsShareRequest):
                    The request object. Message requesting to updating an NFS
                share.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseUpdateNfsShare._get_http_options()
            request, metadata = self._interceptor.pre_update_nfs_share(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseUpdateNfsShare,
                    "_BaseUpdateNfsShare__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.UpdateNfsShare",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateNfsShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._UpdateNfsShare._get_response(
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

            resp = self._interceptor.post_update_nfs_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_nfs_share_with_metadata(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.update_nfs_share",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateNfsShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProvisioningConfig(
        _BaseBareMetalSolutionRestTransport._BaseUpdateProvisioningConfig,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.UpdateProvisioningConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: provisioning.UpdateProvisioningConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> provisioning.ProvisioningConfig:
            r"""Call the update provisioning
            config method over HTTP.

                Args:
                    request (~.provisioning.UpdateProvisioningConfigRequest):
                        The request object. Message for updating a
                    ProvisioningConfig.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.provisioning.ProvisioningConfig:
                        A provisioning configuration.
            """

            http_options = _BaseBareMetalSolutionRestTransport._BaseUpdateProvisioningConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_provisioning_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseUpdateProvisioningConfig,
                    "_BaseUpdateProvisioningConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.UpdateProvisioningConfig",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateProvisioningConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BareMetalSolutionRestTransport._UpdateProvisioningConfig._get_response(
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
            resp = provisioning.ProvisioningConfig()
            pb_resp = provisioning.ProvisioningConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_provisioning_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_provisioning_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = provisioning.ProvisioningConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.update_provisioning_config",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateProvisioningConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateVolume(
        _BaseBareMetalSolutionRestTransport._BaseUpdateVolume, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.UpdateVolume")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcb_volume.UpdateVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update volume method over HTTP.

            Args:
                request (~.gcb_volume.UpdateVolumeRequest):
                    The request object. Message for updating a volume.
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseUpdateVolume._get_http_options()
            request, metadata = self._interceptor.pre_update_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseUpdateVolume,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.UpdateVolume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._UpdateVolume._get_response(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.update_volume",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "UpdateVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_nfs_share(
        self,
    ) -> Callable[[gcb_nfs_share.CreateNfsShareRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNfsShare(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.CreateProvisioningConfigRequest], provisioning.ProvisioningConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProvisioningConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_ssh_key(
        self,
    ) -> Callable[[gcb_ssh_key.CreateSSHKeyRequest], gcb_ssh_key.SSHKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSSHKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_volume_snapshot(
        self,
    ) -> Callable[
        [gcb_volume_snapshot.CreateVolumeSnapshotRequest],
        gcb_volume_snapshot.VolumeSnapshot,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVolumeSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_nfs_share(
        self,
    ) -> Callable[[nfs_share.DeleteNfsShareRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNfsShare(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_ssh_key(
        self,
    ) -> Callable[[ssh_key.DeleteSSHKeyRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSSHKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_volume_snapshot(
        self,
    ) -> Callable[[volume_snapshot.DeleteVolumeSnapshotRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVolumeSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def detach_lun(
        self,
    ) -> Callable[[gcb_instance.DetachLunRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DetachLun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def disable_interactive_serial_console(
        self,
    ) -> Callable[
        [instance.DisableInteractiveSerialConsoleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableInteractiveSerialConsole(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def enable_interactive_serial_console(
        self,
    ) -> Callable[
        [instance.EnableInteractiveSerialConsoleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableInteractiveSerialConsole(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def evict_lun(self) -> Callable[[lun.EvictLunRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EvictLun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def evict_volume(
        self,
    ) -> Callable[[volume.EvictVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EvictVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance(
        self,
    ) -> Callable[[instance.GetInstanceRequest], instance.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_lun(self) -> Callable[[lun.GetLunRequest], lun.Lun]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_network(self) -> Callable[[network.GetNetworkRequest], network.Network]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNetwork(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_nfs_share(
        self,
    ) -> Callable[[nfs_share.GetNfsShareRequest], nfs_share.NfsShare]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNfsShare(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.GetProvisioningConfigRequest], provisioning.ProvisioningConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProvisioningConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_volume(self) -> Callable[[volume.GetVolumeRequest], volume.Volume]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_volume_snapshot(
        self,
    ) -> Callable[
        [volume_snapshot.GetVolumeSnapshotRequest], volume_snapshot.VolumeSnapshot
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVolumeSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_instances(
        self,
    ) -> Callable[[instance.ListInstancesRequest], instance.ListInstancesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_luns(self) -> Callable[[lun.ListLunsRequest], lun.ListLunsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_networks(
        self,
    ) -> Callable[[network.ListNetworksRequest], network.ListNetworksResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNetworks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_network_usage(
        self,
    ) -> Callable[[network.ListNetworkUsageRequest], network.ListNetworkUsageResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNetworkUsage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_nfs_shares(
        self,
    ) -> Callable[[nfs_share.ListNfsSharesRequest], nfs_share.ListNfsSharesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNfsShares(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_os_images(
        self,
    ) -> Callable[[osimage.ListOSImagesRequest], osimage.ListOSImagesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOSImages(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_provisioning_quotas(
        self,
    ) -> Callable[
        [provisioning.ListProvisioningQuotasRequest],
        provisioning.ListProvisioningQuotasResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProvisioningQuotas(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_ssh_keys(
        self,
    ) -> Callable[[ssh_key.ListSSHKeysRequest], ssh_key.ListSSHKeysResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSSHKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_volumes(
        self,
    ) -> Callable[[volume.ListVolumesRequest], volume.ListVolumesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVolumes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_volume_snapshots(
        self,
    ) -> Callable[
        [volume_snapshot.ListVolumeSnapshotsRequest],
        volume_snapshot.ListVolumeSnapshotsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVolumeSnapshots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rename_instance(
        self,
    ) -> Callable[[instance.RenameInstanceRequest], instance.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenameInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rename_network(
        self,
    ) -> Callable[[network.RenameNetworkRequest], network.Network]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenameNetwork(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rename_nfs_share(
        self,
    ) -> Callable[[nfs_share.RenameNfsShareRequest], nfs_share.NfsShare]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenameNfsShare(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rename_volume(self) -> Callable[[volume.RenameVolumeRequest], volume.Volume]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenameVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_instance(
        self,
    ) -> Callable[[instance.ResetInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resize_volume(
        self,
    ) -> Callable[[gcb_volume.ResizeVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResizeVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_volume_snapshot(
        self,
    ) -> Callable[
        [gcb_volume_snapshot.RestoreVolumeSnapshotRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreVolumeSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_instance(
        self,
    ) -> Callable[[instance.StartInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_instance(
        self,
    ) -> Callable[[instance.StopInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def submit_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.SubmitProvisioningConfigRequest],
        provisioning.SubmitProvisioningConfigResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SubmitProvisioningConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_instance(
        self,
    ) -> Callable[[gcb_instance.UpdateInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_network(
        self,
    ) -> Callable[[gcb_network.UpdateNetworkRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNetwork(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_nfs_share(
        self,
    ) -> Callable[[gcb_nfs_share.UpdateNfsShareRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNfsShare(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.UpdateProvisioningConfigRequest], provisioning.ProvisioningConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProvisioningConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_volume(
        self,
    ) -> Callable[[gcb_volume.UpdateVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseBareMetalSolutionRestTransport._BaseGetLocation, BareMetalSolutionRestStub
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBareMetalSolutionRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
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
        _BaseBareMetalSolutionRestTransport._BaseListLocations,
        BareMetalSolutionRestStub,
    ):
        def __hash__(self):
            return hash("BareMetalSolutionRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseBareMetalSolutionRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBareMetalSolutionRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.baremetalsolution_v2.BareMetalSolutionClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BareMetalSolutionRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.baremetalsolution_v2.BareMetalSolutionAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.baremetalsolution.v2.BareMetalSolution",
                        "rpcName": "ListLocations",
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


__all__ = ("BareMetalSolutionRestTransport",)
