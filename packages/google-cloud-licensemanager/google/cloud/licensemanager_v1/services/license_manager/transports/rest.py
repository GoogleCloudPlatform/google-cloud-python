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

from google.cloud.licensemanager_v1._compat import transcode_request
from google.cloud.licensemanager_v1.types import api_entities, licensemanager

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLicenseManagerRestTransport

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


class LicenseManagerRestInterceptor:
    """Interceptor for LicenseManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LicenseManagerRestTransport.

    .. code-block:: python
        class MyCustomLicenseManagerInterceptor(LicenseManagerRestInterceptor):
            def pre_aggregate_usage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_aggregate_usage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_configuration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_configuration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deactivate_configuration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deactivate_configuration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_configuration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_configuration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_configuration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_configuration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_product(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_product(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_configurations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_configurations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_products(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_products(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_configuration_license_usage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_configuration_license_usage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reactivate_configuration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reactivate_configuration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_configuration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_configuration(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LicenseManagerRestTransport(interceptor=MyCustomLicenseManagerInterceptor())
        client = LicenseManagerClient(transport=transport)


    """

    def pre_aggregate_usage(
        self,
        request: licensemanager.AggregateUsageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.AggregateUsageRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for aggregate_usage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_aggregate_usage(
        self, response: licensemanager.AggregateUsageResponse
    ) -> licensemanager.AggregateUsageResponse:
        """Post-rpc interceptor for aggregate_usage

        DEPRECATED. Please use the `post_aggregate_usage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_aggregate_usage` interceptor runs
        before the `post_aggregate_usage_with_metadata` interceptor.
        """
        return response

    def post_aggregate_usage_with_metadata(
        self,
        response: licensemanager.AggregateUsageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.AggregateUsageResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for aggregate_usage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_aggregate_usage_with_metadata`
        interceptor in new development instead of the `post_aggregate_usage` interceptor.
        When both interceptors are used, this `post_aggregate_usage_with_metadata` interceptor runs after the
        `post_aggregate_usage` interceptor. The (possibly modified) response returned by
        `post_aggregate_usage` will be passed to
        `post_aggregate_usage_with_metadata`.
        """
        return response, metadata

    def pre_create_configuration(
        self,
        request: licensemanager.CreateConfigurationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.CreateConfigurationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_configuration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_create_configuration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_configuration

        DEPRECATED. Please use the `post_create_configuration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_create_configuration` interceptor runs
        before the `post_create_configuration_with_metadata` interceptor.
        """
        return response

    def post_create_configuration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_configuration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_create_configuration_with_metadata`
        interceptor in new development instead of the `post_create_configuration` interceptor.
        When both interceptors are used, this `post_create_configuration_with_metadata` interceptor runs after the
        `post_create_configuration` interceptor. The (possibly modified) response returned by
        `post_create_configuration` will be passed to
        `post_create_configuration_with_metadata`.
        """
        return response, metadata

    def pre_deactivate_configuration(
        self,
        request: licensemanager.DeactivateConfigurationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.DeactivateConfigurationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deactivate_configuration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_deactivate_configuration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deactivate_configuration

        DEPRECATED. Please use the `post_deactivate_configuration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_deactivate_configuration` interceptor runs
        before the `post_deactivate_configuration_with_metadata` interceptor.
        """
        return response

    def post_deactivate_configuration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deactivate_configuration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_deactivate_configuration_with_metadata`
        interceptor in new development instead of the `post_deactivate_configuration` interceptor.
        When both interceptors are used, this `post_deactivate_configuration_with_metadata` interceptor runs after the
        `post_deactivate_configuration` interceptor. The (possibly modified) response returned by
        `post_deactivate_configuration` will be passed to
        `post_deactivate_configuration_with_metadata`.
        """
        return response, metadata

    def pre_delete_configuration(
        self,
        request: licensemanager.DeleteConfigurationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.DeleteConfigurationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_configuration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_delete_configuration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_configuration

        DEPRECATED. Please use the `post_delete_configuration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_delete_configuration` interceptor runs
        before the `post_delete_configuration_with_metadata` interceptor.
        """
        return response

    def post_delete_configuration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_configuration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_delete_configuration_with_metadata`
        interceptor in new development instead of the `post_delete_configuration` interceptor.
        When both interceptors are used, this `post_delete_configuration_with_metadata` interceptor runs after the
        `post_delete_configuration` interceptor. The (possibly modified) response returned by
        `post_delete_configuration` will be passed to
        `post_delete_configuration_with_metadata`.
        """
        return response, metadata

    def pre_get_configuration(
        self,
        request: licensemanager.GetConfigurationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.GetConfigurationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_configuration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_get_configuration(
        self, response: api_entities.Configuration
    ) -> api_entities.Configuration:
        """Post-rpc interceptor for get_configuration

        DEPRECATED. Please use the `post_get_configuration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_get_configuration` interceptor runs
        before the `post_get_configuration_with_metadata` interceptor.
        """
        return response

    def post_get_configuration_with_metadata(
        self,
        response: api_entities.Configuration,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[api_entities.Configuration, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_configuration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_get_configuration_with_metadata`
        interceptor in new development instead of the `post_get_configuration` interceptor.
        When both interceptors are used, this `post_get_configuration_with_metadata` interceptor runs after the
        `post_get_configuration` interceptor. The (possibly modified) response returned by
        `post_get_configuration` will be passed to
        `post_get_configuration_with_metadata`.
        """
        return response, metadata

    def pre_get_instance(
        self,
        request: licensemanager.GetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.GetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_get_instance(
        self, response: api_entities.Instance
    ) -> api_entities.Instance:
        """Post-rpc interceptor for get_instance

        DEPRECATED. Please use the `post_get_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_get_instance` interceptor runs
        before the `post_get_instance_with_metadata` interceptor.
        """
        return response

    def post_get_instance_with_metadata(
        self,
        response: api_entities.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[api_entities.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_get_instance_with_metadata`
        interceptor in new development instead of the `post_get_instance` interceptor.
        When both interceptors are used, this `post_get_instance_with_metadata` interceptor runs after the
        `post_get_instance` interceptor. The (possibly modified) response returned by
        `post_get_instance` will be passed to
        `post_get_instance_with_metadata`.
        """
        return response, metadata

    def pre_get_product(
        self,
        request: licensemanager.GetProductRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.GetProductRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_product

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_get_product(self, response: api_entities.Product) -> api_entities.Product:
        """Post-rpc interceptor for get_product

        DEPRECATED. Please use the `post_get_product_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_get_product` interceptor runs
        before the `post_get_product_with_metadata` interceptor.
        """
        return response

    def post_get_product_with_metadata(
        self,
        response: api_entities.Product,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[api_entities.Product, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_product

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_get_product_with_metadata`
        interceptor in new development instead of the `post_get_product` interceptor.
        When both interceptors are used, this `post_get_product_with_metadata` interceptor runs after the
        `post_get_product` interceptor. The (possibly modified) response returned by
        `post_get_product` will be passed to
        `post_get_product_with_metadata`.
        """
        return response, metadata

    def pre_list_configurations(
        self,
        request: licensemanager.ListConfigurationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ListConfigurationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_configurations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_list_configurations(
        self, response: licensemanager.ListConfigurationsResponse
    ) -> licensemanager.ListConfigurationsResponse:
        """Post-rpc interceptor for list_configurations

        DEPRECATED. Please use the `post_list_configurations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_list_configurations` interceptor runs
        before the `post_list_configurations_with_metadata` interceptor.
        """
        return response

    def post_list_configurations_with_metadata(
        self,
        response: licensemanager.ListConfigurationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ListConfigurationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_configurations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_list_configurations_with_metadata`
        interceptor in new development instead of the `post_list_configurations` interceptor.
        When both interceptors are used, this `post_list_configurations_with_metadata` interceptor runs after the
        `post_list_configurations` interceptor. The (possibly modified) response returned by
        `post_list_configurations` will be passed to
        `post_list_configurations_with_metadata`.
        """
        return response, metadata

    def pre_list_instances(
        self,
        request: licensemanager.ListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_list_instances(
        self, response: licensemanager.ListInstancesResponse
    ) -> licensemanager.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        DEPRECATED. Please use the `post_list_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_list_instances` interceptor runs
        before the `post_list_instances_with_metadata` interceptor.
        """
        return response

    def post_list_instances_with_metadata(
        self,
        response: licensemanager.ListInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ListInstancesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_list_instances_with_metadata`
        interceptor in new development instead of the `post_list_instances` interceptor.
        When both interceptors are used, this `post_list_instances_with_metadata` interceptor runs after the
        `post_list_instances` interceptor. The (possibly modified) response returned by
        `post_list_instances` will be passed to
        `post_list_instances_with_metadata`.
        """
        return response, metadata

    def pre_list_products(
        self,
        request: licensemanager.ListProductsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ListProductsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_products

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_list_products(
        self, response: licensemanager.ListProductsResponse
    ) -> licensemanager.ListProductsResponse:
        """Post-rpc interceptor for list_products

        DEPRECATED. Please use the `post_list_products_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_list_products` interceptor runs
        before the `post_list_products_with_metadata` interceptor.
        """
        return response

    def post_list_products_with_metadata(
        self,
        response: licensemanager.ListProductsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ListProductsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_products

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_list_products_with_metadata`
        interceptor in new development instead of the `post_list_products` interceptor.
        When both interceptors are used, this `post_list_products_with_metadata` interceptor runs after the
        `post_list_products` interceptor. The (possibly modified) response returned by
        `post_list_products` will be passed to
        `post_list_products_with_metadata`.
        """
        return response, metadata

    def pre_query_configuration_license_usage(
        self,
        request: licensemanager.QueryConfigurationLicenseUsageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.QueryConfigurationLicenseUsageRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_configuration_license_usage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_query_configuration_license_usage(
        self, response: licensemanager.QueryConfigurationLicenseUsageResponse
    ) -> licensemanager.QueryConfigurationLicenseUsageResponse:
        """Post-rpc interceptor for query_configuration_license_usage

        DEPRECATED. Please use the `post_query_configuration_license_usage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_query_configuration_license_usage` interceptor runs
        before the `post_query_configuration_license_usage_with_metadata` interceptor.
        """
        return response

    def post_query_configuration_license_usage_with_metadata(
        self,
        response: licensemanager.QueryConfigurationLicenseUsageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.QueryConfigurationLicenseUsageResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_configuration_license_usage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_query_configuration_license_usage_with_metadata`
        interceptor in new development instead of the `post_query_configuration_license_usage` interceptor.
        When both interceptors are used, this `post_query_configuration_license_usage_with_metadata` interceptor runs after the
        `post_query_configuration_license_usage` interceptor. The (possibly modified) response returned by
        `post_query_configuration_license_usage` will be passed to
        `post_query_configuration_license_usage_with_metadata`.
        """
        return response, metadata

    def pre_reactivate_configuration(
        self,
        request: licensemanager.ReactivateConfigurationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.ReactivateConfigurationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reactivate_configuration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_reactivate_configuration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reactivate_configuration

        DEPRECATED. Please use the `post_reactivate_configuration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_reactivate_configuration` interceptor runs
        before the `post_reactivate_configuration_with_metadata` interceptor.
        """
        return response

    def post_reactivate_configuration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reactivate_configuration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_reactivate_configuration_with_metadata`
        interceptor in new development instead of the `post_reactivate_configuration` interceptor.
        When both interceptors are used, this `post_reactivate_configuration_with_metadata` interceptor runs after the
        `post_reactivate_configuration` interceptor. The (possibly modified) response returned by
        `post_reactivate_configuration` will be passed to
        `post_reactivate_configuration_with_metadata`.
        """
        return response, metadata

    def pre_update_configuration(
        self,
        request: licensemanager.UpdateConfigurationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        licensemanager.UpdateConfigurationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_configuration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_update_configuration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_configuration

        DEPRECATED. Please use the `post_update_configuration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code. This `post_update_configuration` interceptor runs
        before the `post_update_configuration_with_metadata` interceptor.
        """
        return response

    def post_update_configuration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_configuration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LicenseManager server but before it is returned to user code.

        We recommend only using this `post_update_configuration_with_metadata`
        interceptor in new development instead of the `post_update_configuration` interceptor.
        When both interceptors are used, this `post_update_configuration_with_metadata` interceptor runs after the
        `post_update_configuration` interceptor. The (possibly modified) response returned by
        `post_update_configuration` will be passed to
        `post_update_configuration_with_metadata`.
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
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the LicenseManager server but before
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
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the LicenseManager server but before
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
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LicenseManager server but before
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
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the LicenseManager server but before
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
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LicenseManager server but before
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
        before they are sent to the LicenseManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the LicenseManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LicenseManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LicenseManagerRestInterceptor


class LicenseManagerRestTransport(_BaseLicenseManagerRestTransport):
    """REST backend synchronous transport for LicenseManager.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "licensemanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[LicenseManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'licensemanager.googleapis.com').
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
            interceptor (Optional[LicenseManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LicenseManagerRestInterceptor()
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

    class _AggregateUsage(
        _BaseLicenseManagerRestTransport._BaseAggregateUsage, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.AggregateUsage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.AggregateUsageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> licensemanager.AggregateUsageResponse:
            r"""Call the aggregate usage method over HTTP.

            Args:
                request (~.licensemanager.AggregateUsageRequest):
                    The request object. Message for requesting aggregate of
                Usage per configuration.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.licensemanager.AggregateUsageResponse:
                    Message for response for aggregating
                usage count

            """

            http_options = (
                _BaseLicenseManagerRestTransport._BaseAggregateUsage._get_http_options()
            )
            request, metadata = self._interceptor.pre_aggregate_usage(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseAggregateUsage,
                    "_BaseAggregateUsage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.AggregateUsage",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "AggregateUsage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._AggregateUsage._get_response(
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
            resp = licensemanager.AggregateUsageResponse()
            pb_resp = licensemanager.AggregateUsageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_aggregate_usage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_aggregate_usage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = licensemanager.AggregateUsageResponse.to_json(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.aggregate_usage",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "AggregateUsage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConfiguration(
        _BaseLicenseManagerRestTransport._BaseCreateConfiguration,
        LicenseManagerRestStub,
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.CreateConfiguration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: licensemanager.CreateConfigurationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create configuration method over HTTP.

            Args:
                request (~.licensemanager.CreateConfigurationRequest):
                    The request object. Message for creating a Configuration
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

            http_options = _BaseLicenseManagerRestTransport._BaseCreateConfiguration._get_http_options()
            request, metadata = self._interceptor.pre_create_configuration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseCreateConfiguration,
                    "_BaseCreateConfiguration__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.CreateConfiguration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "CreateConfiguration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._CreateConfiguration._get_response(
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

            resp = self._interceptor.post_create_configuration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_configuration_with_metadata(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.create_configuration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "CreateConfiguration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeactivateConfiguration(
        _BaseLicenseManagerRestTransport._BaseDeactivateConfiguration,
        LicenseManagerRestStub,
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.DeactivateConfiguration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: licensemanager.DeactivateConfigurationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deactivate configuration method over HTTP.

            Args:
                request (~.licensemanager.DeactivateConfigurationRequest):
                    The request object. Message for deactivating a
                Configuration.
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

            http_options = _BaseLicenseManagerRestTransport._BaseDeactivateConfiguration._get_http_options()
            request, metadata = self._interceptor.pre_deactivate_configuration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseDeactivateConfiguration,
                    "_BaseDeactivateConfiguration__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.DeactivateConfiguration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "DeactivateConfiguration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseManagerRestTransport._DeactivateConfiguration._get_response(
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

            resp = self._interceptor.post_deactivate_configuration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deactivate_configuration_with_metadata(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.deactivate_configuration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "DeactivateConfiguration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConfiguration(
        _BaseLicenseManagerRestTransport._BaseDeleteConfiguration,
        LicenseManagerRestStub,
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.DeleteConfiguration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.DeleteConfigurationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete configuration method over HTTP.

            Args:
                request (~.licensemanager.DeleteConfigurationRequest):
                    The request object. Message for deleting a Configuration
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

            http_options = _BaseLicenseManagerRestTransport._BaseDeleteConfiguration._get_http_options()
            request, metadata = self._interceptor.pre_delete_configuration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseDeleteConfiguration,
                    "_BaseDeleteConfiguration__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.DeleteConfiguration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "DeleteConfiguration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._DeleteConfiguration._get_response(
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

            resp = self._interceptor.post_delete_configuration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_configuration_with_metadata(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.delete_configuration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "DeleteConfiguration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConfiguration(
        _BaseLicenseManagerRestTransport._BaseGetConfiguration, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.GetConfiguration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.GetConfigurationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> api_entities.Configuration:
            r"""Call the get configuration method over HTTP.

            Args:
                request (~.licensemanager.GetConfigurationRequest):
                    The request object. Message for getting a Configuration
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.api_entities.Configuration:
                    Configuration for a Google SPLA
                product

            """

            http_options = _BaseLicenseManagerRestTransport._BaseGetConfiguration._get_http_options()
            request, metadata = self._interceptor.pre_get_configuration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseGetConfiguration,
                    "_BaseGetConfiguration__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.GetConfiguration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetConfiguration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._GetConfiguration._get_response(
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
            resp = api_entities.Configuration()
            pb_resp = api_entities.Configuration.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_configuration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_configuration_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = api_entities.Configuration.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.get_configuration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetConfiguration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstance(
        _BaseLicenseManagerRestTransport._BaseGetInstance, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.GetInstance")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.GetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> api_entities.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.licensemanager.GetInstanceRequest):
                    The request object. Message for getting a Instance
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.api_entities.Instance:
                    Message describing Instance object
            """

            http_options = (
                _BaseLicenseManagerRestTransport._BaseGetInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseGetInstance,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.GetInstance",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._GetInstance._get_response(
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
            resp = api_entities.Instance()
            pb_resp = api_entities.Instance.pb(resp)

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
                    response_payload = api_entities.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.get_instance",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProduct(
        _BaseLicenseManagerRestTransport._BaseGetProduct, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.GetProduct")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.GetProductRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> api_entities.Product:
            r"""Call the get product method over HTTP.

            Args:
                request (~.licensemanager.GetProductRequest):
                    The request object. Message for getting a Product
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.api_entities.Product:
                    Products for Google SPLA.
            """

            http_options = (
                _BaseLicenseManagerRestTransport._BaseGetProduct._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_product(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseGetProduct,
                    "_BaseGetProduct__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.GetProduct",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetProduct",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._GetProduct._get_response(
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
            resp = api_entities.Product()
            pb_resp = api_entities.Product.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_product(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_product_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = api_entities.Product.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.get_product",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetProduct",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConfigurations(
        _BaseLicenseManagerRestTransport._BaseListConfigurations, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.ListConfigurations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.ListConfigurationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> licensemanager.ListConfigurationsResponse:
            r"""Call the list configurations method over HTTP.

            Args:
                request (~.licensemanager.ListConfigurationsRequest):
                    The request object. Message for requesting list of
                Configurations
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.licensemanager.ListConfigurationsResponse:
                    Message for response to listing
                Configurations

            """

            http_options = _BaseLicenseManagerRestTransport._BaseListConfigurations._get_http_options()
            request, metadata = self._interceptor.pre_list_configurations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseListConfigurations,
                    "_BaseListConfigurations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.ListConfigurations",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListConfigurations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._ListConfigurations._get_response(
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
            resp = licensemanager.ListConfigurationsResponse()
            pb_resp = licensemanager.ListConfigurationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_configurations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_configurations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        licensemanager.ListConfigurationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.list_configurations",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListConfigurations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInstances(
        _BaseLicenseManagerRestTransport._BaseListInstances, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.ListInstances")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.ListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> licensemanager.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.licensemanager.ListInstancesRequest):
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
                ~.licensemanager.ListInstancesResponse:
                    Message for response to listing
                Instances

            """

            http_options = (
                _BaseLicenseManagerRestTransport._BaseListInstances._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_instances(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseListInstances,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.ListInstances",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._ListInstances._get_response(
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
            resp = licensemanager.ListInstancesResponse()
            pb_resp = licensemanager.ListInstancesResponse.pb(resp)

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
                    response_payload = licensemanager.ListInstancesResponse.to_json(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.list_instances",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProducts(
        _BaseLicenseManagerRestTransport._BaseListProducts, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.ListProducts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.ListProductsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> licensemanager.ListProductsResponse:
            r"""Call the list products method over HTTP.

            Args:
                request (~.licensemanager.ListProductsRequest):
                    The request object. Message for requesting list of
                Products
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.licensemanager.ListProductsResponse:
                    Message for response to listing
                Products

            """

            http_options = (
                _BaseLicenseManagerRestTransport._BaseListProducts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_products(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseListProducts,
                    "_BaseListProducts__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.ListProducts",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListProducts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._ListProducts._get_response(
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
            resp = licensemanager.ListProductsResponse()
            pb_resp = licensemanager.ListProductsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_products(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_products_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = licensemanager.ListProductsResponse.to_json(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.list_products",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListProducts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryConfigurationLicenseUsage(
        _BaseLicenseManagerRestTransport._BaseQueryConfigurationLicenseUsage,
        LicenseManagerRestStub,
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.QueryConfigurationLicenseUsage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: licensemanager.QueryConfigurationLicenseUsageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> licensemanager.QueryConfigurationLicenseUsageResponse:
            r"""Call the query configuration
            license usage method over HTTP.

                Args:
                    request (~.licensemanager.QueryConfigurationLicenseUsageRequest):
                        The request object. Message for requesting license usage
                    per configuration.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.licensemanager.QueryConfigurationLicenseUsageResponse:
                        Message for response to get the
                    license usage per configuration.

            """

            http_options = _BaseLicenseManagerRestTransport._BaseQueryConfigurationLicenseUsage._get_http_options()
            request, metadata = self._interceptor.pre_query_configuration_license_usage(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseQueryConfigurationLicenseUsage,
                    "_BaseQueryConfigurationLicenseUsage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.QueryConfigurationLicenseUsage",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "QueryConfigurationLicenseUsage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._QueryConfigurationLicenseUsage._get_response(
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
            resp = licensemanager.QueryConfigurationLicenseUsageResponse()
            pb_resp = licensemanager.QueryConfigurationLicenseUsageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_configuration_license_usage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_query_configuration_license_usage_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        licensemanager.QueryConfigurationLicenseUsageResponse.to_json(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.query_configuration_license_usage",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "QueryConfigurationLicenseUsage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReactivateConfiguration(
        _BaseLicenseManagerRestTransport._BaseReactivateConfiguration,
        LicenseManagerRestStub,
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.ReactivateConfiguration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: licensemanager.ReactivateConfigurationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reactivate configuration method over HTTP.

            Args:
                request (~.licensemanager.ReactivateConfigurationRequest):
                    The request object. Message for resuming a Configuration.
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

            http_options = _BaseLicenseManagerRestTransport._BaseReactivateConfiguration._get_http_options()
            request, metadata = self._interceptor.pre_reactivate_configuration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseReactivateConfiguration,
                    "_BaseReactivateConfiguration__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.ReactivateConfiguration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ReactivateConfiguration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                LicenseManagerRestTransport._ReactivateConfiguration._get_response(
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

            resp = self._interceptor.post_reactivate_configuration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reactivate_configuration_with_metadata(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.reactivate_configuration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ReactivateConfiguration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConfiguration(
        _BaseLicenseManagerRestTransport._BaseUpdateConfiguration,
        LicenseManagerRestStub,
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.UpdateConfiguration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: licensemanager.UpdateConfigurationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update configuration method over HTTP.

            Args:
                request (~.licensemanager.UpdateConfigurationRequest):
                    The request object. Message for updating a Configuration
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

            http_options = _BaseLicenseManagerRestTransport._BaseUpdateConfiguration._get_http_options()
            request, metadata = self._interceptor.pre_update_configuration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseUpdateConfiguration,
                    "_BaseUpdateConfiguration__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.UpdateConfiguration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "UpdateConfiguration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._UpdateConfiguration._get_response(
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

            resp = self._interceptor.post_update_configuration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_configuration_with_metadata(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerClient.update_configuration",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "UpdateConfiguration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def aggregate_usage(
        self,
    ) -> Callable[
        [licensemanager.AggregateUsageRequest], licensemanager.AggregateUsageResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AggregateUsage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_configuration(
        self,
    ) -> Callable[
        [licensemanager.CreateConfigurationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConfiguration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deactivate_configuration(
        self,
    ) -> Callable[
        [licensemanager.DeactivateConfigurationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeactivateConfiguration(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_configuration(
        self,
    ) -> Callable[
        [licensemanager.DeleteConfigurationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConfiguration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_configuration(
        self,
    ) -> Callable[[licensemanager.GetConfigurationRequest], api_entities.Configuration]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConfiguration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance(
        self,
    ) -> Callable[[licensemanager.GetInstanceRequest], api_entities.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_product(
        self,
    ) -> Callable[[licensemanager.GetProductRequest], api_entities.Product]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProduct(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_configurations(
        self,
    ) -> Callable[
        [licensemanager.ListConfigurationsRequest],
        licensemanager.ListConfigurationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConfigurations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_instances(
        self,
    ) -> Callable[
        [licensemanager.ListInstancesRequest], licensemanager.ListInstancesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_products(
        self,
    ) -> Callable[
        [licensemanager.ListProductsRequest], licensemanager.ListProductsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProducts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_configuration_license_usage(
        self,
    ) -> Callable[
        [licensemanager.QueryConfigurationLicenseUsageRequest],
        licensemanager.QueryConfigurationLicenseUsageResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryConfigurationLicenseUsage(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def reactivate_configuration(
        self,
    ) -> Callable[
        [licensemanager.ReactivateConfigurationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReactivateConfiguration(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_configuration(
        self,
    ) -> Callable[
        [licensemanager.UpdateConfigurationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConfiguration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseLicenseManagerRestTransport._BaseGetLocation, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseLicenseManagerRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
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
        _BaseLicenseManagerRestTransport._BaseListLocations, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseLicenseManagerRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
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
        _BaseLicenseManagerRestTransport._BaseCancelOperation, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseLicenseManagerRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._CancelOperation._get_response(
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
        _BaseLicenseManagerRestTransport._BaseDeleteOperation, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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

            http_options = _BaseLicenseManagerRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._DeleteOperation._get_response(
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
        _BaseLicenseManagerRestTransport._BaseGetOperation, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseLicenseManagerRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
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
        _BaseLicenseManagerRestTransport._BaseListOperations, LicenseManagerRestStub
    ):
        def __hash__(self):
            return hash("LicenseManagerRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseLicenseManagerRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLicenseManagerRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.licensemanager_v1.LicenseManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LicenseManagerRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.licensemanager_v1.LicenseManagerAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.licensemanager.v1.LicenseManager",
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


__all__ = ("LicenseManagerRestTransport",)
