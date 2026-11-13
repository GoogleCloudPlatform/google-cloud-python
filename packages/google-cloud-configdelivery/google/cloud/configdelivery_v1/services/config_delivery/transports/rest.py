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

from google.cloud.configdelivery_v1._compat import transcode_request
from google.cloud.configdelivery_v1.types import config_delivery

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseConfigDeliveryRestTransport

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


class ConfigDeliveryRestInterceptor:
    """Interceptor for ConfigDelivery.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ConfigDeliveryRestTransport.

    .. code-block:: python
        class MyCustomConfigDeliveryInterceptor(ConfigDeliveryRestInterceptor):
            def pre_abort_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_abort_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_fleet_package(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_fleet_package(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_resource_bundle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_resource_bundle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_variant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_variant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_fleet_package(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_fleet_package(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_resource_bundle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_resource_bundle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_variant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_variant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_fleet_package(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_fleet_package(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_resource_bundle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource_bundle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_variant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_variant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_fleet_packages(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_fleet_packages(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_releases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_releases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resource_bundles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resource_bundles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rollouts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rollouts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_variants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_variants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suspend_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suspend_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_fleet_package(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_fleet_package(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_resource_bundle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_resource_bundle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_variant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_variant(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ConfigDeliveryRestTransport(interceptor=MyCustomConfigDeliveryInterceptor())
        client = ConfigDeliveryClient(transport=transport)


    """

    def pre_abort_rollout(
        self,
        request: config_delivery.AbortRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.AbortRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for abort_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_abort_rollout(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for abort_rollout

        DEPRECATED. Please use the `post_abort_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_abort_rollout` interceptor runs
        before the `post_abort_rollout_with_metadata` interceptor.
        """
        return response

    def post_abort_rollout_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for abort_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_abort_rollout_with_metadata`
        interceptor in new development instead of the `post_abort_rollout` interceptor.
        When both interceptors are used, this `post_abort_rollout_with_metadata` interceptor runs after the
        `post_abort_rollout` interceptor. The (possibly modified) response returned by
        `post_abort_rollout` will be passed to
        `post_abort_rollout_with_metadata`.
        """
        return response, metadata

    def pre_create_fleet_package(
        self,
        request: config_delivery.CreateFleetPackageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.CreateFleetPackageRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_fleet_package

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_create_fleet_package(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_fleet_package

        DEPRECATED. Please use the `post_create_fleet_package_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_create_fleet_package` interceptor runs
        before the `post_create_fleet_package_with_metadata` interceptor.
        """
        return response

    def post_create_fleet_package_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_fleet_package

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_create_fleet_package_with_metadata`
        interceptor in new development instead of the `post_create_fleet_package` interceptor.
        When both interceptors are used, this `post_create_fleet_package_with_metadata` interceptor runs after the
        `post_create_fleet_package` interceptor. The (possibly modified) response returned by
        `post_create_fleet_package` will be passed to
        `post_create_fleet_package_with_metadata`.
        """
        return response, metadata

    def pre_create_release(
        self,
        request: config_delivery.CreateReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.CreateReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_create_release(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_release

        DEPRECATED. Please use the `post_create_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_create_release` interceptor runs
        before the `post_create_release_with_metadata` interceptor.
        """
        return response

    def post_create_release_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_create_release_with_metadata`
        interceptor in new development instead of the `post_create_release` interceptor.
        When both interceptors are used, this `post_create_release_with_metadata` interceptor runs after the
        `post_create_release` interceptor. The (possibly modified) response returned by
        `post_create_release` will be passed to
        `post_create_release_with_metadata`.
        """
        return response, metadata

    def pre_create_resource_bundle(
        self,
        request: config_delivery.CreateResourceBundleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.CreateResourceBundleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_resource_bundle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_create_resource_bundle(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_resource_bundle

        DEPRECATED. Please use the `post_create_resource_bundle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_create_resource_bundle` interceptor runs
        before the `post_create_resource_bundle_with_metadata` interceptor.
        """
        return response

    def post_create_resource_bundle_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_resource_bundle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_create_resource_bundle_with_metadata`
        interceptor in new development instead of the `post_create_resource_bundle` interceptor.
        When both interceptors are used, this `post_create_resource_bundle_with_metadata` interceptor runs after the
        `post_create_resource_bundle` interceptor. The (possibly modified) response returned by
        `post_create_resource_bundle` will be passed to
        `post_create_resource_bundle_with_metadata`.
        """
        return response, metadata

    def pre_create_variant(
        self,
        request: config_delivery.CreateVariantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.CreateVariantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_variant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_create_variant(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_variant

        DEPRECATED. Please use the `post_create_variant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_create_variant` interceptor runs
        before the `post_create_variant_with_metadata` interceptor.
        """
        return response

    def post_create_variant_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_variant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_create_variant_with_metadata`
        interceptor in new development instead of the `post_create_variant` interceptor.
        When both interceptors are used, this `post_create_variant_with_metadata` interceptor runs after the
        `post_create_variant` interceptor. The (possibly modified) response returned by
        `post_create_variant` will be passed to
        `post_create_variant_with_metadata`.
        """
        return response, metadata

    def pre_delete_fleet_package(
        self,
        request: config_delivery.DeleteFleetPackageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.DeleteFleetPackageRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_fleet_package

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_delete_fleet_package(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_fleet_package

        DEPRECATED. Please use the `post_delete_fleet_package_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_delete_fleet_package` interceptor runs
        before the `post_delete_fleet_package_with_metadata` interceptor.
        """
        return response

    def post_delete_fleet_package_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_fleet_package

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_delete_fleet_package_with_metadata`
        interceptor in new development instead of the `post_delete_fleet_package` interceptor.
        When both interceptors are used, this `post_delete_fleet_package_with_metadata` interceptor runs after the
        `post_delete_fleet_package` interceptor. The (possibly modified) response returned by
        `post_delete_fleet_package` will be passed to
        `post_delete_fleet_package_with_metadata`.
        """
        return response, metadata

    def pre_delete_release(
        self,
        request: config_delivery.DeleteReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.DeleteReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_delete_release(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_release

        DEPRECATED. Please use the `post_delete_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_delete_release` interceptor runs
        before the `post_delete_release_with_metadata` interceptor.
        """
        return response

    def post_delete_release_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_delete_release_with_metadata`
        interceptor in new development instead of the `post_delete_release` interceptor.
        When both interceptors are used, this `post_delete_release_with_metadata` interceptor runs after the
        `post_delete_release` interceptor. The (possibly modified) response returned by
        `post_delete_release` will be passed to
        `post_delete_release_with_metadata`.
        """
        return response, metadata

    def pre_delete_resource_bundle(
        self,
        request: config_delivery.DeleteResourceBundleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.DeleteResourceBundleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_resource_bundle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_delete_resource_bundle(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_resource_bundle

        DEPRECATED. Please use the `post_delete_resource_bundle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_delete_resource_bundle` interceptor runs
        before the `post_delete_resource_bundle_with_metadata` interceptor.
        """
        return response

    def post_delete_resource_bundle_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_resource_bundle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_delete_resource_bundle_with_metadata`
        interceptor in new development instead of the `post_delete_resource_bundle` interceptor.
        When both interceptors are used, this `post_delete_resource_bundle_with_metadata` interceptor runs after the
        `post_delete_resource_bundle` interceptor. The (possibly modified) response returned by
        `post_delete_resource_bundle` will be passed to
        `post_delete_resource_bundle_with_metadata`.
        """
        return response, metadata

    def pre_delete_variant(
        self,
        request: config_delivery.DeleteVariantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.DeleteVariantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_variant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_delete_variant(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_variant

        DEPRECATED. Please use the `post_delete_variant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_delete_variant` interceptor runs
        before the `post_delete_variant_with_metadata` interceptor.
        """
        return response

    def post_delete_variant_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_variant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_delete_variant_with_metadata`
        interceptor in new development instead of the `post_delete_variant` interceptor.
        When both interceptors are used, this `post_delete_variant_with_metadata` interceptor runs after the
        `post_delete_variant` interceptor. The (possibly modified) response returned by
        `post_delete_variant` will be passed to
        `post_delete_variant_with_metadata`.
        """
        return response, metadata

    def pre_get_fleet_package(
        self,
        request: config_delivery.GetFleetPackageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.GetFleetPackageRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_fleet_package

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_fleet_package(
        self, response: config_delivery.FleetPackage
    ) -> config_delivery.FleetPackage:
        """Post-rpc interceptor for get_fleet_package

        DEPRECATED. Please use the `post_get_fleet_package_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_get_fleet_package` interceptor runs
        before the `post_get_fleet_package_with_metadata` interceptor.
        """
        return response

    def post_get_fleet_package_with_metadata(
        self,
        response: config_delivery.FleetPackage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config_delivery.FleetPackage, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_fleet_package

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_get_fleet_package_with_metadata`
        interceptor in new development instead of the `post_get_fleet_package` interceptor.
        When both interceptors are used, this `post_get_fleet_package_with_metadata` interceptor runs after the
        `post_get_fleet_package` interceptor. The (possibly modified) response returned by
        `post_get_fleet_package` will be passed to
        `post_get_fleet_package_with_metadata`.
        """
        return response, metadata

    def pre_get_release(
        self,
        request: config_delivery.GetReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.GetReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_release(
        self, response: config_delivery.Release
    ) -> config_delivery.Release:
        """Post-rpc interceptor for get_release

        DEPRECATED. Please use the `post_get_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_get_release` interceptor runs
        before the `post_get_release_with_metadata` interceptor.
        """
        return response

    def post_get_release_with_metadata(
        self,
        response: config_delivery.Release,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config_delivery.Release, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_get_release_with_metadata`
        interceptor in new development instead of the `post_get_release` interceptor.
        When both interceptors are used, this `post_get_release_with_metadata` interceptor runs after the
        `post_get_release` interceptor. The (possibly modified) response returned by
        `post_get_release` will be passed to
        `post_get_release_with_metadata`.
        """
        return response, metadata

    def pre_get_resource_bundle(
        self,
        request: config_delivery.GetResourceBundleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.GetResourceBundleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_resource_bundle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_resource_bundle(
        self, response: config_delivery.ResourceBundle
    ) -> config_delivery.ResourceBundle:
        """Post-rpc interceptor for get_resource_bundle

        DEPRECATED. Please use the `post_get_resource_bundle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_get_resource_bundle` interceptor runs
        before the `post_get_resource_bundle_with_metadata` interceptor.
        """
        return response

    def post_get_resource_bundle_with_metadata(
        self,
        response: config_delivery.ResourceBundle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config_delivery.ResourceBundle, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_resource_bundle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_get_resource_bundle_with_metadata`
        interceptor in new development instead of the `post_get_resource_bundle` interceptor.
        When both interceptors are used, this `post_get_resource_bundle_with_metadata` interceptor runs after the
        `post_get_resource_bundle` interceptor. The (possibly modified) response returned by
        `post_get_resource_bundle` will be passed to
        `post_get_resource_bundle_with_metadata`.
        """
        return response, metadata

    def pre_get_rollout(
        self,
        request: config_delivery.GetRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.GetRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_rollout(
        self, response: config_delivery.Rollout
    ) -> config_delivery.Rollout:
        """Post-rpc interceptor for get_rollout

        DEPRECATED. Please use the `post_get_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_get_rollout` interceptor runs
        before the `post_get_rollout_with_metadata` interceptor.
        """
        return response

    def post_get_rollout_with_metadata(
        self,
        response: config_delivery.Rollout,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config_delivery.Rollout, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_get_rollout_with_metadata`
        interceptor in new development instead of the `post_get_rollout` interceptor.
        When both interceptors are used, this `post_get_rollout_with_metadata` interceptor runs after the
        `post_get_rollout` interceptor. The (possibly modified) response returned by
        `post_get_rollout` will be passed to
        `post_get_rollout_with_metadata`.
        """
        return response, metadata

    def pre_get_variant(
        self,
        request: config_delivery.GetVariantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.GetVariantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_variant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_variant(
        self, response: config_delivery.Variant
    ) -> config_delivery.Variant:
        """Post-rpc interceptor for get_variant

        DEPRECATED. Please use the `post_get_variant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_get_variant` interceptor runs
        before the `post_get_variant_with_metadata` interceptor.
        """
        return response

    def post_get_variant_with_metadata(
        self,
        response: config_delivery.Variant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config_delivery.Variant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_variant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_get_variant_with_metadata`
        interceptor in new development instead of the `post_get_variant` interceptor.
        When both interceptors are used, this `post_get_variant_with_metadata` interceptor runs after the
        `post_get_variant` interceptor. The (possibly modified) response returned by
        `post_get_variant` will be passed to
        `post_get_variant_with_metadata`.
        """
        return response, metadata

    def pre_list_fleet_packages(
        self,
        request: config_delivery.ListFleetPackagesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListFleetPackagesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_fleet_packages

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_fleet_packages(
        self, response: config_delivery.ListFleetPackagesResponse
    ) -> config_delivery.ListFleetPackagesResponse:
        """Post-rpc interceptor for list_fleet_packages

        DEPRECATED. Please use the `post_list_fleet_packages_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_list_fleet_packages` interceptor runs
        before the `post_list_fleet_packages_with_metadata` interceptor.
        """
        return response

    def post_list_fleet_packages_with_metadata(
        self,
        response: config_delivery.ListFleetPackagesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListFleetPackagesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_fleet_packages

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_list_fleet_packages_with_metadata`
        interceptor in new development instead of the `post_list_fleet_packages` interceptor.
        When both interceptors are used, this `post_list_fleet_packages_with_metadata` interceptor runs after the
        `post_list_fleet_packages` interceptor. The (possibly modified) response returned by
        `post_list_fleet_packages` will be passed to
        `post_list_fleet_packages_with_metadata`.
        """
        return response, metadata

    def pre_list_releases(
        self,
        request: config_delivery.ListReleasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListReleasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_releases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_releases(
        self, response: config_delivery.ListReleasesResponse
    ) -> config_delivery.ListReleasesResponse:
        """Post-rpc interceptor for list_releases

        DEPRECATED. Please use the `post_list_releases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_list_releases` interceptor runs
        before the `post_list_releases_with_metadata` interceptor.
        """
        return response

    def post_list_releases_with_metadata(
        self,
        response: config_delivery.ListReleasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListReleasesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_releases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_list_releases_with_metadata`
        interceptor in new development instead of the `post_list_releases` interceptor.
        When both interceptors are used, this `post_list_releases_with_metadata` interceptor runs after the
        `post_list_releases` interceptor. The (possibly modified) response returned by
        `post_list_releases` will be passed to
        `post_list_releases_with_metadata`.
        """
        return response, metadata

    def pre_list_resource_bundles(
        self,
        request: config_delivery.ListResourceBundlesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListResourceBundlesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_resource_bundles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_resource_bundles(
        self, response: config_delivery.ListResourceBundlesResponse
    ) -> config_delivery.ListResourceBundlesResponse:
        """Post-rpc interceptor for list_resource_bundles

        DEPRECATED. Please use the `post_list_resource_bundles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_list_resource_bundles` interceptor runs
        before the `post_list_resource_bundles_with_metadata` interceptor.
        """
        return response

    def post_list_resource_bundles_with_metadata(
        self,
        response: config_delivery.ListResourceBundlesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListResourceBundlesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_resource_bundles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_list_resource_bundles_with_metadata`
        interceptor in new development instead of the `post_list_resource_bundles` interceptor.
        When both interceptors are used, this `post_list_resource_bundles_with_metadata` interceptor runs after the
        `post_list_resource_bundles` interceptor. The (possibly modified) response returned by
        `post_list_resource_bundles` will be passed to
        `post_list_resource_bundles_with_metadata`.
        """
        return response, metadata

    def pre_list_rollouts(
        self,
        request: config_delivery.ListRolloutsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListRolloutsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_rollouts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_rollouts(
        self, response: config_delivery.ListRolloutsResponse
    ) -> config_delivery.ListRolloutsResponse:
        """Post-rpc interceptor for list_rollouts

        DEPRECATED. Please use the `post_list_rollouts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_list_rollouts` interceptor runs
        before the `post_list_rollouts_with_metadata` interceptor.
        """
        return response

    def post_list_rollouts_with_metadata(
        self,
        response: config_delivery.ListRolloutsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListRolloutsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_rollouts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_list_rollouts_with_metadata`
        interceptor in new development instead of the `post_list_rollouts` interceptor.
        When both interceptors are used, this `post_list_rollouts_with_metadata` interceptor runs after the
        `post_list_rollouts` interceptor. The (possibly modified) response returned by
        `post_list_rollouts` will be passed to
        `post_list_rollouts_with_metadata`.
        """
        return response, metadata

    def pre_list_variants(
        self,
        request: config_delivery.ListVariantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListVariantsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_variants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_variants(
        self, response: config_delivery.ListVariantsResponse
    ) -> config_delivery.ListVariantsResponse:
        """Post-rpc interceptor for list_variants

        DEPRECATED. Please use the `post_list_variants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_list_variants` interceptor runs
        before the `post_list_variants_with_metadata` interceptor.
        """
        return response

    def post_list_variants_with_metadata(
        self,
        response: config_delivery.ListVariantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ListVariantsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_variants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_list_variants_with_metadata`
        interceptor in new development instead of the `post_list_variants` interceptor.
        When both interceptors are used, this `post_list_variants_with_metadata` interceptor runs after the
        `post_list_variants` interceptor. The (possibly modified) response returned by
        `post_list_variants` will be passed to
        `post_list_variants_with_metadata`.
        """
        return response, metadata

    def pre_resume_rollout(
        self,
        request: config_delivery.ResumeRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.ResumeRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for resume_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_resume_rollout(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for resume_rollout

        DEPRECATED. Please use the `post_resume_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_resume_rollout` interceptor runs
        before the `post_resume_rollout_with_metadata` interceptor.
        """
        return response

    def post_resume_rollout_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resume_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_resume_rollout_with_metadata`
        interceptor in new development instead of the `post_resume_rollout` interceptor.
        When both interceptors are used, this `post_resume_rollout_with_metadata` interceptor runs after the
        `post_resume_rollout` interceptor. The (possibly modified) response returned by
        `post_resume_rollout` will be passed to
        `post_resume_rollout_with_metadata`.
        """
        return response, metadata

    def pre_suspend_rollout(
        self,
        request: config_delivery.SuspendRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.SuspendRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for suspend_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_suspend_rollout(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for suspend_rollout

        DEPRECATED. Please use the `post_suspend_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_suspend_rollout` interceptor runs
        before the `post_suspend_rollout_with_metadata` interceptor.
        """
        return response

    def post_suspend_rollout_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for suspend_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_suspend_rollout_with_metadata`
        interceptor in new development instead of the `post_suspend_rollout` interceptor.
        When both interceptors are used, this `post_suspend_rollout_with_metadata` interceptor runs after the
        `post_suspend_rollout` interceptor. The (possibly modified) response returned by
        `post_suspend_rollout` will be passed to
        `post_suspend_rollout_with_metadata`.
        """
        return response, metadata

    def pre_update_fleet_package(
        self,
        request: config_delivery.UpdateFleetPackageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.UpdateFleetPackageRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_fleet_package

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_update_fleet_package(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_fleet_package

        DEPRECATED. Please use the `post_update_fleet_package_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_update_fleet_package` interceptor runs
        before the `post_update_fleet_package_with_metadata` interceptor.
        """
        return response

    def post_update_fleet_package_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_fleet_package

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_update_fleet_package_with_metadata`
        interceptor in new development instead of the `post_update_fleet_package` interceptor.
        When both interceptors are used, this `post_update_fleet_package_with_metadata` interceptor runs after the
        `post_update_fleet_package` interceptor. The (possibly modified) response returned by
        `post_update_fleet_package` will be passed to
        `post_update_fleet_package_with_metadata`.
        """
        return response, metadata

    def pre_update_release(
        self,
        request: config_delivery.UpdateReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.UpdateReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_update_release(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_release

        DEPRECATED. Please use the `post_update_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_update_release` interceptor runs
        before the `post_update_release_with_metadata` interceptor.
        """
        return response

    def post_update_release_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_update_release_with_metadata`
        interceptor in new development instead of the `post_update_release` interceptor.
        When both interceptors are used, this `post_update_release_with_metadata` interceptor runs after the
        `post_update_release` interceptor. The (possibly modified) response returned by
        `post_update_release` will be passed to
        `post_update_release_with_metadata`.
        """
        return response, metadata

    def pre_update_resource_bundle(
        self,
        request: config_delivery.UpdateResourceBundleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.UpdateResourceBundleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_resource_bundle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_update_resource_bundle(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_resource_bundle

        DEPRECATED. Please use the `post_update_resource_bundle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_update_resource_bundle` interceptor runs
        before the `post_update_resource_bundle_with_metadata` interceptor.
        """
        return response

    def post_update_resource_bundle_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_resource_bundle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_update_resource_bundle_with_metadata`
        interceptor in new development instead of the `post_update_resource_bundle` interceptor.
        When both interceptors are used, this `post_update_resource_bundle_with_metadata` interceptor runs after the
        `post_update_resource_bundle` interceptor. The (possibly modified) response returned by
        `post_update_resource_bundle` will be passed to
        `post_update_resource_bundle_with_metadata`.
        """
        return response, metadata

    def pre_update_variant(
        self,
        request: config_delivery.UpdateVariantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config_delivery.UpdateVariantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_variant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_update_variant(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_variant

        DEPRECATED. Please use the `post_update_variant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code. This `post_update_variant` interceptor runs
        before the `post_update_variant_with_metadata` interceptor.
        """
        return response

    def post_update_variant_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_variant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConfigDelivery server but before it is returned to user code.

        We recommend only using this `post_update_variant_with_metadata`
        interceptor in new development instead of the `post_update_variant` interceptor.
        When both interceptors are used, this `post_update_variant_with_metadata` interceptor runs after the
        `post_update_variant` interceptor. The (possibly modified) response returned by
        `post_update_variant` will be passed to
        `post_update_variant_with_metadata`.
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
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ConfigDelivery server but before
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
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ConfigDelivery server but before
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
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ConfigDelivery server but before
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
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the ConfigDelivery server but before
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
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ConfigDelivery server but before
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
        before they are sent to the ConfigDelivery server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ConfigDelivery server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ConfigDeliveryRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ConfigDeliveryRestInterceptor


class ConfigDeliveryRestTransport(_BaseConfigDeliveryRestTransport):
    """REST backend synchronous transport for ConfigDelivery.

    ConfigDelivery service manages the deployment of kubernetes
    configuration to a fleet of kubernetes clusters.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "configdelivery.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ConfigDeliveryRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'configdelivery.googleapis.com').
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
            interceptor (Optional[ConfigDeliveryRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ConfigDeliveryRestInterceptor()
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

    class _AbortRollout(
        _BaseConfigDeliveryRestTransport._BaseAbortRollout, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.AbortRollout")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.AbortRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the abort rollout method over HTTP.

            Args:
                request (~.config_delivery.AbortRolloutRequest):
                    The request object. Message for aborting a rollout.
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
                _BaseConfigDeliveryRestTransport._BaseAbortRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_abort_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseAbortRollout,
                    "_BaseAbortRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.AbortRollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "AbortRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._AbortRollout._get_response(
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

            resp = self._interceptor.post_abort_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_abort_rollout_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.abort_rollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "AbortRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFleetPackage(
        _BaseConfigDeliveryRestTransport._BaseCreateFleetPackage, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.CreateFleetPackage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.CreateFleetPackageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create fleet package method over HTTP.

            Args:
                request (~.config_delivery.CreateFleetPackageRequest):
                    The request object. Message for creating a FleetPackage
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

            http_options = _BaseConfigDeliveryRestTransport._BaseCreateFleetPackage._get_http_options()
            request, metadata = self._interceptor.pre_create_fleet_package(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseCreateFleetPackage,
                    "_BaseCreateFleetPackage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.CreateFleetPackage",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateFleetPackage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._CreateFleetPackage._get_response(
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

            resp = self._interceptor.post_create_fleet_package(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_fleet_package_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.create_fleet_package",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateFleetPackage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRelease(
        _BaseConfigDeliveryRestTransport._BaseCreateRelease, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.CreateRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.CreateReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create release method over HTTP.

            Args:
                request (~.config_delivery.CreateReleaseRequest):
                    The request object. Message for creating a Release
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
                _BaseConfigDeliveryRestTransport._BaseCreateRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseCreateRelease,
                    "_BaseCreateRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.CreateRelease",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._CreateRelease._get_response(
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

            resp = self._interceptor.post_create_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_release_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.create_release",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateResourceBundle(
        _BaseConfigDeliveryRestTransport._BaseCreateResourceBundle,
        ConfigDeliveryRestStub,
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.CreateResourceBundle")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.CreateResourceBundleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create resource bundle method over HTTP.

            Args:
                request (~.config_delivery.CreateResourceBundleRequest):
                    The request object. Message for creating a
                ResourceBundle.
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

            http_options = _BaseConfigDeliveryRestTransport._BaseCreateResourceBundle._get_http_options()
            request, metadata = self._interceptor.pre_create_resource_bundle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseCreateResourceBundle,
                    "_BaseCreateResourceBundle__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.CreateResourceBundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateResourceBundle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._CreateResourceBundle._get_response(
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

            resp = self._interceptor.post_create_resource_bundle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_resource_bundle_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.create_resource_bundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateResourceBundle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVariant(
        _BaseConfigDeliveryRestTransport._BaseCreateVariant, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.CreateVariant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.CreateVariantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create variant method over HTTP.

            Args:
                request (~.config_delivery.CreateVariantRequest):
                    The request object. Message for creating a Variant
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
                _BaseConfigDeliveryRestTransport._BaseCreateVariant._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_variant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseCreateVariant,
                    "_BaseCreateVariant__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.CreateVariant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateVariant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._CreateVariant._get_response(
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

            resp = self._interceptor.post_create_variant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_variant_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.create_variant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CreateVariant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFleetPackage(
        _BaseConfigDeliveryRestTransport._BaseDeleteFleetPackage, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.DeleteFleetPackage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.DeleteFleetPackageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete fleet package method over HTTP.

            Args:
                request (~.config_delivery.DeleteFleetPackageRequest):
                    The request object. Message for deleting a FleetPackage
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

            http_options = _BaseConfigDeliveryRestTransport._BaseDeleteFleetPackage._get_http_options()
            request, metadata = self._interceptor.pre_delete_fleet_package(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseDeleteFleetPackage,
                    "_BaseDeleteFleetPackage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.DeleteFleetPackage",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteFleetPackage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._DeleteFleetPackage._get_response(
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

            resp = self._interceptor.post_delete_fleet_package(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_fleet_package_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.delete_fleet_package",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteFleetPackage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRelease(
        _BaseConfigDeliveryRestTransport._BaseDeleteRelease, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.DeleteRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.DeleteReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete release method over HTTP.

            Args:
                request (~.config_delivery.DeleteReleaseRequest):
                    The request object. Message for deleting a Release
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
                _BaseConfigDeliveryRestTransport._BaseDeleteRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseDeleteRelease,
                    "_BaseDeleteRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.DeleteRelease",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._DeleteRelease._get_response(
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

            resp = self._interceptor.post_delete_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_release_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.delete_release",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteResourceBundle(
        _BaseConfigDeliveryRestTransport._BaseDeleteResourceBundle,
        ConfigDeliveryRestStub,
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.DeleteResourceBundle")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.DeleteResourceBundleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete resource bundle method over HTTP.

            Args:
                request (~.config_delivery.DeleteResourceBundleRequest):
                    The request object. Message for deleting a ResourceBundle
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

            http_options = _BaseConfigDeliveryRestTransport._BaseDeleteResourceBundle._get_http_options()
            request, metadata = self._interceptor.pre_delete_resource_bundle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseDeleteResourceBundle,
                    "_BaseDeleteResourceBundle__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.DeleteResourceBundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteResourceBundle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._DeleteResourceBundle._get_response(
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

            resp = self._interceptor.post_delete_resource_bundle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_resource_bundle_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.delete_resource_bundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteResourceBundle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteVariant(
        _BaseConfigDeliveryRestTransport._BaseDeleteVariant, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.DeleteVariant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.DeleteVariantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete variant method over HTTP.

            Args:
                request (~.config_delivery.DeleteVariantRequest):
                    The request object. Message for deleting a Variant
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
                _BaseConfigDeliveryRestTransport._BaseDeleteVariant._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_variant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseDeleteVariant,
                    "_BaseDeleteVariant__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.DeleteVariant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteVariant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._DeleteVariant._get_response(
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

            resp = self._interceptor.post_delete_variant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_variant_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.delete_variant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteVariant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFleetPackage(
        _BaseConfigDeliveryRestTransport._BaseGetFleetPackage, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetFleetPackage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.GetFleetPackageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.FleetPackage:
            r"""Call the get fleet package method over HTTP.

            Args:
                request (~.config_delivery.GetFleetPackageRequest):
                    The request object. Message for getting a FleetPackage
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.FleetPackage:
                    A ``FleetPackage`` resource in the Config Delivery API.

                A ``FleetPackage`` defines a package through which
                kubernetes configuration is deployed to a fleet of
                kubernetes clusters.

            """

            http_options = _BaseConfigDeliveryRestTransport._BaseGetFleetPackage._get_http_options()
            request, metadata = self._interceptor.pre_get_fleet_package(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetFleetPackage,
                    "_BaseGetFleetPackage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetFleetPackage",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetFleetPackage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetFleetPackage._get_response(
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
            resp = config_delivery.FleetPackage()
            pb_resp = config_delivery.FleetPackage.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_fleet_package(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_fleet_package_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.FleetPackage.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.get_fleet_package",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetFleetPackage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRelease(
        _BaseConfigDeliveryRestTransport._BaseGetRelease, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.GetReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.Release:
            r"""Call the get release method over HTTP.

            Args:
                request (~.config_delivery.GetReleaseRequest):
                    The request object. Message for getting a Release
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.Release:
                    ``Release`` represents a versioned release containing
                kubernetes manifests.

            """

            http_options = (
                _BaseConfigDeliveryRestTransport._BaseGetRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetRelease,
                    "_BaseGetRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetRelease",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetRelease._get_response(
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
            resp = config_delivery.Release()
            pb_resp = config_delivery.Release.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_release_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.Release.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.get_release",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetResourceBundle(
        _BaseConfigDeliveryRestTransport._BaseGetResourceBundle, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetResourceBundle")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.GetResourceBundleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.ResourceBundle:
            r"""Call the get resource bundle method over HTTP.

            Args:
                request (~.config_delivery.GetResourceBundleRequest):
                    The request object. Message for getting a ResourceBundle.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.ResourceBundle:
                    ResourceBundle represent a collection
                of kubernetes configuration resources.

            """

            http_options = _BaseConfigDeliveryRestTransport._BaseGetResourceBundle._get_http_options()
            request, metadata = self._interceptor.pre_get_resource_bundle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetResourceBundle,
                    "_BaseGetResourceBundle__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetResourceBundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetResourceBundle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetResourceBundle._get_response(
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
            resp = config_delivery.ResourceBundle()
            pb_resp = config_delivery.ResourceBundle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource_bundle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_resource_bundle_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.ResourceBundle.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.get_resource_bundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetResourceBundle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRollout(
        _BaseConfigDeliveryRestTransport._BaseGetRollout, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetRollout")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.GetRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.Rollout:
            r"""Call the get rollout method over HTTP.

            Args:
                request (~.config_delivery.GetRolloutRequest):
                    The request object. Message for getting a Rollout
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.Rollout:
                    Rollout resource represents an instance of
                ``FleetPackage`` rollout operation across a fleet. This
                is a system generated resource and will be read only for
                end-users. It will be primarily used by the service to
                process the changes in the ``FleetPackage`` and other
                changes in the environment.

            """

            http_options = (
                _BaseConfigDeliveryRestTransport._BaseGetRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetRollout,
                    "_BaseGetRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetRollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetRollout._get_response(
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
            resp = config_delivery.Rollout()
            pb_resp = config_delivery.Rollout.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.Rollout.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.get_rollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVariant(
        _BaseConfigDeliveryRestTransport._BaseGetVariant, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetVariant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.GetVariantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.Variant:
            r"""Call the get variant method over HTTP.

            Args:
                request (~.config_delivery.GetVariantRequest):
                    The request object. Message for getting a Variant
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.Variant:
                    Variant represents the content of a ``ResourceBundle``
                variant.

            """

            http_options = (
                _BaseConfigDeliveryRestTransport._BaseGetVariant._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_variant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetVariant,
                    "_BaseGetVariant__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetVariant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetVariant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetVariant._get_response(
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
            resp = config_delivery.Variant()
            pb_resp = config_delivery.Variant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_variant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_variant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.Variant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.get_variant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetVariant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFleetPackages(
        _BaseConfigDeliveryRestTransport._BaseListFleetPackages, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListFleetPackages")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.ListFleetPackagesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.ListFleetPackagesResponse:
            r"""Call the list fleet packages method over HTTP.

            Args:
                request (~.config_delivery.ListFleetPackagesRequest):
                    The request object. Message for requesting list of
                FleetPackage.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.ListFleetPackagesResponse:
                    Message for response to listing
                FleetPackage

            """

            http_options = _BaseConfigDeliveryRestTransport._BaseListFleetPackages._get_http_options()
            request, metadata = self._interceptor.pre_list_fleet_packages(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListFleetPackages,
                    "_BaseListFleetPackages__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListFleetPackages",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListFleetPackages",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListFleetPackages._get_response(
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
            resp = config_delivery.ListFleetPackagesResponse()
            pb_resp = config_delivery.ListFleetPackagesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_fleet_packages(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_fleet_packages_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        config_delivery.ListFleetPackagesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.list_fleet_packages",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListFleetPackages",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReleases(
        _BaseConfigDeliveryRestTransport._BaseListReleases, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListReleases")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.ListReleasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.ListReleasesResponse:
            r"""Call the list releases method over HTTP.

            Args:
                request (~.config_delivery.ListReleasesRequest):
                    The request object. Message for requesting list of
                Releases.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.ListReleasesResponse:
                    Message for response to listing
                Releases

            """

            http_options = (
                _BaseConfigDeliveryRestTransport._BaseListReleases._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_releases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListReleases,
                    "_BaseListReleases__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListReleases",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListReleases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListReleases._get_response(
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
            resp = config_delivery.ListReleasesResponse()
            pb_resp = config_delivery.ListReleasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_releases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_releases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.ListReleasesResponse.to_json(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.list_releases",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListReleases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResourceBundles(
        _BaseConfigDeliveryRestTransport._BaseListResourceBundles,
        ConfigDeliveryRestStub,
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListResourceBundles")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.ListResourceBundlesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.ListResourceBundlesResponse:
            r"""Call the list resource bundles method over HTTP.

            Args:
                request (~.config_delivery.ListResourceBundlesRequest):
                    The request object. Message for requesting list of
                ResourceBundles.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.ListResourceBundlesResponse:
                    Message for response to listing
                ResourceBundles.

            """

            http_options = _BaseConfigDeliveryRestTransport._BaseListResourceBundles._get_http_options()
            request, metadata = self._interceptor.pre_list_resource_bundles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListResourceBundles,
                    "_BaseListResourceBundles__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListResourceBundles",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListResourceBundles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListResourceBundles._get_response(
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
            resp = config_delivery.ListResourceBundlesResponse()
            pb_resp = config_delivery.ListResourceBundlesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resource_bundles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_resource_bundles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        config_delivery.ListResourceBundlesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.list_resource_bundles",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListResourceBundles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRollouts(
        _BaseConfigDeliveryRestTransport._BaseListRollouts, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListRollouts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.ListRolloutsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.ListRolloutsResponse:
            r"""Call the list rollouts method over HTTP.

            Args:
                request (~.config_delivery.ListRolloutsRequest):
                    The request object. Message for requesting list of
                Rollouts
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.ListRolloutsResponse:
                    Message for response to listing
                Rollouts

            """

            http_options = (
                _BaseConfigDeliveryRestTransport._BaseListRollouts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rollouts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListRollouts,
                    "_BaseListRollouts__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListRollouts",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListRollouts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListRollouts._get_response(
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
            resp = config_delivery.ListRolloutsResponse()
            pb_resp = config_delivery.ListRolloutsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rollouts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rollouts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.ListRolloutsResponse.to_json(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.list_rollouts",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListRollouts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVariants(
        _BaseConfigDeliveryRestTransport._BaseListVariants, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListVariants")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.ListVariantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config_delivery.ListVariantsResponse:
            r"""Call the list variants method over HTTP.

            Args:
                request (~.config_delivery.ListVariantsRequest):
                    The request object. Message for requesting list of
                Variants.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config_delivery.ListVariantsResponse:
                    Message for response to listing
                Variants

            """

            http_options = (
                _BaseConfigDeliveryRestTransport._BaseListVariants._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_variants(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListVariants,
                    "_BaseListVariants__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListVariants",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListVariants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListVariants._get_response(
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
            resp = config_delivery.ListVariantsResponse()
            pb_resp = config_delivery.ListVariantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_variants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_variants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config_delivery.ListVariantsResponse.to_json(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.list_variants",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListVariants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResumeRollout(
        _BaseConfigDeliveryRestTransport._BaseResumeRollout, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ResumeRollout")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.ResumeRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the resume rollout method over HTTP.

            Args:
                request (~.config_delivery.ResumeRolloutRequest):
                    The request object. Message for resuming a rollout.
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
                _BaseConfigDeliveryRestTransport._BaseResumeRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_resume_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseResumeRollout,
                    "_BaseResumeRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ResumeRollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ResumeRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ResumeRollout._get_response(
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

            resp = self._interceptor.post_resume_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_rollout_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.resume_rollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ResumeRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SuspendRollout(
        _BaseConfigDeliveryRestTransport._BaseSuspendRollout, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.SuspendRollout")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.SuspendRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the suspend rollout method over HTTP.

            Args:
                request (~.config_delivery.SuspendRolloutRequest):
                    The request object. Message for suspending a rollout.
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
                _BaseConfigDeliveryRestTransport._BaseSuspendRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_suspend_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseSuspendRollout,
                    "_BaseSuspendRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.SuspendRollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "SuspendRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._SuspendRollout._get_response(
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

            resp = self._interceptor.post_suspend_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suspend_rollout_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.suspend_rollout",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "SuspendRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFleetPackage(
        _BaseConfigDeliveryRestTransport._BaseUpdateFleetPackage, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.UpdateFleetPackage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.UpdateFleetPackageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update fleet package method over HTTP.

            Args:
                request (~.config_delivery.UpdateFleetPackageRequest):
                    The request object. Message for updating a FleetPackage
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

            http_options = _BaseConfigDeliveryRestTransport._BaseUpdateFleetPackage._get_http_options()
            request, metadata = self._interceptor.pre_update_fleet_package(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseUpdateFleetPackage,
                    "_BaseUpdateFleetPackage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.UpdateFleetPackage",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateFleetPackage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._UpdateFleetPackage._get_response(
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

            resp = self._interceptor.post_update_fleet_package(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_fleet_package_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.update_fleet_package",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateFleetPackage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRelease(
        _BaseConfigDeliveryRestTransport._BaseUpdateRelease, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.UpdateRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.UpdateReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update release method over HTTP.

            Args:
                request (~.config_delivery.UpdateReleaseRequest):
                    The request object. Message for updating a Release
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
                _BaseConfigDeliveryRestTransport._BaseUpdateRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseUpdateRelease,
                    "_BaseUpdateRelease__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.UpdateRelease",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._UpdateRelease._get_response(
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

            resp = self._interceptor.post_update_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_release_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.update_release",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateResourceBundle(
        _BaseConfigDeliveryRestTransport._BaseUpdateResourceBundle,
        ConfigDeliveryRestStub,
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.UpdateResourceBundle")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.UpdateResourceBundleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update resource bundle method over HTTP.

            Args:
                request (~.config_delivery.UpdateResourceBundleRequest):
                    The request object. Message for updating a ResourceBundle
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

            http_options = _BaseConfigDeliveryRestTransport._BaseUpdateResourceBundle._get_http_options()
            request, metadata = self._interceptor.pre_update_resource_bundle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseUpdateResourceBundle,
                    "_BaseUpdateResourceBundle__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.UpdateResourceBundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateResourceBundle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._UpdateResourceBundle._get_response(
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

            resp = self._interceptor.post_update_resource_bundle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_resource_bundle_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.update_resource_bundle",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateResourceBundle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateVariant(
        _BaseConfigDeliveryRestTransport._BaseUpdateVariant, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.UpdateVariant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config_delivery.UpdateVariantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update variant method over HTTP.

            Args:
                request (~.config_delivery.UpdateVariantRequest):
                    The request object. Message for updating a Variant
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
                _BaseConfigDeliveryRestTransport._BaseUpdateVariant._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_variant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseUpdateVariant,
                    "_BaseUpdateVariant__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.UpdateVariant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateVariant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._UpdateVariant._get_response(
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

            resp = self._interceptor.post_update_variant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_variant_with_metadata(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryClient.update_variant",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "UpdateVariant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def abort_rollout(
        self,
    ) -> Callable[[config_delivery.AbortRolloutRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AbortRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.CreateFleetPackageRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFleetPackage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_release(
        self,
    ) -> Callable[[config_delivery.CreateReleaseRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.CreateResourceBundleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateResourceBundle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_variant(
        self,
    ) -> Callable[[config_delivery.CreateVariantRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVariant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.DeleteFleetPackageRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFleetPackage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_release(
        self,
    ) -> Callable[[config_delivery.DeleteReleaseRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.DeleteResourceBundleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteResourceBundle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_variant(
        self,
    ) -> Callable[[config_delivery.DeleteVariantRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVariant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.GetFleetPackageRequest], config_delivery.FleetPackage
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFleetPackage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_release(
        self,
    ) -> Callable[[config_delivery.GetReleaseRequest], config_delivery.Release]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.GetResourceBundleRequest], config_delivery.ResourceBundle
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResourceBundle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rollout(
        self,
    ) -> Callable[[config_delivery.GetRolloutRequest], config_delivery.Rollout]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_variant(
        self,
    ) -> Callable[[config_delivery.GetVariantRequest], config_delivery.Variant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVariant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_fleet_packages(
        self,
    ) -> Callable[
        [config_delivery.ListFleetPackagesRequest],
        config_delivery.ListFleetPackagesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFleetPackages(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_releases(
        self,
    ) -> Callable[
        [config_delivery.ListReleasesRequest], config_delivery.ListReleasesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReleases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_resource_bundles(
        self,
    ) -> Callable[
        [config_delivery.ListResourceBundlesRequest],
        config_delivery.ListResourceBundlesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResourceBundles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [config_delivery.ListRolloutsRequest], config_delivery.ListRolloutsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRollouts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_variants(
        self,
    ) -> Callable[
        [config_delivery.ListVariantsRequest], config_delivery.ListVariantsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVariants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume_rollout(
        self,
    ) -> Callable[[config_delivery.ResumeRolloutRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def suspend_rollout(
        self,
    ) -> Callable[[config_delivery.SuspendRolloutRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SuspendRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_fleet_package(
        self,
    ) -> Callable[
        [config_delivery.UpdateFleetPackageRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFleetPackage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_release(
        self,
    ) -> Callable[[config_delivery.UpdateReleaseRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_resource_bundle(
        self,
    ) -> Callable[
        [config_delivery.UpdateResourceBundleRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateResourceBundle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_variant(
        self,
    ) -> Callable[[config_delivery.UpdateVariantRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVariant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseConfigDeliveryRestTransport._BaseGetLocation, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigDeliveryRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
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
        _BaseConfigDeliveryRestTransport._BaseListLocations, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigDeliveryRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
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
        _BaseConfigDeliveryRestTransport._BaseCancelOperation, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseConfigDeliveryRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._CancelOperation._get_response(
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
        _BaseConfigDeliveryRestTransport._BaseDeleteOperation, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseConfigDeliveryRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._DeleteOperation._get_response(
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
        _BaseConfigDeliveryRestTransport._BaseGetOperation, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigDeliveryRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
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
        _BaseConfigDeliveryRestTransport._BaseListOperations, ConfigDeliveryRestStub
    ):
        def __hash__(self):
            return hash("ConfigDeliveryRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigDeliveryRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigDeliveryRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.configdelivery_v1.ConfigDeliveryClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigDeliveryRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.configdelivery_v1.ConfigDeliveryAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.configdelivery.v1.ConfigDelivery",
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


__all__ = ("ConfigDeliveryRestTransport",)
