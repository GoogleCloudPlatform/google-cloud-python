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

from google.cloud.saasplatform_saasservicemgmt_v1beta1._compat import transcode_request
from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import (
    deployments_resources,
    deployments_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSaasDeploymentsRestTransport

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


class SaasDeploymentsRestInterceptor:
    """Interceptor for SaasDeployments.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SaasDeploymentsRestTransport.

    .. code-block:: python
        class MyCustomSaasDeploymentsInterceptor(SaasDeploymentsRestInterceptor):
            def pre_create_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_saas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_saas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tenant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_unit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_unit_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_unit_kind(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_unit_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_unit_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_saas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_unit_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_unit_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_saas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_saas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tenant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_unit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_unit_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_unit_kind(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_unit_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_unit_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_releases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_releases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_saas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_saas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tenants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tenants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_unit_kinds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_unit_kinds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_unit_operations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_unit_operations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_units(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_units(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_release(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_release(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_saas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_saas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tenant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tenant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_unit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_unit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_unit_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_unit_kind(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_unit_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_unit_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SaasDeploymentsRestTransport(interceptor=MyCustomSaasDeploymentsInterceptor())
        client = SaasDeploymentsClient(transport=transport)


    """

    def pre_create_release(
        self,
        request: deployments_service.CreateReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.CreateReleaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_create_release(
        self, response: deployments_resources.Release
    ) -> deployments_resources.Release:
        """Post-rpc interceptor for create_release

        DEPRECATED. Please use the `post_create_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_create_release` interceptor runs
        before the `post_create_release_with_metadata` interceptor.
        """
        return response

    def post_create_release_with_metadata(
        self,
        response: deployments_resources.Release,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Release, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_create_release_with_metadata`
        interceptor in new development instead of the `post_create_release` interceptor.
        When both interceptors are used, this `post_create_release_with_metadata` interceptor runs after the
        `post_create_release` interceptor. The (possibly modified) response returned by
        `post_create_release` will be passed to
        `post_create_release_with_metadata`.
        """
        return response, metadata

    def pre_create_saas(
        self,
        request: deployments_service.CreateSaasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.CreateSaasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_saas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_create_saas(
        self, response: deployments_resources.Saas
    ) -> deployments_resources.Saas:
        """Post-rpc interceptor for create_saas

        DEPRECATED. Please use the `post_create_saas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_create_saas` interceptor runs
        before the `post_create_saas_with_metadata` interceptor.
        """
        return response

    def post_create_saas_with_metadata(
        self,
        response: deployments_resources.Saas,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Saas, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_saas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_create_saas_with_metadata`
        interceptor in new development instead of the `post_create_saas` interceptor.
        When both interceptors are used, this `post_create_saas_with_metadata` interceptor runs after the
        `post_create_saas` interceptor. The (possibly modified) response returned by
        `post_create_saas` will be passed to
        `post_create_saas_with_metadata`.
        """
        return response, metadata

    def pre_create_tenant(
        self,
        request: deployments_service.CreateTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.CreateTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_create_tenant(
        self, response: deployments_resources.Tenant
    ) -> deployments_resources.Tenant:
        """Post-rpc interceptor for create_tenant

        DEPRECATED. Please use the `post_create_tenant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_create_tenant` interceptor runs
        before the `post_create_tenant_with_metadata` interceptor.
        """
        return response

    def post_create_tenant_with_metadata(
        self,
        response: deployments_resources.Tenant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Tenant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tenant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_create_tenant_with_metadata`
        interceptor in new development instead of the `post_create_tenant` interceptor.
        When both interceptors are used, this `post_create_tenant_with_metadata` interceptor runs after the
        `post_create_tenant` interceptor. The (possibly modified) response returned by
        `post_create_tenant` will be passed to
        `post_create_tenant_with_metadata`.
        """
        return response, metadata

    def pre_create_unit(
        self,
        request: deployments_service.CreateUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.CreateUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_create_unit(
        self, response: deployments_resources.Unit
    ) -> deployments_resources.Unit:
        """Post-rpc interceptor for create_unit

        DEPRECATED. Please use the `post_create_unit_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_create_unit` interceptor runs
        before the `post_create_unit_with_metadata` interceptor.
        """
        return response

    def post_create_unit_with_metadata(
        self,
        response: deployments_resources.Unit,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Unit, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_unit

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_create_unit_with_metadata`
        interceptor in new development instead of the `post_create_unit` interceptor.
        When both interceptors are used, this `post_create_unit_with_metadata` interceptor runs after the
        `post_create_unit` interceptor. The (possibly modified) response returned by
        `post_create_unit` will be passed to
        `post_create_unit_with_metadata`.
        """
        return response, metadata

    def pre_create_unit_kind(
        self,
        request: deployments_service.CreateUnitKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.CreateUnitKindRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_unit_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_create_unit_kind(
        self, response: deployments_resources.UnitKind
    ) -> deployments_resources.UnitKind:
        """Post-rpc interceptor for create_unit_kind

        DEPRECATED. Please use the `post_create_unit_kind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_create_unit_kind` interceptor runs
        before the `post_create_unit_kind_with_metadata` interceptor.
        """
        return response

    def post_create_unit_kind_with_metadata(
        self,
        response: deployments_resources.UnitKind,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.UnitKind, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_unit_kind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_create_unit_kind_with_metadata`
        interceptor in new development instead of the `post_create_unit_kind` interceptor.
        When both interceptors are used, this `post_create_unit_kind_with_metadata` interceptor runs after the
        `post_create_unit_kind` interceptor. The (possibly modified) response returned by
        `post_create_unit_kind` will be passed to
        `post_create_unit_kind_with_metadata`.
        """
        return response, metadata

    def pre_create_unit_operation(
        self,
        request: deployments_service.CreateUnitOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.CreateUnitOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_unit_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_create_unit_operation(
        self, response: deployments_resources.UnitOperation
    ) -> deployments_resources.UnitOperation:
        """Post-rpc interceptor for create_unit_operation

        DEPRECATED. Please use the `post_create_unit_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_create_unit_operation` interceptor runs
        before the `post_create_unit_operation_with_metadata` interceptor.
        """
        return response

    def post_create_unit_operation_with_metadata(
        self,
        response: deployments_resources.UnitOperation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_resources.UnitOperation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_unit_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_create_unit_operation_with_metadata`
        interceptor in new development instead of the `post_create_unit_operation` interceptor.
        When both interceptors are used, this `post_create_unit_operation_with_metadata` interceptor runs after the
        `post_create_unit_operation` interceptor. The (possibly modified) response returned by
        `post_create_unit_operation` will be passed to
        `post_create_unit_operation_with_metadata`.
        """
        return response, metadata

    def pre_delete_release(
        self,
        request: deployments_service.DeleteReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.DeleteReleaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def pre_delete_saas(
        self,
        request: deployments_service.DeleteSaasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.DeleteSaasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_saas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def pre_delete_tenant(
        self,
        request: deployments_service.DeleteTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.DeleteTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def pre_delete_unit(
        self,
        request: deployments_service.DeleteUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.DeleteUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def pre_delete_unit_kind(
        self,
        request: deployments_service.DeleteUnitKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.DeleteUnitKindRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_unit_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def pre_delete_unit_operation(
        self,
        request: deployments_service.DeleteUnitOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.DeleteUnitOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_unit_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def pre_get_release(
        self,
        request: deployments_service.GetReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.GetReleaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_release(
        self, response: deployments_resources.Release
    ) -> deployments_resources.Release:
        """Post-rpc interceptor for get_release

        DEPRECATED. Please use the `post_get_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_get_release` interceptor runs
        before the `post_get_release_with_metadata` interceptor.
        """
        return response

    def post_get_release_with_metadata(
        self,
        response: deployments_resources.Release,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Release, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_get_release_with_metadata`
        interceptor in new development instead of the `post_get_release` interceptor.
        When both interceptors are used, this `post_get_release_with_metadata` interceptor runs after the
        `post_get_release` interceptor. The (possibly modified) response returned by
        `post_get_release` will be passed to
        `post_get_release_with_metadata`.
        """
        return response, metadata

    def pre_get_saas(
        self,
        request: deployments_service.GetSaasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.GetSaasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_saas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_saas(
        self, response: deployments_resources.Saas
    ) -> deployments_resources.Saas:
        """Post-rpc interceptor for get_saas

        DEPRECATED. Please use the `post_get_saas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_get_saas` interceptor runs
        before the `post_get_saas_with_metadata` interceptor.
        """
        return response

    def post_get_saas_with_metadata(
        self,
        response: deployments_resources.Saas,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Saas, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_saas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_get_saas_with_metadata`
        interceptor in new development instead of the `post_get_saas` interceptor.
        When both interceptors are used, this `post_get_saas_with_metadata` interceptor runs after the
        `post_get_saas` interceptor. The (possibly modified) response returned by
        `post_get_saas` will be passed to
        `post_get_saas_with_metadata`.
        """
        return response, metadata

    def pre_get_tenant(
        self,
        request: deployments_service.GetTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.GetTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_tenant(
        self, response: deployments_resources.Tenant
    ) -> deployments_resources.Tenant:
        """Post-rpc interceptor for get_tenant

        DEPRECATED. Please use the `post_get_tenant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_get_tenant` interceptor runs
        before the `post_get_tenant_with_metadata` interceptor.
        """
        return response

    def post_get_tenant_with_metadata(
        self,
        response: deployments_resources.Tenant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Tenant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tenant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_get_tenant_with_metadata`
        interceptor in new development instead of the `post_get_tenant` interceptor.
        When both interceptors are used, this `post_get_tenant_with_metadata` interceptor runs after the
        `post_get_tenant` interceptor. The (possibly modified) response returned by
        `post_get_tenant` will be passed to
        `post_get_tenant_with_metadata`.
        """
        return response, metadata

    def pre_get_unit(
        self,
        request: deployments_service.GetUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.GetUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_unit(
        self, response: deployments_resources.Unit
    ) -> deployments_resources.Unit:
        """Post-rpc interceptor for get_unit

        DEPRECATED. Please use the `post_get_unit_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_get_unit` interceptor runs
        before the `post_get_unit_with_metadata` interceptor.
        """
        return response

    def post_get_unit_with_metadata(
        self,
        response: deployments_resources.Unit,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Unit, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_unit

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_get_unit_with_metadata`
        interceptor in new development instead of the `post_get_unit` interceptor.
        When both interceptors are used, this `post_get_unit_with_metadata` interceptor runs after the
        `post_get_unit` interceptor. The (possibly modified) response returned by
        `post_get_unit` will be passed to
        `post_get_unit_with_metadata`.
        """
        return response, metadata

    def pre_get_unit_kind(
        self,
        request: deployments_service.GetUnitKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.GetUnitKindRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_unit_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_unit_kind(
        self, response: deployments_resources.UnitKind
    ) -> deployments_resources.UnitKind:
        """Post-rpc interceptor for get_unit_kind

        DEPRECATED. Please use the `post_get_unit_kind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_get_unit_kind` interceptor runs
        before the `post_get_unit_kind_with_metadata` interceptor.
        """
        return response

    def post_get_unit_kind_with_metadata(
        self,
        response: deployments_resources.UnitKind,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.UnitKind, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_unit_kind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_get_unit_kind_with_metadata`
        interceptor in new development instead of the `post_get_unit_kind` interceptor.
        When both interceptors are used, this `post_get_unit_kind_with_metadata` interceptor runs after the
        `post_get_unit_kind` interceptor. The (possibly modified) response returned by
        `post_get_unit_kind` will be passed to
        `post_get_unit_kind_with_metadata`.
        """
        return response, metadata

    def pre_get_unit_operation(
        self,
        request: deployments_service.GetUnitOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.GetUnitOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_unit_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_unit_operation(
        self, response: deployments_resources.UnitOperation
    ) -> deployments_resources.UnitOperation:
        """Post-rpc interceptor for get_unit_operation

        DEPRECATED. Please use the `post_get_unit_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_get_unit_operation` interceptor runs
        before the `post_get_unit_operation_with_metadata` interceptor.
        """
        return response

    def post_get_unit_operation_with_metadata(
        self,
        response: deployments_resources.UnitOperation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_resources.UnitOperation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_unit_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_get_unit_operation_with_metadata`
        interceptor in new development instead of the `post_get_unit_operation` interceptor.
        When both interceptors are used, this `post_get_unit_operation_with_metadata` interceptor runs after the
        `post_get_unit_operation` interceptor. The (possibly modified) response returned by
        `post_get_unit_operation` will be passed to
        `post_get_unit_operation_with_metadata`.
        """
        return response, metadata

    def pre_list_releases(
        self,
        request: deployments_service.ListReleasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListReleasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_releases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_releases(
        self, response: deployments_service.ListReleasesResponse
    ) -> deployments_service.ListReleasesResponse:
        """Post-rpc interceptor for list_releases

        DEPRECATED. Please use the `post_list_releases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_list_releases` interceptor runs
        before the `post_list_releases_with_metadata` interceptor.
        """
        return response

    def post_list_releases_with_metadata(
        self,
        response: deployments_service.ListReleasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListReleasesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_releases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_list_releases_with_metadata`
        interceptor in new development instead of the `post_list_releases` interceptor.
        When both interceptors are used, this `post_list_releases_with_metadata` interceptor runs after the
        `post_list_releases` interceptor. The (possibly modified) response returned by
        `post_list_releases` will be passed to
        `post_list_releases_with_metadata`.
        """
        return response, metadata

    def pre_list_saas(
        self,
        request: deployments_service.ListSaasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListSaasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_saas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_saas(
        self, response: deployments_service.ListSaasResponse
    ) -> deployments_service.ListSaasResponse:
        """Post-rpc interceptor for list_saas

        DEPRECATED. Please use the `post_list_saas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_list_saas` interceptor runs
        before the `post_list_saas_with_metadata` interceptor.
        """
        return response

    def post_list_saas_with_metadata(
        self,
        response: deployments_service.ListSaasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListSaasResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_saas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_list_saas_with_metadata`
        interceptor in new development instead of the `post_list_saas` interceptor.
        When both interceptors are used, this `post_list_saas_with_metadata` interceptor runs after the
        `post_list_saas` interceptor. The (possibly modified) response returned by
        `post_list_saas` will be passed to
        `post_list_saas_with_metadata`.
        """
        return response, metadata

    def pre_list_tenants(
        self,
        request: deployments_service.ListTenantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListTenantsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_tenants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_tenants(
        self, response: deployments_service.ListTenantsResponse
    ) -> deployments_service.ListTenantsResponse:
        """Post-rpc interceptor for list_tenants

        DEPRECATED. Please use the `post_list_tenants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_list_tenants` interceptor runs
        before the `post_list_tenants_with_metadata` interceptor.
        """
        return response

    def post_list_tenants_with_metadata(
        self,
        response: deployments_service.ListTenantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListTenantsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_tenants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_list_tenants_with_metadata`
        interceptor in new development instead of the `post_list_tenants` interceptor.
        When both interceptors are used, this `post_list_tenants_with_metadata` interceptor runs after the
        `post_list_tenants` interceptor. The (possibly modified) response returned by
        `post_list_tenants` will be passed to
        `post_list_tenants_with_metadata`.
        """
        return response, metadata

    def pre_list_unit_kinds(
        self,
        request: deployments_service.ListUnitKindsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListUnitKindsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_unit_kinds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_unit_kinds(
        self, response: deployments_service.ListUnitKindsResponse
    ) -> deployments_service.ListUnitKindsResponse:
        """Post-rpc interceptor for list_unit_kinds

        DEPRECATED. Please use the `post_list_unit_kinds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_list_unit_kinds` interceptor runs
        before the `post_list_unit_kinds_with_metadata` interceptor.
        """
        return response

    def post_list_unit_kinds_with_metadata(
        self,
        response: deployments_service.ListUnitKindsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListUnitKindsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_unit_kinds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_list_unit_kinds_with_metadata`
        interceptor in new development instead of the `post_list_unit_kinds` interceptor.
        When both interceptors are used, this `post_list_unit_kinds_with_metadata` interceptor runs after the
        `post_list_unit_kinds` interceptor. The (possibly modified) response returned by
        `post_list_unit_kinds` will be passed to
        `post_list_unit_kinds_with_metadata`.
        """
        return response, metadata

    def pre_list_unit_operations(
        self,
        request: deployments_service.ListUnitOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListUnitOperationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_unit_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_unit_operations(
        self, response: deployments_service.ListUnitOperationsResponse
    ) -> deployments_service.ListUnitOperationsResponse:
        """Post-rpc interceptor for list_unit_operations

        DEPRECATED. Please use the `post_list_unit_operations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_list_unit_operations` interceptor runs
        before the `post_list_unit_operations_with_metadata` interceptor.
        """
        return response

    def post_list_unit_operations_with_metadata(
        self,
        response: deployments_service.ListUnitOperationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListUnitOperationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_unit_operations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_list_unit_operations_with_metadata`
        interceptor in new development instead of the `post_list_unit_operations` interceptor.
        When both interceptors are used, this `post_list_unit_operations_with_metadata` interceptor runs after the
        `post_list_unit_operations` interceptor. The (possibly modified) response returned by
        `post_list_unit_operations` will be passed to
        `post_list_unit_operations_with_metadata`.
        """
        return response, metadata

    def pre_list_units(
        self,
        request: deployments_service.ListUnitsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListUnitsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_units

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_units(
        self, response: deployments_service.ListUnitsResponse
    ) -> deployments_service.ListUnitsResponse:
        """Post-rpc interceptor for list_units

        DEPRECATED. Please use the `post_list_units_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_list_units` interceptor runs
        before the `post_list_units_with_metadata` interceptor.
        """
        return response

    def post_list_units_with_metadata(
        self,
        response: deployments_service.ListUnitsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.ListUnitsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_units

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_list_units_with_metadata`
        interceptor in new development instead of the `post_list_units` interceptor.
        When both interceptors are used, this `post_list_units_with_metadata` interceptor runs after the
        `post_list_units` interceptor. The (possibly modified) response returned by
        `post_list_units` will be passed to
        `post_list_units_with_metadata`.
        """
        return response, metadata

    def pre_update_release(
        self,
        request: deployments_service.UpdateReleaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.UpdateReleaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_release

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_update_release(
        self, response: deployments_resources.Release
    ) -> deployments_resources.Release:
        """Post-rpc interceptor for update_release

        DEPRECATED. Please use the `post_update_release_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_update_release` interceptor runs
        before the `post_update_release_with_metadata` interceptor.
        """
        return response

    def post_update_release_with_metadata(
        self,
        response: deployments_resources.Release,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Release, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_release

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_update_release_with_metadata`
        interceptor in new development instead of the `post_update_release` interceptor.
        When both interceptors are used, this `post_update_release_with_metadata` interceptor runs after the
        `post_update_release` interceptor. The (possibly modified) response returned by
        `post_update_release` will be passed to
        `post_update_release_with_metadata`.
        """
        return response, metadata

    def pre_update_saas(
        self,
        request: deployments_service.UpdateSaasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.UpdateSaasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_saas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_update_saas(
        self, response: deployments_resources.Saas
    ) -> deployments_resources.Saas:
        """Post-rpc interceptor for update_saas

        DEPRECATED. Please use the `post_update_saas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_update_saas` interceptor runs
        before the `post_update_saas_with_metadata` interceptor.
        """
        return response

    def post_update_saas_with_metadata(
        self,
        response: deployments_resources.Saas,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Saas, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_saas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_update_saas_with_metadata`
        interceptor in new development instead of the `post_update_saas` interceptor.
        When both interceptors are used, this `post_update_saas_with_metadata` interceptor runs after the
        `post_update_saas` interceptor. The (possibly modified) response returned by
        `post_update_saas` will be passed to
        `post_update_saas_with_metadata`.
        """
        return response, metadata

    def pre_update_tenant(
        self,
        request: deployments_service.UpdateTenantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.UpdateTenantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_tenant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_update_tenant(
        self, response: deployments_resources.Tenant
    ) -> deployments_resources.Tenant:
        """Post-rpc interceptor for update_tenant

        DEPRECATED. Please use the `post_update_tenant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_update_tenant` interceptor runs
        before the `post_update_tenant_with_metadata` interceptor.
        """
        return response

    def post_update_tenant_with_metadata(
        self,
        response: deployments_resources.Tenant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Tenant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tenant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_update_tenant_with_metadata`
        interceptor in new development instead of the `post_update_tenant` interceptor.
        When both interceptors are used, this `post_update_tenant_with_metadata` interceptor runs after the
        `post_update_tenant` interceptor. The (possibly modified) response returned by
        `post_update_tenant` will be passed to
        `post_update_tenant_with_metadata`.
        """
        return response, metadata

    def pre_update_unit(
        self,
        request: deployments_service.UpdateUnitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.UpdateUnitRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_unit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_update_unit(
        self, response: deployments_resources.Unit
    ) -> deployments_resources.Unit:
        """Post-rpc interceptor for update_unit

        DEPRECATED. Please use the `post_update_unit_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_update_unit` interceptor runs
        before the `post_update_unit_with_metadata` interceptor.
        """
        return response

    def post_update_unit_with_metadata(
        self,
        response: deployments_resources.Unit,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.Unit, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_unit

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_update_unit_with_metadata`
        interceptor in new development instead of the `post_update_unit` interceptor.
        When both interceptors are used, this `post_update_unit_with_metadata` interceptor runs after the
        `post_update_unit` interceptor. The (possibly modified) response returned by
        `post_update_unit` will be passed to
        `post_update_unit_with_metadata`.
        """
        return response, metadata

    def pre_update_unit_kind(
        self,
        request: deployments_service.UpdateUnitKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.UpdateUnitKindRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_unit_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_update_unit_kind(
        self, response: deployments_resources.UnitKind
    ) -> deployments_resources.UnitKind:
        """Post-rpc interceptor for update_unit_kind

        DEPRECATED. Please use the `post_update_unit_kind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_update_unit_kind` interceptor runs
        before the `post_update_unit_kind_with_metadata` interceptor.
        """
        return response

    def post_update_unit_kind_with_metadata(
        self,
        response: deployments_resources.UnitKind,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[deployments_resources.UnitKind, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_unit_kind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_update_unit_kind_with_metadata`
        interceptor in new development instead of the `post_update_unit_kind` interceptor.
        When both interceptors are used, this `post_update_unit_kind_with_metadata` interceptor runs after the
        `post_update_unit_kind` interceptor. The (possibly modified) response returned by
        `post_update_unit_kind` will be passed to
        `post_update_unit_kind_with_metadata`.
        """
        return response, metadata

    def pre_update_unit_operation(
        self,
        request: deployments_service.UpdateUnitOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_service.UpdateUnitOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_unit_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_update_unit_operation(
        self, response: deployments_resources.UnitOperation
    ) -> deployments_resources.UnitOperation:
        """Post-rpc interceptor for update_unit_operation

        DEPRECATED. Please use the `post_update_unit_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code. This `post_update_unit_operation` interceptor runs
        before the `post_update_unit_operation_with_metadata` interceptor.
        """
        return response

    def post_update_unit_operation_with_metadata(
        self,
        response: deployments_resources.UnitOperation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployments_resources.UnitOperation, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_unit_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasDeployments server but before it is returned to user code.

        We recommend only using this `post_update_unit_operation_with_metadata`
        interceptor in new development instead of the `post_update_unit_operation` interceptor.
        When both interceptors are used, this `post_update_unit_operation_with_metadata` interceptor runs after the
        `post_update_unit_operation` interceptor. The (possibly modified) response returned by
        `post_update_unit_operation` will be passed to
        `post_update_unit_operation_with_metadata`.
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
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the SaasDeployments server but before
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
        before they are sent to the SaasDeployments server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the SaasDeployments server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SaasDeploymentsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SaasDeploymentsRestInterceptor


class SaasDeploymentsRestTransport(_BaseSaasDeploymentsRestTransport):
    """REST backend synchronous transport for SaasDeployments.

    Manages the deployment of SaaS services.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "saasservicemgmt.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SaasDeploymentsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'saasservicemgmt.googleapis.com').
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
            interceptor (Optional[SaasDeploymentsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SaasDeploymentsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateRelease(
        _BaseSaasDeploymentsRestTransport._BaseCreateRelease, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.CreateRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.CreateReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Release:
            r"""Call the create release method over HTTP.

            Args:
                request (~.deployments_service.CreateReleaseRequest):
                    The request object. The request structure for the
                CreateRelease method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Release:
                    A new version to be propagated and
                deployed to units. This includes
                pointers to packaged blueprints for
                actuation (e.g Helm or Terraform
                configuration packages) via artifact
                registry.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseCreateRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseCreateRelease,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.CreateRelease",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._CreateRelease._get_response(
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
            resp = deployments_resources.Release()
            pb_resp = deployments_resources.Release.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_release_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Release.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.create_release",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSaas(
        _BaseSaasDeploymentsRestTransport._BaseCreateSaas, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.CreateSaas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.CreateSaasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Saas:
            r"""Call the create saas method over HTTP.

            Args:
                request (~.deployments_service.CreateSaasRequest):
                    The request object. The request structure for the
                CreateSaas method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Saas:
                    Saas is a representation of a SaaS
                service managed by the Producer.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseCreateSaas._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_saas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseCreateSaas,
                    "_BaseCreateSaas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.CreateSaas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateSaas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._CreateSaas._get_response(
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
            resp = deployments_resources.Saas()
            pb_resp = deployments_resources.Saas.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_saas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_saas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Saas.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.create_saas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateSaas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTenant(
        _BaseSaasDeploymentsRestTransport._BaseCreateTenant, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.CreateTenant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.CreateTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Tenant:
            r"""Call the create tenant method over HTTP.

            Args:
                request (~.deployments_service.CreateTenantRequest):
                    The request object. The request structure for the
                CreateTenant method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Tenant:
                    Tenant represents the service producer side of an
                instance of the service created based on a request from
                a consumer. In a typical scenario a Tenant has a
                one-to-one mapping with a resource given out to a
                service consumer.

                Example:

                ::

                   tenant:
                     name: "projects/svc1/locations/loc/tenants/inst-068afff8"
                     consumer_resource: "projects/gshoe/locations/loc/shoes/black-shoe"

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseCreateTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseCreateTenant,
                    "_BaseCreateTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.CreateTenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._CreateTenant._get_response(
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
            resp = deployments_resources.Tenant()
            pb_resp = deployments_resources.Tenant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_tenant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tenant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Tenant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.create_tenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateTenant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUnit(
        _BaseSaasDeploymentsRestTransport._BaseCreateUnit, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.CreateUnit")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.CreateUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Unit:
            r"""Call the create unit method over HTTP.

            Args:
                request (~.deployments_service.CreateUnitRequest):
                    The request object. The request structure for the
                CreateUnit method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Unit:
                    A unit of deployment that has its
                lifecycle via a CRUD API using an
                actuation engine under the hood (e.g.
                based on Terraform, Helm or a custom
                implementation provided by a service
                producer). A building block of a SaaS
                Tenant.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseCreateUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseCreateUnit,
                    "_BaseCreateUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.CreateUnit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._CreateUnit._get_response(
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
            resp = deployments_resources.Unit()
            pb_resp = deployments_resources.Unit.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_unit(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_unit_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Unit.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.create_unit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateUnit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUnitKind(
        _BaseSaasDeploymentsRestTransport._BaseCreateUnitKind, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.CreateUnitKind")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.CreateUnitKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.UnitKind:
            r"""Call the create unit kind method over HTTP.

            Args:
                request (~.deployments_service.CreateUnitKindRequest):
                    The request object. The request structure for the
                CreateUnitKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.UnitKind:
                    Definition of a Unit. Units belonging
                to the same UnitKind are managed
                together; for example they follow the
                same release model (blueprints, versions
                etc.) and are typically rolled out
                together.

            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseCreateUnitKind._get_http_options()
            request, metadata = self._interceptor.pre_create_unit_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseCreateUnitKind,
                    "_BaseCreateUnitKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.CreateUnitKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateUnitKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._CreateUnitKind._get_response(
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
            resp = deployments_resources.UnitKind()
            pb_resp = deployments_resources.UnitKind.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_unit_kind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_unit_kind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.UnitKind.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.create_unit_kind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateUnitKind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUnitOperation(
        _BaseSaasDeploymentsRestTransport._BaseCreateUnitOperation,
        SaasDeploymentsRestStub,
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.CreateUnitOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.CreateUnitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.UnitOperation:
            r"""Call the create unit operation method over HTTP.

            Args:
                request (~.deployments_service.CreateUnitOperationRequest):
                    The request object. The request structure for the
                CreateUnitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.UnitOperation:
                    UnitOperation encapsulates the intent
                of changing/interacting with the service
                component represented by the specific
                Unit. Multiple UnitOperations can be
                created (requested) and scheduled in the
                future, however only one will be allowed
                to execute at a time (that can change in
                the future for non-mutating operations).

                UnitOperations allow different actors
                interacting with the same unit to focus
                only on the change they have requested.

                This is a base object that contains the
                common fields in all unit operations.
                Next: 22

            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseCreateUnitOperation._get_http_options()
            request, metadata = self._interceptor.pre_create_unit_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseCreateUnitOperation,
                    "_BaseCreateUnitOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.CreateUnitOperation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateUnitOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._CreateUnitOperation._get_response(
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
            resp = deployments_resources.UnitOperation()
            pb_resp = deployments_resources.UnitOperation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_unit_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_unit_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.UnitOperation.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.create_unit_operation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "CreateUnitOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRelease(
        _BaseSaasDeploymentsRestTransport._BaseDeleteRelease, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.DeleteRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.DeleteReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete release method over HTTP.

            Args:
                request (~.deployments_service.DeleteReleaseRequest):
                    The request object. The request structure for the
                DeleteRelease method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseDeleteRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseDeleteRelease,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.DeleteRelease",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "DeleteRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._DeleteRelease._get_response(
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

    class _DeleteSaas(
        _BaseSaasDeploymentsRestTransport._BaseDeleteSaas, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.DeleteSaas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.DeleteSaasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete saas method over HTTP.

            Args:
                request (~.deployments_service.DeleteSaasRequest):
                    The request object. The request structure for the
                DeleteSaas method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseDeleteSaas._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_saas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseDeleteSaas,
                    "_BaseDeleteSaas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.DeleteSaas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "DeleteSaas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._DeleteSaas._get_response(
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

    class _DeleteTenant(
        _BaseSaasDeploymentsRestTransport._BaseDeleteTenant, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.DeleteTenant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.DeleteTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete tenant method over HTTP.

            Args:
                request (~.deployments_service.DeleteTenantRequest):
                    The request object. The request structure for the
                DeleteTenant method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseDeleteTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseDeleteTenant,
                    "_BaseDeleteTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.DeleteTenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "DeleteTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._DeleteTenant._get_response(
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

    class _DeleteUnit(
        _BaseSaasDeploymentsRestTransport._BaseDeleteUnit, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.DeleteUnit")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.DeleteUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete unit method over HTTP.

            Args:
                request (~.deployments_service.DeleteUnitRequest):
                    The request object. The request structure for the
                DeleteUnit method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseDeleteUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseDeleteUnit,
                    "_BaseDeleteUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.DeleteUnit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "DeleteUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._DeleteUnit._get_response(
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

    class _DeleteUnitKind(
        _BaseSaasDeploymentsRestTransport._BaseDeleteUnitKind, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.DeleteUnitKind")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.DeleteUnitKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete unit kind method over HTTP.

            Args:
                request (~.deployments_service.DeleteUnitKindRequest):
                    The request object. The request structure for the
                DeleteUnitKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseDeleteUnitKind._get_http_options()
            request, metadata = self._interceptor.pre_delete_unit_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseDeleteUnitKind,
                    "_BaseDeleteUnitKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.DeleteUnitKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "DeleteUnitKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._DeleteUnitKind._get_response(
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

    class _DeleteUnitOperation(
        _BaseSaasDeploymentsRestTransport._BaseDeleteUnitOperation,
        SaasDeploymentsRestStub,
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.DeleteUnitOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.DeleteUnitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete unit operation method over HTTP.

            Args:
                request (~.deployments_service.DeleteUnitOperationRequest):
                    The request object. The request structure for the
                DeleteUnitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseDeleteUnitOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_unit_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseDeleteUnitOperation,
                    "_BaseDeleteUnitOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.DeleteUnitOperation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "DeleteUnitOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._DeleteUnitOperation._get_response(
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

    class _GetRelease(
        _BaseSaasDeploymentsRestTransport._BaseGetRelease, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.GetReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Release:
            r"""Call the get release method over HTTP.

            Args:
                request (~.deployments_service.GetReleaseRequest):
                    The request object. The request structure for the
                GetRelease method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Release:
                    A new version to be propagated and
                deployed to units. This includes
                pointers to packaged blueprints for
                actuation (e.g Helm or Terraform
                configuration packages) via artifact
                registry.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseGetRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetRelease,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetRelease",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetRelease._get_response(
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
            resp = deployments_resources.Release()
            pb_resp = deployments_resources.Release.pb(resp)

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
                    response_payload = deployments_resources.Release.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.get_release",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSaas(
        _BaseSaasDeploymentsRestTransport._BaseGetSaas, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetSaas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.GetSaasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Saas:
            r"""Call the get saas method over HTTP.

            Args:
                request (~.deployments_service.GetSaasRequest):
                    The request object. The request structure for the GetSaas
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Saas:
                    Saas is a representation of a SaaS
                service managed by the Producer.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseGetSaas._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_saas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetSaas,
                    "_BaseGetSaas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetSaas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetSaas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetSaas._get_response(
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
            resp = deployments_resources.Saas()
            pb_resp = deployments_resources.Saas.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_saas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_saas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Saas.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.get_saas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetSaas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTenant(
        _BaseSaasDeploymentsRestTransport._BaseGetTenant, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetTenant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.GetTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Tenant:
            r"""Call the get tenant method over HTTP.

            Args:
                request (~.deployments_service.GetTenantRequest):
                    The request object. The request structure for the
                GetTenant method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Tenant:
                    Tenant represents the service producer side of an
                instance of the service created based on a request from
                a consumer. In a typical scenario a Tenant has a
                one-to-one mapping with a resource given out to a
                service consumer.

                Example:

                ::

                   tenant:
                     name: "projects/svc1/locations/loc/tenants/inst-068afff8"
                     consumer_resource: "projects/gshoe/locations/loc/shoes/black-shoe"

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseGetTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetTenant,
                    "_BaseGetTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetTenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetTenant._get_response(
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
            resp = deployments_resources.Tenant()
            pb_resp = deployments_resources.Tenant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tenant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tenant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Tenant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.get_tenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetTenant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUnit(
        _BaseSaasDeploymentsRestTransport._BaseGetUnit, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetUnit")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.GetUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Unit:
            r"""Call the get unit method over HTTP.

            Args:
                request (~.deployments_service.GetUnitRequest):
                    The request object. The request structure for the GetUnit
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Unit:
                    A unit of deployment that has its
                lifecycle via a CRUD API using an
                actuation engine under the hood (e.g.
                based on Terraform, Helm or a custom
                implementation provided by a service
                producer). A building block of a SaaS
                Tenant.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseGetUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetUnit,
                    "_BaseGetUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetUnit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetUnit._get_response(
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
            resp = deployments_resources.Unit()
            pb_resp = deployments_resources.Unit.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_unit(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_unit_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Unit.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.get_unit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetUnit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUnitKind(
        _BaseSaasDeploymentsRestTransport._BaseGetUnitKind, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetUnitKind")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.GetUnitKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.UnitKind:
            r"""Call the get unit kind method over HTTP.

            Args:
                request (~.deployments_service.GetUnitKindRequest):
                    The request object. The request structure for the
                GetUnitKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.UnitKind:
                    Definition of a Unit. Units belonging
                to the same UnitKind are managed
                together; for example they follow the
                same release model (blueprints, versions
                etc.) and are typically rolled out
                together.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseGetUnitKind._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_unit_kind(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetUnitKind,
                    "_BaseGetUnitKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetUnitKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetUnitKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetUnitKind._get_response(
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
            resp = deployments_resources.UnitKind()
            pb_resp = deployments_resources.UnitKind.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_unit_kind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_unit_kind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.UnitKind.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.get_unit_kind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetUnitKind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUnitOperation(
        _BaseSaasDeploymentsRestTransport._BaseGetUnitOperation, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetUnitOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.GetUnitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.UnitOperation:
            r"""Call the get unit operation method over HTTP.

            Args:
                request (~.deployments_service.GetUnitOperationRequest):
                    The request object. The request structure for the
                GetUnitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.UnitOperation:
                    UnitOperation encapsulates the intent
                of changing/interacting with the service
                component represented by the specific
                Unit. Multiple UnitOperations can be
                created (requested) and scheduled in the
                future, however only one will be allowed
                to execute at a time (that can change in
                the future for non-mutating operations).

                UnitOperations allow different actors
                interacting with the same unit to focus
                only on the change they have requested.

                This is a base object that contains the
                common fields in all unit operations.
                Next: 22

            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseGetUnitOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_unit_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetUnitOperation,
                    "_BaseGetUnitOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetUnitOperation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetUnitOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetUnitOperation._get_response(
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
            resp = deployments_resources.UnitOperation()
            pb_resp = deployments_resources.UnitOperation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_unit_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_unit_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.UnitOperation.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.get_unit_operation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetUnitOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReleases(
        _BaseSaasDeploymentsRestTransport._BaseListReleases, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListReleases")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.ListReleasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_service.ListReleasesResponse:
            r"""Call the list releases method over HTTP.

            Args:
                request (~.deployments_service.ListReleasesRequest):
                    The request object. The request structure for the
                ListReleases method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_service.ListReleasesResponse:
                    The response structure for the
                ListReleases method.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseListReleases._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_releases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListReleases,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListReleases",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListReleases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListReleases._get_response(
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
            resp = deployments_service.ListReleasesResponse()
            pb_resp = deployments_service.ListReleasesResponse.pb(resp)

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
                    response_payload = deployments_service.ListReleasesResponse.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.list_releases",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListReleases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSaas(
        _BaseSaasDeploymentsRestTransport._BaseListSaas, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListSaas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.ListSaasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_service.ListSaasResponse:
            r"""Call the list saas method over HTTP.

            Args:
                request (~.deployments_service.ListSaasRequest):
                    The request object. The request structure for the
                ListSaas method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_service.ListSaasResponse:
                    The response structure for the
                ListSaas method.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseListSaas._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_saas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListSaas,
                    "_BaseListSaas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListSaas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListSaas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListSaas._get_response(
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
            resp = deployments_service.ListSaasResponse()
            pb_resp = deployments_service.ListSaasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_saas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_saas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_service.ListSaasResponse.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.list_saas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListSaas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTenants(
        _BaseSaasDeploymentsRestTransport._BaseListTenants, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListTenants")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.ListTenantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_service.ListTenantsResponse:
            r"""Call the list tenants method over HTTP.

            Args:
                request (~.deployments_service.ListTenantsRequest):
                    The request object. The request structure for the
                ListTenants method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_service.ListTenantsResponse:
                    The response structure for the
                ListTenants method.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseListTenants._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tenants(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListTenants,
                    "_BaseListTenants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListTenants",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListTenants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListTenants._get_response(
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
            resp = deployments_service.ListTenantsResponse()
            pb_resp = deployments_service.ListTenantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tenants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tenants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_service.ListTenantsResponse.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.list_tenants",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListTenants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUnitKinds(
        _BaseSaasDeploymentsRestTransport._BaseListUnitKinds, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListUnitKinds")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.ListUnitKindsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_service.ListUnitKindsResponse:
            r"""Call the list unit kinds method over HTTP.

            Args:
                request (~.deployments_service.ListUnitKindsRequest):
                    The request object. The request structure for the
                ListUnitKinds method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_service.ListUnitKindsResponse:
                    The response structure for the
                ListUnitKinds method.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseListUnitKinds._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_unit_kinds(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListUnitKinds,
                    "_BaseListUnitKinds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListUnitKinds",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListUnitKinds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListUnitKinds._get_response(
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
            resp = deployments_service.ListUnitKindsResponse()
            pb_resp = deployments_service.ListUnitKindsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_unit_kinds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_unit_kinds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        deployments_service.ListUnitKindsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.list_unit_kinds",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListUnitKinds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUnitOperations(
        _BaseSaasDeploymentsRestTransport._BaseListUnitOperations,
        SaasDeploymentsRestStub,
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListUnitOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.ListUnitOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_service.ListUnitOperationsResponse:
            r"""Call the list unit operations method over HTTP.

            Args:
                request (~.deployments_service.ListUnitOperationsRequest):
                    The request object. The request structure for the
                ListUnitOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_service.ListUnitOperationsResponse:
                    The response structure for the
                ListUnitOperations method.

            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseListUnitOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_unit_operations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListUnitOperations,
                    "_BaseListUnitOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListUnitOperations",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListUnitOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListUnitOperations._get_response(
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
            resp = deployments_service.ListUnitOperationsResponse()
            pb_resp = deployments_service.ListUnitOperationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_unit_operations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_unit_operations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        deployments_service.ListUnitOperationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.list_unit_operations",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListUnitOperations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUnits(
        _BaseSaasDeploymentsRestTransport._BaseListUnits, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListUnits")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.ListUnitsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_service.ListUnitsResponse:
            r"""Call the list units method over HTTP.

            Args:
                request (~.deployments_service.ListUnitsRequest):
                    The request object. The request structure for the
                ListUnits method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_service.ListUnitsResponse:
                    The response structure for the
                ListUnits method.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseListUnits._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_units(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListUnits,
                    "_BaseListUnits__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListUnits",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListUnits",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListUnits._get_response(
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
            resp = deployments_service.ListUnitsResponse()
            pb_resp = deployments_service.ListUnitsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_units(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_units_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_service.ListUnitsResponse.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.list_units",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListUnits",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRelease(
        _BaseSaasDeploymentsRestTransport._BaseUpdateRelease, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.UpdateRelease")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.UpdateReleaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Release:
            r"""Call the update release method over HTTP.

            Args:
                request (~.deployments_service.UpdateReleaseRequest):
                    The request object. The request structure for the
                UpdateRelease method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Release:
                    A new version to be propagated and
                deployed to units. This includes
                pointers to packaged blueprints for
                actuation (e.g Helm or Terraform
                configuration packages) via artifact
                registry.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseUpdateRelease._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_release(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseUpdateRelease,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.UpdateRelease",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateRelease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._UpdateRelease._get_response(
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
            resp = deployments_resources.Release()
            pb_resp = deployments_resources.Release.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_release(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_release_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Release.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.update_release",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateRelease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSaas(
        _BaseSaasDeploymentsRestTransport._BaseUpdateSaas, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.UpdateSaas")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.UpdateSaasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Saas:
            r"""Call the update saas method over HTTP.

            Args:
                request (~.deployments_service.UpdateSaasRequest):
                    The request object. The request structure for the
                UpdateSaas method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Saas:
                    Saas is a representation of a SaaS
                service managed by the Producer.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseUpdateSaas._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_saas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseUpdateSaas,
                    "_BaseUpdateSaas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.UpdateSaas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateSaas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._UpdateSaas._get_response(
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
            resp = deployments_resources.Saas()
            pb_resp = deployments_resources.Saas.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_saas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_saas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Saas.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.update_saas",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateSaas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTenant(
        _BaseSaasDeploymentsRestTransport._BaseUpdateTenant, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.UpdateTenant")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.UpdateTenantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Tenant:
            r"""Call the update tenant method over HTTP.

            Args:
                request (~.deployments_service.UpdateTenantRequest):
                    The request object. The request structure for the
                UpdateTenant method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Tenant:
                    Tenant represents the service producer side of an
                instance of the service created based on a request from
                a consumer. In a typical scenario a Tenant has a
                one-to-one mapping with a resource given out to a
                service consumer.

                Example:

                ::

                   tenant:
                     name: "projects/svc1/locations/loc/tenants/inst-068afff8"
                     consumer_resource: "projects/gshoe/locations/loc/shoes/black-shoe"

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseUpdateTenant._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tenant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseUpdateTenant,
                    "_BaseUpdateTenant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.UpdateTenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateTenant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._UpdateTenant._get_response(
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
            resp = deployments_resources.Tenant()
            pb_resp = deployments_resources.Tenant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_tenant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tenant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Tenant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.update_tenant",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateTenant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUnit(
        _BaseSaasDeploymentsRestTransport._BaseUpdateUnit, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.UpdateUnit")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.UpdateUnitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.Unit:
            r"""Call the update unit method over HTTP.

            Args:
                request (~.deployments_service.UpdateUnitRequest):
                    The request object. The request structure for the
                UpdateUnit method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.Unit:
                    A unit of deployment that has its
                lifecycle via a CRUD API using an
                actuation engine under the hood (e.g.
                based on Terraform, Helm or a custom
                implementation provided by a service
                producer). A building block of a SaaS
                Tenant.

            """

            http_options = (
                _BaseSaasDeploymentsRestTransport._BaseUpdateUnit._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_unit(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseUpdateUnit,
                    "_BaseUpdateUnit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.UpdateUnit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateUnit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._UpdateUnit._get_response(
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
            resp = deployments_resources.Unit()
            pb_resp = deployments_resources.Unit.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_unit(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_unit_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.Unit.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.update_unit",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateUnit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUnitKind(
        _BaseSaasDeploymentsRestTransport._BaseUpdateUnitKind, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.UpdateUnitKind")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.UpdateUnitKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.UnitKind:
            r"""Call the update unit kind method over HTTP.

            Args:
                request (~.deployments_service.UpdateUnitKindRequest):
                    The request object. The request structure for the
                UpdateUnitKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.UnitKind:
                    Definition of a Unit. Units belonging
                to the same UnitKind are managed
                together; for example they follow the
                same release model (blueprints, versions
                etc.) and are typically rolled out
                together.

            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseUpdateUnitKind._get_http_options()
            request, metadata = self._interceptor.pre_update_unit_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseUpdateUnitKind,
                    "_BaseUpdateUnitKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.UpdateUnitKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateUnitKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._UpdateUnitKind._get_response(
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
            resp = deployments_resources.UnitKind()
            pb_resp = deployments_resources.UnitKind.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_unit_kind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_unit_kind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.UnitKind.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.update_unit_kind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateUnitKind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUnitOperation(
        _BaseSaasDeploymentsRestTransport._BaseUpdateUnitOperation,
        SaasDeploymentsRestStub,
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.UpdateUnitOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: deployments_service.UpdateUnitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployments_resources.UnitOperation:
            r"""Call the update unit operation method over HTTP.

            Args:
                request (~.deployments_service.UpdateUnitOperationRequest):
                    The request object. The request structure for the
                UpdateUnitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployments_resources.UnitOperation:
                    UnitOperation encapsulates the intent
                of changing/interacting with the service
                component represented by the specific
                Unit. Multiple UnitOperations can be
                created (requested) and scheduled in the
                future, however only one will be allowed
                to execute at a time (that can change in
                the future for non-mutating operations).

                UnitOperations allow different actors
                interacting with the same unit to focus
                only on the change they have requested.

                This is a base object that contains the
                common fields in all unit operations.
                Next: 22

            """

            http_options = _BaseSaasDeploymentsRestTransport._BaseUpdateUnitOperation._get_http_options()
            request, metadata = self._interceptor.pre_update_unit_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseUpdateUnitOperation,
                    "_BaseUpdateUnitOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.UpdateUnitOperation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateUnitOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._UpdateUnitOperation._get_response(
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
            resp = deployments_resources.UnitOperation()
            pb_resp = deployments_resources.UnitOperation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_unit_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_unit_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployments_resources.UnitOperation.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.update_unit_operation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "UpdateUnitOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_release(
        self,
    ) -> Callable[
        [deployments_service.CreateReleaseRequest], deployments_resources.Release
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_saas(
        self,
    ) -> Callable[[deployments_service.CreateSaasRequest], deployments_resources.Saas]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSaas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tenant(
        self,
    ) -> Callable[
        [deployments_service.CreateTenantRequest], deployments_resources.Tenant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_unit(
        self,
    ) -> Callable[[deployments_service.CreateUnitRequest], deployments_resources.Unit]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_unit_kind(
        self,
    ) -> Callable[
        [deployments_service.CreateUnitKindRequest], deployments_resources.UnitKind
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUnitKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_unit_operation(
        self,
    ) -> Callable[
        [deployments_service.CreateUnitOperationRequest],
        deployments_resources.UnitOperation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUnitOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_release(
        self,
    ) -> Callable[[deployments_service.DeleteReleaseRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_saas(
        self,
    ) -> Callable[[deployments_service.DeleteSaasRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSaas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tenant(
        self,
    ) -> Callable[[deployments_service.DeleteTenantRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_unit(
        self,
    ) -> Callable[[deployments_service.DeleteUnitRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_unit_kind(
        self,
    ) -> Callable[[deployments_service.DeleteUnitKindRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUnitKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_unit_operation(
        self,
    ) -> Callable[[deployments_service.DeleteUnitOperationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUnitOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_release(
        self,
    ) -> Callable[
        [deployments_service.GetReleaseRequest], deployments_resources.Release
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_saas(
        self,
    ) -> Callable[[deployments_service.GetSaasRequest], deployments_resources.Saas]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSaas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tenant(
        self,
    ) -> Callable[[deployments_service.GetTenantRequest], deployments_resources.Tenant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_unit(
        self,
    ) -> Callable[[deployments_service.GetUnitRequest], deployments_resources.Unit]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_unit_kind(
        self,
    ) -> Callable[
        [deployments_service.GetUnitKindRequest], deployments_resources.UnitKind
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUnitKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_unit_operation(
        self,
    ) -> Callable[
        [deployments_service.GetUnitOperationRequest],
        deployments_resources.UnitOperation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUnitOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_releases(
        self,
    ) -> Callable[
        [deployments_service.ListReleasesRequest],
        deployments_service.ListReleasesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReleases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_saas(
        self,
    ) -> Callable[
        [deployments_service.ListSaasRequest], deployments_service.ListSaasResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSaas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tenants(
        self,
    ) -> Callable[
        [deployments_service.ListTenantsRequest],
        deployments_service.ListTenantsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTenants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_unit_kinds(
        self,
    ) -> Callable[
        [deployments_service.ListUnitKindsRequest],
        deployments_service.ListUnitKindsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUnitKinds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_unit_operations(
        self,
    ) -> Callable[
        [deployments_service.ListUnitOperationsRequest],
        deployments_service.ListUnitOperationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUnitOperations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_units(
        self,
    ) -> Callable[
        [deployments_service.ListUnitsRequest], deployments_service.ListUnitsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUnits(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_release(
        self,
    ) -> Callable[
        [deployments_service.UpdateReleaseRequest], deployments_resources.Release
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRelease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_saas(
        self,
    ) -> Callable[[deployments_service.UpdateSaasRequest], deployments_resources.Saas]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSaas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tenant(
        self,
    ) -> Callable[
        [deployments_service.UpdateTenantRequest], deployments_resources.Tenant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTenant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_unit(
        self,
    ) -> Callable[[deployments_service.UpdateUnitRequest], deployments_resources.Unit]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUnit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_unit_kind(
        self,
    ) -> Callable[
        [deployments_service.UpdateUnitKindRequest], deployments_resources.UnitKind
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUnitKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_unit_operation(
        self,
    ) -> Callable[
        [deployments_service.UpdateUnitOperationRequest],
        deployments_resources.UnitOperation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUnitOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseSaasDeploymentsRestTransport._BaseGetLocation, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseSaasDeploymentsRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
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
        _BaseSaasDeploymentsRestTransport._BaseListLocations, SaasDeploymentsRestStub
    ):
        def __hash__(self):
            return hash("SaasDeploymentsRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseSaasDeploymentsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasDeploymentsRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasDeploymentsRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
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


__all__ = ("SaasDeploymentsRestTransport",)
