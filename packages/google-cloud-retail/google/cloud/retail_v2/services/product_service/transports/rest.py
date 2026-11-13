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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.retail_v2._compat import transcode_request
from google.cloud.retail_v2.types import (
    import_config,
    product,
    product_service,
    purge_config,
)
from google.cloud.retail_v2.types import product as gcr_product

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseProductServiceRestTransport

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


class ProductServiceRestInterceptor:
    """Interceptor for ProductService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ProductServiceRestTransport.

    .. code-block:: python
        class MyCustomProductServiceInterceptor(ProductServiceRestInterceptor):
            def pre_add_fulfillment_places(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_fulfillment_places(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_local_inventories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_local_inventories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_product(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_product(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_product(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_product(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_product(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_products(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_products(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_products(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_products(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_products(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_products(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_fulfillment_places(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_fulfillment_places(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_local_inventories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_local_inventories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_inventory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_inventory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_product(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_product(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ProductServiceRestTransport(interceptor=MyCustomProductServiceInterceptor())
        client = ProductServiceClient(transport=transport)


    """

    def pre_add_fulfillment_places(
        self,
        request: product_service.AddFulfillmentPlacesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.AddFulfillmentPlacesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_fulfillment_places

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_add_fulfillment_places(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for add_fulfillment_places

        DEPRECATED. Please use the `post_add_fulfillment_places_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_add_fulfillment_places` interceptor runs
        before the `post_add_fulfillment_places_with_metadata` interceptor.
        """
        return response

    def post_add_fulfillment_places_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_fulfillment_places

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_add_fulfillment_places_with_metadata`
        interceptor in new development instead of the `post_add_fulfillment_places` interceptor.
        When both interceptors are used, this `post_add_fulfillment_places_with_metadata` interceptor runs after the
        `post_add_fulfillment_places` interceptor. The (possibly modified) response returned by
        `post_add_fulfillment_places` will be passed to
        `post_add_fulfillment_places_with_metadata`.
        """
        return response, metadata

    def pre_add_local_inventories(
        self,
        request: product_service.AddLocalInventoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.AddLocalInventoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_local_inventories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_add_local_inventories(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for add_local_inventories

        DEPRECATED. Please use the `post_add_local_inventories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_add_local_inventories` interceptor runs
        before the `post_add_local_inventories_with_metadata` interceptor.
        """
        return response

    def post_add_local_inventories_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_local_inventories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_add_local_inventories_with_metadata`
        interceptor in new development instead of the `post_add_local_inventories` interceptor.
        When both interceptors are used, this `post_add_local_inventories_with_metadata` interceptor runs after the
        `post_add_local_inventories` interceptor. The (possibly modified) response returned by
        `post_add_local_inventories` will be passed to
        `post_add_local_inventories_with_metadata`.
        """
        return response, metadata

    def pre_create_product(
        self,
        request: product_service.CreateProductRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.CreateProductRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_product

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_create_product(self, response: gcr_product.Product) -> gcr_product.Product:
        """Post-rpc interceptor for create_product

        DEPRECATED. Please use the `post_create_product_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_create_product` interceptor runs
        before the `post_create_product_with_metadata` interceptor.
        """
        return response

    def post_create_product_with_metadata(
        self,
        response: gcr_product.Product,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcr_product.Product, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_product

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_create_product_with_metadata`
        interceptor in new development instead of the `post_create_product` interceptor.
        When both interceptors are used, this `post_create_product_with_metadata` interceptor runs after the
        `post_create_product` interceptor. The (possibly modified) response returned by
        `post_create_product` will be passed to
        `post_create_product_with_metadata`.
        """
        return response, metadata

    def pre_delete_product(
        self,
        request: product_service.DeleteProductRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.DeleteProductRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_product

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def pre_get_product(
        self,
        request: product_service.GetProductRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.GetProductRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_product

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_get_product(self, response: product.Product) -> product.Product:
        """Post-rpc interceptor for get_product

        DEPRECATED. Please use the `post_get_product_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_get_product` interceptor runs
        before the `post_get_product_with_metadata` interceptor.
        """
        return response

    def post_get_product_with_metadata(
        self,
        response: product.Product,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[product.Product, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_product

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_get_product_with_metadata`
        interceptor in new development instead of the `post_get_product` interceptor.
        When both interceptors are used, this `post_get_product_with_metadata` interceptor runs after the
        `post_get_product` interceptor. The (possibly modified) response returned by
        `post_get_product` will be passed to
        `post_get_product_with_metadata`.
        """
        return response, metadata

    def pre_import_products(
        self,
        request: import_config.ImportProductsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        import_config.ImportProductsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import_products

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_import_products(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_products

        DEPRECATED. Please use the `post_import_products_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_import_products` interceptor runs
        before the `post_import_products_with_metadata` interceptor.
        """
        return response

    def post_import_products_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_products

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_import_products_with_metadata`
        interceptor in new development instead of the `post_import_products` interceptor.
        When both interceptors are used, this `post_import_products_with_metadata` interceptor runs after the
        `post_import_products` interceptor. The (possibly modified) response returned by
        `post_import_products` will be passed to
        `post_import_products_with_metadata`.
        """
        return response, metadata

    def pre_list_products(
        self,
        request: product_service.ListProductsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.ListProductsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_products

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_list_products(
        self, response: product_service.ListProductsResponse
    ) -> product_service.ListProductsResponse:
        """Post-rpc interceptor for list_products

        DEPRECATED. Please use the `post_list_products_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_list_products` interceptor runs
        before the `post_list_products_with_metadata` interceptor.
        """
        return response

    def post_list_products_with_metadata(
        self,
        response: product_service.ListProductsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.ListProductsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_products

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_list_products_with_metadata`
        interceptor in new development instead of the `post_list_products` interceptor.
        When both interceptors are used, this `post_list_products_with_metadata` interceptor runs after the
        `post_list_products` interceptor. The (possibly modified) response returned by
        `post_list_products` will be passed to
        `post_list_products_with_metadata`.
        """
        return response, metadata

    def pre_purge_products(
        self,
        request: purge_config.PurgeProductsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        purge_config.PurgeProductsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for purge_products

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_purge_products(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_products

        DEPRECATED. Please use the `post_purge_products_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_purge_products` interceptor runs
        before the `post_purge_products_with_metadata` interceptor.
        """
        return response

    def post_purge_products_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for purge_products

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_purge_products_with_metadata`
        interceptor in new development instead of the `post_purge_products` interceptor.
        When both interceptors are used, this `post_purge_products_with_metadata` interceptor runs after the
        `post_purge_products` interceptor. The (possibly modified) response returned by
        `post_purge_products` will be passed to
        `post_purge_products_with_metadata`.
        """
        return response, metadata

    def pre_remove_fulfillment_places(
        self,
        request: product_service.RemoveFulfillmentPlacesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.RemoveFulfillmentPlacesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_fulfillment_places

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_remove_fulfillment_places(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for remove_fulfillment_places

        DEPRECATED. Please use the `post_remove_fulfillment_places_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_remove_fulfillment_places` interceptor runs
        before the `post_remove_fulfillment_places_with_metadata` interceptor.
        """
        return response

    def post_remove_fulfillment_places_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_fulfillment_places

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_remove_fulfillment_places_with_metadata`
        interceptor in new development instead of the `post_remove_fulfillment_places` interceptor.
        When both interceptors are used, this `post_remove_fulfillment_places_with_metadata` interceptor runs after the
        `post_remove_fulfillment_places` interceptor. The (possibly modified) response returned by
        `post_remove_fulfillment_places` will be passed to
        `post_remove_fulfillment_places_with_metadata`.
        """
        return response, metadata

    def pre_remove_local_inventories(
        self,
        request: product_service.RemoveLocalInventoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.RemoveLocalInventoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_local_inventories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_remove_local_inventories(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for remove_local_inventories

        DEPRECATED. Please use the `post_remove_local_inventories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_remove_local_inventories` interceptor runs
        before the `post_remove_local_inventories_with_metadata` interceptor.
        """
        return response

    def post_remove_local_inventories_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_local_inventories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_remove_local_inventories_with_metadata`
        interceptor in new development instead of the `post_remove_local_inventories` interceptor.
        When both interceptors are used, this `post_remove_local_inventories_with_metadata` interceptor runs after the
        `post_remove_local_inventories` interceptor. The (possibly modified) response returned by
        `post_remove_local_inventories` will be passed to
        `post_remove_local_inventories_with_metadata`.
        """
        return response, metadata

    def pre_set_inventory(
        self,
        request: product_service.SetInventoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.SetInventoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_inventory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_set_inventory(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for set_inventory

        DEPRECATED. Please use the `post_set_inventory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_set_inventory` interceptor runs
        before the `post_set_inventory_with_metadata` interceptor.
        """
        return response

    def post_set_inventory_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_inventory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_set_inventory_with_metadata`
        interceptor in new development instead of the `post_set_inventory` interceptor.
        When both interceptors are used, this `post_set_inventory_with_metadata` interceptor runs after the
        `post_set_inventory` interceptor. The (possibly modified) response returned by
        `post_set_inventory` will be passed to
        `post_set_inventory_with_metadata`.
        """
        return response, metadata

    def pre_update_product(
        self,
        request: product_service.UpdateProductRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        product_service.UpdateProductRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_product

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_update_product(self, response: gcr_product.Product) -> gcr_product.Product:
        """Post-rpc interceptor for update_product

        DEPRECATED. Please use the `post_update_product_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code. This `post_update_product` interceptor runs
        before the `post_update_product_with_metadata` interceptor.
        """
        return response

    def post_update_product_with_metadata(
        self,
        response: gcr_product.Product,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcr_product.Product, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_product

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductService server but before it is returned to user code.

        We recommend only using this `post_update_product_with_metadata`
        interceptor in new development instead of the `post_update_product` interceptor.
        When both interceptors are used, this `post_update_product_with_metadata` interceptor runs after the
        `post_update_product` interceptor. The (possibly modified) response returned by
        `post_update_product` will be passed to
        `post_update_product_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ProductService server but before
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
        before they are sent to the ProductService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ProductService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ProductServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ProductServiceRestInterceptor


class ProductServiceRestTransport(_BaseProductServiceRestTransport):
    """REST backend synchronous transport for ProductService.

    Service for ingesting [Product][google.cloud.retail.v2.Product]
    information of the customer's website.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ProductServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'retail.googleapis.com').
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
            interceptor (Optional[ProductServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ProductServiceRestInterceptor()
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
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/catalogs/*/branches/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/catalogs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*/locations/*/catalogs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2/{name=projects/*}/operations",
                    },
                ],
            }

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

    class _AddFulfillmentPlaces(
        _BaseProductServiceRestTransport._BaseAddFulfillmentPlaces,
        ProductServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.AddFulfillmentPlaces")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.AddFulfillmentPlacesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the add fulfillment places method over HTTP.

            Args:
                request (~.product_service.AddFulfillmentPlacesRequest):
                    The request object. Request message for
                [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2.ProductService.AddFulfillmentPlaces]
                method.
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

            http_options = _BaseProductServiceRestTransport._BaseAddFulfillmentPlaces._get_http_options()
            request, metadata = self._interceptor.pre_add_fulfillment_places(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseAddFulfillmentPlaces,
                    "_BaseAddFulfillmentPlaces__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.AddFulfillmentPlaces",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "AddFulfillmentPlaces",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._AddFulfillmentPlaces._get_response(
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

            resp = self._interceptor.post_add_fulfillment_places(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_fulfillment_places_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.add_fulfillment_places",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "AddFulfillmentPlaces",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddLocalInventories(
        _BaseProductServiceRestTransport._BaseAddLocalInventories,
        ProductServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.AddLocalInventories")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.AddLocalInventoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the add local inventories method over HTTP.

            Args:
                request (~.product_service.AddLocalInventoriesRequest):
                    The request object. Request message for
                [ProductService.AddLocalInventories][google.cloud.retail.v2.ProductService.AddLocalInventories]
                method.
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

            http_options = _BaseProductServiceRestTransport._BaseAddLocalInventories._get_http_options()
            request, metadata = self._interceptor.pre_add_local_inventories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseAddLocalInventories,
                    "_BaseAddLocalInventories__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.AddLocalInventories",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "AddLocalInventories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._AddLocalInventories._get_response(
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

            resp = self._interceptor.post_add_local_inventories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_local_inventories_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.add_local_inventories",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "AddLocalInventories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProduct(
        _BaseProductServiceRestTransport._BaseCreateProduct, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.CreateProduct")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.CreateProductRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_product.Product:
            r"""Call the create product method over HTTP.

            Args:
                request (~.product_service.CreateProductRequest):
                    The request object. Request message for
                [ProductService.CreateProduct][google.cloud.retail.v2.ProductService.CreateProduct]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_product.Product:
                    Product captures all metadata
                information of items to be recommended
                or searched.

            """

            http_options = (
                _BaseProductServiceRestTransport._BaseCreateProduct._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_product(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseCreateProduct,
                    "_BaseCreateProduct__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.CreateProduct",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "CreateProduct",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._CreateProduct._get_response(
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
            resp = gcr_product.Product()
            pb_resp = gcr_product.Product.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_product(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_product_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_product.Product.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2.ProductServiceClient.create_product",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "CreateProduct",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteProduct(
        _BaseProductServiceRestTransport._BaseDeleteProduct, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.DeleteProduct")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: product_service.DeleteProductRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete product method over HTTP.

            Args:
                request (~.product_service.DeleteProductRequest):
                    The request object. Request message for
                [ProductService.DeleteProduct][google.cloud.retail.v2.ProductService.DeleteProduct]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseProductServiceRestTransport._BaseDeleteProduct._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_product(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseDeleteProduct,
                    "_BaseDeleteProduct__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.DeleteProduct",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "DeleteProduct",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._DeleteProduct._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetProduct(
        _BaseProductServiceRestTransport._BaseGetProduct, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.GetProduct")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: product_service.GetProductRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> product.Product:
            r"""Call the get product method over HTTP.

            Args:
                request (~.product_service.GetProductRequest):
                    The request object. Request message for
                [ProductService.GetProduct][google.cloud.retail.v2.ProductService.GetProduct]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.product.Product:
                    Product captures all metadata
                information of items to be recommended
                or searched.

            """

            http_options = (
                _BaseProductServiceRestTransport._BaseGetProduct._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_product(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseGetProduct,
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
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.GetProduct",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "GetProduct",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._GetProduct._get_response(
                self._host,
                metadata,
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
            resp = product.Product()
            pb_resp = product.Product.pb(resp)

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
                    response_payload = product.Product.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2.ProductServiceClient.get_product",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "GetProduct",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportProducts(
        _BaseProductServiceRestTransport._BaseImportProducts, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.ImportProducts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: import_config.ImportProductsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import products method over HTTP.

            Args:
                request (~.import_config.ImportProductsRequest):
                    The request object. Request message for Import methods.
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
                _BaseProductServiceRestTransport._BaseImportProducts._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_products(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseImportProducts,
                    "_BaseImportProducts__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.ImportProducts",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "ImportProducts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._ImportProducts._get_response(
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

            resp = self._interceptor.post_import_products(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_products_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.import_products",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "ImportProducts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProducts(
        _BaseProductServiceRestTransport._BaseListProducts, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.ListProducts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: product_service.ListProductsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> product_service.ListProductsResponse:
            r"""Call the list products method over HTTP.

            Args:
                request (~.product_service.ListProductsRequest):
                    The request object. Request message for
                [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.product_service.ListProductsResponse:
                    Response message for
                [ProductService.ListProducts][google.cloud.retail.v2.ProductService.ListProducts]
                method.

            """

            http_options = (
                _BaseProductServiceRestTransport._BaseListProducts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_products(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseListProducts,
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
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.ListProducts",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "ListProducts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._ListProducts._get_response(
                self._host,
                metadata,
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
            resp = product_service.ListProductsResponse()
            pb_resp = product_service.ListProductsResponse.pb(resp)

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
                    response_payload = product_service.ListProductsResponse.to_json(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.list_products",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "ListProducts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PurgeProducts(
        _BaseProductServiceRestTransport._BasePurgeProducts, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.PurgeProducts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: purge_config.PurgeProductsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge products method over HTTP.

            Args:
                request (~.purge_config.PurgeProductsRequest):
                    The request object. Request message for PurgeProducts
                method.
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
                _BaseProductServiceRestTransport._BasePurgeProducts._get_http_options()
            )
            request, metadata = self._interceptor.pre_purge_products(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BasePurgeProducts,
                    "_BasePurgeProducts__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.PurgeProducts",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "PurgeProducts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._PurgeProducts._get_response(
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

            resp = self._interceptor.post_purge_products(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_purge_products_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.purge_products",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "PurgeProducts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveFulfillmentPlaces(
        _BaseProductServiceRestTransport._BaseRemoveFulfillmentPlaces,
        ProductServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.RemoveFulfillmentPlaces")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.RemoveFulfillmentPlacesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the remove fulfillment places method over HTTP.

            Args:
                request (~.product_service.RemoveFulfillmentPlacesRequest):
                    The request object. Request message for
                [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2.ProductService.RemoveFulfillmentPlaces]
                method.
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

            http_options = _BaseProductServiceRestTransport._BaseRemoveFulfillmentPlaces._get_http_options()
            request, metadata = self._interceptor.pre_remove_fulfillment_places(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseRemoveFulfillmentPlaces,
                    "_BaseRemoveFulfillmentPlaces__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.RemoveFulfillmentPlaces",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "RemoveFulfillmentPlaces",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProductServiceRestTransport._RemoveFulfillmentPlaces._get_response(
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

            resp = self._interceptor.post_remove_fulfillment_places(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_fulfillment_places_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.remove_fulfillment_places",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "RemoveFulfillmentPlaces",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveLocalInventories(
        _BaseProductServiceRestTransport._BaseRemoveLocalInventories,
        ProductServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.RemoveLocalInventories")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.RemoveLocalInventoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the remove local inventories method over HTTP.

            Args:
                request (~.product_service.RemoveLocalInventoriesRequest):
                    The request object. Request message for
                [ProductService.RemoveLocalInventories][google.cloud.retail.v2.ProductService.RemoveLocalInventories]
                method.
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

            http_options = _BaseProductServiceRestTransport._BaseRemoveLocalInventories._get_http_options()
            request, metadata = self._interceptor.pre_remove_local_inventories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseRemoveLocalInventories,
                    "_BaseRemoveLocalInventories__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.RemoveLocalInventories",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "RemoveLocalInventories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProductServiceRestTransport._RemoveLocalInventories._get_response(
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

            resp = self._interceptor.post_remove_local_inventories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_local_inventories_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.remove_local_inventories",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "RemoveLocalInventories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetInventory(
        _BaseProductServiceRestTransport._BaseSetInventory, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.SetInventory")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.SetInventoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the set inventory method over HTTP.

            Args:
                request (~.product_service.SetInventoryRequest):
                    The request object. Request message for
                [ProductService.SetInventory][google.cloud.retail.v2.ProductService.SetInventory]
                method.
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
                _BaseProductServiceRestTransport._BaseSetInventory._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_inventory(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseSetInventory,
                    "_BaseSetInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.SetInventory",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "SetInventory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._SetInventory._get_response(
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

            resp = self._interceptor.post_set_inventory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_inventory_with_metadata(
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
                    "Received response for google.cloud.retail_v2.ProductServiceClient.set_inventory",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "SetInventory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProduct(
        _BaseProductServiceRestTransport._BaseUpdateProduct, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.UpdateProduct")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: product_service.UpdateProductRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_product.Product:
            r"""Call the update product method over HTTP.

            Args:
                request (~.product_service.UpdateProductRequest):
                    The request object. Request message for
                [ProductService.UpdateProduct][google.cloud.retail.v2.ProductService.UpdateProduct]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_product.Product:
                    Product captures all metadata
                information of items to be recommended
                or searched.

            """

            http_options = (
                _BaseProductServiceRestTransport._BaseUpdateProduct._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_product(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseUpdateProduct,
                    "_BaseUpdateProduct__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.UpdateProduct",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "UpdateProduct",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._UpdateProduct._get_response(
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
            resp = gcr_product.Product()
            pb_resp = gcr_product.Product.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_product(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_product_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_product.Product.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2.ProductServiceClient.update_product",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "UpdateProduct",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_fulfillment_places(
        self,
    ) -> Callable[
        [product_service.AddFulfillmentPlacesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddFulfillmentPlaces(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_local_inventories(
        self,
    ) -> Callable[
        [product_service.AddLocalInventoriesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddLocalInventories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_product(
        self,
    ) -> Callable[[product_service.CreateProductRequest], gcr_product.Product]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProduct(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_product(
        self,
    ) -> Callable[[product_service.DeleteProductRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProduct(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_product(
        self,
    ) -> Callable[[product_service.GetProductRequest], product.Product]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProduct(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_products(
        self,
    ) -> Callable[[import_config.ImportProductsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportProducts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_products(
        self,
    ) -> Callable[
        [product_service.ListProductsRequest], product_service.ListProductsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProducts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_products(
        self,
    ) -> Callable[[purge_config.PurgeProductsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeProducts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_fulfillment_places(
        self,
    ) -> Callable[
        [product_service.RemoveFulfillmentPlacesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveFulfillmentPlaces(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def remove_local_inventories(
        self,
    ) -> Callable[
        [product_service.RemoveLocalInventoriesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveLocalInventories(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_inventory(
        self,
    ) -> Callable[[product_service.SetInventoryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetInventory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_product(
        self,
    ) -> Callable[[product_service.UpdateProductRequest], gcr_product.Product]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProduct(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseProductServiceRestTransport._BaseGetOperation, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseProductServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._GetOperation._get_response(
                self._host,
                metadata,
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
                    "Received response for google.cloud.retail_v2.ProductServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
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
        _BaseProductServiceRestTransport._BaseListOperations, ProductServiceRestStub
    ):
        def __hash__(self):
            return hash("ProductServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseProductServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.retail_v2.ProductServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProductServiceRestTransport._ListOperations._get_response(
                self._host,
                metadata,
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
                    "Received response for google.cloud.retail_v2.ProductServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2.ProductService",
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


__all__ = ("ProductServiceRestTransport",)
