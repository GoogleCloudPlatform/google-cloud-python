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

from google.cloud.dataplex_v1._compat import transcode_request
from google.cloud.dataplex_v1.types import data_taxonomy
from google.cloud.dataplex_v1.types import data_taxonomy as gcd_data_taxonomy

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataTaxonomyServiceRestTransport

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


class DataTaxonomyServiceRestInterceptor:
    """Interceptor for DataTaxonomyService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataTaxonomyServiceRestTransport.

    .. code-block:: python
        class MyCustomDataTaxonomyServiceInterceptor(DataTaxonomyServiceRestInterceptor):
            def pre_create_data_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_attribute_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_attribute_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_taxonomy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_taxonomy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_data_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_data_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_data_attribute_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_data_attribute_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_data_taxonomy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_data_taxonomy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_attribute_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_attribute_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_taxonomy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_taxonomy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_attribute_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_attribute_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_attributes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_attributes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_taxonomies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_taxonomies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_attribute_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_attribute_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_taxonomy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_taxonomy(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataTaxonomyServiceRestTransport(interceptor=MyCustomDataTaxonomyServiceInterceptor())
        client = DataTaxonomyServiceClient(transport=transport)


    """

    def pre_create_data_attribute(
        self,
        request: data_taxonomy.CreateDataAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.CreateDataAttributeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_data_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_create_data_attribute(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_data_attribute

        DEPRECATED. Please use the `post_create_data_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_create_data_attribute` interceptor runs
        before the `post_create_data_attribute_with_metadata` interceptor.
        """
        return response

    def post_create_data_attribute_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_create_data_attribute_with_metadata`
        interceptor in new development instead of the `post_create_data_attribute` interceptor.
        When both interceptors are used, this `post_create_data_attribute_with_metadata` interceptor runs after the
        `post_create_data_attribute` interceptor. The (possibly modified) response returned by
        `post_create_data_attribute` will be passed to
        `post_create_data_attribute_with_metadata`.
        """
        return response, metadata

    def pre_create_data_attribute_binding(
        self,
        request: data_taxonomy.CreateDataAttributeBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.CreateDataAttributeBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_data_attribute_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_create_data_attribute_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_data_attribute_binding

        DEPRECATED. Please use the `post_create_data_attribute_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_create_data_attribute_binding` interceptor runs
        before the `post_create_data_attribute_binding_with_metadata` interceptor.
        """
        return response

    def post_create_data_attribute_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_attribute_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_create_data_attribute_binding_with_metadata`
        interceptor in new development instead of the `post_create_data_attribute_binding` interceptor.
        When both interceptors are used, this `post_create_data_attribute_binding_with_metadata` interceptor runs after the
        `post_create_data_attribute_binding` interceptor. The (possibly modified) response returned by
        `post_create_data_attribute_binding` will be passed to
        `post_create_data_attribute_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_data_taxonomy(
        self,
        request: gcd_data_taxonomy.CreateDataTaxonomyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_data_taxonomy.CreateDataTaxonomyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_data_taxonomy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_create_data_taxonomy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_data_taxonomy

        DEPRECATED. Please use the `post_create_data_taxonomy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_create_data_taxonomy` interceptor runs
        before the `post_create_data_taxonomy_with_metadata` interceptor.
        """
        return response

    def post_create_data_taxonomy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_taxonomy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_create_data_taxonomy_with_metadata`
        interceptor in new development instead of the `post_create_data_taxonomy` interceptor.
        When both interceptors are used, this `post_create_data_taxonomy_with_metadata` interceptor runs after the
        `post_create_data_taxonomy` interceptor. The (possibly modified) response returned by
        `post_create_data_taxonomy` will be passed to
        `post_create_data_taxonomy_with_metadata`.
        """
        return response, metadata

    def pre_delete_data_attribute(
        self,
        request: data_taxonomy.DeleteDataAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.DeleteDataAttributeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_data_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_delete_data_attribute(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_data_attribute

        DEPRECATED. Please use the `post_delete_data_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_delete_data_attribute` interceptor runs
        before the `post_delete_data_attribute_with_metadata` interceptor.
        """
        return response

    def post_delete_data_attribute_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_data_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_delete_data_attribute_with_metadata`
        interceptor in new development instead of the `post_delete_data_attribute` interceptor.
        When both interceptors are used, this `post_delete_data_attribute_with_metadata` interceptor runs after the
        `post_delete_data_attribute` interceptor. The (possibly modified) response returned by
        `post_delete_data_attribute` will be passed to
        `post_delete_data_attribute_with_metadata`.
        """
        return response, metadata

    def pre_delete_data_attribute_binding(
        self,
        request: data_taxonomy.DeleteDataAttributeBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.DeleteDataAttributeBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_data_attribute_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_delete_data_attribute_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_data_attribute_binding

        DEPRECATED. Please use the `post_delete_data_attribute_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_delete_data_attribute_binding` interceptor runs
        before the `post_delete_data_attribute_binding_with_metadata` interceptor.
        """
        return response

    def post_delete_data_attribute_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_data_attribute_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_delete_data_attribute_binding_with_metadata`
        interceptor in new development instead of the `post_delete_data_attribute_binding` interceptor.
        When both interceptors are used, this `post_delete_data_attribute_binding_with_metadata` interceptor runs after the
        `post_delete_data_attribute_binding` interceptor. The (possibly modified) response returned by
        `post_delete_data_attribute_binding` will be passed to
        `post_delete_data_attribute_binding_with_metadata`.
        """
        return response, metadata

    def pre_delete_data_taxonomy(
        self,
        request: data_taxonomy.DeleteDataTaxonomyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.DeleteDataTaxonomyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_data_taxonomy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_delete_data_taxonomy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_data_taxonomy

        DEPRECATED. Please use the `post_delete_data_taxonomy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_delete_data_taxonomy` interceptor runs
        before the `post_delete_data_taxonomy_with_metadata` interceptor.
        """
        return response

    def post_delete_data_taxonomy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_data_taxonomy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_delete_data_taxonomy_with_metadata`
        interceptor in new development instead of the `post_delete_data_taxonomy` interceptor.
        When both interceptors are used, this `post_delete_data_taxonomy_with_metadata` interceptor runs after the
        `post_delete_data_taxonomy` interceptor. The (possibly modified) response returned by
        `post_delete_data_taxonomy` will be passed to
        `post_delete_data_taxonomy_with_metadata`.
        """
        return response, metadata

    def pre_get_data_attribute(
        self,
        request: data_taxonomy.GetDataAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.GetDataAttributeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_get_data_attribute(
        self, response: data_taxonomy.DataAttribute
    ) -> data_taxonomy.DataAttribute:
        """Post-rpc interceptor for get_data_attribute

        DEPRECATED. Please use the `post_get_data_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_get_data_attribute` interceptor runs
        before the `post_get_data_attribute_with_metadata` interceptor.
        """
        return response

    def post_get_data_attribute_with_metadata(
        self,
        response: data_taxonomy.DataAttribute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_taxonomy.DataAttribute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_get_data_attribute_with_metadata`
        interceptor in new development instead of the `post_get_data_attribute` interceptor.
        When both interceptors are used, this `post_get_data_attribute_with_metadata` interceptor runs after the
        `post_get_data_attribute` interceptor. The (possibly modified) response returned by
        `post_get_data_attribute` will be passed to
        `post_get_data_attribute_with_metadata`.
        """
        return response, metadata

    def pre_get_data_attribute_binding(
        self,
        request: data_taxonomy.GetDataAttributeBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.GetDataAttributeBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_attribute_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_get_data_attribute_binding(
        self, response: data_taxonomy.DataAttributeBinding
    ) -> data_taxonomy.DataAttributeBinding:
        """Post-rpc interceptor for get_data_attribute_binding

        DEPRECATED. Please use the `post_get_data_attribute_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_get_data_attribute_binding` interceptor runs
        before the `post_get_data_attribute_binding_with_metadata` interceptor.
        """
        return response

    def post_get_data_attribute_binding_with_metadata(
        self,
        response: data_taxonomy.DataAttributeBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.DataAttributeBinding, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_data_attribute_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_get_data_attribute_binding_with_metadata`
        interceptor in new development instead of the `post_get_data_attribute_binding` interceptor.
        When both interceptors are used, this `post_get_data_attribute_binding_with_metadata` interceptor runs after the
        `post_get_data_attribute_binding` interceptor. The (possibly modified) response returned by
        `post_get_data_attribute_binding` will be passed to
        `post_get_data_attribute_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_data_taxonomy(
        self,
        request: data_taxonomy.GetDataTaxonomyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.GetDataTaxonomyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_taxonomy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_get_data_taxonomy(
        self, response: data_taxonomy.DataTaxonomy
    ) -> data_taxonomy.DataTaxonomy:
        """Post-rpc interceptor for get_data_taxonomy

        DEPRECATED. Please use the `post_get_data_taxonomy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_get_data_taxonomy` interceptor runs
        before the `post_get_data_taxonomy_with_metadata` interceptor.
        """
        return response

    def post_get_data_taxonomy_with_metadata(
        self,
        response: data_taxonomy.DataTaxonomy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_taxonomy.DataTaxonomy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_taxonomy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_get_data_taxonomy_with_metadata`
        interceptor in new development instead of the `post_get_data_taxonomy` interceptor.
        When both interceptors are used, this `post_get_data_taxonomy_with_metadata` interceptor runs after the
        `post_get_data_taxonomy` interceptor. The (possibly modified) response returned by
        `post_get_data_taxonomy` will be passed to
        `post_get_data_taxonomy_with_metadata`.
        """
        return response, metadata

    def pre_list_data_attribute_bindings(
        self,
        request: data_taxonomy.ListDataAttributeBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.ListDataAttributeBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_data_attribute_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_list_data_attribute_bindings(
        self, response: data_taxonomy.ListDataAttributeBindingsResponse
    ) -> data_taxonomy.ListDataAttributeBindingsResponse:
        """Post-rpc interceptor for list_data_attribute_bindings

        DEPRECATED. Please use the `post_list_data_attribute_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_list_data_attribute_bindings` interceptor runs
        before the `post_list_data_attribute_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_data_attribute_bindings_with_metadata(
        self,
        response: data_taxonomy.ListDataAttributeBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.ListDataAttributeBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_data_attribute_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_list_data_attribute_bindings_with_metadata`
        interceptor in new development instead of the `post_list_data_attribute_bindings` interceptor.
        When both interceptors are used, this `post_list_data_attribute_bindings_with_metadata` interceptor runs after the
        `post_list_data_attribute_bindings` interceptor. The (possibly modified) response returned by
        `post_list_data_attribute_bindings` will be passed to
        `post_list_data_attribute_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_data_attributes(
        self,
        request: data_taxonomy.ListDataAttributesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.ListDataAttributesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_attributes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_list_data_attributes(
        self, response: data_taxonomy.ListDataAttributesResponse
    ) -> data_taxonomy.ListDataAttributesResponse:
        """Post-rpc interceptor for list_data_attributes

        DEPRECATED. Please use the `post_list_data_attributes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_list_data_attributes` interceptor runs
        before the `post_list_data_attributes_with_metadata` interceptor.
        """
        return response

    def post_list_data_attributes_with_metadata(
        self,
        response: data_taxonomy.ListDataAttributesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.ListDataAttributesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_data_attributes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_list_data_attributes_with_metadata`
        interceptor in new development instead of the `post_list_data_attributes` interceptor.
        When both interceptors are used, this `post_list_data_attributes_with_metadata` interceptor runs after the
        `post_list_data_attributes` interceptor. The (possibly modified) response returned by
        `post_list_data_attributes` will be passed to
        `post_list_data_attributes_with_metadata`.
        """
        return response, metadata

    def pre_list_data_taxonomies(
        self,
        request: data_taxonomy.ListDataTaxonomiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.ListDataTaxonomiesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_taxonomies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_list_data_taxonomies(
        self, response: data_taxonomy.ListDataTaxonomiesResponse
    ) -> data_taxonomy.ListDataTaxonomiesResponse:
        """Post-rpc interceptor for list_data_taxonomies

        DEPRECATED. Please use the `post_list_data_taxonomies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_list_data_taxonomies` interceptor runs
        before the `post_list_data_taxonomies_with_metadata` interceptor.
        """
        return response

    def post_list_data_taxonomies_with_metadata(
        self,
        response: data_taxonomy.ListDataTaxonomiesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.ListDataTaxonomiesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_data_taxonomies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_list_data_taxonomies_with_metadata`
        interceptor in new development instead of the `post_list_data_taxonomies` interceptor.
        When both interceptors are used, this `post_list_data_taxonomies_with_metadata` interceptor runs after the
        `post_list_data_taxonomies` interceptor. The (possibly modified) response returned by
        `post_list_data_taxonomies` will be passed to
        `post_list_data_taxonomies_with_metadata`.
        """
        return response, metadata

    def pre_update_data_attribute(
        self,
        request: data_taxonomy.UpdateDataAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.UpdateDataAttributeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_update_data_attribute(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_data_attribute

        DEPRECATED. Please use the `post_update_data_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_update_data_attribute` interceptor runs
        before the `post_update_data_attribute_with_metadata` interceptor.
        """
        return response

    def post_update_data_attribute_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_update_data_attribute_with_metadata`
        interceptor in new development instead of the `post_update_data_attribute` interceptor.
        When both interceptors are used, this `post_update_data_attribute_with_metadata` interceptor runs after the
        `post_update_data_attribute` interceptor. The (possibly modified) response returned by
        `post_update_data_attribute` will be passed to
        `post_update_data_attribute_with_metadata`.
        """
        return response, metadata

    def pre_update_data_attribute_binding(
        self,
        request: data_taxonomy.UpdateDataAttributeBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_taxonomy.UpdateDataAttributeBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_attribute_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_update_data_attribute_binding(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_data_attribute_binding

        DEPRECATED. Please use the `post_update_data_attribute_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_update_data_attribute_binding` interceptor runs
        before the `post_update_data_attribute_binding_with_metadata` interceptor.
        """
        return response

    def post_update_data_attribute_binding_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_attribute_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_update_data_attribute_binding_with_metadata`
        interceptor in new development instead of the `post_update_data_attribute_binding` interceptor.
        When both interceptors are used, this `post_update_data_attribute_binding_with_metadata` interceptor runs after the
        `post_update_data_attribute_binding` interceptor. The (possibly modified) response returned by
        `post_update_data_attribute_binding` will be passed to
        `post_update_data_attribute_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_data_taxonomy(
        self,
        request: gcd_data_taxonomy.UpdateDataTaxonomyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_data_taxonomy.UpdateDataTaxonomyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_taxonomy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_update_data_taxonomy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_data_taxonomy

        DEPRECATED. Please use the `post_update_data_taxonomy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code. This `post_update_data_taxonomy` interceptor runs
        before the `post_update_data_taxonomy_with_metadata` interceptor.
        """
        return response

    def post_update_data_taxonomy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_taxonomy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTaxonomyService server but before it is returned to user code.

        We recommend only using this `post_update_data_taxonomy_with_metadata`
        interceptor in new development instead of the `post_update_data_taxonomy` interceptor.
        When both interceptors are used, this `post_update_data_taxonomy_with_metadata` interceptor runs after the
        `post_update_data_taxonomy` interceptor. The (possibly modified) response returned by
        `post_update_data_taxonomy` will be passed to
        `post_update_data_taxonomy_with_metadata`.
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
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
        before they are sent to the DataTaxonomyService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DataTaxonomyService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DataTaxonomyServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataTaxonomyServiceRestInterceptor


class DataTaxonomyServiceRestTransport(_BaseDataTaxonomyServiceRestTransport):
    """REST backend synchronous transport for DataTaxonomyService.

    DataTaxonomyService enables attribute-based governance. The
    resources currently offered include DataTaxonomy and
    DataAttribute.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dataplex.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataTaxonomyServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dataplex.googleapis.com').
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
            interceptor (Optional[DataTaxonomyServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataTaxonomyServiceRestInterceptor()
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
                    {
                        "method": "post",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*}/operations",
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

    class _CreateDataAttribute(
        _BaseDataTaxonomyServiceRestTransport._BaseCreateDataAttribute,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.CreateDataAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.CreateDataAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create data attribute method over HTTP.

            Args:
                request (~.data_taxonomy.CreateDataAttributeRequest):
                    The request object. Create DataAttribute request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseCreateDataAttribute._get_http_options()
            request, metadata = self._interceptor.pre_create_data_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseCreateDataAttribute,
                    "_BaseCreateDataAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.CreateDataAttribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CreateDataAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._CreateDataAttribute._get_response(
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

            resp = self._interceptor.post_create_data_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_attribute_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.create_data_attribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CreateDataAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataAttributeBinding(
        _BaseDataTaxonomyServiceRestTransport._BaseCreateDataAttributeBinding,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.CreateDataAttributeBinding")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.CreateDataAttributeBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create data attribute
            binding method over HTTP.

                Args:
                    request (~.data_taxonomy.CreateDataAttributeBindingRequest):
                        The request object. Create DataAttributeBinding request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseCreateDataAttributeBinding._get_http_options()
            request, metadata = self._interceptor.pre_create_data_attribute_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseCreateDataAttributeBinding,
                    "_BaseCreateDataAttributeBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.CreateDataAttributeBinding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CreateDataAttributeBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._CreateDataAttributeBinding._get_response(
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

            resp = self._interceptor.post_create_data_attribute_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_data_attribute_binding_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.create_data_attribute_binding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CreateDataAttributeBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataTaxonomy(
        _BaseDataTaxonomyServiceRestTransport._BaseCreateDataTaxonomy,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.CreateDataTaxonomy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcd_data_taxonomy.CreateDataTaxonomyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create data taxonomy method over HTTP.

            Args:
                request (~.gcd_data_taxonomy.CreateDataTaxonomyRequest):
                    The request object. Create DataTaxonomy request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseCreateDataTaxonomy._get_http_options()
            request, metadata = self._interceptor.pre_create_data_taxonomy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseCreateDataTaxonomy,
                    "_BaseCreateDataTaxonomy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.CreateDataTaxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CreateDataTaxonomy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._CreateDataTaxonomy._get_response(
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

            resp = self._interceptor.post_create_data_taxonomy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_taxonomy_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.create_data_taxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CreateDataTaxonomy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataAttribute(
        _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataAttribute,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.DeleteDataAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.DeleteDataAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete data attribute method over HTTP.

            Args:
                request (~.data_taxonomy.DeleteDataAttributeRequest):
                    The request object. Delete DataAttribute request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataAttribute._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataAttribute,
                    "_BaseDeleteDataAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.DeleteDataAttribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteDataAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._DeleteDataAttribute._get_response(
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

            resp = self._interceptor.post_delete_data_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_data_attribute_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.delete_data_attribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteDataAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataAttributeBinding(
        _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataAttributeBinding,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.DeleteDataAttributeBinding")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.DeleteDataAttributeBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete data attribute
            binding method over HTTP.

                Args:
                    request (~.data_taxonomy.DeleteDataAttributeBindingRequest):
                        The request object. Delete DataAttributeBinding request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataAttributeBinding._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_attribute_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataAttributeBinding,
                    "_BaseDeleteDataAttributeBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.DeleteDataAttributeBinding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteDataAttributeBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._DeleteDataAttributeBinding._get_response(
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

            resp = self._interceptor.post_delete_data_attribute_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_data_attribute_binding_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.delete_data_attribute_binding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteDataAttributeBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataTaxonomy(
        _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataTaxonomy,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.DeleteDataTaxonomy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.DeleteDataTaxonomyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete data taxonomy method over HTTP.

            Args:
                request (~.data_taxonomy.DeleteDataTaxonomyRequest):
                    The request object. Delete DataTaxonomy request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataTaxonomy._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_taxonomy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseDeleteDataTaxonomy,
                    "_BaseDeleteDataTaxonomy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.DeleteDataTaxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteDataTaxonomy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._DeleteDataTaxonomy._get_response(
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

            resp = self._interceptor.post_delete_data_taxonomy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_data_taxonomy_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.delete_data_taxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteDataTaxonomy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataAttribute(
        _BaseDataTaxonomyServiceRestTransport._BaseGetDataAttribute,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.GetDataAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.GetDataAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_taxonomy.DataAttribute:
            r"""Call the get data attribute method over HTTP.

            Args:
                request (~.data_taxonomy.GetDataAttributeRequest):
                    The request object. Get DataAttribute request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_taxonomy.DataAttribute:
                    Denotes one dataAttribute in a dataTaxonomy, for
                example, PII. DataAttribute resources can be defined in
                a hierarchy. A single dataAttribute resource can contain
                specs of multiple types

                ::

                   PII
                     - ResourceAccessSpec :
                                   - readers :foo@bar.com
                     - DataAccessSpec :
                                   - readers :bar@foo.com

            """

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseGetDataAttribute._get_http_options()
            request, metadata = self._interceptor.pre_get_data_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseGetDataAttribute,
                    "_BaseGetDataAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.GetDataAttribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetDataAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._GetDataAttribute._get_response(
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
            resp = data_taxonomy.DataAttribute()
            pb_resp = data_taxonomy.DataAttribute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_taxonomy.DataAttribute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.get_data_attribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetDataAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataAttributeBinding(
        _BaseDataTaxonomyServiceRestTransport._BaseGetDataAttributeBinding,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.GetDataAttributeBinding")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.GetDataAttributeBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_taxonomy.DataAttributeBinding:
            r"""Call the get data attribute
            binding method over HTTP.

                Args:
                    request (~.data_taxonomy.GetDataAttributeBindingRequest):
                        The request object. Get DataAttributeBinding request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.data_taxonomy.DataAttributeBinding:
                        DataAttributeBinding represents
                    binding of attributes to resources. Eg:
                    Bind 'CustomerInfo' entity with 'PII'
                    attribute.

            """

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseGetDataAttributeBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_data_attribute_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseGetDataAttributeBinding,
                    "_BaseGetDataAttributeBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.GetDataAttributeBinding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetDataAttributeBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._GetDataAttributeBinding._get_response(
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
            resp = data_taxonomy.DataAttributeBinding()
            pb_resp = data_taxonomy.DataAttributeBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_attribute_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_attribute_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_taxonomy.DataAttributeBinding.to_json(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.get_data_attribute_binding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetDataAttributeBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataTaxonomy(
        _BaseDataTaxonomyServiceRestTransport._BaseGetDataTaxonomy,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.GetDataTaxonomy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.GetDataTaxonomyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_taxonomy.DataTaxonomy:
            r"""Call the get data taxonomy method over HTTP.

            Args:
                request (~.data_taxonomy.GetDataTaxonomyRequest):
                    The request object. Get DataTaxonomy request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_taxonomy.DataTaxonomy:
                    DataTaxonomy represents a set of
                hierarchical DataAttributes resources,
                grouped with a common theme Eg:
                'SensitiveDataTaxonomy' can have
                attributes to manage PII data. It is
                defined at project level.

            """

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseGetDataTaxonomy._get_http_options()
            request, metadata = self._interceptor.pre_get_data_taxonomy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseGetDataTaxonomy,
                    "_BaseGetDataTaxonomy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.GetDataTaxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetDataTaxonomy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._GetDataTaxonomy._get_response(
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
            resp = data_taxonomy.DataTaxonomy()
            pb_resp = data_taxonomy.DataTaxonomy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_taxonomy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_taxonomy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_taxonomy.DataTaxonomy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.get_data_taxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetDataTaxonomy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataAttributeBindings(
        _BaseDataTaxonomyServiceRestTransport._BaseListDataAttributeBindings,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.ListDataAttributeBindings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.ListDataAttributeBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_taxonomy.ListDataAttributeBindingsResponse:
            r"""Call the list data attribute
            bindings method over HTTP.

                Args:
                    request (~.data_taxonomy.ListDataAttributeBindingsRequest):
                        The request object. List DataAttributeBindings request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.data_taxonomy.ListDataAttributeBindingsResponse:
                        List DataAttributeBindings response.
            """

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseListDataAttributeBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_data_attribute_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseListDataAttributeBindings,
                    "_BaseListDataAttributeBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.ListDataAttributeBindings",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListDataAttributeBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._ListDataAttributeBindings._get_response(
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
            resp = data_taxonomy.ListDataAttributeBindingsResponse()
            pb_resp = data_taxonomy.ListDataAttributeBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_attribute_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_attribute_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_taxonomy.ListDataAttributeBindingsResponse.to_json(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.list_data_attribute_bindings",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListDataAttributeBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataAttributes(
        _BaseDataTaxonomyServiceRestTransport._BaseListDataAttributes,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.ListDataAttributes")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.ListDataAttributesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_taxonomy.ListDataAttributesResponse:
            r"""Call the list data attributes method over HTTP.

            Args:
                request (~.data_taxonomy.ListDataAttributesRequest):
                    The request object. List DataAttributes request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_taxonomy.ListDataAttributesResponse:
                    List DataAttributes response.
            """

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseListDataAttributes._get_http_options()
            request, metadata = self._interceptor.pre_list_data_attributes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseListDataAttributes,
                    "_BaseListDataAttributes__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.ListDataAttributes",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListDataAttributes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._ListDataAttributes._get_response(
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
            resp = data_taxonomy.ListDataAttributesResponse()
            pb_resp = data_taxonomy.ListDataAttributesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_attributes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_attributes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_taxonomy.ListDataAttributesResponse.to_json(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.list_data_attributes",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListDataAttributes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataTaxonomies(
        _BaseDataTaxonomyServiceRestTransport._BaseListDataTaxonomies,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.ListDataTaxonomies")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.ListDataTaxonomiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_taxonomy.ListDataTaxonomiesResponse:
            r"""Call the list data taxonomies method over HTTP.

            Args:
                request (~.data_taxonomy.ListDataTaxonomiesRequest):
                    The request object. List DataTaxonomies request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_taxonomy.ListDataTaxonomiesResponse:
                    List DataTaxonomies response.
            """

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseListDataTaxonomies._get_http_options()
            request, metadata = self._interceptor.pre_list_data_taxonomies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseListDataTaxonomies,
                    "_BaseListDataTaxonomies__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.ListDataTaxonomies",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListDataTaxonomies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._ListDataTaxonomies._get_response(
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
            resp = data_taxonomy.ListDataTaxonomiesResponse()
            pb_resp = data_taxonomy.ListDataTaxonomiesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_taxonomies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_taxonomies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_taxonomy.ListDataTaxonomiesResponse.to_json(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.list_data_taxonomies",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListDataTaxonomies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataAttribute(
        _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataAttribute,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.UpdateDataAttribute")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.UpdateDataAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update data attribute method over HTTP.

            Args:
                request (~.data_taxonomy.UpdateDataAttributeRequest):
                    The request object. Update DataAttribute request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataAttribute._get_http_options()
            request, metadata = self._interceptor.pre_update_data_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataAttribute,
                    "_BaseUpdateDataAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.UpdateDataAttribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "UpdateDataAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._UpdateDataAttribute._get_response(
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

            resp = self._interceptor.post_update_data_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_attribute_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.update_data_attribute",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "UpdateDataAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataAttributeBinding(
        _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataAttributeBinding,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.UpdateDataAttributeBinding")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: data_taxonomy.UpdateDataAttributeBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update data attribute
            binding method over HTTP.

                Args:
                    request (~.data_taxonomy.UpdateDataAttributeBindingRequest):
                        The request object. Update DataAttributeBinding request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataAttributeBinding._get_http_options()
            request, metadata = self._interceptor.pre_update_data_attribute_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataAttributeBinding,
                    "_BaseUpdateDataAttributeBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.UpdateDataAttributeBinding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "UpdateDataAttributeBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._UpdateDataAttributeBinding._get_response(
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

            resp = self._interceptor.post_update_data_attribute_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_data_attribute_binding_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.update_data_attribute_binding",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "UpdateDataAttributeBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataTaxonomy(
        _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataTaxonomy,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.UpdateDataTaxonomy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcd_data_taxonomy.UpdateDataTaxonomyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update data taxonomy method over HTTP.

            Args:
                request (~.gcd_data_taxonomy.UpdateDataTaxonomyRequest):
                    The request object. Update DataTaxonomy request.
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataTaxonomy._get_http_options()
            request, metadata = self._interceptor.pre_update_data_taxonomy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseUpdateDataTaxonomy,
                    "_BaseUpdateDataTaxonomy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.UpdateDataTaxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "UpdateDataTaxonomy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._UpdateDataTaxonomy._get_response(
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

            resp = self._interceptor.post_update_data_taxonomy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_taxonomy_with_metadata(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceClient.update_data_taxonomy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "UpdateDataTaxonomy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_data_attribute(
        self,
    ) -> Callable[[data_taxonomy.CreateDataAttributeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_data_attribute_binding(
        self,
    ) -> Callable[
        [data_taxonomy.CreateDataAttributeBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataAttributeBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_data_taxonomy(
        self,
    ) -> Callable[
        [gcd_data_taxonomy.CreateDataTaxonomyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataTaxonomy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_attribute(
        self,
    ) -> Callable[[data_taxonomy.DeleteDataAttributeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_attribute_binding(
        self,
    ) -> Callable[
        [data_taxonomy.DeleteDataAttributeBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataAttributeBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_data_taxonomy(
        self,
    ) -> Callable[[data_taxonomy.DeleteDataTaxonomyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataTaxonomy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_attribute(
        self,
    ) -> Callable[[data_taxonomy.GetDataAttributeRequest], data_taxonomy.DataAttribute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_attribute_binding(
        self,
    ) -> Callable[
        [data_taxonomy.GetDataAttributeBindingRequest],
        data_taxonomy.DataAttributeBinding,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataAttributeBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_data_taxonomy(
        self,
    ) -> Callable[[data_taxonomy.GetDataTaxonomyRequest], data_taxonomy.DataTaxonomy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataTaxonomy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_attribute_bindings(
        self,
    ) -> Callable[
        [data_taxonomy.ListDataAttributeBindingsRequest],
        data_taxonomy.ListDataAttributeBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataAttributeBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_data_attributes(
        self,
    ) -> Callable[
        [data_taxonomy.ListDataAttributesRequest],
        data_taxonomy.ListDataAttributesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataAttributes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_taxonomies(
        self,
    ) -> Callable[
        [data_taxonomy.ListDataTaxonomiesRequest],
        data_taxonomy.ListDataTaxonomiesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataTaxonomies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_attribute(
        self,
    ) -> Callable[[data_taxonomy.UpdateDataAttributeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_attribute_binding(
        self,
    ) -> Callable[
        [data_taxonomy.UpdateDataAttributeBindingRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataAttributeBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_data_taxonomy(
        self,
    ) -> Callable[
        [gcd_data_taxonomy.UpdateDataTaxonomyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataTaxonomy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDataTaxonomyServiceRestTransport._BaseGetLocation,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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
        _BaseDataTaxonomyServiceRestTransport._BaseListLocations,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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
        _BaseDataTaxonomyServiceRestTransport._BaseGetIamPolicy,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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
        _BaseDataTaxonomyServiceRestTransport._BaseSetIamPolicy,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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
        _BaseDataTaxonomyServiceRestTransport._BaseTestIamPermissions,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTaxonomyServiceRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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
        _BaseDataTaxonomyServiceRestTransport._BaseCancelOperation,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._CancelOperation._get_response(
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
        _BaseDataTaxonomyServiceRestTransport._BaseDeleteOperation,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._DeleteOperation._get_response(
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
        _BaseDataTaxonomyServiceRestTransport._BaseGetOperation,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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
        _BaseDataTaxonomyServiceRestTransport._BaseListOperations,
        DataTaxonomyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTaxonomyServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseDataTaxonomyServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTaxonomyServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dataplex_v1.DataTaxonomyServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTaxonomyServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dataplex_v1.DataTaxonomyServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.DataTaxonomyService",
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


__all__ = ("DataTaxonomyServiceRestTransport",)
