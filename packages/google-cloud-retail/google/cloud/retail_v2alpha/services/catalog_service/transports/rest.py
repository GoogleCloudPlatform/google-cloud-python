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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.retail_v2alpha._compat import transcode_request
from google.cloud.retail_v2alpha.types import catalog, catalog_service
from google.cloud.retail_v2alpha.types import catalog as gcr_catalog

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCatalogServiceRestTransport

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


class CatalogServiceRestInterceptor:
    """Interceptor for CatalogService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CatalogServiceRestTransport.

    .. code-block:: python
        class MyCustomCatalogServiceInterceptor(CatalogServiceRestInterceptor):
            def pre_add_catalog_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_catalog_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_remove_catalog_attributes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_remove_catalog_attributes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_attributes_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_attributes_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_completion_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_completion_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_default_branch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_default_branch(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_catalogs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_catalogs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_catalog_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_catalog_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_replace_catalog_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_replace_catalog_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_default_branch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_update_attributes_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_attributes_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_completion_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_completion_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CatalogServiceRestTransport(interceptor=MyCustomCatalogServiceInterceptor())
        client = CatalogServiceClient(transport=transport)


    """

    def pre_add_catalog_attribute(
        self,
        request: catalog_service.AddCatalogAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.AddCatalogAttributeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_catalog_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_add_catalog_attribute(
        self, response: catalog.AttributesConfig
    ) -> catalog.AttributesConfig:
        """Post-rpc interceptor for add_catalog_attribute

        DEPRECATED. Please use the `post_add_catalog_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_add_catalog_attribute` interceptor runs
        before the `post_add_catalog_attribute_with_metadata` interceptor.
        """
        return response

    def post_add_catalog_attribute_with_metadata(
        self,
        response: catalog.AttributesConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.AttributesConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_catalog_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_add_catalog_attribute_with_metadata`
        interceptor in new development instead of the `post_add_catalog_attribute` interceptor.
        When both interceptors are used, this `post_add_catalog_attribute_with_metadata` interceptor runs after the
        `post_add_catalog_attribute` interceptor. The (possibly modified) response returned by
        `post_add_catalog_attribute` will be passed to
        `post_add_catalog_attribute_with_metadata`.
        """
        return response, metadata

    def pre_batch_remove_catalog_attributes(
        self,
        request: catalog_service.BatchRemoveCatalogAttributesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.BatchRemoveCatalogAttributesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_remove_catalog_attributes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_batch_remove_catalog_attributes(
        self, response: catalog_service.BatchRemoveCatalogAttributesResponse
    ) -> catalog_service.BatchRemoveCatalogAttributesResponse:
        """Post-rpc interceptor for batch_remove_catalog_attributes

        DEPRECATED. Please use the `post_batch_remove_catalog_attributes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_batch_remove_catalog_attributes` interceptor runs
        before the `post_batch_remove_catalog_attributes_with_metadata` interceptor.
        """
        return response

    def post_batch_remove_catalog_attributes_with_metadata(
        self,
        response: catalog_service.BatchRemoveCatalogAttributesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.BatchRemoveCatalogAttributesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_remove_catalog_attributes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_batch_remove_catalog_attributes_with_metadata`
        interceptor in new development instead of the `post_batch_remove_catalog_attributes` interceptor.
        When both interceptors are used, this `post_batch_remove_catalog_attributes_with_metadata` interceptor runs after the
        `post_batch_remove_catalog_attributes` interceptor. The (possibly modified) response returned by
        `post_batch_remove_catalog_attributes` will be passed to
        `post_batch_remove_catalog_attributes_with_metadata`.
        """
        return response, metadata

    def pre_get_attributes_config(
        self,
        request: catalog_service.GetAttributesConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.GetAttributesConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_attributes_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_get_attributes_config(
        self, response: catalog.AttributesConfig
    ) -> catalog.AttributesConfig:
        """Post-rpc interceptor for get_attributes_config

        DEPRECATED. Please use the `post_get_attributes_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_get_attributes_config` interceptor runs
        before the `post_get_attributes_config_with_metadata` interceptor.
        """
        return response

    def post_get_attributes_config_with_metadata(
        self,
        response: catalog.AttributesConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.AttributesConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_attributes_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_get_attributes_config_with_metadata`
        interceptor in new development instead of the `post_get_attributes_config` interceptor.
        When both interceptors are used, this `post_get_attributes_config_with_metadata` interceptor runs after the
        `post_get_attributes_config` interceptor. The (possibly modified) response returned by
        `post_get_attributes_config` will be passed to
        `post_get_attributes_config_with_metadata`.
        """
        return response, metadata

    def pre_get_completion_config(
        self,
        request: catalog_service.GetCompletionConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.GetCompletionConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_completion_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_get_completion_config(
        self, response: catalog.CompletionConfig
    ) -> catalog.CompletionConfig:
        """Post-rpc interceptor for get_completion_config

        DEPRECATED. Please use the `post_get_completion_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_get_completion_config` interceptor runs
        before the `post_get_completion_config_with_metadata` interceptor.
        """
        return response

    def post_get_completion_config_with_metadata(
        self,
        response: catalog.CompletionConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.CompletionConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_completion_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_get_completion_config_with_metadata`
        interceptor in new development instead of the `post_get_completion_config` interceptor.
        When both interceptors are used, this `post_get_completion_config_with_metadata` interceptor runs after the
        `post_get_completion_config` interceptor. The (possibly modified) response returned by
        `post_get_completion_config` will be passed to
        `post_get_completion_config_with_metadata`.
        """
        return response, metadata

    def pre_get_default_branch(
        self,
        request: catalog_service.GetDefaultBranchRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.GetDefaultBranchRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_default_branch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_get_default_branch(
        self, response: catalog_service.GetDefaultBranchResponse
    ) -> catalog_service.GetDefaultBranchResponse:
        """Post-rpc interceptor for get_default_branch

        DEPRECATED. Please use the `post_get_default_branch_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_get_default_branch` interceptor runs
        before the `post_get_default_branch_with_metadata` interceptor.
        """
        return response

    def post_get_default_branch_with_metadata(
        self,
        response: catalog_service.GetDefaultBranchResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.GetDefaultBranchResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_default_branch

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_get_default_branch_with_metadata`
        interceptor in new development instead of the `post_get_default_branch` interceptor.
        When both interceptors are used, this `post_get_default_branch_with_metadata` interceptor runs after the
        `post_get_default_branch` interceptor. The (possibly modified) response returned by
        `post_get_default_branch` will be passed to
        `post_get_default_branch_with_metadata`.
        """
        return response, metadata

    def pre_list_catalogs(
        self,
        request: catalog_service.ListCatalogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.ListCatalogsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_catalogs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_list_catalogs(
        self, response: catalog_service.ListCatalogsResponse
    ) -> catalog_service.ListCatalogsResponse:
        """Post-rpc interceptor for list_catalogs

        DEPRECATED. Please use the `post_list_catalogs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_list_catalogs` interceptor runs
        before the `post_list_catalogs_with_metadata` interceptor.
        """
        return response

    def post_list_catalogs_with_metadata(
        self,
        response: catalog_service.ListCatalogsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.ListCatalogsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_catalogs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_list_catalogs_with_metadata`
        interceptor in new development instead of the `post_list_catalogs` interceptor.
        When both interceptors are used, this `post_list_catalogs_with_metadata` interceptor runs after the
        `post_list_catalogs` interceptor. The (possibly modified) response returned by
        `post_list_catalogs` will be passed to
        `post_list_catalogs_with_metadata`.
        """
        return response, metadata

    def pre_remove_catalog_attribute(
        self,
        request: catalog_service.RemoveCatalogAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.RemoveCatalogAttributeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_catalog_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_remove_catalog_attribute(
        self, response: catalog.AttributesConfig
    ) -> catalog.AttributesConfig:
        """Post-rpc interceptor for remove_catalog_attribute

        DEPRECATED. Please use the `post_remove_catalog_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_remove_catalog_attribute` interceptor runs
        before the `post_remove_catalog_attribute_with_metadata` interceptor.
        """
        return response

    def post_remove_catalog_attribute_with_metadata(
        self,
        response: catalog.AttributesConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.AttributesConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_catalog_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_remove_catalog_attribute_with_metadata`
        interceptor in new development instead of the `post_remove_catalog_attribute` interceptor.
        When both interceptors are used, this `post_remove_catalog_attribute_with_metadata` interceptor runs after the
        `post_remove_catalog_attribute` interceptor. The (possibly modified) response returned by
        `post_remove_catalog_attribute` will be passed to
        `post_remove_catalog_attribute_with_metadata`.
        """
        return response, metadata

    def pre_replace_catalog_attribute(
        self,
        request: catalog_service.ReplaceCatalogAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.ReplaceCatalogAttributeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for replace_catalog_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_replace_catalog_attribute(
        self, response: catalog.AttributesConfig
    ) -> catalog.AttributesConfig:
        """Post-rpc interceptor for replace_catalog_attribute

        DEPRECATED. Please use the `post_replace_catalog_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_replace_catalog_attribute` interceptor runs
        before the `post_replace_catalog_attribute_with_metadata` interceptor.
        """
        return response

    def post_replace_catalog_attribute_with_metadata(
        self,
        response: catalog.AttributesConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.AttributesConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for replace_catalog_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_replace_catalog_attribute_with_metadata`
        interceptor in new development instead of the `post_replace_catalog_attribute` interceptor.
        When both interceptors are used, this `post_replace_catalog_attribute_with_metadata` interceptor runs after the
        `post_replace_catalog_attribute` interceptor. The (possibly modified) response returned by
        `post_replace_catalog_attribute` will be passed to
        `post_replace_catalog_attribute_with_metadata`.
        """
        return response, metadata

    def pre_set_default_branch(
        self,
        request: catalog_service.SetDefaultBranchRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.SetDefaultBranchRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_default_branch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def pre_update_attributes_config(
        self,
        request: catalog_service.UpdateAttributesConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.UpdateAttributesConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_attributes_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_update_attributes_config(
        self, response: catalog.AttributesConfig
    ) -> catalog.AttributesConfig:
        """Post-rpc interceptor for update_attributes_config

        DEPRECATED. Please use the `post_update_attributes_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_update_attributes_config` interceptor runs
        before the `post_update_attributes_config_with_metadata` interceptor.
        """
        return response

    def post_update_attributes_config_with_metadata(
        self,
        response: catalog.AttributesConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.AttributesConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_attributes_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_update_attributes_config_with_metadata`
        interceptor in new development instead of the `post_update_attributes_config` interceptor.
        When both interceptors are used, this `post_update_attributes_config_with_metadata` interceptor runs after the
        `post_update_attributes_config` interceptor. The (possibly modified) response returned by
        `post_update_attributes_config` will be passed to
        `post_update_attributes_config_with_metadata`.
        """
        return response, metadata

    def pre_update_catalog(
        self,
        request: catalog_service.UpdateCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.UpdateCatalogRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_update_catalog(self, response: gcr_catalog.Catalog) -> gcr_catalog.Catalog:
        """Post-rpc interceptor for update_catalog

        DEPRECATED. Please use the `post_update_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_update_catalog` interceptor runs
        before the `post_update_catalog_with_metadata` interceptor.
        """
        return response

    def post_update_catalog_with_metadata(
        self,
        response: gcr_catalog.Catalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcr_catalog.Catalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_update_catalog_with_metadata`
        interceptor in new development instead of the `post_update_catalog` interceptor.
        When both interceptors are used, this `post_update_catalog_with_metadata` interceptor runs after the
        `post_update_catalog` interceptor. The (possibly modified) response returned by
        `post_update_catalog` will be passed to
        `post_update_catalog_with_metadata`.
        """
        return response, metadata

    def pre_update_completion_config(
        self,
        request: catalog_service.UpdateCompletionConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_service.UpdateCompletionConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_completion_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_update_completion_config(
        self, response: catalog.CompletionConfig
    ) -> catalog.CompletionConfig:
        """Post-rpc interceptor for update_completion_config

        DEPRECATED. Please use the `post_update_completion_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code. This `post_update_completion_config` interceptor runs
        before the `post_update_completion_config_with_metadata` interceptor.
        """
        return response

    def post_update_completion_config_with_metadata(
        self,
        response: catalog.CompletionConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog.CompletionConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_completion_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CatalogService server but before it is returned to user code.

        We recommend only using this `post_update_completion_config_with_metadata`
        interceptor in new development instead of the `post_update_completion_config` interceptor.
        When both interceptors are used, this `post_update_completion_config_with_metadata` interceptor runs after the
        `post_update_completion_config` interceptor. The (possibly modified) response returned by
        `post_update_completion_config` will be passed to
        `post_update_completion_config_with_metadata`.
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
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CatalogService server but before
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
        before they are sent to the CatalogService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CatalogService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CatalogServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CatalogServiceRestInterceptor


class CatalogServiceRestTransport(_BaseCatalogServiceRestTransport):
    """REST backend synchronous transport for CatalogService.

    Service for managing catalog configuration.

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
        interceptor: Optional[CatalogServiceRestInterceptor] = None,
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
            interceptor (Optional[CatalogServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CatalogServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AddCatalogAttribute(
        _BaseCatalogServiceRestTransport._BaseAddCatalogAttribute,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.AddCatalogAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.AddCatalogAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.AttributesConfig:
            r"""Call the add catalog attribute method over HTTP.

            Args:
                request (~.catalog_service.AddCatalogAttributeRequest):
                    The request object. Request for
                [CatalogService.AddCatalogAttribute][google.cloud.retail.v2alpha.CatalogService.AddCatalogAttribute]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.AttributesConfig:
                    Catalog level attribute config.
            """

            http_options = _BaseCatalogServiceRestTransport._BaseAddCatalogAttribute._get_http_options()
            request, metadata = self._interceptor.pre_add_catalog_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseAddCatalogAttribute,
                    "_BaseAddCatalogAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.AddCatalogAttribute",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "AddCatalogAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._AddCatalogAttribute._get_response(
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
            resp = catalog.AttributesConfig()
            pb_resp = catalog.AttributesConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_catalog_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_catalog_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.AttributesConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.add_catalog_attribute",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "AddCatalogAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRemoveCatalogAttributes(
        _BaseCatalogServiceRestTransport._BaseBatchRemoveCatalogAttributes,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.BatchRemoveCatalogAttributes")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.BatchRemoveCatalogAttributesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_service.BatchRemoveCatalogAttributesResponse:
            r"""Call the batch remove catalog
            attributes method over HTTP.

                Args:
                    request (~.catalog_service.BatchRemoveCatalogAttributesRequest):
                        The request object. Request for
                    [CatalogService.BatchRemoveCatalogAttributes][google.cloud.retail.v2alpha.CatalogService.BatchRemoveCatalogAttributes]
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.catalog_service.BatchRemoveCatalogAttributesResponse:
                        Response of the
                    [CatalogService.BatchRemoveCatalogAttributes][google.cloud.retail.v2alpha.CatalogService.BatchRemoveCatalogAttributes].

            """

            http_options = _BaseCatalogServiceRestTransport._BaseBatchRemoveCatalogAttributes._get_http_options()
            request, metadata = self._interceptor.pre_batch_remove_catalog_attributes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseBatchRemoveCatalogAttributes,
                    "_BaseBatchRemoveCatalogAttributes__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.BatchRemoveCatalogAttributes",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "BatchRemoveCatalogAttributes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CatalogServiceRestTransport._BatchRemoveCatalogAttributes._get_response(
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
            resp = catalog_service.BatchRemoveCatalogAttributesResponse()
            pb_resp = catalog_service.BatchRemoveCatalogAttributesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_remove_catalog_attributes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_remove_catalog_attributes_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        catalog_service.BatchRemoveCatalogAttributesResponse.to_json(
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
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.batch_remove_catalog_attributes",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "BatchRemoveCatalogAttributes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAttributesConfig(
        _BaseCatalogServiceRestTransport._BaseGetAttributesConfig,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.GetAttributesConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: catalog_service.GetAttributesConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.AttributesConfig:
            r"""Call the get attributes config method over HTTP.

            Args:
                request (~.catalog_service.GetAttributesConfigRequest):
                    The request object. Request for
                [CatalogService.GetAttributesConfig][google.cloud.retail.v2alpha.CatalogService.GetAttributesConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.AttributesConfig:
                    Catalog level attribute config.
            """

            http_options = _BaseCatalogServiceRestTransport._BaseGetAttributesConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_attributes_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseGetAttributesConfig,
                    "_BaseGetAttributesConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.GetAttributesConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetAttributesConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._GetAttributesConfig._get_response(
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
            resp = catalog.AttributesConfig()
            pb_resp = catalog.AttributesConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_attributes_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_attributes_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.AttributesConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.get_attributes_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetAttributesConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCompletionConfig(
        _BaseCatalogServiceRestTransport._BaseGetCompletionConfig,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.GetCompletionConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: catalog_service.GetCompletionConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.CompletionConfig:
            r"""Call the get completion config method over HTTP.

            Args:
                request (~.catalog_service.GetCompletionConfigRequest):
                    The request object. Request for
                [CatalogService.GetCompletionConfig][google.cloud.retail.v2alpha.CatalogService.GetCompletionConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.CompletionConfig:
                    Catalog level autocomplete config for
                customers to customize autocomplete
                feature's settings.

            """

            http_options = _BaseCatalogServiceRestTransport._BaseGetCompletionConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_completion_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseGetCompletionConfig,
                    "_BaseGetCompletionConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.GetCompletionConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetCompletionConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._GetCompletionConfig._get_response(
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
            resp = catalog.CompletionConfig()
            pb_resp = catalog.CompletionConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_completion_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_completion_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.CompletionConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.get_completion_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetCompletionConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDefaultBranch(
        _BaseCatalogServiceRestTransport._BaseGetDefaultBranch, CatalogServiceRestStub
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.GetDefaultBranch")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: catalog_service.GetDefaultBranchRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_service.GetDefaultBranchResponse:
            r"""Call the get default branch method over HTTP.

            Args:
                request (~.catalog_service.GetDefaultBranchRequest):
                    The request object. Request message to show which branch
                is currently the default branch.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_service.GetDefaultBranchResponse:
                    Response message of
                [CatalogService.GetDefaultBranch][google.cloud.retail.v2alpha.CatalogService.GetDefaultBranch].

            """

            http_options = _BaseCatalogServiceRestTransport._BaseGetDefaultBranch._get_http_options()
            request, metadata = self._interceptor.pre_get_default_branch(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseGetDefaultBranch,
                    "_BaseGetDefaultBranch__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.GetDefaultBranch",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetDefaultBranch",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._GetDefaultBranch._get_response(
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
            resp = catalog_service.GetDefaultBranchResponse()
            pb_resp = catalog_service.GetDefaultBranchResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_default_branch(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_default_branch_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_service.GetDefaultBranchResponse.to_json(
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
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.get_default_branch",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetDefaultBranch",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCatalogs(
        _BaseCatalogServiceRestTransport._BaseListCatalogs, CatalogServiceRestStub
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.ListCatalogs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: catalog_service.ListCatalogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_service.ListCatalogsResponse:
            r"""Call the list catalogs method over HTTP.

            Args:
                request (~.catalog_service.ListCatalogsRequest):
                    The request object. Request for
                [CatalogService.ListCatalogs][google.cloud.retail.v2alpha.CatalogService.ListCatalogs]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_service.ListCatalogsResponse:
                    Response for
                [CatalogService.ListCatalogs][google.cloud.retail.v2alpha.CatalogService.ListCatalogs]
                method.

            """

            http_options = (
                _BaseCatalogServiceRestTransport._BaseListCatalogs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_catalogs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseListCatalogs,
                    "_BaseListCatalogs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.ListCatalogs",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "ListCatalogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._ListCatalogs._get_response(
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
            resp = catalog_service.ListCatalogsResponse()
            pb_resp = catalog_service.ListCatalogsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_catalogs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_catalogs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_service.ListCatalogsResponse.to_json(
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
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.list_catalogs",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "ListCatalogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveCatalogAttribute(
        _BaseCatalogServiceRestTransport._BaseRemoveCatalogAttribute,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.RemoveCatalogAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.RemoveCatalogAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.AttributesConfig:
            r"""Call the remove catalog attribute method over HTTP.

            Args:
                request (~.catalog_service.RemoveCatalogAttributeRequest):
                    The request object. Request for
                [CatalogService.RemoveCatalogAttribute][google.cloud.retail.v2alpha.CatalogService.RemoveCatalogAttribute]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.AttributesConfig:
                    Catalog level attribute config.
            """

            http_options = _BaseCatalogServiceRestTransport._BaseRemoveCatalogAttribute._get_http_options()
            request, metadata = self._interceptor.pre_remove_catalog_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseRemoveCatalogAttribute,
                    "_BaseRemoveCatalogAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.RemoveCatalogAttribute",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "RemoveCatalogAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CatalogServiceRestTransport._RemoveCatalogAttribute._get_response(
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
            resp = catalog.AttributesConfig()
            pb_resp = catalog.AttributesConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_catalog_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_catalog_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.AttributesConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.remove_catalog_attribute",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "RemoveCatalogAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReplaceCatalogAttribute(
        _BaseCatalogServiceRestTransport._BaseReplaceCatalogAttribute,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.ReplaceCatalogAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.ReplaceCatalogAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.AttributesConfig:
            r"""Call the replace catalog attribute method over HTTP.

            Args:
                request (~.catalog_service.ReplaceCatalogAttributeRequest):
                    The request object. Request for
                [CatalogService.ReplaceCatalogAttribute][google.cloud.retail.v2alpha.CatalogService.ReplaceCatalogAttribute]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.AttributesConfig:
                    Catalog level attribute config.
            """

            http_options = _BaseCatalogServiceRestTransport._BaseReplaceCatalogAttribute._get_http_options()
            request, metadata = self._interceptor.pre_replace_catalog_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseReplaceCatalogAttribute,
                    "_BaseReplaceCatalogAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.ReplaceCatalogAttribute",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "ReplaceCatalogAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CatalogServiceRestTransport._ReplaceCatalogAttribute._get_response(
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
            resp = catalog.AttributesConfig()
            pb_resp = catalog.AttributesConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_replace_catalog_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_replace_catalog_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.AttributesConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.replace_catalog_attribute",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "ReplaceCatalogAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetDefaultBranch(
        _BaseCatalogServiceRestTransport._BaseSetDefaultBranch, CatalogServiceRestStub
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.SetDefaultBranch")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.SetDefaultBranchRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the set default branch method over HTTP.

            Args:
                request (~.catalog_service.SetDefaultBranchRequest):
                    The request object. Request message to set a specified branch as new
                default_branch.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCatalogServiceRestTransport._BaseSetDefaultBranch._get_http_options()
            request, metadata = self._interceptor.pre_set_default_branch(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseSetDefaultBranch,
                    "_BaseSetDefaultBranch__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.SetDefaultBranch",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "SetDefaultBranch",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._SetDefaultBranch._get_response(
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

    class _UpdateAttributesConfig(
        _BaseCatalogServiceRestTransport._BaseUpdateAttributesConfig,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.UpdateAttributesConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.UpdateAttributesConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.AttributesConfig:
            r"""Call the update attributes config method over HTTP.

            Args:
                request (~.catalog_service.UpdateAttributesConfigRequest):
                    The request object. Request for
                [CatalogService.UpdateAttributesConfig][google.cloud.retail.v2alpha.CatalogService.UpdateAttributesConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.AttributesConfig:
                    Catalog level attribute config.
            """

            http_options = _BaseCatalogServiceRestTransport._BaseUpdateAttributesConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_attributes_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseUpdateAttributesConfig,
                    "_BaseUpdateAttributesConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.UpdateAttributesConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "UpdateAttributesConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CatalogServiceRestTransport._UpdateAttributesConfig._get_response(
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
            resp = catalog.AttributesConfig()
            pb_resp = catalog.AttributesConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_attributes_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_attributes_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.AttributesConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.update_attributes_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "UpdateAttributesConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCatalog(
        _BaseCatalogServiceRestTransport._BaseUpdateCatalog, CatalogServiceRestStub
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.UpdateCatalog")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.UpdateCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_catalog.Catalog:
            r"""Call the update catalog method over HTTP.

            Args:
                request (~.catalog_service.UpdateCatalogRequest):
                    The request object. Request for
                [CatalogService.UpdateCatalog][google.cloud.retail.v2alpha.CatalogService.UpdateCatalog]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_catalog.Catalog:
                    The catalog configuration.
            """

            http_options = (
                _BaseCatalogServiceRestTransport._BaseUpdateCatalog._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_catalog(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseUpdateCatalog,
                    "_BaseUpdateCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.UpdateCatalog",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "UpdateCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._UpdateCatalog._get_response(
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
            resp = gcr_catalog.Catalog()
            pb_resp = gcr_catalog.Catalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_catalog.Catalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.update_catalog",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "UpdateCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCompletionConfig(
        _BaseCatalogServiceRestTransport._BaseUpdateCompletionConfig,
        CatalogServiceRestStub,
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.UpdateCompletionConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: catalog_service.UpdateCompletionConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog.CompletionConfig:
            r"""Call the update completion config method over HTTP.

            Args:
                request (~.catalog_service.UpdateCompletionConfigRequest):
                    The request object. Request for
                [CatalogService.UpdateCompletionConfig][google.cloud.retail.v2alpha.CatalogService.UpdateCompletionConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog.CompletionConfig:
                    Catalog level autocomplete config for
                customers to customize autocomplete
                feature's settings.

            """

            http_options = _BaseCatalogServiceRestTransport._BaseUpdateCompletionConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_completion_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseUpdateCompletionConfig,
                    "_BaseUpdateCompletionConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.UpdateCompletionConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "UpdateCompletionConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CatalogServiceRestTransport._UpdateCompletionConfig._get_response(
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
            resp = catalog.CompletionConfig()
            pb_resp = catalog.CompletionConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_completion_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_completion_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog.CompletionConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceClient.update_completion_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "UpdateCompletionConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_catalog_attribute(
        self,
    ) -> Callable[
        [catalog_service.AddCatalogAttributeRequest], catalog.AttributesConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddCatalogAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_remove_catalog_attributes(
        self,
    ) -> Callable[
        [catalog_service.BatchRemoveCatalogAttributesRequest],
        catalog_service.BatchRemoveCatalogAttributesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRemoveCatalogAttributes(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_attributes_config(
        self,
    ) -> Callable[
        [catalog_service.GetAttributesConfigRequest], catalog.AttributesConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAttributesConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_completion_config(
        self,
    ) -> Callable[
        [catalog_service.GetCompletionConfigRequest], catalog.CompletionConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCompletionConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_default_branch(
        self,
    ) -> Callable[
        [catalog_service.GetDefaultBranchRequest],
        catalog_service.GetDefaultBranchResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDefaultBranch(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_catalogs(
        self,
    ) -> Callable[
        [catalog_service.ListCatalogsRequest], catalog_service.ListCatalogsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCatalogs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_catalog_attribute(
        self,
    ) -> Callable[
        [catalog_service.RemoveCatalogAttributeRequest], catalog.AttributesConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveCatalogAttribute(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def replace_catalog_attribute(
        self,
    ) -> Callable[
        [catalog_service.ReplaceCatalogAttributeRequest], catalog.AttributesConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReplaceCatalogAttribute(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def set_default_branch(
        self,
    ) -> Callable[[catalog_service.SetDefaultBranchRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetDefaultBranch(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_attributes_config(
        self,
    ) -> Callable[
        [catalog_service.UpdateAttributesConfigRequest], catalog.AttributesConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAttributesConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_catalog(
        self,
    ) -> Callable[[catalog_service.UpdateCatalogRequest], gcr_catalog.Catalog]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_completion_config(
        self,
    ) -> Callable[
        [catalog_service.UpdateCompletionConfigRequest], catalog.CompletionConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCompletionConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCatalogServiceRestTransport._BaseGetOperation, CatalogServiceRestStub
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseCatalogServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
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
        _BaseCatalogServiceRestTransport._BaseListOperations, CatalogServiceRestStub
    ):
        def __hash__(self):
            return hash("CatalogServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
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
                _BaseCatalogServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCatalogServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.retail_v2alpha.CatalogServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CatalogServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.retail_v2alpha.CatalogServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.CatalogService",
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


__all__ = ("CatalogServiceRestTransport",)
