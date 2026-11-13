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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.compute_v1._compat import transcode_request
from google.cloud.compute_v1.types import compute

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseInstancesRestTransport

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


class InstancesRestInterceptor:
    """Interceptor for Instances.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the InstancesRestTransport.

    .. code-block:: python
        class MyCustomInstancesInterceptor(InstancesRestInterceptor):
            def pre_add_access_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_access_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_network_interface(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_network_interface(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_resource_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_resource_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_aggregated_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_aggregated_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_attach_disk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_attach_disk(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_insert(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_insert(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_access_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_access_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_network_interface(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_network_interface(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_detach_disk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_detach_disk(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_effective_firewalls(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_effective_firewalls(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_guest_attributes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_guest_attributes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_screenshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_screenshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_serial_port_output(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_serial_port_output(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_shielded_instance_identity(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_shielded_instance_identity(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_referrers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_referrers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_perform_maintenance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_perform_maintenance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_resource_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_resource_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_report_host_as_faulty(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_report_host_as_faulty(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_send_diagnostic_interrupt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_send_diagnostic_interrupt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_deletion_protection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_deletion_protection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_disk_auto_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_disk_auto_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_machine_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_machine_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_machine_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_machine_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_metadata(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_metadata(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_min_cpu_platform(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_min_cpu_platform(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_name(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_name(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_scheduling(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_scheduling(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_security_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_security_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_service_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_service_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_shielded_instance_integrity_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_shielded_instance_integrity_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_tags(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_tags(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_simulate_maintenance_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_simulate_maintenance_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_with_encryption_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_with_encryption_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suspend(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suspend(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_access_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_access_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_display_device(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_display_device(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_network_interface(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_network_interface(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_shielded_instance_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_shielded_instance_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = InstancesRestTransport(interceptor=MyCustomInstancesInterceptor())
        client = InstancesClient(transport=transport)


    """

    def pre_add_access_config(
        self,
        request: compute.AddAccessConfigInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AddAccessConfigInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for add_access_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_add_access_config(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for add_access_config

        DEPRECATED. Please use the `post_add_access_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_add_access_config` interceptor runs
        before the `post_add_access_config_with_metadata` interceptor.
        """
        return response

    def post_add_access_config_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_access_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_add_access_config_with_metadata`
        interceptor in new development instead of the `post_add_access_config` interceptor.
        When both interceptors are used, this `post_add_access_config_with_metadata` interceptor runs after the
        `post_add_access_config` interceptor. The (possibly modified) response returned by
        `post_add_access_config` will be passed to
        `post_add_access_config_with_metadata`.
        """
        return response, metadata

    def pre_add_network_interface(
        self,
        request: compute.AddNetworkInterfaceInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AddNetworkInterfaceInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_network_interface

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_add_network_interface(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for add_network_interface

        DEPRECATED. Please use the `post_add_network_interface_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_add_network_interface` interceptor runs
        before the `post_add_network_interface_with_metadata` interceptor.
        """
        return response

    def post_add_network_interface_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_network_interface

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_add_network_interface_with_metadata`
        interceptor in new development instead of the `post_add_network_interface` interceptor.
        When both interceptors are used, this `post_add_network_interface_with_metadata` interceptor runs after the
        `post_add_network_interface` interceptor. The (possibly modified) response returned by
        `post_add_network_interface` will be passed to
        `post_add_network_interface_with_metadata`.
        """
        return response, metadata

    def pre_add_resource_policies(
        self,
        request: compute.AddResourcePoliciesInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AddResourcePoliciesInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_resource_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_add_resource_policies(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for add_resource_policies

        DEPRECATED. Please use the `post_add_resource_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_add_resource_policies` interceptor runs
        before the `post_add_resource_policies_with_metadata` interceptor.
        """
        return response

    def post_add_resource_policies_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_resource_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_add_resource_policies_with_metadata`
        interceptor in new development instead of the `post_add_resource_policies` interceptor.
        When both interceptors are used, this `post_add_resource_policies_with_metadata` interceptor runs after the
        `post_add_resource_policies` interceptor. The (possibly modified) response returned by
        `post_add_resource_policies` will be passed to
        `post_add_resource_policies_with_metadata`.
        """
        return response, metadata

    def pre_aggregated_list(
        self,
        request: compute.AggregatedListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AggregatedListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for aggregated_list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_aggregated_list(
        self, response: compute.InstanceAggregatedList
    ) -> compute.InstanceAggregatedList:
        """Post-rpc interceptor for aggregated_list

        DEPRECATED. Please use the `post_aggregated_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_aggregated_list` interceptor runs
        before the `post_aggregated_list_with_metadata` interceptor.
        """
        return response

    def post_aggregated_list_with_metadata(
        self,
        response: compute.InstanceAggregatedList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.InstanceAggregatedList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for aggregated_list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_aggregated_list_with_metadata`
        interceptor in new development instead of the `post_aggregated_list` interceptor.
        When both interceptors are used, this `post_aggregated_list_with_metadata` interceptor runs after the
        `post_aggregated_list` interceptor. The (possibly modified) response returned by
        `post_aggregated_list` will be passed to
        `post_aggregated_list_with_metadata`.
        """
        return response, metadata

    def pre_attach_disk(
        self,
        request: compute.AttachDiskInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.AttachDiskInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for attach_disk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_attach_disk(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for attach_disk

        DEPRECATED. Please use the `post_attach_disk_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_attach_disk` interceptor runs
        before the `post_attach_disk_with_metadata` interceptor.
        """
        return response

    def post_attach_disk_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for attach_disk

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_attach_disk_with_metadata`
        interceptor in new development instead of the `post_attach_disk` interceptor.
        When both interceptors are used, this `post_attach_disk_with_metadata` interceptor runs after the
        `post_attach_disk` interceptor. The (possibly modified) response returned by
        `post_attach_disk` will be passed to
        `post_attach_disk_with_metadata`.
        """
        return response, metadata

    def pre_bulk_insert(
        self,
        request: compute.BulkInsertInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.BulkInsertInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for bulk_insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_bulk_insert(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for bulk_insert

        DEPRECATED. Please use the `post_bulk_insert_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_bulk_insert` interceptor runs
        before the `post_bulk_insert_with_metadata` interceptor.
        """
        return response

    def post_bulk_insert_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for bulk_insert

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_bulk_insert_with_metadata`
        interceptor in new development instead of the `post_bulk_insert` interceptor.
        When both interceptors are used, this `post_bulk_insert_with_metadata` interceptor runs after the
        `post_bulk_insert` interceptor. The (possibly modified) response returned by
        `post_bulk_insert` will be passed to
        `post_bulk_insert_with_metadata`.
        """
        return response, metadata

    def pre_delete(
        self,
        request: compute.DeleteInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.DeleteInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_delete(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for delete

        DEPRECATED. Please use the `post_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_delete` interceptor runs
        before the `post_delete_with_metadata` interceptor.
        """
        return response

    def post_delete_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_delete_with_metadata`
        interceptor in new development instead of the `post_delete` interceptor.
        When both interceptors are used, this `post_delete_with_metadata` interceptor runs after the
        `post_delete` interceptor. The (possibly modified) response returned by
        `post_delete` will be passed to
        `post_delete_with_metadata`.
        """
        return response, metadata

    def pre_delete_access_config(
        self,
        request: compute.DeleteAccessConfigInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DeleteAccessConfigInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_access_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_delete_access_config(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for delete_access_config

        DEPRECATED. Please use the `post_delete_access_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_delete_access_config` interceptor runs
        before the `post_delete_access_config_with_metadata` interceptor.
        """
        return response

    def post_delete_access_config_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_access_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_delete_access_config_with_metadata`
        interceptor in new development instead of the `post_delete_access_config` interceptor.
        When both interceptors are used, this `post_delete_access_config_with_metadata` interceptor runs after the
        `post_delete_access_config` interceptor. The (possibly modified) response returned by
        `post_delete_access_config` will be passed to
        `post_delete_access_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_network_interface(
        self,
        request: compute.DeleteNetworkInterfaceInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DeleteNetworkInterfaceInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_network_interface

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_delete_network_interface(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for delete_network_interface

        DEPRECATED. Please use the `post_delete_network_interface_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_delete_network_interface` interceptor runs
        before the `post_delete_network_interface_with_metadata` interceptor.
        """
        return response

    def post_delete_network_interface_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_network_interface

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_delete_network_interface_with_metadata`
        interceptor in new development instead of the `post_delete_network_interface` interceptor.
        When both interceptors are used, this `post_delete_network_interface_with_metadata` interceptor runs after the
        `post_delete_network_interface` interceptor. The (possibly modified) response returned by
        `post_delete_network_interface` will be passed to
        `post_delete_network_interface_with_metadata`.
        """
        return response, metadata

    def pre_detach_disk(
        self,
        request: compute.DetachDiskInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DetachDiskInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for detach_disk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_detach_disk(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for detach_disk

        DEPRECATED. Please use the `post_detach_disk_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_detach_disk` interceptor runs
        before the `post_detach_disk_with_metadata` interceptor.
        """
        return response

    def post_detach_disk_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for detach_disk

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_detach_disk_with_metadata`
        interceptor in new development instead of the `post_detach_disk` interceptor.
        When both interceptors are used, this `post_detach_disk_with_metadata` interceptor runs after the
        `post_detach_disk` interceptor. The (possibly modified) response returned by
        `post_detach_disk` will be passed to
        `post_detach_disk_with_metadata`.
        """
        return response, metadata

    def pre_get(
        self,
        request: compute.GetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.GetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get(self, response: compute.Instance) -> compute.Instance:
        """Post-rpc interceptor for get

        DEPRECATED. Please use the `post_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get` interceptor runs
        before the `post_get_with_metadata` interceptor.
        """
        return response

    def post_get_with_metadata(
        self,
        response: compute.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_with_metadata`
        interceptor in new development instead of the `post_get` interceptor.
        When both interceptors are used, this `post_get_with_metadata` interceptor runs after the
        `post_get` interceptor. The (possibly modified) response returned by
        `post_get` will be passed to
        `post_get_with_metadata`.
        """
        return response, metadata

    def pre_get_effective_firewalls(
        self,
        request: compute.GetEffectiveFirewallsInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetEffectiveFirewallsInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_effective_firewalls

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get_effective_firewalls(
        self, response: compute.InstancesGetEffectiveFirewallsResponse
    ) -> compute.InstancesGetEffectiveFirewallsResponse:
        """Post-rpc interceptor for get_effective_firewalls

        DEPRECATED. Please use the `post_get_effective_firewalls_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get_effective_firewalls` interceptor runs
        before the `post_get_effective_firewalls_with_metadata` interceptor.
        """
        return response

    def post_get_effective_firewalls_with_metadata(
        self,
        response: compute.InstancesGetEffectiveFirewallsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.InstancesGetEffectiveFirewallsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_effective_firewalls

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_effective_firewalls_with_metadata`
        interceptor in new development instead of the `post_get_effective_firewalls` interceptor.
        When both interceptors are used, this `post_get_effective_firewalls_with_metadata` interceptor runs after the
        `post_get_effective_firewalls` interceptor. The (possibly modified) response returned by
        `post_get_effective_firewalls` will be passed to
        `post_get_effective_firewalls_with_metadata`.
        """
        return response, metadata

    def pre_get_guest_attributes(
        self,
        request: compute.GetGuestAttributesInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetGuestAttributesInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_guest_attributes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get_guest_attributes(
        self, response: compute.GuestAttributes
    ) -> compute.GuestAttributes:
        """Post-rpc interceptor for get_guest_attributes

        DEPRECATED. Please use the `post_get_guest_attributes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get_guest_attributes` interceptor runs
        before the `post_get_guest_attributes_with_metadata` interceptor.
        """
        return response

    def post_get_guest_attributes_with_metadata(
        self,
        response: compute.GuestAttributes,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.GuestAttributes, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_guest_attributes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_guest_attributes_with_metadata`
        interceptor in new development instead of the `post_get_guest_attributes` interceptor.
        When both interceptors are used, this `post_get_guest_attributes_with_metadata` interceptor runs after the
        `post_get_guest_attributes` interceptor. The (possibly modified) response returned by
        `post_get_guest_attributes` will be passed to
        `post_get_guest_attributes_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: compute.GetIamPolicyInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetIamPolicyInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: compute.Policy) -> compute.Policy:
        """Post-rpc interceptor for get_iam_policy

        DEPRECATED. Please use the `post_get_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get_iam_policy` interceptor runs
        before the `post_get_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_get_iam_policy_with_metadata(
        self,
        response: compute.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy` interceptor.
        When both interceptors are used, this `post_get_iam_policy_with_metadata` interceptor runs after the
        `post_get_iam_policy` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy` will be passed to
        `post_get_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_screenshot(
        self,
        request: compute.GetScreenshotInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetScreenshotInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_screenshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get_screenshot(self, response: compute.Screenshot) -> compute.Screenshot:
        """Post-rpc interceptor for get_screenshot

        DEPRECATED. Please use the `post_get_screenshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get_screenshot` interceptor runs
        before the `post_get_screenshot_with_metadata` interceptor.
        """
        return response

    def post_get_screenshot_with_metadata(
        self,
        response: compute.Screenshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Screenshot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_screenshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_screenshot_with_metadata`
        interceptor in new development instead of the `post_get_screenshot` interceptor.
        When both interceptors are used, this `post_get_screenshot_with_metadata` interceptor runs after the
        `post_get_screenshot` interceptor. The (possibly modified) response returned by
        `post_get_screenshot` will be passed to
        `post_get_screenshot_with_metadata`.
        """
        return response, metadata

    def pre_get_serial_port_output(
        self,
        request: compute.GetSerialPortOutputInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetSerialPortOutputInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_serial_port_output

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get_serial_port_output(
        self, response: compute.SerialPortOutput
    ) -> compute.SerialPortOutput:
        """Post-rpc interceptor for get_serial_port_output

        DEPRECATED. Please use the `post_get_serial_port_output_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get_serial_port_output` interceptor runs
        before the `post_get_serial_port_output_with_metadata` interceptor.
        """
        return response

    def post_get_serial_port_output_with_metadata(
        self,
        response: compute.SerialPortOutput,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SerialPortOutput, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_serial_port_output

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_serial_port_output_with_metadata`
        interceptor in new development instead of the `post_get_serial_port_output` interceptor.
        When both interceptors are used, this `post_get_serial_port_output_with_metadata` interceptor runs after the
        `post_get_serial_port_output` interceptor. The (possibly modified) response returned by
        `post_get_serial_port_output` will be passed to
        `post_get_serial_port_output_with_metadata`.
        """
        return response, metadata

    def pre_get_shielded_instance_identity(
        self,
        request: compute.GetShieldedInstanceIdentityInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetShieldedInstanceIdentityInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_shielded_instance_identity

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_get_shielded_instance_identity(
        self, response: compute.ShieldedInstanceIdentity
    ) -> compute.ShieldedInstanceIdentity:
        """Post-rpc interceptor for get_shielded_instance_identity

        DEPRECATED. Please use the `post_get_shielded_instance_identity_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_get_shielded_instance_identity` interceptor runs
        before the `post_get_shielded_instance_identity_with_metadata` interceptor.
        """
        return response

    def post_get_shielded_instance_identity_with_metadata(
        self,
        response: compute.ShieldedInstanceIdentity,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ShieldedInstanceIdentity, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_shielded_instance_identity

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_get_shielded_instance_identity_with_metadata`
        interceptor in new development instead of the `post_get_shielded_instance_identity` interceptor.
        When both interceptors are used, this `post_get_shielded_instance_identity_with_metadata` interceptor runs after the
        `post_get_shielded_instance_identity` interceptor. The (possibly modified) response returned by
        `post_get_shielded_instance_identity` will be passed to
        `post_get_shielded_instance_identity_with_metadata`.
        """
        return response, metadata

    def pre_insert(
        self,
        request: compute.InsertInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.InsertInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_insert(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for insert

        DEPRECATED. Please use the `post_insert_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_insert` interceptor runs
        before the `post_insert_with_metadata` interceptor.
        """
        return response

    def post_insert_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_insert_with_metadata`
        interceptor in new development instead of the `post_insert` interceptor.
        When both interceptors are used, this `post_insert_with_metadata` interceptor runs after the
        `post_insert` interceptor. The (possibly modified) response returned by
        `post_insert` will be passed to
        `post_insert_with_metadata`.
        """
        return response, metadata

    def pre_list(
        self,
        request: compute.ListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.ListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_list(self, response: compute.InstanceList) -> compute.InstanceList:
        """Post-rpc interceptor for list

        DEPRECATED. Please use the `post_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_list` interceptor runs
        before the `post_list_with_metadata` interceptor.
        """
        return response

    def post_list_with_metadata(
        self,
        response: compute.InstanceList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.InstanceList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_list_with_metadata`
        interceptor in new development instead of the `post_list` interceptor.
        When both interceptors are used, this `post_list_with_metadata` interceptor runs after the
        `post_list` interceptor. The (possibly modified) response returned by
        `post_list` will be passed to
        `post_list_with_metadata`.
        """
        return response, metadata

    def pre_list_referrers(
        self,
        request: compute.ListReferrersInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListReferrersInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_referrers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_list_referrers(
        self, response: compute.InstanceListReferrers
    ) -> compute.InstanceListReferrers:
        """Post-rpc interceptor for list_referrers

        DEPRECATED. Please use the `post_list_referrers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_list_referrers` interceptor runs
        before the `post_list_referrers_with_metadata` interceptor.
        """
        return response

    def post_list_referrers_with_metadata(
        self,
        response: compute.InstanceListReferrers,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.InstanceListReferrers, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_referrers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_list_referrers_with_metadata`
        interceptor in new development instead of the `post_list_referrers` interceptor.
        When both interceptors are used, this `post_list_referrers_with_metadata` interceptor runs after the
        `post_list_referrers` interceptor. The (possibly modified) response returned by
        `post_list_referrers` will be passed to
        `post_list_referrers_with_metadata`.
        """
        return response, metadata

    def pre_perform_maintenance(
        self,
        request: compute.PerformMaintenanceInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.PerformMaintenanceInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for perform_maintenance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_perform_maintenance(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for perform_maintenance

        DEPRECATED. Please use the `post_perform_maintenance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_perform_maintenance` interceptor runs
        before the `post_perform_maintenance_with_metadata` interceptor.
        """
        return response

    def post_perform_maintenance_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for perform_maintenance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_perform_maintenance_with_metadata`
        interceptor in new development instead of the `post_perform_maintenance` interceptor.
        When both interceptors are used, this `post_perform_maintenance_with_metadata` interceptor runs after the
        `post_perform_maintenance` interceptor. The (possibly modified) response returned by
        `post_perform_maintenance` will be passed to
        `post_perform_maintenance_with_metadata`.
        """
        return response, metadata

    def pre_remove_resource_policies(
        self,
        request: compute.RemoveResourcePoliciesInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.RemoveResourcePoliciesInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_resource_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_remove_resource_policies(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for remove_resource_policies

        DEPRECATED. Please use the `post_remove_resource_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_remove_resource_policies` interceptor runs
        before the `post_remove_resource_policies_with_metadata` interceptor.
        """
        return response

    def post_remove_resource_policies_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_resource_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_remove_resource_policies_with_metadata`
        interceptor in new development instead of the `post_remove_resource_policies` interceptor.
        When both interceptors are used, this `post_remove_resource_policies_with_metadata` interceptor runs after the
        `post_remove_resource_policies` interceptor. The (possibly modified) response returned by
        `post_remove_resource_policies` will be passed to
        `post_remove_resource_policies_with_metadata`.
        """
        return response, metadata

    def pre_report_host_as_faulty(
        self,
        request: compute.ReportHostAsFaultyInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ReportHostAsFaultyInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for report_host_as_faulty

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_report_host_as_faulty(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for report_host_as_faulty

        DEPRECATED. Please use the `post_report_host_as_faulty_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_report_host_as_faulty` interceptor runs
        before the `post_report_host_as_faulty_with_metadata` interceptor.
        """
        return response

    def post_report_host_as_faulty_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for report_host_as_faulty

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_report_host_as_faulty_with_metadata`
        interceptor in new development instead of the `post_report_host_as_faulty` interceptor.
        When both interceptors are used, this `post_report_host_as_faulty_with_metadata` interceptor runs after the
        `post_report_host_as_faulty` interceptor. The (possibly modified) response returned by
        `post_report_host_as_faulty` will be passed to
        `post_report_host_as_faulty_with_metadata`.
        """
        return response, metadata

    def pre_reset(
        self,
        request: compute.ResetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.ResetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for reset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_reset(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for reset

        DEPRECATED. Please use the `post_reset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_reset` interceptor runs
        before the `post_reset_with_metadata` interceptor.
        """
        return response

    def post_reset_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_reset_with_metadata`
        interceptor in new development instead of the `post_reset` interceptor.
        When both interceptors are used, this `post_reset_with_metadata` interceptor runs after the
        `post_reset` interceptor. The (possibly modified) response returned by
        `post_reset` will be passed to
        `post_reset_with_metadata`.
        """
        return response, metadata

    def pre_resume(
        self,
        request: compute.ResumeInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.ResumeInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for resume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_resume(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for resume

        DEPRECATED. Please use the `post_resume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_resume` interceptor runs
        before the `post_resume_with_metadata` interceptor.
        """
        return response

    def post_resume_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_resume_with_metadata`
        interceptor in new development instead of the `post_resume` interceptor.
        When both interceptors are used, this `post_resume_with_metadata` interceptor runs after the
        `post_resume` interceptor. The (possibly modified) response returned by
        `post_resume` will be passed to
        `post_resume_with_metadata`.
        """
        return response, metadata

    def pre_send_diagnostic_interrupt(
        self,
        request: compute.SendDiagnosticInterruptInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SendDiagnosticInterruptInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for send_diagnostic_interrupt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_send_diagnostic_interrupt(
        self, response: compute.SendDiagnosticInterruptInstanceResponse
    ) -> compute.SendDiagnosticInterruptInstanceResponse:
        """Post-rpc interceptor for send_diagnostic_interrupt

        DEPRECATED. Please use the `post_send_diagnostic_interrupt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_send_diagnostic_interrupt` interceptor runs
        before the `post_send_diagnostic_interrupt_with_metadata` interceptor.
        """
        return response

    def post_send_diagnostic_interrupt_with_metadata(
        self,
        response: compute.SendDiagnosticInterruptInstanceResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SendDiagnosticInterruptInstanceResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for send_diagnostic_interrupt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_send_diagnostic_interrupt_with_metadata`
        interceptor in new development instead of the `post_send_diagnostic_interrupt` interceptor.
        When both interceptors are used, this `post_send_diagnostic_interrupt_with_metadata` interceptor runs after the
        `post_send_diagnostic_interrupt` interceptor. The (possibly modified) response returned by
        `post_send_diagnostic_interrupt` will be passed to
        `post_send_diagnostic_interrupt_with_metadata`.
        """
        return response, metadata

    def pre_set_deletion_protection(
        self,
        request: compute.SetDeletionProtectionInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetDeletionProtectionInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_deletion_protection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_deletion_protection(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_deletion_protection

        DEPRECATED. Please use the `post_set_deletion_protection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_deletion_protection` interceptor runs
        before the `post_set_deletion_protection_with_metadata` interceptor.
        """
        return response

    def post_set_deletion_protection_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_deletion_protection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_deletion_protection_with_metadata`
        interceptor in new development instead of the `post_set_deletion_protection` interceptor.
        When both interceptors are used, this `post_set_deletion_protection_with_metadata` interceptor runs after the
        `post_set_deletion_protection` interceptor. The (possibly modified) response returned by
        `post_set_deletion_protection` will be passed to
        `post_set_deletion_protection_with_metadata`.
        """
        return response, metadata

    def pre_set_disk_auto_delete(
        self,
        request: compute.SetDiskAutoDeleteInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetDiskAutoDeleteInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_disk_auto_delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_disk_auto_delete(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_disk_auto_delete

        DEPRECATED. Please use the `post_set_disk_auto_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_disk_auto_delete` interceptor runs
        before the `post_set_disk_auto_delete_with_metadata` interceptor.
        """
        return response

    def post_set_disk_auto_delete_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_disk_auto_delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_disk_auto_delete_with_metadata`
        interceptor in new development instead of the `post_set_disk_auto_delete` interceptor.
        When both interceptors are used, this `post_set_disk_auto_delete_with_metadata` interceptor runs after the
        `post_set_disk_auto_delete` interceptor. The (possibly modified) response returned by
        `post_set_disk_auto_delete` will be passed to
        `post_set_disk_auto_delete_with_metadata`.
        """
        return response, metadata

    def pre_set_iam_policy(
        self,
        request: compute.SetIamPolicyInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetIamPolicyInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: compute.Policy) -> compute.Policy:
        """Post-rpc interceptor for set_iam_policy

        DEPRECATED. Please use the `post_set_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_iam_policy` interceptor runs
        before the `post_set_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_set_iam_policy_with_metadata(
        self,
        response: compute.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_iam_policy_with_metadata`
        interceptor in new development instead of the `post_set_iam_policy` interceptor.
        When both interceptors are used, this `post_set_iam_policy_with_metadata` interceptor runs after the
        `post_set_iam_policy` interceptor. The (possibly modified) response returned by
        `post_set_iam_policy` will be passed to
        `post_set_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_set_labels(
        self,
        request: compute.SetLabelsInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetLabelsInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_labels(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_labels

        DEPRECATED. Please use the `post_set_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_labels` interceptor runs
        before the `post_set_labels_with_metadata` interceptor.
        """
        return response

    def post_set_labels_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_labels_with_metadata`
        interceptor in new development instead of the `post_set_labels` interceptor.
        When both interceptors are used, this `post_set_labels_with_metadata` interceptor runs after the
        `post_set_labels` interceptor. The (possibly modified) response returned by
        `post_set_labels` will be passed to
        `post_set_labels_with_metadata`.
        """
        return response, metadata

    def pre_set_machine_resources(
        self,
        request: compute.SetMachineResourcesInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetMachineResourcesInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_machine_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_machine_resources(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_machine_resources

        DEPRECATED. Please use the `post_set_machine_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_machine_resources` interceptor runs
        before the `post_set_machine_resources_with_metadata` interceptor.
        """
        return response

    def post_set_machine_resources_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_machine_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_machine_resources_with_metadata`
        interceptor in new development instead of the `post_set_machine_resources` interceptor.
        When both interceptors are used, this `post_set_machine_resources_with_metadata` interceptor runs after the
        `post_set_machine_resources` interceptor. The (possibly modified) response returned by
        `post_set_machine_resources` will be passed to
        `post_set_machine_resources_with_metadata`.
        """
        return response, metadata

    def pre_set_machine_type(
        self,
        request: compute.SetMachineTypeInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetMachineTypeInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_machine_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_machine_type(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_machine_type

        DEPRECATED. Please use the `post_set_machine_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_machine_type` interceptor runs
        before the `post_set_machine_type_with_metadata` interceptor.
        """
        return response

    def post_set_machine_type_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_machine_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_machine_type_with_metadata`
        interceptor in new development instead of the `post_set_machine_type` interceptor.
        When both interceptors are used, this `post_set_machine_type_with_metadata` interceptor runs after the
        `post_set_machine_type` interceptor. The (possibly modified) response returned by
        `post_set_machine_type` will be passed to
        `post_set_machine_type_with_metadata`.
        """
        return response, metadata

    def pre_set_metadata(
        self,
        request: compute.SetMetadataInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetMetadataInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_metadata

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_metadata(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_metadata

        DEPRECATED. Please use the `post_set_metadata_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_metadata` interceptor runs
        before the `post_set_metadata_with_metadata` interceptor.
        """
        return response

    def post_set_metadata_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_metadata

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_metadata_with_metadata`
        interceptor in new development instead of the `post_set_metadata` interceptor.
        When both interceptors are used, this `post_set_metadata_with_metadata` interceptor runs after the
        `post_set_metadata` interceptor. The (possibly modified) response returned by
        `post_set_metadata` will be passed to
        `post_set_metadata_with_metadata`.
        """
        return response, metadata

    def pre_set_min_cpu_platform(
        self,
        request: compute.SetMinCpuPlatformInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetMinCpuPlatformInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_min_cpu_platform

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_min_cpu_platform(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_min_cpu_platform

        DEPRECATED. Please use the `post_set_min_cpu_platform_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_min_cpu_platform` interceptor runs
        before the `post_set_min_cpu_platform_with_metadata` interceptor.
        """
        return response

    def post_set_min_cpu_platform_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_min_cpu_platform

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_min_cpu_platform_with_metadata`
        interceptor in new development instead of the `post_set_min_cpu_platform` interceptor.
        When both interceptors are used, this `post_set_min_cpu_platform_with_metadata` interceptor runs after the
        `post_set_min_cpu_platform` interceptor. The (possibly modified) response returned by
        `post_set_min_cpu_platform` will be passed to
        `post_set_min_cpu_platform_with_metadata`.
        """
        return response, metadata

    def pre_set_name(
        self,
        request: compute.SetNameInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SetNameInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for set_name

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_name(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_name

        DEPRECATED. Please use the `post_set_name_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_name` interceptor runs
        before the `post_set_name_with_metadata` interceptor.
        """
        return response

    def post_set_name_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_name

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_name_with_metadata`
        interceptor in new development instead of the `post_set_name` interceptor.
        When both interceptors are used, this `post_set_name_with_metadata` interceptor runs after the
        `post_set_name` interceptor. The (possibly modified) response returned by
        `post_set_name` will be passed to
        `post_set_name_with_metadata`.
        """
        return response, metadata

    def pre_set_scheduling(
        self,
        request: compute.SetSchedulingInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetSchedulingInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_scheduling

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_scheduling(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_scheduling

        DEPRECATED. Please use the `post_set_scheduling_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_scheduling` interceptor runs
        before the `post_set_scheduling_with_metadata` interceptor.
        """
        return response

    def post_set_scheduling_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_scheduling

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_scheduling_with_metadata`
        interceptor in new development instead of the `post_set_scheduling` interceptor.
        When both interceptors are used, this `post_set_scheduling_with_metadata` interceptor runs after the
        `post_set_scheduling` interceptor. The (possibly modified) response returned by
        `post_set_scheduling` will be passed to
        `post_set_scheduling_with_metadata`.
        """
        return response, metadata

    def pre_set_security_policy(
        self,
        request: compute.SetSecurityPolicyInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetSecurityPolicyInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_security_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_security_policy(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_security_policy

        DEPRECATED. Please use the `post_set_security_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_security_policy` interceptor runs
        before the `post_set_security_policy_with_metadata` interceptor.
        """
        return response

    def post_set_security_policy_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_security_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_security_policy_with_metadata`
        interceptor in new development instead of the `post_set_security_policy` interceptor.
        When both interceptors are used, this `post_set_security_policy_with_metadata` interceptor runs after the
        `post_set_security_policy` interceptor. The (possibly modified) response returned by
        `post_set_security_policy` will be passed to
        `post_set_security_policy_with_metadata`.
        """
        return response, metadata

    def pre_set_service_account(
        self,
        request: compute.SetServiceAccountInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetServiceAccountInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_service_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_service_account(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_service_account

        DEPRECATED. Please use the `post_set_service_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_service_account` interceptor runs
        before the `post_set_service_account_with_metadata` interceptor.
        """
        return response

    def post_set_service_account_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_service_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_service_account_with_metadata`
        interceptor in new development instead of the `post_set_service_account` interceptor.
        When both interceptors are used, this `post_set_service_account_with_metadata` interceptor runs after the
        `post_set_service_account` interceptor. The (possibly modified) response returned by
        `post_set_service_account` will be passed to
        `post_set_service_account_with_metadata`.
        """
        return response, metadata

    def pre_set_shielded_instance_integrity_policy(
        self,
        request: compute.SetShieldedInstanceIntegrityPolicyInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetShieldedInstanceIntegrityPolicyInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_shielded_instance_integrity_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_shielded_instance_integrity_policy(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_shielded_instance_integrity_policy

        DEPRECATED. Please use the `post_set_shielded_instance_integrity_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_shielded_instance_integrity_policy` interceptor runs
        before the `post_set_shielded_instance_integrity_policy_with_metadata` interceptor.
        """
        return response

    def post_set_shielded_instance_integrity_policy_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_shielded_instance_integrity_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_shielded_instance_integrity_policy_with_metadata`
        interceptor in new development instead of the `post_set_shielded_instance_integrity_policy` interceptor.
        When both interceptors are used, this `post_set_shielded_instance_integrity_policy_with_metadata` interceptor runs after the
        `post_set_shielded_instance_integrity_policy` interceptor. The (possibly modified) response returned by
        `post_set_shielded_instance_integrity_policy` will be passed to
        `post_set_shielded_instance_integrity_policy_with_metadata`.
        """
        return response, metadata

    def pre_set_tags(
        self,
        request: compute.SetTagsInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SetTagsInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for set_tags

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_set_tags(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_tags

        DEPRECATED. Please use the `post_set_tags_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_set_tags` interceptor runs
        before the `post_set_tags_with_metadata` interceptor.
        """
        return response

    def post_set_tags_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_tags

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_set_tags_with_metadata`
        interceptor in new development instead of the `post_set_tags` interceptor.
        When both interceptors are used, this `post_set_tags_with_metadata` interceptor runs after the
        `post_set_tags` interceptor. The (possibly modified) response returned by
        `post_set_tags` will be passed to
        `post_set_tags_with_metadata`.
        """
        return response, metadata

    def pre_simulate_maintenance_event(
        self,
        request: compute.SimulateMaintenanceEventInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SimulateMaintenanceEventInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for simulate_maintenance_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_simulate_maintenance_event(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for simulate_maintenance_event

        DEPRECATED. Please use the `post_simulate_maintenance_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_simulate_maintenance_event` interceptor runs
        before the `post_simulate_maintenance_event_with_metadata` interceptor.
        """
        return response

    def post_simulate_maintenance_event_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for simulate_maintenance_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_simulate_maintenance_event_with_metadata`
        interceptor in new development instead of the `post_simulate_maintenance_event` interceptor.
        When both interceptors are used, this `post_simulate_maintenance_event_with_metadata` interceptor runs after the
        `post_simulate_maintenance_event` interceptor. The (possibly modified) response returned by
        `post_simulate_maintenance_event` will be passed to
        `post_simulate_maintenance_event_with_metadata`.
        """
        return response, metadata

    def pre_start(
        self,
        request: compute.StartInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.StartInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for start

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_start(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for start

        DEPRECATED. Please use the `post_start_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_start` interceptor runs
        before the `post_start_with_metadata` interceptor.
        """
        return response

    def post_start_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_start_with_metadata`
        interceptor in new development instead of the `post_start` interceptor.
        When both interceptors are used, this `post_start_with_metadata` interceptor runs after the
        `post_start` interceptor. The (possibly modified) response returned by
        `post_start` will be passed to
        `post_start_with_metadata`.
        """
        return response, metadata

    def pre_start_with_encryption_key(
        self,
        request: compute.StartWithEncryptionKeyInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.StartWithEncryptionKeyInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_with_encryption_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_start_with_encryption_key(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for start_with_encryption_key

        DEPRECATED. Please use the `post_start_with_encryption_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_start_with_encryption_key` interceptor runs
        before the `post_start_with_encryption_key_with_metadata` interceptor.
        """
        return response

    def post_start_with_encryption_key_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_with_encryption_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_start_with_encryption_key_with_metadata`
        interceptor in new development instead of the `post_start_with_encryption_key` interceptor.
        When both interceptors are used, this `post_start_with_encryption_key_with_metadata` interceptor runs after the
        `post_start_with_encryption_key` interceptor. The (possibly modified) response returned by
        `post_start_with_encryption_key` will be passed to
        `post_start_with_encryption_key_with_metadata`.
        """
        return response, metadata

    def pre_stop(
        self,
        request: compute.StopInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.StopInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for stop

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_stop(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for stop

        DEPRECATED. Please use the `post_stop_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_stop` interceptor runs
        before the `post_stop_with_metadata` interceptor.
        """
        return response

    def post_stop_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_stop_with_metadata`
        interceptor in new development instead of the `post_stop` interceptor.
        When both interceptors are used, this `post_stop_with_metadata` interceptor runs after the
        `post_stop` interceptor. The (possibly modified) response returned by
        `post_stop` will be passed to
        `post_stop_with_metadata`.
        """
        return response, metadata

    def pre_suspend(
        self,
        request: compute.SuspendInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.SuspendInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for suspend

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_suspend(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for suspend

        DEPRECATED. Please use the `post_suspend_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_suspend` interceptor runs
        before the `post_suspend_with_metadata` interceptor.
        """
        return response

    def post_suspend_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for suspend

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_suspend_with_metadata`
        interceptor in new development instead of the `post_suspend` interceptor.
        When both interceptors are used, this `post_suspend_with_metadata` interceptor runs after the
        `post_suspend` interceptor. The (possibly modified) response returned by
        `post_suspend` will be passed to
        `post_suspend_with_metadata`.
        """
        return response, metadata

    def pre_test_iam_permissions(
        self,
        request: compute.TestIamPermissionsInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.TestIamPermissionsInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: compute.TestPermissionsResponse
    ) -> compute.TestPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_test_iam_permissions` interceptor runs
        before the `post_test_iam_permissions_with_metadata` interceptor.
        """
        return response

    def post_test_iam_permissions_with_metadata(
        self,
        response: compute.TestPermissionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.TestPermissionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata

    def pre_update(
        self,
        request: compute.UpdateInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.UpdateInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_update(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for update

        DEPRECATED. Please use the `post_update_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_update` interceptor runs
        before the `post_update_with_metadata` interceptor.
        """
        return response

    def post_update_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_update_with_metadata`
        interceptor in new development instead of the `post_update` interceptor.
        When both interceptors are used, this `post_update_with_metadata` interceptor runs after the
        `post_update` interceptor. The (possibly modified) response returned by
        `post_update` will be passed to
        `post_update_with_metadata`.
        """
        return response, metadata

    def pre_update_access_config(
        self,
        request: compute.UpdateAccessConfigInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.UpdateAccessConfigInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_access_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_update_access_config(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for update_access_config

        DEPRECATED. Please use the `post_update_access_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_update_access_config` interceptor runs
        before the `post_update_access_config_with_metadata` interceptor.
        """
        return response

    def post_update_access_config_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_access_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_update_access_config_with_metadata`
        interceptor in new development instead of the `post_update_access_config` interceptor.
        When both interceptors are used, this `post_update_access_config_with_metadata` interceptor runs after the
        `post_update_access_config` interceptor. The (possibly modified) response returned by
        `post_update_access_config` will be passed to
        `post_update_access_config_with_metadata`.
        """
        return response, metadata

    def pre_update_display_device(
        self,
        request: compute.UpdateDisplayDeviceInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.UpdateDisplayDeviceInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_display_device

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_update_display_device(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for update_display_device

        DEPRECATED. Please use the `post_update_display_device_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_update_display_device` interceptor runs
        before the `post_update_display_device_with_metadata` interceptor.
        """
        return response

    def post_update_display_device_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_display_device

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_update_display_device_with_metadata`
        interceptor in new development instead of the `post_update_display_device` interceptor.
        When both interceptors are used, this `post_update_display_device_with_metadata` interceptor runs after the
        `post_update_display_device` interceptor. The (possibly modified) response returned by
        `post_update_display_device` will be passed to
        `post_update_display_device_with_metadata`.
        """
        return response, metadata

    def pre_update_network_interface(
        self,
        request: compute.UpdateNetworkInterfaceInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.UpdateNetworkInterfaceInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_network_interface

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_update_network_interface(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for update_network_interface

        DEPRECATED. Please use the `post_update_network_interface_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_update_network_interface` interceptor runs
        before the `post_update_network_interface_with_metadata` interceptor.
        """
        return response

    def post_update_network_interface_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_network_interface

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_update_network_interface_with_metadata`
        interceptor in new development instead of the `post_update_network_interface` interceptor.
        When both interceptors are used, this `post_update_network_interface_with_metadata` interceptor runs after the
        `post_update_network_interface` interceptor. The (possibly modified) response returned by
        `post_update_network_interface` will be passed to
        `post_update_network_interface_with_metadata`.
        """
        return response, metadata

    def pre_update_shielded_instance_config(
        self,
        request: compute.UpdateShieldedInstanceConfigInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.UpdateShieldedInstanceConfigInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_shielded_instance_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Instances server.
        """
        return request, metadata

    def post_update_shielded_instance_config(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for update_shielded_instance_config

        DEPRECATED. Please use the `post_update_shielded_instance_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Instances server but before
        it is returned to user code. This `post_update_shielded_instance_config` interceptor runs
        before the `post_update_shielded_instance_config_with_metadata` interceptor.
        """
        return response

    def post_update_shielded_instance_config_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_shielded_instance_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Instances server but before it is returned to user code.

        We recommend only using this `post_update_shielded_instance_config_with_metadata`
        interceptor in new development instead of the `post_update_shielded_instance_config` interceptor.
        When both interceptors are used, this `post_update_shielded_instance_config_with_metadata` interceptor runs after the
        `post_update_shielded_instance_config` interceptor. The (possibly modified) response returned by
        `post_update_shielded_instance_config` will be passed to
        `post_update_shielded_instance_config_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class InstancesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: InstancesRestInterceptor


class InstancesRestTransport(_BaseInstancesRestTransport):
    """REST backend synchronous transport for Instances.

    The Instances API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[InstancesRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'compute.googleapis.com').
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
             interceptor (Optional[InstancesRestInterceptor]): Interceptor used
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
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or InstancesRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AddAccessConfig(
        _BaseInstancesRestTransport._BaseAddAccessConfig, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.AddAccessConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AddAccessConfigInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the add access config method over HTTP.

            Args:
                request (~.compute.AddAccessConfigInstanceRequest):
                    The request object. A request message for
                Instances.AddAccessConfig. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseAddAccessConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_add_access_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseAddAccessConfig,
                    "_BaseAddAccessConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.AddAccessConfig",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AddAccessConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._AddAccessConfig._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_access_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_access_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.add_access_config",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AddAccessConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddNetworkInterface(
        _BaseInstancesRestTransport._BaseAddNetworkInterface, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.AddNetworkInterface")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AddNetworkInterfaceInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the add network interface method over HTTP.

            Args:
                request (~.compute.AddNetworkInterfaceInstanceRequest):
                    The request object. A request message for
                Instances.AddNetworkInterface. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseAddNetworkInterface._get_http_options()
            )
            request, metadata = self._interceptor.pre_add_network_interface(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseAddNetworkInterface,
                    "_BaseAddNetworkInterface__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.AddNetworkInterface",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AddNetworkInterface",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._AddNetworkInterface._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_network_interface(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_network_interface_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.add_network_interface",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AddNetworkInterface",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddResourcePolicies(
        _BaseInstancesRestTransport._BaseAddResourcePolicies, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.AddResourcePolicies")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AddResourcePoliciesInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the add resource policies method over HTTP.

            Args:
                request (~.compute.AddResourcePoliciesInstanceRequest):
                    The request object. A request message for
                Instances.AddResourcePolicies. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseAddResourcePolicies._get_http_options()
            )
            request, metadata = self._interceptor.pre_add_resource_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseAddResourcePolicies,
                    "_BaseAddResourcePolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.AddResourcePolicies",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AddResourcePolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._AddResourcePolicies._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_resource_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_resource_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.add_resource_policies",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AddResourcePolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AggregatedList(
        _BaseInstancesRestTransport._BaseAggregatedList, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.AggregatedList")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AggregatedListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.InstanceAggregatedList:
            r"""Call the aggregated list method over HTTP.

            Args:
                request (~.compute.AggregatedListInstancesRequest):
                    The request object. A request message for
                Instances.AggregatedList. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.InstanceAggregatedList:

            """

            http_options = (
                _BaseInstancesRestTransport._BaseAggregatedList._get_http_options()
            )
            request, metadata = self._interceptor.pre_aggregated_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseAggregatedList,
                    "_BaseAggregatedList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.AggregatedList",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AggregatedList",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._AggregatedList._get_response(
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
            resp = compute.InstanceAggregatedList()
            pb_resp = compute.InstanceAggregatedList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_aggregated_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_aggregated_list_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.InstanceAggregatedList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.aggregated_list",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AggregatedList",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AttachDisk(_BaseInstancesRestTransport._BaseAttachDisk, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.AttachDisk")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.AttachDiskInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the attach disk method over HTTP.

            Args:
                request (~.compute.AttachDiskInstanceRequest):
                    The request object. A request message for
                Instances.AttachDisk. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseAttachDisk._get_http_options()
            )
            request, metadata = self._interceptor.pre_attach_disk(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseAttachDisk,
                    "_BaseAttachDisk__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.AttachDisk",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AttachDisk",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._AttachDisk._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_attach_disk(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_attach_disk_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.attach_disk",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "AttachDisk",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkInsert(_BaseInstancesRestTransport._BaseBulkInsert, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.BulkInsert")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.BulkInsertInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the bulk insert method over HTTP.

            Args:
                request (~.compute.BulkInsertInstanceRequest):
                    The request object. A request message for
                Instances.BulkInsert. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseBulkInsert._get_http_options()
            )
            request, metadata = self._interceptor.pre_bulk_insert(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseBulkInsert,
                    "_BaseBulkInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.BulkInsert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "BulkInsert",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._BulkInsert._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_bulk_insert(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_insert_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.bulk_insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "BulkInsert",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Delete(_BaseInstancesRestTransport._BaseDelete, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Delete")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.DeleteInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete method over HTTP.

            Args:
                request (~.compute.DeleteInstanceRequest):
                    The request object. A request message for
                Instances.Delete. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseDelete._get_http_options()
            request, metadata = self._interceptor.pre_delete(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseDelete,
                    "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Delete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Delete._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Delete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAccessConfig(
        _BaseInstancesRestTransport._BaseDeleteAccessConfig, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.DeleteAccessConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.DeleteAccessConfigInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete access config method over HTTP.

            Args:
                request (~.compute.DeleteAccessConfigInstanceRequest):
                    The request object. A request message for
                Instances.DeleteAccessConfig. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseDeleteAccessConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_access_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseDeleteAccessConfig,
                    "_BaseDeleteAccessConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.DeleteAccessConfig",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "DeleteAccessConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._DeleteAccessConfig._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_access_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_access_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.delete_access_config",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "DeleteAccessConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNetworkInterface(
        _BaseInstancesRestTransport._BaseDeleteNetworkInterface, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.DeleteNetworkInterface")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.DeleteNetworkInterfaceInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete network interface method over HTTP.

            Args:
                request (~.compute.DeleteNetworkInterfaceInstanceRequest):
                    The request object. A request message for
                Instances.DeleteNetworkInterface. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseDeleteNetworkInterface._get_http_options()
            request, metadata = self._interceptor.pre_delete_network_interface(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseDeleteNetworkInterface,
                    "_BaseDeleteNetworkInterface__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.DeleteNetworkInterface",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "DeleteNetworkInterface",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._DeleteNetworkInterface._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_network_interface(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_network_interface_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.delete_network_interface",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "DeleteNetworkInterface",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DetachDisk(_BaseInstancesRestTransport._BaseDetachDisk, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.DetachDisk")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.DetachDiskInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the detach disk method over HTTP.

            Args:
                request (~.compute.DetachDiskInstanceRequest):
                    The request object. A request message for
                Instances.DetachDisk. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseDetachDisk._get_http_options()
            )
            request, metadata = self._interceptor.pre_detach_disk(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseDetachDisk,
                    "_BaseDetachDisk__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.DetachDisk",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "DetachDisk",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._DetachDisk._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_detach_disk(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_detach_disk_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.detach_disk",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "DetachDisk",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Get(_BaseInstancesRestTransport._BaseGet, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Get")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Instance:
            r"""Call the get method over HTTP.

            Args:
                request (~.compute.GetInstanceRequest):
                    The request object. A request message for Instances.Get.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Instance:
                    Represents an Instance resource.

                An instance is a virtual machine that is
                hosted on Google Cloud Platform. For
                more information, readVirtual Machine
                Instances.

            """

            http_options = _BaseInstancesRestTransport._BaseGet._get_http_options()
            request, metadata = self._interceptor.pre_get(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGet,
                    "_BaseGet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Get",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Get",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Get._get_response(
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
            resp = compute.Instance()
            pb_resp = compute.Instance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.get",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Get",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEffectiveFirewalls(
        _BaseInstancesRestTransport._BaseGetEffectiveFirewalls, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.GetEffectiveFirewalls")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetEffectiveFirewallsInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.InstancesGetEffectiveFirewallsResponse:
            r"""Call the get effective firewalls method over HTTP.

            Args:
                request (~.compute.GetEffectiveFirewallsInstanceRequest):
                    The request object. A request message for
                Instances.GetEffectiveFirewalls. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.InstancesGetEffectiveFirewallsResponse:

            """

            http_options = _BaseInstancesRestTransport._BaseGetEffectiveFirewalls._get_http_options()
            request, metadata = self._interceptor.pre_get_effective_firewalls(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGetEffectiveFirewalls,
                    "_BaseGetEffectiveFirewalls__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.GetEffectiveFirewalls",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetEffectiveFirewalls",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._GetEffectiveFirewalls._get_response(
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
            resp = compute.InstancesGetEffectiveFirewallsResponse()
            pb_resp = compute.InstancesGetEffectiveFirewallsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_effective_firewalls(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_effective_firewalls_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        compute.InstancesGetEffectiveFirewallsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.get_effective_firewalls",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetEffectiveFirewalls",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGuestAttributes(
        _BaseInstancesRestTransport._BaseGetGuestAttributes, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.GetGuestAttributes")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetGuestAttributesInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.GuestAttributes:
            r"""Call the get guest attributes method over HTTP.

            Args:
                request (~.compute.GetGuestAttributesInstanceRequest):
                    The request object. A request message for
                Instances.GetGuestAttributes. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.GuestAttributes:
                    A guest attributes entry.
            """

            http_options = (
                _BaseInstancesRestTransport._BaseGetGuestAttributes._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_guest_attributes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGetGuestAttributes,
                    "_BaseGetGuestAttributes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.GetGuestAttributes",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetGuestAttributes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._GetGuestAttributes._get_response(
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
            resp = compute.GuestAttributes()
            pb_resp = compute.GuestAttributes.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_guest_attributes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_guest_attributes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.GuestAttributes.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.get_guest_attributes",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetGuestAttributes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIamPolicy(
        _BaseInstancesRestTransport._BaseGetIamPolicy, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetIamPolicyInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (~.compute.GetIamPolicyInstanceRequest):
                    The request object. A request message for
                Instances.GetIamPolicy. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGetIamPolicy,
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._GetIamPolicy._get_response(
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
            resp = compute.Policy()
            pb_resp = compute.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iam_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.get_iam_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScreenshot(
        _BaseInstancesRestTransport._BaseGetScreenshot, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.GetScreenshot")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetScreenshotInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Screenshot:
            r"""Call the get screenshot method over HTTP.

            Args:
                request (~.compute.GetScreenshotInstanceRequest):
                    The request object. A request message for
                Instances.GetScreenshot. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Screenshot:
                    An instance's screenshot.
            """

            http_options = (
                _BaseInstancesRestTransport._BaseGetScreenshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_screenshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGetScreenshot,
                    "_BaseGetScreenshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.GetScreenshot",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetScreenshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._GetScreenshot._get_response(
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
            resp = compute.Screenshot()
            pb_resp = compute.Screenshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_screenshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_screenshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Screenshot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.get_screenshot",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetScreenshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSerialPortOutput(
        _BaseInstancesRestTransport._BaseGetSerialPortOutput, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.GetSerialPortOutput")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetSerialPortOutputInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SerialPortOutput:
            r"""Call the get serial port output method over HTTP.

            Args:
                request (~.compute.GetSerialPortOutputInstanceRequest):
                    The request object. A request message for
                Instances.GetSerialPortOutput. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.SerialPortOutput:
                    An instance serial console output.
            """

            http_options = (
                _BaseInstancesRestTransport._BaseGetSerialPortOutput._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_serial_port_output(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGetSerialPortOutput,
                    "_BaseGetSerialPortOutput__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.GetSerialPortOutput",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetSerialPortOutput",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._GetSerialPortOutput._get_response(
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
            resp = compute.SerialPortOutput()
            pb_resp = compute.SerialPortOutput.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_serial_port_output(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_serial_port_output_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.SerialPortOutput.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.get_serial_port_output",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetSerialPortOutput",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetShieldedInstanceIdentity(
        _BaseInstancesRestTransport._BaseGetShieldedInstanceIdentity, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.GetShieldedInstanceIdentity")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.GetShieldedInstanceIdentityInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.ShieldedInstanceIdentity:
            r"""Call the get shielded instance
            identity method over HTTP.

                Args:
                    request (~.compute.GetShieldedInstanceIdentityInstanceRequest):
                        The request object. A request message for
                    Instances.GetShieldedInstanceIdentity.
                    See the method description for details.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.compute.ShieldedInstanceIdentity:
                        A Shielded Instance Identity.
            """

            http_options = _BaseInstancesRestTransport._BaseGetShieldedInstanceIdentity._get_http_options()
            request, metadata = self._interceptor.pre_get_shielded_instance_identity(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseGetShieldedInstanceIdentity,
                    "_BaseGetShieldedInstanceIdentity__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.GetShieldedInstanceIdentity",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetShieldedInstanceIdentity",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InstancesRestTransport._GetShieldedInstanceIdentity._get_response(
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
            resp = compute.ShieldedInstanceIdentity()
            pb_resp = compute.ShieldedInstanceIdentity.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_shielded_instance_identity(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_shielded_instance_identity_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.ShieldedInstanceIdentity.to_json(
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
                    "Received response for google.cloud.compute_v1.InstancesClient.get_shielded_instance_identity",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "GetShieldedInstanceIdentity",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Insert(_BaseInstancesRestTransport._BaseInsert, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Insert")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.InsertInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the insert method over HTTP.

            Args:
                request (~.compute.InsertInstanceRequest):
                    The request object. A request message for
                Instances.Insert. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseInsert._get_http_options()
            request, metadata = self._interceptor.pre_insert(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseInsert,
                    "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Insert",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Insert._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Insert",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _List(_BaseInstancesRestTransport._BaseList, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.List")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.InstanceList:
            r"""Call the list method over HTTP.

            Args:
                request (~.compute.ListInstancesRequest):
                    The request object. A request message for Instances.List.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.InstanceList:
                    Contains a list of instances.
            """

            http_options = _BaseInstancesRestTransport._BaseList._get_http_options()
            request, metadata = self._interceptor.pre_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseList,
                    "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.List",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "List",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._List._get_response(
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
            resp = compute.InstanceList()
            pb_resp = compute.InstanceList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.InstanceList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.list",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "List",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReferrers(
        _BaseInstancesRestTransport._BaseListReferrers, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.ListReferrers")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ListReferrersInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.InstanceListReferrers:
            r"""Call the list referrers method over HTTP.

            Args:
                request (~.compute.ListReferrersInstancesRequest):
                    The request object. A request message for
                Instances.ListReferrers. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.InstanceListReferrers:
                    Contains a list of instance
                referrers.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseListReferrers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_referrers(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseListReferrers,
                    "_BaseListReferrers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.ListReferrers",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "ListReferrers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._ListReferrers._get_response(
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
            resp = compute.InstanceListReferrers()
            pb_resp = compute.InstanceListReferrers.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_referrers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_referrers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.InstanceListReferrers.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.list_referrers",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "ListReferrers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PerformMaintenance(
        _BaseInstancesRestTransport._BasePerformMaintenance, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.PerformMaintenance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.PerformMaintenanceInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the perform maintenance method over HTTP.

            Args:
                request (~.compute.PerformMaintenanceInstanceRequest):
                    The request object. A request message for
                Instances.PerformMaintenance. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BasePerformMaintenance._get_http_options()
            )
            request, metadata = self._interceptor.pre_perform_maintenance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BasePerformMaintenance,
                    "_BasePerformMaintenance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.PerformMaintenance",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "PerformMaintenance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._PerformMaintenance._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_perform_maintenance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_perform_maintenance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.perform_maintenance",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "PerformMaintenance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveResourcePolicies(
        _BaseInstancesRestTransport._BaseRemoveResourcePolicies, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.RemoveResourcePolicies")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.RemoveResourcePoliciesInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the remove resource policies method over HTTP.

            Args:
                request (~.compute.RemoveResourcePoliciesInstanceRequest):
                    The request object. A request message for
                Instances.RemoveResourcePolicies. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseRemoveResourcePolicies._get_http_options()
            request, metadata = self._interceptor.pre_remove_resource_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseRemoveResourcePolicies,
                    "_BaseRemoveResourcePolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.RemoveResourcePolicies",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "RemoveResourcePolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._RemoveResourcePolicies._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_resource_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_resource_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.remove_resource_policies",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "RemoveResourcePolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReportHostAsFaulty(
        _BaseInstancesRestTransport._BaseReportHostAsFaulty, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.ReportHostAsFaulty")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ReportHostAsFaultyInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the report host as faulty method over HTTP.

            Args:
                request (~.compute.ReportHostAsFaultyInstanceRequest):
                    The request object. A request message for
                Instances.ReportHostAsFaulty. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseReportHostAsFaulty._get_http_options()
            )
            request, metadata = self._interceptor.pre_report_host_as_faulty(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseReportHostAsFaulty,
                    "_BaseReportHostAsFaulty__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.ReportHostAsFaulty",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "ReportHostAsFaulty",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._ReportHostAsFaulty._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_report_host_as_faulty(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_report_host_as_faulty_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.report_host_as_faulty",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "ReportHostAsFaulty",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Reset(_BaseInstancesRestTransport._BaseReset, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Reset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ResetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the reset method over HTTP.

            Args:
                request (~.compute.ResetInstanceRequest):
                    The request object. A request message for
                Instances.Reset. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseReset._get_http_options()
            request, metadata = self._interceptor.pre_reset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseReset,
                    "_BaseReset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Reset",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Reset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Reset._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.reset",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Reset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Resume(_BaseInstancesRestTransport._BaseResume, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Resume")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.ResumeInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the resume method over HTTP.

            Args:
                request (~.compute.ResumeInstanceRequest):
                    The request object. A request message for
                Instances.Resume. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseResume._get_http_options()
            request, metadata = self._interceptor.pre_resume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseResume,
                    "_BaseResume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Resume",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Resume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Resume._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_resume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.resume",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Resume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SendDiagnosticInterrupt(
        _BaseInstancesRestTransport._BaseSendDiagnosticInterrupt, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SendDiagnosticInterrupt")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SendDiagnosticInterruptInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.SendDiagnosticInterruptInstanceResponse:
            r"""Call the send diagnostic interrupt method over HTTP.

            Args:
                request (~.compute.SendDiagnosticInterruptInstanceRequest):
                    The request object. A request message for
                Instances.SendDiagnosticInterrupt. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.SendDiagnosticInterruptInstanceResponse:
                    A response message for
                Instances.SendDiagnosticInterrupt. See
                the method description for details.

            """

            http_options = _BaseInstancesRestTransport._BaseSendDiagnosticInterrupt._get_http_options()
            request, metadata = self._interceptor.pre_send_diagnostic_interrupt(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSendDiagnosticInterrupt,
                    "_BaseSendDiagnosticInterrupt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SendDiagnosticInterrupt",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SendDiagnosticInterrupt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SendDiagnosticInterrupt._get_response(
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
            resp = compute.SendDiagnosticInterruptInstanceResponse()
            pb_resp = compute.SendDiagnosticInterruptInstanceResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_send_diagnostic_interrupt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_send_diagnostic_interrupt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        compute.SendDiagnosticInterruptInstanceResponse.to_json(
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
                    "Received response for google.cloud.compute_v1.InstancesClient.send_diagnostic_interrupt",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SendDiagnosticInterrupt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetDeletionProtection(
        _BaseInstancesRestTransport._BaseSetDeletionProtection, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetDeletionProtection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetDeletionProtectionInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set deletion protection method over HTTP.

            Args:
                request (~.compute.SetDeletionProtectionInstanceRequest):
                    The request object. A request message for
                Instances.SetDeletionProtection. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseSetDeletionProtection._get_http_options()
            request, metadata = self._interceptor.pre_set_deletion_protection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetDeletionProtection,
                    "_BaseSetDeletionProtection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetDeletionProtection",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetDeletionProtection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetDeletionProtection._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_deletion_protection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_deletion_protection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_deletion_protection",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetDeletionProtection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetDiskAutoDelete(
        _BaseInstancesRestTransport._BaseSetDiskAutoDelete, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetDiskAutoDelete")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetDiskAutoDeleteInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set disk auto delete method over HTTP.

            Args:
                request (~.compute.SetDiskAutoDeleteInstanceRequest):
                    The request object. A request message for
                Instances.SetDiskAutoDelete. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetDiskAutoDelete._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_disk_auto_delete(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetDiskAutoDelete,
                    "_BaseSetDiskAutoDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetDiskAutoDelete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetDiskAutoDelete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetDiskAutoDelete._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_disk_auto_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_disk_auto_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_disk_auto_delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetDiskAutoDelete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicy(
        _BaseInstancesRestTransport._BaseSetIamPolicy, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetIamPolicyInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (~.compute.SetIamPolicyInstanceRequest):
                    The request object. A request message for
                Instances.SetIamPolicy. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetIamPolicy,
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetIamPolicy._get_response(
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
            resp = compute.Policy()
            pb_resp = compute.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_iam_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_iam_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetLabels(_BaseInstancesRestTransport._BaseSetLabels, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.SetLabels")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetLabelsInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set labels method over HTTP.

            Args:
                request (~.compute.SetLabelsInstanceRequest):
                    The request object. A request message for
                Instances.SetLabels. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetLabels._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_labels(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetLabels,
                    "_BaseSetLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetLabels",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetLabels._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_labels",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMachineResources(
        _BaseInstancesRestTransport._BaseSetMachineResources, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetMachineResources")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetMachineResourcesInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set machine resources method over HTTP.

            Args:
                request (~.compute.SetMachineResourcesInstanceRequest):
                    The request object. A request message for
                Instances.SetMachineResources. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetMachineResources._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_machine_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetMachineResources,
                    "_BaseSetMachineResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetMachineResources",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMachineResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetMachineResources._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_machine_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_machine_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_machine_resources",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMachineResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMachineType(
        _BaseInstancesRestTransport._BaseSetMachineType, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetMachineType")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetMachineTypeInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set machine type method over HTTP.

            Args:
                request (~.compute.SetMachineTypeInstanceRequest):
                    The request object. A request message for
                Instances.SetMachineType. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetMachineType._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_machine_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetMachineType,
                    "_BaseSetMachineType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetMachineType",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMachineType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetMachineType._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_machine_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_machine_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_machine_type",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMachineType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMetadata(_BaseInstancesRestTransport._BaseSetMetadata, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.SetMetadata")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetMetadataInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set metadata method over HTTP.

            Args:
                request (~.compute.SetMetadataInstanceRequest):
                    The request object. A request message for
                Instances.SetMetadata. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetMetadata._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_metadata(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetMetadata,
                    "_BaseSetMetadata__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetMetadata",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMetadata",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetMetadata._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_metadata(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_metadata_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_metadata",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMetadata",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetMinCpuPlatform(
        _BaseInstancesRestTransport._BaseSetMinCpuPlatform, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetMinCpuPlatform")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetMinCpuPlatformInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set min cpu platform method over HTTP.

            Args:
                request (~.compute.SetMinCpuPlatformInstanceRequest):
                    The request object. A request message for
                Instances.SetMinCpuPlatform. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetMinCpuPlatform._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_min_cpu_platform(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetMinCpuPlatform,
                    "_BaseSetMinCpuPlatform__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetMinCpuPlatform",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMinCpuPlatform",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetMinCpuPlatform._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_min_cpu_platform(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_min_cpu_platform_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_min_cpu_platform",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetMinCpuPlatform",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetName(_BaseInstancesRestTransport._BaseSetName, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.SetName")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetNameInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set name method over HTTP.

            Args:
                request (~.compute.SetNameInstanceRequest):
                    The request object. A request message for
                Instances.SetName. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseSetName._get_http_options()
            request, metadata = self._interceptor.pre_set_name(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetName,
                    "_BaseSetName__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetName",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetName",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetName._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_name(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_name_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_name",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetName",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetScheduling(
        _BaseInstancesRestTransport._BaseSetScheduling, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetScheduling")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetSchedulingInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set scheduling method over HTTP.

            Args:
                request (~.compute.SetSchedulingInstanceRequest):
                    The request object. A request message for
                Instances.SetScheduling. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetScheduling._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_scheduling(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetScheduling,
                    "_BaseSetScheduling__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetScheduling",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetScheduling",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetScheduling._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_scheduling(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_scheduling_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_scheduling",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetScheduling",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetSecurityPolicy(
        _BaseInstancesRestTransport._BaseSetSecurityPolicy, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetSecurityPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetSecurityPolicyInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set security policy method over HTTP.

            Args:
                request (~.compute.SetSecurityPolicyInstanceRequest):
                    The request object. A request message for
                Instances.SetSecurityPolicy. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetSecurityPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_security_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetSecurityPolicy,
                    "_BaseSetSecurityPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetSecurityPolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetSecurityPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetSecurityPolicy._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_security_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_security_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_security_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetSecurityPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetServiceAccount(
        _BaseInstancesRestTransport._BaseSetServiceAccount, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetServiceAccount")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetServiceAccountInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set service account method over HTTP.

            Args:
                request (~.compute.SetServiceAccountInstanceRequest):
                    The request object. A request message for
                Instances.SetServiceAccount. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseSetServiceAccount._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_service_account(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetServiceAccount,
                    "_BaseSetServiceAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetServiceAccount",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetServiceAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetServiceAccount._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_service_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_service_account_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_service_account",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetServiceAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetShieldedInstanceIntegrityPolicy(
        _BaseInstancesRestTransport._BaseSetShieldedInstanceIntegrityPolicy,
        InstancesRestStub,
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SetShieldedInstanceIntegrityPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetShieldedInstanceIntegrityPolicyInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set shielded instance
            integrity policy method over HTTP.

                Args:
                    request (~.compute.SetShieldedInstanceIntegrityPolicyInstanceRequest):
                        The request object. A request message for
                    Instances.SetShieldedInstanceIntegrityPolicy.
                    See the method description for details.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.compute.Operation:
                        Represents an Operation resource.

                    Google Compute Engine has three Operation resources:

                    - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                    - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                    - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                    You can use an operation resource to manage asynchronous
                    API requests. For more information, readHandling API
                    responses.

                    Operations can be global, regional or zonal.

                    ::

                       - For global operations, use the `globalOperations`
                       resource.
                       - For regional operations, use the
                       `regionOperations` resource.
                       - For zonal operations, use
                       the `zoneOperations` resource.

                    For more information, read Global, Regional, and Zonal
                    Resources.

                    Note that completed Operation resources have a limited
                    retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseSetShieldedInstanceIntegrityPolicy._get_http_options()
            request, metadata = (
                self._interceptor.pre_set_shielded_instance_integrity_policy(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetShieldedInstanceIntegrityPolicy,
                    "_BaseSetShieldedInstanceIntegrityPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetShieldedInstanceIntegrityPolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetShieldedInstanceIntegrityPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetShieldedInstanceIntegrityPolicy._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_shielded_instance_integrity_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_set_shielded_instance_integrity_policy_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_shielded_instance_integrity_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetShieldedInstanceIntegrityPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetTags(_BaseInstancesRestTransport._BaseSetTags, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.SetTags")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SetTagsInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set tags method over HTTP.

            Args:
                request (~.compute.SetTagsInstanceRequest):
                    The request object. A request message for
                Instances.SetTags. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseSetTags._get_http_options()
            request, metadata = self._interceptor.pre_set_tags(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSetTags,
                    "_BaseSetTags__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SetTags",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetTags",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SetTags._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_tags(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_tags_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.set_tags",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SetTags",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SimulateMaintenanceEvent(
        _BaseInstancesRestTransport._BaseSimulateMaintenanceEvent, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.SimulateMaintenanceEvent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SimulateMaintenanceEventInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the simulate maintenance
            event method over HTTP.

                Args:
                    request (~.compute.SimulateMaintenanceEventInstanceRequest):
                        The request object. A request message for
                    Instances.SimulateMaintenanceEvent. See
                    the method description for details.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.compute.Operation:
                        Represents an Operation resource.

                    Google Compute Engine has three Operation resources:

                    - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                    - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                    - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                    You can use an operation resource to manage asynchronous
                    API requests. For more information, readHandling API
                    responses.

                    Operations can be global, regional or zonal.

                    ::

                       - For global operations, use the `globalOperations`
                       resource.
                       - For regional operations, use the
                       `regionOperations` resource.
                       - For zonal operations, use
                       the `zoneOperations` resource.

                    For more information, read Global, Regional, and Zonal
                    Resources.

                    Note that completed Operation resources have a limited
                    retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseSimulateMaintenanceEvent._get_http_options()
            request, metadata = self._interceptor.pre_simulate_maintenance_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSimulateMaintenanceEvent,
                    "_BaseSimulateMaintenanceEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.SimulateMaintenanceEvent",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SimulateMaintenanceEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._SimulateMaintenanceEvent._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_simulate_maintenance_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_simulate_maintenance_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.simulate_maintenance_event",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "SimulateMaintenanceEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Start(_BaseInstancesRestTransport._BaseStart, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Start")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.StartInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the start method over HTTP.

            Args:
                request (~.compute.StartInstanceRequest):
                    The request object. A request message for
                Instances.Start. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseStart._get_http_options()
            request, metadata = self._interceptor.pre_start(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseStart,
                    "_BaseStart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Start",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Start",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Start._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.start",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Start",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartWithEncryptionKey(
        _BaseInstancesRestTransport._BaseStartWithEncryptionKey, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.StartWithEncryptionKey")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.StartWithEncryptionKeyInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the start with encryption key method over HTTP.

            Args:
                request (~.compute.StartWithEncryptionKeyInstanceRequest):
                    The request object. A request message for
                Instances.StartWithEncryptionKey. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseStartWithEncryptionKey._get_http_options()
            request, metadata = self._interceptor.pre_start_with_encryption_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseStartWithEncryptionKey,
                    "_BaseStartWithEncryptionKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.StartWithEncryptionKey",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "StartWithEncryptionKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._StartWithEncryptionKey._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_with_encryption_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_with_encryption_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.start_with_encryption_key",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "StartWithEncryptionKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Stop(_BaseInstancesRestTransport._BaseStop, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Stop")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.StopInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the stop method over HTTP.

            Args:
                request (~.compute.StopInstanceRequest):
                    The request object. A request message for Instances.Stop.
                See the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseStop._get_http_options()
            request, metadata = self._interceptor.pre_stop(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseStop,
                    "_BaseStop__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Stop",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Stop",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Stop._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.stop",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Stop",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Suspend(_BaseInstancesRestTransport._BaseSuspend, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Suspend")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.SuspendInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the suspend method over HTTP.

            Args:
                request (~.compute.SuspendInstanceRequest):
                    The request object. A request message for
                Instances.Suspend. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseSuspend._get_http_options()
            request, metadata = self._interceptor.pre_suspend(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseSuspend,
                    "_BaseSuspend__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Suspend",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Suspend",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Suspend._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_suspend(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suspend_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.suspend",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Suspend",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseInstancesRestTransport._BaseTestIamPermissions, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.TestIamPermissionsInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.TestPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (~.compute.TestIamPermissionsInstanceRequest):
                    The request object. A request message for
                Instances.TestIamPermissions. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.TestPermissionsResponse:

            """

            http_options = (
                _BaseInstancesRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseTestIamPermissions,
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._TestIamPermissions._get_response(
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
            resp = compute.TestPermissionsResponse()
            pb_resp = compute.TestPermissionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_iam_permissions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_iam_permissions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.TestPermissionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Update(_BaseInstancesRestTransport._BaseUpdate, InstancesRestStub):
        def __hash__(self):
            return hash("InstancesRestTransport.Update")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.UpdateInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update method over HTTP.

            Args:
                request (~.compute.UpdateInstanceRequest):
                    The request object. A request message for
                Instances.Update. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseUpdate._get_http_options()
            request, metadata = self._interceptor.pre_update(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseUpdate,
                    "_BaseUpdate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.Update",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Update",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._Update._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.update",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "Update",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAccessConfig(
        _BaseInstancesRestTransport._BaseUpdateAccessConfig, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.UpdateAccessConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.UpdateAccessConfigInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update access config method over HTTP.

            Args:
                request (~.compute.UpdateAccessConfigInstanceRequest):
                    The request object. A request message for
                Instances.UpdateAccessConfig. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseUpdateAccessConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_access_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseUpdateAccessConfig,
                    "_BaseUpdateAccessConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.UpdateAccessConfig",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateAccessConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._UpdateAccessConfig._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_access_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_access_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.update_access_config",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateAccessConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDisplayDevice(
        _BaseInstancesRestTransport._BaseUpdateDisplayDevice, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.UpdateDisplayDevice")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.UpdateDisplayDeviceInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update display device method over HTTP.

            Args:
                request (~.compute.UpdateDisplayDeviceInstanceRequest):
                    The request object. A request message for
                Instances.UpdateDisplayDevice. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseInstancesRestTransport._BaseUpdateDisplayDevice._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_display_device(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseUpdateDisplayDevice,
                    "_BaseUpdateDisplayDevice__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.UpdateDisplayDevice",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateDisplayDevice",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._UpdateDisplayDevice._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_display_device(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_display_device_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.update_display_device",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateDisplayDevice",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNetworkInterface(
        _BaseInstancesRestTransport._BaseUpdateNetworkInterface, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.UpdateNetworkInterface")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.UpdateNetworkInterfaceInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update network interface method over HTTP.

            Args:
                request (~.compute.UpdateNetworkInterfaceInstanceRequest):
                    The request object. A request message for
                Instances.UpdateNetworkInterface. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseUpdateNetworkInterface._get_http_options()
            request, metadata = self._interceptor.pre_update_network_interface(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseUpdateNetworkInterface,
                    "_BaseUpdateNetworkInterface__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.UpdateNetworkInterface",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateNetworkInterface",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InstancesRestTransport._UpdateNetworkInterface._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_network_interface(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_network_interface_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.update_network_interface",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateNetworkInterface",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateShieldedInstanceConfig(
        _BaseInstancesRestTransport._BaseUpdateShieldedInstanceConfig, InstancesRestStub
    ):
        def __hash__(self):
            return hash("InstancesRestTransport.UpdateShieldedInstanceConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: compute.UpdateShieldedInstanceConfigInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the update shielded instance
            config method over HTTP.

                Args:
                    request (~.compute.UpdateShieldedInstanceConfigInstanceRequest):
                        The request object. A request message for
                    Instances.UpdateShieldedInstanceConfig.
                    See the method description for details.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.compute.Operation:
                        Represents an Operation resource.

                    Google Compute Engine has three Operation resources:

                    - `Global </compute/docs/reference/rest/v1/globalOperations>`__
                    - `Regional </compute/docs/reference/rest/v1/regionOperations>`__
                    - `Zonal </compute/docs/reference/rest/v1/zoneOperations>`__

                    You can use an operation resource to manage asynchronous
                    API requests. For more information, readHandling API
                    responses.

                    Operations can be global, regional or zonal.

                    ::

                       - For global operations, use the `globalOperations`
                       resource.
                       - For regional operations, use the
                       `regionOperations` resource.
                       - For zonal operations, use
                       the `zoneOperations` resource.

                    For more information, read Global, Regional, and Zonal
                    Resources.

                    Note that completed Operation resources have a limited
                    retention period.

            """

            http_options = _BaseInstancesRestTransport._BaseUpdateShieldedInstanceConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_shielded_instance_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInstancesRestTransport._BaseUpdateShieldedInstanceConfig,
                    "_BaseUpdateShieldedInstanceConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.compute_v1.InstancesClient.UpdateShieldedInstanceConfig",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateShieldedInstanceConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InstancesRestTransport._UpdateShieldedInstanceConfig._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_shielded_instance_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_shielded_instance_config_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1.InstancesClient.update_shielded_instance_config",
                    extra={
                        "serviceName": "google.cloud.compute.v1.Instances",
                        "rpcName": "UpdateShieldedInstanceConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_access_config(
        self,
    ) -> Callable[[compute.AddAccessConfigInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddAccessConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_network_interface(
        self,
    ) -> Callable[[compute.AddNetworkInterfaceInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddNetworkInterface(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_resource_policies(
        self,
    ) -> Callable[[compute.AddResourcePoliciesInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddResourcePolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def aggregated_list(
        self,
    ) -> Callable[
        [compute.AggregatedListInstancesRequest], compute.InstanceAggregatedList
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AggregatedList(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def attach_disk(
        self,
    ) -> Callable[[compute.AttachDiskInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AttachDisk(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def bulk_insert(
        self,
    ) -> Callable[[compute.BulkInsertInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkInsert(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete(self) -> Callable[[compute.DeleteInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Delete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_access_config(
        self,
    ) -> Callable[[compute.DeleteAccessConfigInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAccessConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_network_interface(
        self,
    ) -> Callable[[compute.DeleteNetworkInterfaceInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNetworkInterface(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def detach_disk(
        self,
    ) -> Callable[[compute.DetachDiskInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DetachDisk(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get(self) -> Callable[[compute.GetInstanceRequest], compute.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Get(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_effective_firewalls(
        self,
    ) -> Callable[
        [compute.GetEffectiveFirewallsInstanceRequest],
        compute.InstancesGetEffectiveFirewallsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEffectiveFirewalls(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_guest_attributes(
        self,
    ) -> Callable[[compute.GetGuestAttributesInstanceRequest], compute.GuestAttributes]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGuestAttributes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[compute.GetIamPolicyInstanceRequest], compute.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_screenshot(
        self,
    ) -> Callable[[compute.GetScreenshotInstanceRequest], compute.Screenshot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScreenshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_serial_port_output(
        self,
    ) -> Callable[
        [compute.GetSerialPortOutputInstanceRequest], compute.SerialPortOutput
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSerialPortOutput(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_shielded_instance_identity(
        self,
    ) -> Callable[
        [compute.GetShieldedInstanceIdentityInstanceRequest],
        compute.ShieldedInstanceIdentity,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetShieldedInstanceIdentity(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def insert(self) -> Callable[[compute.InsertInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Insert(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list(self) -> Callable[[compute.ListInstancesRequest], compute.InstanceList]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._List(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_referrers(
        self,
    ) -> Callable[
        [compute.ListReferrersInstancesRequest], compute.InstanceListReferrers
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReferrers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def perform_maintenance(
        self,
    ) -> Callable[[compute.PerformMaintenanceInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PerformMaintenance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_resource_policies(
        self,
    ) -> Callable[[compute.RemoveResourcePoliciesInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveResourcePolicies(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def report_host_as_faulty(
        self,
    ) -> Callable[[compute.ReportHostAsFaultyInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReportHostAsFaulty(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset(self) -> Callable[[compute.ResetInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Reset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume(self) -> Callable[[compute.ResumeInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Resume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def send_diagnostic_interrupt(
        self,
    ) -> Callable[
        [compute.SendDiagnosticInterruptInstanceRequest],
        compute.SendDiagnosticInterruptInstanceResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SendDiagnosticInterrupt(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_deletion_protection(
        self,
    ) -> Callable[[compute.SetDeletionProtectionInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetDeletionProtection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_disk_auto_delete(
        self,
    ) -> Callable[[compute.SetDiskAutoDeleteInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetDiskAutoDelete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[compute.SetIamPolicyInstanceRequest], compute.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_labels(
        self,
    ) -> Callable[[compute.SetLabelsInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_machine_resources(
        self,
    ) -> Callable[[compute.SetMachineResourcesInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMachineResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_machine_type(
        self,
    ) -> Callable[[compute.SetMachineTypeInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMachineType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_metadata(
        self,
    ) -> Callable[[compute.SetMetadataInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMetadata(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_min_cpu_platform(
        self,
    ) -> Callable[[compute.SetMinCpuPlatformInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetMinCpuPlatform(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_name(self) -> Callable[[compute.SetNameInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetName(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_scheduling(
        self,
    ) -> Callable[[compute.SetSchedulingInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetScheduling(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_security_policy(
        self,
    ) -> Callable[[compute.SetSecurityPolicyInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetSecurityPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_service_account(
        self,
    ) -> Callable[[compute.SetServiceAccountInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetServiceAccount(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_shielded_instance_integrity_policy(
        self,
    ) -> Callable[
        [compute.SetShieldedInstanceIntegrityPolicyInstanceRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetShieldedInstanceIntegrityPolicy(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_tags(self) -> Callable[[compute.SetTagsInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetTags(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def simulate_maintenance_event(
        self,
    ) -> Callable[[compute.SimulateMaintenanceEventInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SimulateMaintenanceEvent(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def start(self) -> Callable[[compute.StartInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Start(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_with_encryption_key(
        self,
    ) -> Callable[[compute.StartWithEncryptionKeyInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartWithEncryptionKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def stop(self) -> Callable[[compute.StopInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Stop(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def suspend(self) -> Callable[[compute.SuspendInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Suspend(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [compute.TestIamPermissionsInstanceRequest], compute.TestPermissionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update(self) -> Callable[[compute.UpdateInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Update(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_access_config(
        self,
    ) -> Callable[[compute.UpdateAccessConfigInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAccessConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_display_device(
        self,
    ) -> Callable[[compute.UpdateDisplayDeviceInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDisplayDevice(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_network_interface(
        self,
    ) -> Callable[[compute.UpdateNetworkInterfaceInstanceRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNetworkInterface(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_shielded_instance_config(
        self,
    ) -> Callable[
        [compute.UpdateShieldedInstanceConfigInstanceRequest], compute.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateShieldedInstanceConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("InstancesRestTransport",)
