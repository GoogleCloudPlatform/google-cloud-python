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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
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

from google.cloud.managedkafka_schemaregistry_v1._compat import transcode_request
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry,
    schema_registry_resources,
)
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry as gcms_schema_registry,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseManagedSchemaRegistryRestTransport

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


class ManagedSchemaRegistryRestInterceptor:
    """Interceptor for ManagedSchemaRegistry.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ManagedSchemaRegistryRestTransport.

    .. code-block:: python
        class MyCustomManagedSchemaRegistryInterceptor(ManagedSchemaRegistryRestInterceptor):
            def pre_check_compatibility(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_check_compatibility(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_schema_registry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_schema_registry(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_schema_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_schema_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_schema_mode(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_schema_mode(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_schema_registry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_subject(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_subject(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_context(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_context(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_raw_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_raw_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_raw_schema_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_raw_schema_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_schema_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_schema_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_schema_mode(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_schema_mode(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_schema_registry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_schema_registry(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_contexts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_contexts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_referenced_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_referenced_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_schema_registries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_schema_registries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_schema_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_schema_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_schema_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_schema_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_subjects(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subjects(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_subjects_by_schema_id(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subjects_by_schema_id(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_schema_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_schema_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_schema_mode(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_schema_mode(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ManagedSchemaRegistryRestTransport(interceptor=MyCustomManagedSchemaRegistryInterceptor())
        client = ManagedSchemaRegistryClient(transport=transport)


    """

    def pre_check_compatibility(
        self,
        request: schema_registry.CheckCompatibilityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.CheckCompatibilityRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for check_compatibility

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_check_compatibility(
        self, response: schema_registry.CheckCompatibilityResponse
    ) -> schema_registry.CheckCompatibilityResponse:
        """Post-rpc interceptor for check_compatibility

        DEPRECATED. Please use the `post_check_compatibility_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_check_compatibility` interceptor runs
        before the `post_check_compatibility_with_metadata` interceptor.
        """
        return response

    def post_check_compatibility_with_metadata(
        self,
        response: schema_registry.CheckCompatibilityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.CheckCompatibilityResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for check_compatibility

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_check_compatibility_with_metadata`
        interceptor in new development instead of the `post_check_compatibility` interceptor.
        When both interceptors are used, this `post_check_compatibility_with_metadata` interceptor runs after the
        `post_check_compatibility` interceptor. The (possibly modified) response returned by
        `post_check_compatibility` will be passed to
        `post_check_compatibility_with_metadata`.
        """
        return response, metadata

    def pre_create_schema_registry(
        self,
        request: gcms_schema_registry.CreateSchemaRegistryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcms_schema_registry.CreateSchemaRegistryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_schema_registry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_create_schema_registry(
        self, response: schema_registry_resources.SchemaRegistry
    ) -> schema_registry_resources.SchemaRegistry:
        """Post-rpc interceptor for create_schema_registry

        DEPRECATED. Please use the `post_create_schema_registry_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_create_schema_registry` interceptor runs
        before the `post_create_schema_registry_with_metadata` interceptor.
        """
        return response

    def post_create_schema_registry_with_metadata(
        self,
        response: schema_registry_resources.SchemaRegistry,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaRegistry,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_schema_registry

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_create_schema_registry_with_metadata`
        interceptor in new development instead of the `post_create_schema_registry` interceptor.
        When both interceptors are used, this `post_create_schema_registry_with_metadata` interceptor runs after the
        `post_create_schema_registry` interceptor. The (possibly modified) response returned by
        `post_create_schema_registry` will be passed to
        `post_create_schema_registry_with_metadata`.
        """
        return response, metadata

    def pre_create_version(
        self,
        request: schema_registry.CreateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.CreateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_create_version(
        self, response: schema_registry.CreateVersionResponse
    ) -> schema_registry.CreateVersionResponse:
        """Post-rpc interceptor for create_version

        DEPRECATED. Please use the `post_create_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_create_version` interceptor runs
        before the `post_create_version_with_metadata` interceptor.
        """
        return response

    def post_create_version_with_metadata(
        self,
        response: schema_registry.CreateVersionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.CreateVersionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_create_version_with_metadata`
        interceptor in new development instead of the `post_create_version` interceptor.
        When both interceptors are used, this `post_create_version_with_metadata` interceptor runs after the
        `post_create_version` interceptor. The (possibly modified) response returned by
        `post_create_version` will be passed to
        `post_create_version_with_metadata`.
        """
        return response, metadata

    def pre_delete_schema_config(
        self,
        request: schema_registry.DeleteSchemaConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.DeleteSchemaConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_schema_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_delete_schema_config(
        self, response: schema_registry_resources.SchemaConfig
    ) -> schema_registry_resources.SchemaConfig:
        """Post-rpc interceptor for delete_schema_config

        DEPRECATED. Please use the `post_delete_schema_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_delete_schema_config` interceptor runs
        before the `post_delete_schema_config_with_metadata` interceptor.
        """
        return response

    def post_delete_schema_config_with_metadata(
        self,
        response: schema_registry_resources.SchemaConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for delete_schema_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_schema_config_with_metadata`
        interceptor in new development instead of the `post_delete_schema_config` interceptor.
        When both interceptors are used, this `post_delete_schema_config_with_metadata` interceptor runs after the
        `post_delete_schema_config` interceptor. The (possibly modified) response returned by
        `post_delete_schema_config` will be passed to
        `post_delete_schema_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_schema_mode(
        self,
        request: schema_registry.DeleteSchemaModeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.DeleteSchemaModeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_schema_mode

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_delete_schema_mode(
        self, response: schema_registry_resources.SchemaMode
    ) -> schema_registry_resources.SchemaMode:
        """Post-rpc interceptor for delete_schema_mode

        DEPRECATED. Please use the `post_delete_schema_mode_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_delete_schema_mode` interceptor runs
        before the `post_delete_schema_mode_with_metadata` interceptor.
        """
        return response

    def post_delete_schema_mode_with_metadata(
        self,
        response: schema_registry_resources.SchemaMode,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaMode, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for delete_schema_mode

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_schema_mode_with_metadata`
        interceptor in new development instead of the `post_delete_schema_mode` interceptor.
        When both interceptors are used, this `post_delete_schema_mode_with_metadata` interceptor runs after the
        `post_delete_schema_mode` interceptor. The (possibly modified) response returned by
        `post_delete_schema_mode` will be passed to
        `post_delete_schema_mode_with_metadata`.
        """
        return response, metadata

    def pre_delete_schema_registry(
        self,
        request: schema_registry.DeleteSchemaRegistryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.DeleteSchemaRegistryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_schema_registry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def pre_delete_subject(
        self,
        request: schema_registry.DeleteSubjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.DeleteSubjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_subject

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_delete_subject(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for delete_subject

        DEPRECATED. Please use the `post_delete_subject_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_delete_subject` interceptor runs
        before the `post_delete_subject_with_metadata` interceptor.
        """
        return response

    def post_delete_subject_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_subject

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_subject_with_metadata`
        interceptor in new development instead of the `post_delete_subject` interceptor.
        When both interceptors are used, this `post_delete_subject_with_metadata` interceptor runs after the
        `post_delete_subject` interceptor. The (possibly modified) response returned by
        `post_delete_subject` will be passed to
        `post_delete_subject_with_metadata`.
        """
        return response, metadata

    def pre_delete_version(
        self,
        request: schema_registry.DeleteVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.DeleteVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_delete_version(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for delete_version

        DEPRECATED. Please use the `post_delete_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_delete_version` interceptor runs
        before the `post_delete_version_with_metadata` interceptor.
        """
        return response

    def post_delete_version_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_version_with_metadata`
        interceptor in new development instead of the `post_delete_version` interceptor.
        When both interceptors are used, this `post_delete_version_with_metadata` interceptor runs after the
        `post_delete_version` interceptor. The (possibly modified) response returned by
        `post_delete_version` will be passed to
        `post_delete_version_with_metadata`.
        """
        return response, metadata

    def pre_get_context(
        self,
        request: schema_registry.GetContextRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetContextRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_context

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_context(
        self, response: schema_registry_resources.Context
    ) -> schema_registry_resources.Context:
        """Post-rpc interceptor for get_context

        DEPRECATED. Please use the `post_get_context_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_context` interceptor runs
        before the `post_get_context_with_metadata` interceptor.
        """
        return response

    def post_get_context_with_metadata(
        self,
        response: schema_registry_resources.Context,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.Context, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_context

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_context_with_metadata`
        interceptor in new development instead of the `post_get_context` interceptor.
        When both interceptors are used, this `post_get_context_with_metadata` interceptor runs after the
        `post_get_context` interceptor. The (possibly modified) response returned by
        `post_get_context` will be passed to
        `post_get_context_with_metadata`.
        """
        return response, metadata

    def pre_get_raw_schema(
        self,
        request: schema_registry.GetSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_raw_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_raw_schema(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for get_raw_schema

        DEPRECATED. Please use the `post_get_raw_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_raw_schema` interceptor runs
        before the `post_get_raw_schema_with_metadata` interceptor.
        """
        return response

    def post_get_raw_schema_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_raw_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_raw_schema_with_metadata`
        interceptor in new development instead of the `post_get_raw_schema` interceptor.
        When both interceptors are used, this `post_get_raw_schema_with_metadata` interceptor runs after the
        `post_get_raw_schema` interceptor. The (possibly modified) response returned by
        `post_get_raw_schema` will be passed to
        `post_get_raw_schema_with_metadata`.
        """
        return response, metadata

    def pre_get_raw_schema_version(
        self,
        request: schema_registry.GetVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_raw_schema_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_raw_schema_version(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for get_raw_schema_version

        DEPRECATED. Please use the `post_get_raw_schema_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_raw_schema_version` interceptor runs
        before the `post_get_raw_schema_version_with_metadata` interceptor.
        """
        return response

    def post_get_raw_schema_version_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_raw_schema_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_raw_schema_version_with_metadata`
        interceptor in new development instead of the `post_get_raw_schema_version` interceptor.
        When both interceptors are used, this `post_get_raw_schema_version_with_metadata` interceptor runs after the
        `post_get_raw_schema_version` interceptor. The (possibly modified) response returned by
        `post_get_raw_schema_version` will be passed to
        `post_get_raw_schema_version_with_metadata`.
        """
        return response, metadata

    def pre_get_schema(
        self,
        request: schema_registry.GetSchemaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetSchemaRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_schema(
        self, response: schema_registry_resources.Schema
    ) -> schema_registry_resources.Schema:
        """Post-rpc interceptor for get_schema

        DEPRECATED. Please use the `post_get_schema_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_schema` interceptor runs
        before the `post_get_schema_with_metadata` interceptor.
        """
        return response

    def post_get_schema_with_metadata(
        self,
        response: schema_registry_resources.Schema,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.Schema, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_schema

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_schema_with_metadata`
        interceptor in new development instead of the `post_get_schema` interceptor.
        When both interceptors are used, this `post_get_schema_with_metadata` interceptor runs after the
        `post_get_schema` interceptor. The (possibly modified) response returned by
        `post_get_schema` will be passed to
        `post_get_schema_with_metadata`.
        """
        return response, metadata

    def pre_get_schema_config(
        self,
        request: schema_registry.GetSchemaConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetSchemaConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_schema_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_schema_config(
        self, response: schema_registry_resources.SchemaConfig
    ) -> schema_registry_resources.SchemaConfig:
        """Post-rpc interceptor for get_schema_config

        DEPRECATED. Please use the `post_get_schema_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_schema_config` interceptor runs
        before the `post_get_schema_config_with_metadata` interceptor.
        """
        return response

    def post_get_schema_config_with_metadata(
        self,
        response: schema_registry_resources.SchemaConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_schema_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_schema_config_with_metadata`
        interceptor in new development instead of the `post_get_schema_config` interceptor.
        When both interceptors are used, this `post_get_schema_config_with_metadata` interceptor runs after the
        `post_get_schema_config` interceptor. The (possibly modified) response returned by
        `post_get_schema_config` will be passed to
        `post_get_schema_config_with_metadata`.
        """
        return response, metadata

    def pre_get_schema_mode(
        self,
        request: schema_registry.GetSchemaModeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetSchemaModeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_schema_mode

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_schema_mode(
        self, response: schema_registry_resources.SchemaMode
    ) -> schema_registry_resources.SchemaMode:
        """Post-rpc interceptor for get_schema_mode

        DEPRECATED. Please use the `post_get_schema_mode_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_schema_mode` interceptor runs
        before the `post_get_schema_mode_with_metadata` interceptor.
        """
        return response

    def post_get_schema_mode_with_metadata(
        self,
        response: schema_registry_resources.SchemaMode,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaMode, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_schema_mode

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_schema_mode_with_metadata`
        interceptor in new development instead of the `post_get_schema_mode` interceptor.
        When both interceptors are used, this `post_get_schema_mode_with_metadata` interceptor runs after the
        `post_get_schema_mode` interceptor. The (possibly modified) response returned by
        `post_get_schema_mode` will be passed to
        `post_get_schema_mode_with_metadata`.
        """
        return response, metadata

    def pre_get_schema_registry(
        self,
        request: schema_registry.GetSchemaRegistryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetSchemaRegistryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_schema_registry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_schema_registry(
        self, response: schema_registry_resources.SchemaRegistry
    ) -> schema_registry_resources.SchemaRegistry:
        """Post-rpc interceptor for get_schema_registry

        DEPRECATED. Please use the `post_get_schema_registry_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_schema_registry` interceptor runs
        before the `post_get_schema_registry_with_metadata` interceptor.
        """
        return response

    def post_get_schema_registry_with_metadata(
        self,
        response: schema_registry_resources.SchemaRegistry,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaRegistry,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_schema_registry

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_schema_registry_with_metadata`
        interceptor in new development instead of the `post_get_schema_registry` interceptor.
        When both interceptors are used, this `post_get_schema_registry_with_metadata` interceptor runs after the
        `post_get_schema_registry` interceptor. The (possibly modified) response returned by
        `post_get_schema_registry` will be passed to
        `post_get_schema_registry_with_metadata`.
        """
        return response, metadata

    def pre_get_version(
        self,
        request: schema_registry.GetVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.GetVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_version(
        self, response: schema_registry_resources.SchemaVersion
    ) -> schema_registry_resources.SchemaVersion:
        """Post-rpc interceptor for get_version

        DEPRECATED. Please use the `post_get_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_get_version` interceptor runs
        before the `post_get_version_with_metadata` interceptor.
        """
        return response

    def post_get_version_with_metadata(
        self,
        response: schema_registry_resources.SchemaVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaVersion, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_get_version_with_metadata`
        interceptor in new development instead of the `post_get_version` interceptor.
        When both interceptors are used, this `post_get_version_with_metadata` interceptor runs after the
        `post_get_version` interceptor. The (possibly modified) response returned by
        `post_get_version` will be passed to
        `post_get_version_with_metadata`.
        """
        return response, metadata

    def pre_list_contexts(
        self,
        request: schema_registry.ListContextsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListContextsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_contexts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_contexts(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_contexts

        DEPRECATED. Please use the `post_list_contexts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_contexts` interceptor runs
        before the `post_list_contexts_with_metadata` interceptor.
        """
        return response

    def post_list_contexts_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_contexts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_contexts_with_metadata`
        interceptor in new development instead of the `post_list_contexts` interceptor.
        When both interceptors are used, this `post_list_contexts_with_metadata` interceptor runs after the
        `post_list_contexts` interceptor. The (possibly modified) response returned by
        `post_list_contexts` will be passed to
        `post_list_contexts_with_metadata`.
        """
        return response, metadata

    def pre_list_referenced_schemas(
        self,
        request: schema_registry.ListReferencedSchemasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListReferencedSchemasRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_referenced_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_referenced_schemas(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_referenced_schemas

        DEPRECATED. Please use the `post_list_referenced_schemas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_referenced_schemas` interceptor runs
        before the `post_list_referenced_schemas_with_metadata` interceptor.
        """
        return response

    def post_list_referenced_schemas_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_referenced_schemas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_referenced_schemas_with_metadata`
        interceptor in new development instead of the `post_list_referenced_schemas` interceptor.
        When both interceptors are used, this `post_list_referenced_schemas_with_metadata` interceptor runs after the
        `post_list_referenced_schemas` interceptor. The (possibly modified) response returned by
        `post_list_referenced_schemas` will be passed to
        `post_list_referenced_schemas_with_metadata`.
        """
        return response, metadata

    def pre_list_schema_registries(
        self,
        request: schema_registry.ListSchemaRegistriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListSchemaRegistriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_schema_registries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_schema_registries(
        self, response: schema_registry.ListSchemaRegistriesResponse
    ) -> schema_registry.ListSchemaRegistriesResponse:
        """Post-rpc interceptor for list_schema_registries

        DEPRECATED. Please use the `post_list_schema_registries_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_schema_registries` interceptor runs
        before the `post_list_schema_registries_with_metadata` interceptor.
        """
        return response

    def post_list_schema_registries_with_metadata(
        self,
        response: schema_registry.ListSchemaRegistriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListSchemaRegistriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_schema_registries

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_schema_registries_with_metadata`
        interceptor in new development instead of the `post_list_schema_registries` interceptor.
        When both interceptors are used, this `post_list_schema_registries_with_metadata` interceptor runs after the
        `post_list_schema_registries` interceptor. The (possibly modified) response returned by
        `post_list_schema_registries` will be passed to
        `post_list_schema_registries_with_metadata`.
        """
        return response, metadata

    def pre_list_schema_types(
        self,
        request: schema_registry.ListSchemaTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListSchemaTypesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_schema_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_schema_types(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_schema_types

        DEPRECATED. Please use the `post_list_schema_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_schema_types` interceptor runs
        before the `post_list_schema_types_with_metadata` interceptor.
        """
        return response

    def post_list_schema_types_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_schema_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_schema_types_with_metadata`
        interceptor in new development instead of the `post_list_schema_types` interceptor.
        When both interceptors are used, this `post_list_schema_types_with_metadata` interceptor runs after the
        `post_list_schema_types` interceptor. The (possibly modified) response returned by
        `post_list_schema_types` will be passed to
        `post_list_schema_types_with_metadata`.
        """
        return response, metadata

    def pre_list_schema_versions(
        self,
        request: schema_registry.ListSchemaVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListSchemaVersionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_schema_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_schema_versions(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_schema_versions

        DEPRECATED. Please use the `post_list_schema_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_schema_versions` interceptor runs
        before the `post_list_schema_versions_with_metadata` interceptor.
        """
        return response

    def post_list_schema_versions_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_schema_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_schema_versions_with_metadata`
        interceptor in new development instead of the `post_list_schema_versions` interceptor.
        When both interceptors are used, this `post_list_schema_versions_with_metadata` interceptor runs after the
        `post_list_schema_versions` interceptor. The (possibly modified) response returned by
        `post_list_schema_versions` will be passed to
        `post_list_schema_versions_with_metadata`.
        """
        return response, metadata

    def pre_list_subjects(
        self,
        request: schema_registry.ListSubjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListSubjectsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_subjects

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_subjects(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_subjects

        DEPRECATED. Please use the `post_list_subjects_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_subjects` interceptor runs
        before the `post_list_subjects_with_metadata` interceptor.
        """
        return response

    def post_list_subjects_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_subjects

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_subjects_with_metadata`
        interceptor in new development instead of the `post_list_subjects` interceptor.
        When both interceptors are used, this `post_list_subjects_with_metadata` interceptor runs after the
        `post_list_subjects` interceptor. The (possibly modified) response returned by
        `post_list_subjects` will be passed to
        `post_list_subjects_with_metadata`.
        """
        return response, metadata

    def pre_list_subjects_by_schema_id(
        self,
        request: schema_registry.ListSubjectsBySchemaIdRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListSubjectsBySchemaIdRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_subjects_by_schema_id

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_subjects_by_schema_id(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_subjects_by_schema_id

        DEPRECATED. Please use the `post_list_subjects_by_schema_id_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_subjects_by_schema_id` interceptor runs
        before the `post_list_subjects_by_schema_id_with_metadata` interceptor.
        """
        return response

    def post_list_subjects_by_schema_id_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_subjects_by_schema_id

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_subjects_by_schema_id_with_metadata`
        interceptor in new development instead of the `post_list_subjects_by_schema_id` interceptor.
        When both interceptors are used, this `post_list_subjects_by_schema_id_with_metadata` interceptor runs after the
        `post_list_subjects_by_schema_id` interceptor. The (possibly modified) response returned by
        `post_list_subjects_by_schema_id` will be passed to
        `post_list_subjects_by_schema_id_with_metadata`.
        """
        return response, metadata

    def pre_list_versions(
        self,
        request: schema_registry.ListVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.ListVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_versions(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for list_versions

        DEPRECATED. Please use the `post_list_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_list_versions` interceptor runs
        before the `post_list_versions_with_metadata` interceptor.
        """
        return response

    def post_list_versions_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_list_versions_with_metadata`
        interceptor in new development instead of the `post_list_versions` interceptor.
        When both interceptors are used, this `post_list_versions_with_metadata` interceptor runs after the
        `post_list_versions` interceptor. The (possibly modified) response returned by
        `post_list_versions` will be passed to
        `post_list_versions_with_metadata`.
        """
        return response, metadata

    def pre_lookup_version(
        self,
        request: schema_registry.LookupVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.LookupVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for lookup_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_lookup_version(
        self, response: schema_registry_resources.SchemaVersion
    ) -> schema_registry_resources.SchemaVersion:
        """Post-rpc interceptor for lookup_version

        DEPRECATED. Please use the `post_lookup_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_lookup_version` interceptor runs
        before the `post_lookup_version_with_metadata` interceptor.
        """
        return response

    def post_lookup_version_with_metadata(
        self,
        response: schema_registry_resources.SchemaVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaVersion, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for lookup_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_lookup_version_with_metadata`
        interceptor in new development instead of the `post_lookup_version` interceptor.
        When both interceptors are used, this `post_lookup_version_with_metadata` interceptor runs after the
        `post_lookup_version` interceptor. The (possibly modified) response returned by
        `post_lookup_version` will be passed to
        `post_lookup_version_with_metadata`.
        """
        return response, metadata

    def pre_update_schema_config(
        self,
        request: schema_registry.UpdateSchemaConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.UpdateSchemaConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_schema_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_update_schema_config(
        self, response: schema_registry_resources.SchemaConfig
    ) -> schema_registry_resources.SchemaConfig:
        """Post-rpc interceptor for update_schema_config

        DEPRECATED. Please use the `post_update_schema_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_update_schema_config` interceptor runs
        before the `post_update_schema_config_with_metadata` interceptor.
        """
        return response

    def post_update_schema_config_with_metadata(
        self,
        response: schema_registry_resources.SchemaConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaConfig, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_schema_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_update_schema_config_with_metadata`
        interceptor in new development instead of the `post_update_schema_config` interceptor.
        When both interceptors are used, this `post_update_schema_config_with_metadata` interceptor runs after the
        `post_update_schema_config` interceptor. The (possibly modified) response returned by
        `post_update_schema_config` will be passed to
        `post_update_schema_config_with_metadata`.
        """
        return response, metadata

    def pre_update_schema_mode(
        self,
        request: schema_registry.UpdateSchemaModeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry.UpdateSchemaModeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_schema_mode

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_update_schema_mode(
        self, response: schema_registry_resources.SchemaMode
    ) -> schema_registry_resources.SchemaMode:
        """Post-rpc interceptor for update_schema_mode

        DEPRECATED. Please use the `post_update_schema_mode_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code. This `post_update_schema_mode` interceptor runs
        before the `post_update_schema_mode_with_metadata` interceptor.
        """
        return response

    def post_update_schema_mode_with_metadata(
        self,
        response: schema_registry_resources.SchemaMode,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        schema_registry_resources.SchemaMode, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_schema_mode

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedSchemaRegistry server but before it is returned to user code.

        We recommend only using this `post_update_schema_mode_with_metadata`
        interceptor in new development instead of the `post_update_schema_mode` interceptor.
        When both interceptors are used, this `post_update_schema_mode_with_metadata` interceptor runs after the
        `post_update_schema_mode` interceptor. The (possibly modified) response returned by
        `post_update_schema_mode` will be passed to
        `post_update_schema_mode_with_metadata`.
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
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
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
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
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
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
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
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
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
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
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
        before they are sent to the ManagedSchemaRegistry server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ManagedSchemaRegistry server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ManagedSchemaRegistryRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ManagedSchemaRegistryRestInterceptor


class ManagedSchemaRegistryRestTransport(_BaseManagedSchemaRegistryRestTransport):
    """REST backend synchronous transport for ManagedSchemaRegistry.

    SchemaRegistry is a service that allows users to manage schemas for
    their Kafka clusters. It provides APIs to register, list, and delete
    schemas, as well as to get the schema for a given schema id or a
    given version id under a subject, to update the global or
    subject-specific compatibility mode, and to check the compatibility
    of a schema against a subject or a version. The main resource
    hierarchy is as follows:

    - SchemaRegistry
    - SchemaRegistry/Context
    - SchemaRegistry/Context/Schema
    - SchemaRegistry/Context/Subject
    - SchemaRegistry/Context/Subject/Version
    - SchemaRegistry/Config
    - SchemaRegistry/Mode

    **SchemaRegistry** is the root resource to represent a schema
    registry instance. A customer can have multiple schema registry
    instances in a project.

    **Context** is a context resource that represents a group of
    schemas, subjects and versions. A schema registry instance can have
    multiple contexts and always has a 'default' context. Contexts are
    independent of each other. Context is optional and if not specified,
    it falls back to the 'default' context.

    **Schema** is a schema resource that represents a unique schema in a
    context of a schema registry instance. Each schema has a unique
    schema id, and can be referenced by a version of a subject.

    **Subject** refers to the name under which the schema is registered.
    A typical subject is the Kafka topic name. A schema registry
    instance can have multiple subjects.

    **Version** represents a version of a subject. A subject can have
    multiple versions. Creation of new version of a subject is guarded
    by the compatibility mode configured globally or for the subject
    specifically.

    **Config** represents a config at global level cross all registry
    instances or at subject level. Currently, only compatibility is
    supported in config.

    **Mode** represents the mode of a schema registry or a specific
    subject. Three modes are supported:

    - READONLY: The schema registry is in read-only mode, no write
      operations allowed..
    - READWRITE: The schema registry is in read-write mode, which allows
      limited write operations on the schema.
    - IMPORT: The schema registry is in import mode, which allows more
      editing operations on the schema for data importing purposes.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "managedkafka.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ManagedSchemaRegistryRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'managedkafka.googleapis.com').
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
            interceptor (Optional[ManagedSchemaRegistryRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ManagedSchemaRegistryRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CheckCompatibility(
        _BaseManagedSchemaRegistryRestTransport._BaseCheckCompatibility,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.CheckCompatibility")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.CheckCompatibilityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry.CheckCompatibilityResponse:
            r"""Call the check compatibility method over HTTP.

            Args:
                request (~.schema_registry.CheckCompatibilityRequest):
                    The request object. Request for CheckCompatibility.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry.CheckCompatibilityResponse:
                    Response for CheckCompatibility.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseCheckCompatibility._get_http_options()
            request, metadata = self._interceptor.pre_check_compatibility(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseCheckCompatibility,
                    "_BaseCheckCompatibility__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.CheckCompatibility",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CheckCompatibility",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._CheckCompatibility._get_response(
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
            resp = schema_registry.CheckCompatibilityResponse()
            pb_resp = schema_registry.CheckCompatibilityResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_check_compatibility(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_check_compatibility_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        schema_registry.CheckCompatibilityResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.check_compatibility",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CheckCompatibility",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSchemaRegistry(
        _BaseManagedSchemaRegistryRestTransport._BaseCreateSchemaRegistry,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.CreateSchemaRegistry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcms_schema_registry.CreateSchemaRegistryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaRegistry:
            r"""Call the create schema registry method over HTTP.

            Args:
                request (~.gcms_schema_registry.CreateSchemaRegistryRequest):
                    The request object. Request to create a schema registry
                instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaRegistry:
                    SchemaRegistry is a schema registry
                instance.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseCreateSchemaRegistry._get_http_options()
            request, metadata = self._interceptor.pre_create_schema_registry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseCreateSchemaRegistry,
                    "_BaseCreateSchemaRegistry__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.CreateSchemaRegistry",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CreateSchemaRegistry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._CreateSchemaRegistry._get_response(
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
            resp = schema_registry_resources.SchemaRegistry()
            pb_resp = schema_registry_resources.SchemaRegistry.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_schema_registry(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_schema_registry_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaRegistry.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.create_schema_registry",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CreateSchemaRegistry",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVersion(
        _BaseManagedSchemaRegistryRestTransport._BaseCreateVersion,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.CreateVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.CreateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry.CreateVersionResponse:
            r"""Call the create version method over HTTP.

            Args:
                request (~.schema_registry.CreateVersionRequest):
                    The request object. Request for CreateVersion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry.CreateVersionResponse:
                    Response for CreateVersion.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseCreateVersion._get_http_options()
            request, metadata = self._interceptor.pre_create_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseCreateVersion,
                    "_BaseCreateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.CreateVersion",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CreateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._CreateVersion._get_response(
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
            resp = schema_registry.CreateVersionResponse()
            pb_resp = schema_registry.CreateVersionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry.CreateVersionResponse.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.create_version",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CreateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSchemaConfig(
        _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaConfig,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.DeleteSchemaConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.DeleteSchemaConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaConfig:
            r"""Call the delete schema config method over HTTP.

            Args:
                request (~.schema_registry.DeleteSchemaConfigRequest):
                    The request object. Request for deleting schema config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaConfig:
                    SchemaConfig represents configuration
                for a schema registry or a specific
                subject.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_schema_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaConfig,
                    "_BaseDeleteSchemaConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.DeleteSchemaConfig",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSchemaConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._DeleteSchemaConfig._get_response(
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
            resp = schema_registry_resources.SchemaConfig()
            pb_resp = schema_registry_resources.SchemaConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_schema_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_schema_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaConfig.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.delete_schema_config",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSchemaConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSchemaMode(
        _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaMode,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.DeleteSchemaMode")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.DeleteSchemaModeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaMode:
            r"""Call the delete schema mode method over HTTP.

            Args:
                request (~.schema_registry.DeleteSchemaModeRequest):
                    The request object. Request for deleting schema mode.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaMode:
                    SchemaMode represents the mode of a schema registry or a
                specific subject. Four modes are supported:

                - NONE: deprecated. This was the default mode for a
                  subject, but now the default is unset (which means use
                  the global schema registry setting)
                - READONLY: The schema registry is in read-only mode.
                - READWRITE: The schema registry is in read-write mode,
                  which allows limited write operations on the schema.
                - IMPORT: The schema registry is in import mode, which
                  allows more editing operations on the schema for data
                  importing purposes.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaMode._get_http_options()
            request, metadata = self._interceptor.pre_delete_schema_mode(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaMode,
                    "_BaseDeleteSchemaMode__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.DeleteSchemaMode",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSchemaMode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._DeleteSchemaMode._get_response(
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
            resp = schema_registry_resources.SchemaMode()
            pb_resp = schema_registry_resources.SchemaMode.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_schema_mode(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_schema_mode_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaMode.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.delete_schema_mode",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSchemaMode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSchemaRegistry(
        _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaRegistry,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.DeleteSchemaRegistry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.DeleteSchemaRegistryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete schema registry method over HTTP.

            Args:
                request (~.schema_registry.DeleteSchemaRegistryRequest):
                    The request object. Request for DeleteSchemaRegistry.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaRegistry._get_http_options()
            request, metadata = self._interceptor.pre_delete_schema_registry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseDeleteSchemaRegistry,
                    "_BaseDeleteSchemaRegistry__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.DeleteSchemaRegistry",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSchemaRegistry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._DeleteSchemaRegistry._get_response(
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

    class _DeleteSubject(
        _BaseManagedSchemaRegistryRestTransport._BaseDeleteSubject,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.DeleteSubject")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.DeleteSubjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the delete subject method over HTTP.

            Args:
                request (~.schema_registry.DeleteSubjectRequest):
                    The request object. Request for DeleteSubject.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseDeleteSubject._get_http_options()
            request, metadata = self._interceptor.pre_delete_subject(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseDeleteSubject,
                    "_BaseDeleteSubject__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.DeleteSubject",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSubject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._DeleteSubject._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_subject(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_subject_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.delete_subject",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteSubject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteVersion(
        _BaseManagedSchemaRegistryRestTransport._BaseDeleteVersion,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.DeleteVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.DeleteVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the delete version method over HTTP.

            Args:
                request (~.schema_registry.DeleteVersionRequest):
                    The request object. Request for DeleteVersion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseDeleteVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseDeleteVersion,
                    "_BaseDeleteVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.DeleteVersion",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._DeleteVersion._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_version_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.delete_version",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetContext(
        _BaseManagedSchemaRegistryRestTransport._BaseGetContext,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetContext")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetContextRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.Context:
            r"""Call the get context method over HTTP.

            Args:
                request (~.schema_registry.GetContextRequest):
                    The request object. Request for GetContext
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.Context:
                    Context represents an independent
                schema grouping in a schema registry
                instance.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetContext._get_http_options()
            request, metadata = self._interceptor.pre_get_context(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetContext,
                    "_BaseGetContext__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetContext",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetContext",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetContext._get_response(
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
            resp = schema_registry_resources.Context()
            pb_resp = schema_registry_resources.Context.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_context(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_context_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.Context.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_context",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetContext",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRawSchema(
        _BaseManagedSchemaRegistryRestTransport._BaseGetRawSchema,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetRawSchema")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the get raw schema method over HTTP.

            Args:
                request (~.schema_registry.GetSchemaRequest):
                    The request object. Request for GetSchema.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetRawSchema._get_http_options()
            request, metadata = self._interceptor.pre_get_raw_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetRawSchema,
                    "_BaseGetRawSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetRawSchema",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetRawSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetRawSchema._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_raw_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_raw_schema_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_raw_schema",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetRawSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRawSchemaVersion(
        _BaseManagedSchemaRegistryRestTransport._BaseGetRawSchemaVersion,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetRawSchemaVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the get raw schema version method over HTTP.

            Args:
                request (~.schema_registry.GetVersionRequest):
                    The request object. Request for GetVersion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetRawSchemaVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_raw_schema_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetRawSchemaVersion,
                    "_BaseGetRawSchemaVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetRawSchemaVersion",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetRawSchemaVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._GetRawSchemaVersion._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_raw_schema_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_raw_schema_version_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_raw_schema_version",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetRawSchemaVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSchema(
        _BaseManagedSchemaRegistryRestTransport._BaseGetSchema,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetSchema")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.Schema:
            r"""Call the get schema method over HTTP.

            Args:
                request (~.schema_registry.GetSchemaRequest):
                    The request object. Request for GetSchema.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.Schema:
                    Schema for a Kafka message.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetSchema._get_http_options()
            request, metadata = self._interceptor.pre_get_schema(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetSchema,
                    "_BaseGetSchema__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetSchema",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchema",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetSchema._get_response(
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
            resp = schema_registry_resources.Schema()
            pb_resp = schema_registry_resources.Schema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_schema(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_schema_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.Schema.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_schema",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchema",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSchemaConfig(
        _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaConfig,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetSchemaConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetSchemaConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaConfig:
            r"""Call the get schema config method over HTTP.

            Args:
                request (~.schema_registry.GetSchemaConfigRequest):
                    The request object. Request for getting config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaConfig:
                    SchemaConfig represents configuration
                for a schema registry or a specific
                subject.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_schema_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaConfig,
                    "_BaseGetSchemaConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetSchemaConfig",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchemaConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._GetSchemaConfig._get_response(
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
            resp = schema_registry_resources.SchemaConfig()
            pb_resp = schema_registry_resources.SchemaConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_schema_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_schema_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaConfig.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_schema_config",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchemaConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSchemaMode(
        _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaMode,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetSchemaMode")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetSchemaModeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaMode:
            r"""Call the get schema mode method over HTTP.

            Args:
                request (~.schema_registry.GetSchemaModeRequest):
                    The request object. Request for getting schema registry
                or subject mode.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaMode:
                    SchemaMode represents the mode of a schema registry or a
                specific subject. Four modes are supported:

                - NONE: deprecated. This was the default mode for a
                  subject, but now the default is unset (which means use
                  the global schema registry setting)
                - READONLY: The schema registry is in read-only mode.
                - READWRITE: The schema registry is in read-write mode,
                  which allows limited write operations on the schema.
                - IMPORT: The schema registry is in import mode, which
                  allows more editing operations on the schema for data
                  importing purposes.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaMode._get_http_options()
            request, metadata = self._interceptor.pre_get_schema_mode(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaMode,
                    "_BaseGetSchemaMode__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetSchemaMode",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchemaMode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetSchemaMode._get_response(
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
            resp = schema_registry_resources.SchemaMode()
            pb_resp = schema_registry_resources.SchemaMode.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_schema_mode(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_schema_mode_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaMode.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_schema_mode",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchemaMode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSchemaRegistry(
        _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaRegistry,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetSchemaRegistry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetSchemaRegistryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaRegistry:
            r"""Call the get schema registry method over HTTP.

            Args:
                request (~.schema_registry.GetSchemaRegistryRequest):
                    The request object. Request for GetSchemaRegistry.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaRegistry:
                    SchemaRegistry is a schema registry
                instance.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaRegistry._get_http_options()
            request, metadata = self._interceptor.pre_get_schema_registry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetSchemaRegistry,
                    "_BaseGetSchemaRegistry__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetSchemaRegistry",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchemaRegistry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._GetSchemaRegistry._get_response(
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
            resp = schema_registry_resources.SchemaRegistry()
            pb_resp = schema_registry_resources.SchemaRegistry.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_schema_registry(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_schema_registry_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaRegistry.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_schema_registry",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetSchemaRegistry",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVersion(
        _BaseManagedSchemaRegistryRestTransport._BaseGetVersion,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.GetVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaVersion:
            r"""Call the get version method over HTTP.

            Args:
                request (~.schema_registry.GetVersionRequest):
                    The request object. Request for GetVersion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaVersion:
                    Version of a schema.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetVersion,
                    "_BaseGetVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetVersion",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetVersion._get_response(
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
            resp = schema_registry_resources.SchemaVersion()
            pb_resp = schema_registry_resources.SchemaVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaVersion.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.get_version",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListContexts(
        _BaseManagedSchemaRegistryRestTransport._BaseListContexts,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListContexts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListContextsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list contexts method over HTTP.

            Args:
                request (~.schema_registry.ListContextsRequest):
                    The request object. Request for ListContexts.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListContexts._get_http_options()
            request, metadata = self._interceptor.pre_list_contexts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListContexts,
                    "_BaseListContexts__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListContexts",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListContexts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._ListContexts._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_contexts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_contexts_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_contexts",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListContexts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReferencedSchemas(
        _BaseManagedSchemaRegistryRestTransport._BaseListReferencedSchemas,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListReferencedSchemas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListReferencedSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list referenced schemas method over HTTP.

            Args:
                request (~.schema_registry.ListReferencedSchemasRequest):
                    The request object. Request for ListReferencedSchemas.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListReferencedSchemas._get_http_options()
            request, metadata = self._interceptor.pre_list_referenced_schemas(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListReferencedSchemas,
                    "_BaseListReferencedSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListReferencedSchemas",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListReferencedSchemas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._ListReferencedSchemas._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_referenced_schemas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_referenced_schemas_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_referenced_schemas",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListReferencedSchemas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSchemaRegistries(
        _BaseManagedSchemaRegistryRestTransport._BaseListSchemaRegistries,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListSchemaRegistries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListSchemaRegistriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry.ListSchemaRegistriesResponse:
            r"""Call the list schema registries method over HTTP.

            Args:
                request (~.schema_registry.ListSchemaRegistriesRequest):
                    The request object. Request for ListSchemaRegistries.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry.ListSchemaRegistriesResponse:
                    Request for ListSchemaRegistries.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListSchemaRegistries._get_http_options()
            request, metadata = self._interceptor.pre_list_schema_registries(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListSchemaRegistries,
                    "_BaseListSchemaRegistries__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListSchemaRegistries",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSchemaRegistries",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._ListSchemaRegistries._get_response(
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
            resp = schema_registry.ListSchemaRegistriesResponse()
            pb_resp = schema_registry.ListSchemaRegistriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_schema_registries(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_schema_registries_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        schema_registry.ListSchemaRegistriesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_schema_registries",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSchemaRegistries",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSchemaTypes(
        _BaseManagedSchemaRegistryRestTransport._BaseListSchemaTypes,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListSchemaTypes")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListSchemaTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list schema types method over HTTP.

            Args:
                request (~.schema_registry.ListSchemaTypesRequest):
                    The request object. Request for ListSchemaTypes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListSchemaTypes._get_http_options()
            request, metadata = self._interceptor.pre_list_schema_types(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListSchemaTypes,
                    "_BaseListSchemaTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListSchemaTypes",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSchemaTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._ListSchemaTypes._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_schema_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_schema_types_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_schema_types",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSchemaTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSchemaVersions(
        _BaseManagedSchemaRegistryRestTransport._BaseListSchemaVersions,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListSchemaVersions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListSchemaVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list schema versions method over HTTP.

            Args:
                request (~.schema_registry.ListSchemaVersionsRequest):
                    The request object. Request for ListSchemaVersions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListSchemaVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_schema_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListSchemaVersions,
                    "_BaseListSchemaVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListSchemaVersions",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSchemaVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._ListSchemaVersions._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_schema_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_schema_versions_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_schema_versions",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSchemaVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSubjects(
        _BaseManagedSchemaRegistryRestTransport._BaseListSubjects,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListSubjects")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListSubjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list subjects method over HTTP.

            Args:
                request (~.schema_registry.ListSubjectsRequest):
                    The request object. Request for listing subjects.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListSubjects._get_http_options()
            request, metadata = self._interceptor.pre_list_subjects(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListSubjects,
                    "_BaseListSubjects__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListSubjects",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSubjects",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._ListSubjects._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_subjects(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_subjects_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_subjects",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSubjects",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSubjectsBySchemaId(
        _BaseManagedSchemaRegistryRestTransport._BaseListSubjectsBySchemaId,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListSubjectsBySchemaId")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListSubjectsBySchemaIdRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list subjects by schema
            id method over HTTP.

                Args:
                    request (~.schema_registry.ListSubjectsBySchemaIdRequest):
                        The request object. Request for listing subjects.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.httpbody_pb2.HttpBody:
                        Message that represents an arbitrary HTTP body. It
                    should only be used for payload formats that can't be
                    represented as JSON, such as raw binary or an HTML page.

                    This message can be used both in streaming and
                    non-streaming API methods in the request as well as the
                    response.

                    It can be used as a top-level request field, which is
                    convenient if one wants to extract parameters from
                    either the URL or HTTP template into the request fields
                    and also want access to the raw HTTP body.

                    Example:

                    ::

                        message GetResourceRequest {
                          // A unique request id.
                          string request_id = 1;

                          // The raw HTTP body is bound to this field.
                          google.api.HttpBody http_body = 2;

                        }

                        service ResourceService {
                          rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);
                          rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                        }

                    Example with streaming methods:

                    ::

                        service CaldavService {
                          rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);
                          rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                        }

                    Use of this type only changes how the request and
                    response bodies are handled, all other features will
                    continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListSubjectsBySchemaId._get_http_options()
            request, metadata = self._interceptor.pre_list_subjects_by_schema_id(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListSubjectsBySchemaId,
                    "_BaseListSubjectsBySchemaId__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListSubjectsBySchemaId",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSubjectsBySchemaId",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._ListSubjectsBySchemaId._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_subjects_by_schema_id(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_subjects_by_schema_id_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_subjects_by_schema_id",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListSubjectsBySchemaId",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVersions(
        _BaseManagedSchemaRegistryRestTransport._BaseListVersions,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListVersions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.ListVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the list versions method over HTTP.

            Args:
                request (~.schema_registry.ListVersionsRequest):
                    The request object. Request for GetVersions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_versions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListVersions,
                    "_BaseListVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListVersions",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._ListVersions._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_versions_with_metadata(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.list_versions",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupVersion(
        _BaseManagedSchemaRegistryRestTransport._BaseLookupVersion,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.LookupVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.LookupVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaVersion:
            r"""Call the lookup version method over HTTP.

            Args:
                request (~.schema_registry.LookupVersionRequest):
                    The request object. Request for LookupVersion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaVersion:
                    Version of a schema.
            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseLookupVersion._get_http_options()
            request, metadata = self._interceptor.pre_lookup_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseLookupVersion,
                    "_BaseLookupVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.LookupVersion",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "LookupVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._LookupVersion._get_response(
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
            resp = schema_registry_resources.SchemaVersion()
            pb_resp = schema_registry_resources.SchemaVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaVersion.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.lookup_version",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "LookupVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSchemaConfig(
        _BaseManagedSchemaRegistryRestTransport._BaseUpdateSchemaConfig,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.UpdateSchemaConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.UpdateSchemaConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaConfig:
            r"""Call the update schema config method over HTTP.

            Args:
                request (~.schema_registry.UpdateSchemaConfigRequest):
                    The request object. Request for updating schema config.
                On a SchemaSubject-level SchemaConfig,
                an unset field will be removed from the
                SchemaConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaConfig:
                    SchemaConfig represents configuration
                for a schema registry or a specific
                subject.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseUpdateSchemaConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_schema_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseUpdateSchemaConfig,
                    "_BaseUpdateSchemaConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.UpdateSchemaConfig",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "UpdateSchemaConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._UpdateSchemaConfig._get_response(
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
            resp = schema_registry_resources.SchemaConfig()
            pb_resp = schema_registry_resources.SchemaConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_schema_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_schema_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaConfig.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.update_schema_config",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "UpdateSchemaConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSchemaMode(
        _BaseManagedSchemaRegistryRestTransport._BaseUpdateSchemaMode,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.UpdateSchemaMode")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: schema_registry.UpdateSchemaModeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> schema_registry_resources.SchemaMode:
            r"""Call the update schema mode method over HTTP.

            Args:
                request (~.schema_registry.UpdateSchemaModeRequest):
                    The request object. Request for updating schema registry
                or subject mode.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.schema_registry_resources.SchemaMode:
                    SchemaMode represents the mode of a schema registry or a
                specific subject. Four modes are supported:

                - NONE: deprecated. This was the default mode for a
                  subject, but now the default is unset (which means use
                  the global schema registry setting)
                - READONLY: The schema registry is in read-only mode.
                - READWRITE: The schema registry is in read-write mode,
                  which allows limited write operations on the schema.
                - IMPORT: The schema registry is in import mode, which
                  allows more editing operations on the schema for data
                  importing purposes.

            """

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseUpdateSchemaMode._get_http_options()
            request, metadata = self._interceptor.pre_update_schema_mode(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseUpdateSchemaMode,
                    "_BaseUpdateSchemaMode__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.UpdateSchemaMode",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "UpdateSchemaMode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._UpdateSchemaMode._get_response(
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
            resp = schema_registry_resources.SchemaMode()
            pb_resp = schema_registry_resources.SchemaMode.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_schema_mode(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_schema_mode_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = schema_registry_resources.SchemaMode.to_json(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.update_schema_mode",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "UpdateSchemaMode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def check_compatibility(
        self,
    ) -> Callable[
        [schema_registry.CheckCompatibilityRequest],
        schema_registry.CheckCompatibilityResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CheckCompatibility(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_schema_registry(
        self,
    ) -> Callable[
        [gcms_schema_registry.CreateSchemaRegistryRequest],
        schema_registry_resources.SchemaRegistry,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSchemaRegistry(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_version(
        self,
    ) -> Callable[
        [schema_registry.CreateVersionRequest], schema_registry.CreateVersionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_schema_config(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaConfigRequest],
        schema_registry_resources.SchemaConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSchemaConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaModeRequest], schema_registry_resources.SchemaMode
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSchemaMode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_schema_registry(
        self,
    ) -> Callable[[schema_registry.DeleteSchemaRegistryRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSchemaRegistry(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_subject(
        self,
    ) -> Callable[[schema_registry.DeleteSubjectRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSubject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_version(
        self,
    ) -> Callable[[schema_registry.DeleteVersionRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_context(
        self,
    ) -> Callable[
        [schema_registry.GetContextRequest], schema_registry_resources.Context
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetContext(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_raw_schema(
        self,
    ) -> Callable[[schema_registry.GetSchemaRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRawSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_raw_schema_version(
        self,
    ) -> Callable[[schema_registry.GetVersionRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRawSchemaVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_schema(
        self,
    ) -> Callable[[schema_registry.GetSchemaRequest], schema_registry_resources.Schema]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_schema_config(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaConfigRequest], schema_registry_resources.SchemaConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSchemaConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaModeRequest], schema_registry_resources.SchemaMode
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSchemaMode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_schema_registry(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaRegistryRequest],
        schema_registry_resources.SchemaRegistry,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSchemaRegistry(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_version(
        self,
    ) -> Callable[
        [schema_registry.GetVersionRequest], schema_registry_resources.SchemaVersion
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_contexts(
        self,
    ) -> Callable[[schema_registry.ListContextsRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListContexts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_referenced_schemas(
        self,
    ) -> Callable[
        [schema_registry.ListReferencedSchemasRequest], httpbody_pb2.HttpBody
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReferencedSchemas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_schema_registries(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaRegistriesRequest],
        schema_registry.ListSchemaRegistriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSchemaRegistries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_schema_types(
        self,
    ) -> Callable[[schema_registry.ListSchemaTypesRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSchemaTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_schema_versions(
        self,
    ) -> Callable[[schema_registry.ListSchemaVersionsRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSchemaVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_subjects(
        self,
    ) -> Callable[[schema_registry.ListSubjectsRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubjects(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_subjects_by_schema_id(
        self,
    ) -> Callable[
        [schema_registry.ListSubjectsBySchemaIdRequest], httpbody_pb2.HttpBody
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubjectsBySchemaId(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_versions(
        self,
    ) -> Callable[[schema_registry.ListVersionsRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup_version(
        self,
    ) -> Callable[
        [schema_registry.LookupVersionRequest], schema_registry_resources.SchemaVersion
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_schema_config(
        self,
    ) -> Callable[
        [schema_registry.UpdateSchemaConfigRequest],
        schema_registry_resources.SchemaConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSchemaConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.UpdateSchemaModeRequest], schema_registry_resources.SchemaMode
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSchemaMode(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseManagedSchemaRegistryRestTransport._BaseGetLocation,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
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
        _BaseManagedSchemaRegistryRestTransport._BaseListLocations,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
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
        _BaseManagedSchemaRegistryRestTransport._BaseCancelOperation,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseManagedSchemaRegistryRestTransport._BaseDeleteOperation,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedSchemaRegistryRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseManagedSchemaRegistryRestTransport._BaseGetOperation,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
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
        _BaseManagedSchemaRegistryRestTransport._BaseListOperations,
        ManagedSchemaRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ManagedSchemaRegistryRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseManagedSchemaRegistryRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedSchemaRegistryRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedSchemaRegistryRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
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


__all__ = ("ManagedSchemaRegistryRestTransport",)
