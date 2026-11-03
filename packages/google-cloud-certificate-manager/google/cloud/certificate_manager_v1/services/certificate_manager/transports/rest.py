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

from google.cloud.certificate_manager_v1._compat import transcode_request
from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config,
    certificate_manager,
    trust_config,
)
from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config as gcc_certificate_issuance_config,
)
from google.cloud.certificate_manager_v1.types import trust_config as gcc_trust_config

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCertificateManagerRestTransport

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


class CertificateManagerRestInterceptor:
    """Interceptor for CertificateManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CertificateManagerRestTransport.

    .. code-block:: python
        class MyCustomCertificateManagerInterceptor(CertificateManagerRestInterceptor):
            def pre_create_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_certificate_issuance_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_certificate_issuance_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_certificate_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_certificate_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_certificate_map_entry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_certificate_map_entry(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_dns_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dns_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_trust_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_trust_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_certificate_issuance_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_certificate_issuance_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_certificate_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_certificate_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_certificate_map_entry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_certificate_map_entry(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_dns_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_dns_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_trust_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_trust_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_certificate_issuance_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_certificate_issuance_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_certificate_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_certificate_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_certificate_map_entry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_certificate_map_entry(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dns_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dns_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_trust_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_trust_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_certificate_issuance_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_certificate_issuance_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_certificate_map_entries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_certificate_map_entries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_certificate_maps(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_certificate_maps(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_certificates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_certificates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dns_authorizations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dns_authorizations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_trust_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_trust_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_certificate_issuance_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_certificate_issuance_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_certificate_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_certificate_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_certificate_map_entry(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_certificate_map_entry(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dns_authorization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dns_authorization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_trust_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_trust_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CertificateManagerRestTransport(interceptor=MyCustomCertificateManagerInterceptor())
        client = CertificateManagerClient(transport=transport)


    """

    def pre_create_certificate(
        self,
        request: certificate_manager.CreateCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.CreateCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_create_certificate(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_certificate

        DEPRECATED. Please use the `post_create_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_create_certificate` interceptor runs
        before the `post_create_certificate_with_metadata` interceptor.
        """
        return response

    def post_create_certificate_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_create_certificate_with_metadata`
        interceptor in new development instead of the `post_create_certificate` interceptor.
        When both interceptors are used, this `post_create_certificate_with_metadata` interceptor runs after the
        `post_create_certificate` interceptor. The (possibly modified) response returned by
        `post_create_certificate` will be passed to
        `post_create_certificate_with_metadata`.
        """
        return response, metadata

    def pre_create_certificate_issuance_config(
        self,
        request: gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_certificate_issuance_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_create_certificate_issuance_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_certificate_issuance_config

        DEPRECATED. Please use the `post_create_certificate_issuance_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_create_certificate_issuance_config` interceptor runs
        before the `post_create_certificate_issuance_config_with_metadata` interceptor.
        """
        return response

    def post_create_certificate_issuance_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_certificate_issuance_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_create_certificate_issuance_config_with_metadata`
        interceptor in new development instead of the `post_create_certificate_issuance_config` interceptor.
        When both interceptors are used, this `post_create_certificate_issuance_config_with_metadata` interceptor runs after the
        `post_create_certificate_issuance_config` interceptor. The (possibly modified) response returned by
        `post_create_certificate_issuance_config` will be passed to
        `post_create_certificate_issuance_config_with_metadata`.
        """
        return response, metadata

    def pre_create_certificate_map(
        self,
        request: certificate_manager.CreateCertificateMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.CreateCertificateMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_certificate_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_create_certificate_map(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_certificate_map

        DEPRECATED. Please use the `post_create_certificate_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_create_certificate_map` interceptor runs
        before the `post_create_certificate_map_with_metadata` interceptor.
        """
        return response

    def post_create_certificate_map_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_certificate_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_create_certificate_map_with_metadata`
        interceptor in new development instead of the `post_create_certificate_map` interceptor.
        When both interceptors are used, this `post_create_certificate_map_with_metadata` interceptor runs after the
        `post_create_certificate_map` interceptor. The (possibly modified) response returned by
        `post_create_certificate_map` will be passed to
        `post_create_certificate_map_with_metadata`.
        """
        return response, metadata

    def pre_create_certificate_map_entry(
        self,
        request: certificate_manager.CreateCertificateMapEntryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.CreateCertificateMapEntryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_certificate_map_entry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_create_certificate_map_entry(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_certificate_map_entry

        DEPRECATED. Please use the `post_create_certificate_map_entry_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_create_certificate_map_entry` interceptor runs
        before the `post_create_certificate_map_entry_with_metadata` interceptor.
        """
        return response

    def post_create_certificate_map_entry_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_certificate_map_entry

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_create_certificate_map_entry_with_metadata`
        interceptor in new development instead of the `post_create_certificate_map_entry` interceptor.
        When both interceptors are used, this `post_create_certificate_map_entry_with_metadata` interceptor runs after the
        `post_create_certificate_map_entry` interceptor. The (possibly modified) response returned by
        `post_create_certificate_map_entry` will be passed to
        `post_create_certificate_map_entry_with_metadata`.
        """
        return response, metadata

    def pre_create_dns_authorization(
        self,
        request: certificate_manager.CreateDnsAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.CreateDnsAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_dns_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_create_dns_authorization(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_dns_authorization

        DEPRECATED. Please use the `post_create_dns_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_create_dns_authorization` interceptor runs
        before the `post_create_dns_authorization_with_metadata` interceptor.
        """
        return response

    def post_create_dns_authorization_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dns_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_create_dns_authorization_with_metadata`
        interceptor in new development instead of the `post_create_dns_authorization` interceptor.
        When both interceptors are used, this `post_create_dns_authorization_with_metadata` interceptor runs after the
        `post_create_dns_authorization` interceptor. The (possibly modified) response returned by
        `post_create_dns_authorization` will be passed to
        `post_create_dns_authorization_with_metadata`.
        """
        return response, metadata

    def pre_create_trust_config(
        self,
        request: gcc_trust_config.CreateTrustConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_trust_config.CreateTrustConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_trust_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_create_trust_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_trust_config

        DEPRECATED. Please use the `post_create_trust_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_create_trust_config` interceptor runs
        before the `post_create_trust_config_with_metadata` interceptor.
        """
        return response

    def post_create_trust_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_trust_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_create_trust_config_with_metadata`
        interceptor in new development instead of the `post_create_trust_config` interceptor.
        When both interceptors are used, this `post_create_trust_config_with_metadata` interceptor runs after the
        `post_create_trust_config` interceptor. The (possibly modified) response returned by
        `post_create_trust_config` will be passed to
        `post_create_trust_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_certificate(
        self,
        request: certificate_manager.DeleteCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.DeleteCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_certificate(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_certificate

        DEPRECATED. Please use the `post_delete_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_delete_certificate` interceptor runs
        before the `post_delete_certificate_with_metadata` interceptor.
        """
        return response

    def post_delete_certificate_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_delete_certificate_with_metadata`
        interceptor in new development instead of the `post_delete_certificate` interceptor.
        When both interceptors are used, this `post_delete_certificate_with_metadata` interceptor runs after the
        `post_delete_certificate` interceptor. The (possibly modified) response returned by
        `post_delete_certificate` will be passed to
        `post_delete_certificate_with_metadata`.
        """
        return response, metadata

    def pre_delete_certificate_issuance_config(
        self,
        request: certificate_issuance_config.DeleteCertificateIssuanceConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_issuance_config.DeleteCertificateIssuanceConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_certificate_issuance_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_certificate_issuance_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_certificate_issuance_config

        DEPRECATED. Please use the `post_delete_certificate_issuance_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_delete_certificate_issuance_config` interceptor runs
        before the `post_delete_certificate_issuance_config_with_metadata` interceptor.
        """
        return response

    def post_delete_certificate_issuance_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_certificate_issuance_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_delete_certificate_issuance_config_with_metadata`
        interceptor in new development instead of the `post_delete_certificate_issuance_config` interceptor.
        When both interceptors are used, this `post_delete_certificate_issuance_config_with_metadata` interceptor runs after the
        `post_delete_certificate_issuance_config` interceptor. The (possibly modified) response returned by
        `post_delete_certificate_issuance_config` will be passed to
        `post_delete_certificate_issuance_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_certificate_map(
        self,
        request: certificate_manager.DeleteCertificateMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.DeleteCertificateMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_certificate_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_certificate_map(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_certificate_map

        DEPRECATED. Please use the `post_delete_certificate_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_delete_certificate_map` interceptor runs
        before the `post_delete_certificate_map_with_metadata` interceptor.
        """
        return response

    def post_delete_certificate_map_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_certificate_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_delete_certificate_map_with_metadata`
        interceptor in new development instead of the `post_delete_certificate_map` interceptor.
        When both interceptors are used, this `post_delete_certificate_map_with_metadata` interceptor runs after the
        `post_delete_certificate_map` interceptor. The (possibly modified) response returned by
        `post_delete_certificate_map` will be passed to
        `post_delete_certificate_map_with_metadata`.
        """
        return response, metadata

    def pre_delete_certificate_map_entry(
        self,
        request: certificate_manager.DeleteCertificateMapEntryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.DeleteCertificateMapEntryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_certificate_map_entry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_certificate_map_entry(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_certificate_map_entry

        DEPRECATED. Please use the `post_delete_certificate_map_entry_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_delete_certificate_map_entry` interceptor runs
        before the `post_delete_certificate_map_entry_with_metadata` interceptor.
        """
        return response

    def post_delete_certificate_map_entry_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_certificate_map_entry

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_delete_certificate_map_entry_with_metadata`
        interceptor in new development instead of the `post_delete_certificate_map_entry` interceptor.
        When both interceptors are used, this `post_delete_certificate_map_entry_with_metadata` interceptor runs after the
        `post_delete_certificate_map_entry` interceptor. The (possibly modified) response returned by
        `post_delete_certificate_map_entry` will be passed to
        `post_delete_certificate_map_entry_with_metadata`.
        """
        return response, metadata

    def pre_delete_dns_authorization(
        self,
        request: certificate_manager.DeleteDnsAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.DeleteDnsAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_dns_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_dns_authorization(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_dns_authorization

        DEPRECATED. Please use the `post_delete_dns_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_delete_dns_authorization` interceptor runs
        before the `post_delete_dns_authorization_with_metadata` interceptor.
        """
        return response

    def post_delete_dns_authorization_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_dns_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_delete_dns_authorization_with_metadata`
        interceptor in new development instead of the `post_delete_dns_authorization` interceptor.
        When both interceptors are used, this `post_delete_dns_authorization_with_metadata` interceptor runs after the
        `post_delete_dns_authorization` interceptor. The (possibly modified) response returned by
        `post_delete_dns_authorization` will be passed to
        `post_delete_dns_authorization_with_metadata`.
        """
        return response, metadata

    def pre_delete_trust_config(
        self,
        request: trust_config.DeleteTrustConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        trust_config.DeleteTrustConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_trust_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_trust_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_trust_config

        DEPRECATED. Please use the `post_delete_trust_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_delete_trust_config` interceptor runs
        before the `post_delete_trust_config_with_metadata` interceptor.
        """
        return response

    def post_delete_trust_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_trust_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_delete_trust_config_with_metadata`
        interceptor in new development instead of the `post_delete_trust_config` interceptor.
        When both interceptors are used, this `post_delete_trust_config_with_metadata` interceptor runs after the
        `post_delete_trust_config` interceptor. The (possibly modified) response returned by
        `post_delete_trust_config` will be passed to
        `post_delete_trust_config_with_metadata`.
        """
        return response, metadata

    def pre_get_certificate(
        self,
        request: certificate_manager.GetCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.GetCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_certificate(
        self, response: certificate_manager.Certificate
    ) -> certificate_manager.Certificate:
        """Post-rpc interceptor for get_certificate

        DEPRECATED. Please use the `post_get_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_get_certificate` interceptor runs
        before the `post_get_certificate_with_metadata` interceptor.
        """
        return response

    def post_get_certificate_with_metadata(
        self,
        response: certificate_manager.Certificate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.Certificate, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_get_certificate_with_metadata`
        interceptor in new development instead of the `post_get_certificate` interceptor.
        When both interceptors are used, this `post_get_certificate_with_metadata` interceptor runs after the
        `post_get_certificate` interceptor. The (possibly modified) response returned by
        `post_get_certificate` will be passed to
        `post_get_certificate_with_metadata`.
        """
        return response, metadata

    def pre_get_certificate_issuance_config(
        self,
        request: certificate_issuance_config.GetCertificateIssuanceConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_issuance_config.GetCertificateIssuanceConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_certificate_issuance_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_certificate_issuance_config(
        self, response: certificate_issuance_config.CertificateIssuanceConfig
    ) -> certificate_issuance_config.CertificateIssuanceConfig:
        """Post-rpc interceptor for get_certificate_issuance_config

        DEPRECATED. Please use the `post_get_certificate_issuance_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_get_certificate_issuance_config` interceptor runs
        before the `post_get_certificate_issuance_config_with_metadata` interceptor.
        """
        return response

    def post_get_certificate_issuance_config_with_metadata(
        self,
        response: certificate_issuance_config.CertificateIssuanceConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_issuance_config.CertificateIssuanceConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_certificate_issuance_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_get_certificate_issuance_config_with_metadata`
        interceptor in new development instead of the `post_get_certificate_issuance_config` interceptor.
        When both interceptors are used, this `post_get_certificate_issuance_config_with_metadata` interceptor runs after the
        `post_get_certificate_issuance_config` interceptor. The (possibly modified) response returned by
        `post_get_certificate_issuance_config` will be passed to
        `post_get_certificate_issuance_config_with_metadata`.
        """
        return response, metadata

    def pre_get_certificate_map(
        self,
        request: certificate_manager.GetCertificateMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.GetCertificateMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_certificate_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_certificate_map(
        self, response: certificate_manager.CertificateMap
    ) -> certificate_manager.CertificateMap:
        """Post-rpc interceptor for get_certificate_map

        DEPRECATED. Please use the `post_get_certificate_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_get_certificate_map` interceptor runs
        before the `post_get_certificate_map_with_metadata` interceptor.
        """
        return response

    def post_get_certificate_map_with_metadata(
        self,
        response: certificate_manager.CertificateMap,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.CertificateMap, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_certificate_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_get_certificate_map_with_metadata`
        interceptor in new development instead of the `post_get_certificate_map` interceptor.
        When both interceptors are used, this `post_get_certificate_map_with_metadata` interceptor runs after the
        `post_get_certificate_map` interceptor. The (possibly modified) response returned by
        `post_get_certificate_map` will be passed to
        `post_get_certificate_map_with_metadata`.
        """
        return response, metadata

    def pre_get_certificate_map_entry(
        self,
        request: certificate_manager.GetCertificateMapEntryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.GetCertificateMapEntryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_certificate_map_entry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_certificate_map_entry(
        self, response: certificate_manager.CertificateMapEntry
    ) -> certificate_manager.CertificateMapEntry:
        """Post-rpc interceptor for get_certificate_map_entry

        DEPRECATED. Please use the `post_get_certificate_map_entry_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_get_certificate_map_entry` interceptor runs
        before the `post_get_certificate_map_entry_with_metadata` interceptor.
        """
        return response

    def post_get_certificate_map_entry_with_metadata(
        self,
        response: certificate_manager.CertificateMapEntry,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.CertificateMapEntry, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_certificate_map_entry

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_get_certificate_map_entry_with_metadata`
        interceptor in new development instead of the `post_get_certificate_map_entry` interceptor.
        When both interceptors are used, this `post_get_certificate_map_entry_with_metadata` interceptor runs after the
        `post_get_certificate_map_entry` interceptor. The (possibly modified) response returned by
        `post_get_certificate_map_entry` will be passed to
        `post_get_certificate_map_entry_with_metadata`.
        """
        return response, metadata

    def pre_get_dns_authorization(
        self,
        request: certificate_manager.GetDnsAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.GetDnsAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_dns_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_dns_authorization(
        self, response: certificate_manager.DnsAuthorization
    ) -> certificate_manager.DnsAuthorization:
        """Post-rpc interceptor for get_dns_authorization

        DEPRECATED. Please use the `post_get_dns_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_get_dns_authorization` interceptor runs
        before the `post_get_dns_authorization_with_metadata` interceptor.
        """
        return response

    def post_get_dns_authorization_with_metadata(
        self,
        response: certificate_manager.DnsAuthorization,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.DnsAuthorization, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_dns_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_get_dns_authorization_with_metadata`
        interceptor in new development instead of the `post_get_dns_authorization` interceptor.
        When both interceptors are used, this `post_get_dns_authorization_with_metadata` interceptor runs after the
        `post_get_dns_authorization` interceptor. The (possibly modified) response returned by
        `post_get_dns_authorization` will be passed to
        `post_get_dns_authorization_with_metadata`.
        """
        return response, metadata

    def pre_get_trust_config(
        self,
        request: trust_config.GetTrustConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        trust_config.GetTrustConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_trust_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_trust_config(
        self, response: trust_config.TrustConfig
    ) -> trust_config.TrustConfig:
        """Post-rpc interceptor for get_trust_config

        DEPRECATED. Please use the `post_get_trust_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_get_trust_config` interceptor runs
        before the `post_get_trust_config_with_metadata` interceptor.
        """
        return response

    def post_get_trust_config_with_metadata(
        self,
        response: trust_config.TrustConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[trust_config.TrustConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_trust_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_get_trust_config_with_metadata`
        interceptor in new development instead of the `post_get_trust_config` interceptor.
        When both interceptors are used, this `post_get_trust_config_with_metadata` interceptor runs after the
        `post_get_trust_config` interceptor. The (possibly modified) response returned by
        `post_get_trust_config` will be passed to
        `post_get_trust_config_with_metadata`.
        """
        return response, metadata

    def pre_list_certificate_issuance_configs(
        self,
        request: certificate_issuance_config.ListCertificateIssuanceConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_issuance_config.ListCertificateIssuanceConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_certificate_issuance_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_certificate_issuance_configs(
        self,
        response: certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
    ) -> certificate_issuance_config.ListCertificateIssuanceConfigsResponse:
        """Post-rpc interceptor for list_certificate_issuance_configs

        DEPRECATED. Please use the `post_list_certificate_issuance_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_list_certificate_issuance_configs` interceptor runs
        before the `post_list_certificate_issuance_configs_with_metadata` interceptor.
        """
        return response

    def post_list_certificate_issuance_configs_with_metadata(
        self,
        response: certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_certificate_issuance_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_list_certificate_issuance_configs_with_metadata`
        interceptor in new development instead of the `post_list_certificate_issuance_configs` interceptor.
        When both interceptors are used, this `post_list_certificate_issuance_configs_with_metadata` interceptor runs after the
        `post_list_certificate_issuance_configs` interceptor. The (possibly modified) response returned by
        `post_list_certificate_issuance_configs` will be passed to
        `post_list_certificate_issuance_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_certificate_map_entries(
        self,
        request: certificate_manager.ListCertificateMapEntriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListCertificateMapEntriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_certificate_map_entries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_certificate_map_entries(
        self, response: certificate_manager.ListCertificateMapEntriesResponse
    ) -> certificate_manager.ListCertificateMapEntriesResponse:
        """Post-rpc interceptor for list_certificate_map_entries

        DEPRECATED. Please use the `post_list_certificate_map_entries_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_list_certificate_map_entries` interceptor runs
        before the `post_list_certificate_map_entries_with_metadata` interceptor.
        """
        return response

    def post_list_certificate_map_entries_with_metadata(
        self,
        response: certificate_manager.ListCertificateMapEntriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListCertificateMapEntriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_certificate_map_entries

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_list_certificate_map_entries_with_metadata`
        interceptor in new development instead of the `post_list_certificate_map_entries` interceptor.
        When both interceptors are used, this `post_list_certificate_map_entries_with_metadata` interceptor runs after the
        `post_list_certificate_map_entries` interceptor. The (possibly modified) response returned by
        `post_list_certificate_map_entries` will be passed to
        `post_list_certificate_map_entries_with_metadata`.
        """
        return response, metadata

    def pre_list_certificate_maps(
        self,
        request: certificate_manager.ListCertificateMapsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListCertificateMapsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_certificate_maps

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_certificate_maps(
        self, response: certificate_manager.ListCertificateMapsResponse
    ) -> certificate_manager.ListCertificateMapsResponse:
        """Post-rpc interceptor for list_certificate_maps

        DEPRECATED. Please use the `post_list_certificate_maps_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_list_certificate_maps` interceptor runs
        before the `post_list_certificate_maps_with_metadata` interceptor.
        """
        return response

    def post_list_certificate_maps_with_metadata(
        self,
        response: certificate_manager.ListCertificateMapsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListCertificateMapsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_certificate_maps

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_list_certificate_maps_with_metadata`
        interceptor in new development instead of the `post_list_certificate_maps` interceptor.
        When both interceptors are used, this `post_list_certificate_maps_with_metadata` interceptor runs after the
        `post_list_certificate_maps` interceptor. The (possibly modified) response returned by
        `post_list_certificate_maps` will be passed to
        `post_list_certificate_maps_with_metadata`.
        """
        return response, metadata

    def pre_list_certificates(
        self,
        request: certificate_manager.ListCertificatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListCertificatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_certificates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_certificates(
        self, response: certificate_manager.ListCertificatesResponse
    ) -> certificate_manager.ListCertificatesResponse:
        """Post-rpc interceptor for list_certificates

        DEPRECATED. Please use the `post_list_certificates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_list_certificates` interceptor runs
        before the `post_list_certificates_with_metadata` interceptor.
        """
        return response

    def post_list_certificates_with_metadata(
        self,
        response: certificate_manager.ListCertificatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListCertificatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_certificates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_list_certificates_with_metadata`
        interceptor in new development instead of the `post_list_certificates` interceptor.
        When both interceptors are used, this `post_list_certificates_with_metadata` interceptor runs after the
        `post_list_certificates` interceptor. The (possibly modified) response returned by
        `post_list_certificates` will be passed to
        `post_list_certificates_with_metadata`.
        """
        return response, metadata

    def pre_list_dns_authorizations(
        self,
        request: certificate_manager.ListDnsAuthorizationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListDnsAuthorizationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_dns_authorizations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_dns_authorizations(
        self, response: certificate_manager.ListDnsAuthorizationsResponse
    ) -> certificate_manager.ListDnsAuthorizationsResponse:
        """Post-rpc interceptor for list_dns_authorizations

        DEPRECATED. Please use the `post_list_dns_authorizations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_list_dns_authorizations` interceptor runs
        before the `post_list_dns_authorizations_with_metadata` interceptor.
        """
        return response

    def post_list_dns_authorizations_with_metadata(
        self,
        response: certificate_manager.ListDnsAuthorizationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.ListDnsAuthorizationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_dns_authorizations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_list_dns_authorizations_with_metadata`
        interceptor in new development instead of the `post_list_dns_authorizations` interceptor.
        When both interceptors are used, this `post_list_dns_authorizations_with_metadata` interceptor runs after the
        `post_list_dns_authorizations` interceptor. The (possibly modified) response returned by
        `post_list_dns_authorizations` will be passed to
        `post_list_dns_authorizations_with_metadata`.
        """
        return response, metadata

    def pre_list_trust_configs(
        self,
        request: trust_config.ListTrustConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        trust_config.ListTrustConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_trust_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_trust_configs(
        self, response: trust_config.ListTrustConfigsResponse
    ) -> trust_config.ListTrustConfigsResponse:
        """Post-rpc interceptor for list_trust_configs

        DEPRECATED. Please use the `post_list_trust_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_list_trust_configs` interceptor runs
        before the `post_list_trust_configs_with_metadata` interceptor.
        """
        return response

    def post_list_trust_configs_with_metadata(
        self,
        response: trust_config.ListTrustConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        trust_config.ListTrustConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_trust_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_list_trust_configs_with_metadata`
        interceptor in new development instead of the `post_list_trust_configs` interceptor.
        When both interceptors are used, this `post_list_trust_configs_with_metadata` interceptor runs after the
        `post_list_trust_configs` interceptor. The (possibly modified) response returned by
        `post_list_trust_configs` will be passed to
        `post_list_trust_configs_with_metadata`.
        """
        return response, metadata

    def pre_update_certificate(
        self,
        request: certificate_manager.UpdateCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.UpdateCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_update_certificate(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_certificate

        DEPRECATED. Please use the `post_update_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_update_certificate` interceptor runs
        before the `post_update_certificate_with_metadata` interceptor.
        """
        return response

    def post_update_certificate_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_update_certificate_with_metadata`
        interceptor in new development instead of the `post_update_certificate` interceptor.
        When both interceptors are used, this `post_update_certificate_with_metadata` interceptor runs after the
        `post_update_certificate` interceptor. The (possibly modified) response returned by
        `post_update_certificate` will be passed to
        `post_update_certificate_with_metadata`.
        """
        return response, metadata

    def pre_update_certificate_issuance_config(
        self,
        request: gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_certificate_issuance_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_update_certificate_issuance_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_certificate_issuance_config

        DEPRECATED. Please use the `post_update_certificate_issuance_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_update_certificate_issuance_config` interceptor runs
        before the `post_update_certificate_issuance_config_with_metadata` interceptor.
        """
        return response

    def post_update_certificate_issuance_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_certificate_issuance_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_update_certificate_issuance_config_with_metadata`
        interceptor in new development instead of the `post_update_certificate_issuance_config` interceptor.
        When both interceptors are used, this `post_update_certificate_issuance_config_with_metadata` interceptor runs after the
        `post_update_certificate_issuance_config` interceptor. The (possibly modified) response returned by
        `post_update_certificate_issuance_config` will be passed to
        `post_update_certificate_issuance_config_with_metadata`.
        """
        return response, metadata

    def pre_update_certificate_map(
        self,
        request: certificate_manager.UpdateCertificateMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.UpdateCertificateMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_certificate_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_update_certificate_map(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_certificate_map

        DEPRECATED. Please use the `post_update_certificate_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_update_certificate_map` interceptor runs
        before the `post_update_certificate_map_with_metadata` interceptor.
        """
        return response

    def post_update_certificate_map_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_certificate_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_update_certificate_map_with_metadata`
        interceptor in new development instead of the `post_update_certificate_map` interceptor.
        When both interceptors are used, this `post_update_certificate_map_with_metadata` interceptor runs after the
        `post_update_certificate_map` interceptor. The (possibly modified) response returned by
        `post_update_certificate_map` will be passed to
        `post_update_certificate_map_with_metadata`.
        """
        return response, metadata

    def pre_update_certificate_map_entry(
        self,
        request: certificate_manager.UpdateCertificateMapEntryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.UpdateCertificateMapEntryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_certificate_map_entry

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_update_certificate_map_entry(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_certificate_map_entry

        DEPRECATED. Please use the `post_update_certificate_map_entry_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_update_certificate_map_entry` interceptor runs
        before the `post_update_certificate_map_entry_with_metadata` interceptor.
        """
        return response

    def post_update_certificate_map_entry_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_certificate_map_entry

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_update_certificate_map_entry_with_metadata`
        interceptor in new development instead of the `post_update_certificate_map_entry` interceptor.
        When both interceptors are used, this `post_update_certificate_map_entry_with_metadata` interceptor runs after the
        `post_update_certificate_map_entry` interceptor. The (possibly modified) response returned by
        `post_update_certificate_map_entry` will be passed to
        `post_update_certificate_map_entry_with_metadata`.
        """
        return response, metadata

    def pre_update_dns_authorization(
        self,
        request: certificate_manager.UpdateDnsAuthorizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        certificate_manager.UpdateDnsAuthorizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_dns_authorization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_update_dns_authorization(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_dns_authorization

        DEPRECATED. Please use the `post_update_dns_authorization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_update_dns_authorization` interceptor runs
        before the `post_update_dns_authorization_with_metadata` interceptor.
        """
        return response

    def post_update_dns_authorization_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dns_authorization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_update_dns_authorization_with_metadata`
        interceptor in new development instead of the `post_update_dns_authorization` interceptor.
        When both interceptors are used, this `post_update_dns_authorization_with_metadata` interceptor runs after the
        `post_update_dns_authorization` interceptor. The (possibly modified) response returned by
        `post_update_dns_authorization` will be passed to
        `post_update_dns_authorization_with_metadata`.
        """
        return response, metadata

    def pre_update_trust_config(
        self,
        request: gcc_trust_config.UpdateTrustConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_trust_config.UpdateTrustConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_trust_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_update_trust_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_trust_config

        DEPRECATED. Please use the `post_update_trust_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code. This `post_update_trust_config` interceptor runs
        before the `post_update_trust_config_with_metadata` interceptor.
        """
        return response

    def post_update_trust_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_trust_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CertificateManager server but before it is returned to user code.

        We recommend only using this `post_update_trust_config_with_metadata`
        interceptor in new development instead of the `post_update_trust_config` interceptor.
        When both interceptors are used, this `post_update_trust_config_with_metadata` interceptor runs after the
        `post_update_trust_config` interceptor. The (possibly modified) response returned by
        `post_update_trust_config` will be passed to
        `post_update_trust_config_with_metadata`.
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
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the CertificateManager server but before
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
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the CertificateManager server but before
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
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CertificateManager server but before
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
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the CertificateManager server but before
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
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CertificateManager server but before
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
        before they are sent to the CertificateManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CertificateManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CertificateManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CertificateManagerRestInterceptor


class CertificateManagerRestTransport(_BaseCertificateManagerRestTransport):
    """REST backend synchronous transport for CertificateManager.

    API Overview

    Certificates Manager API allows customers to see and manage all
    their TLS certificates.

    Certificates Manager API service provides methods to manage
    certificates, group them into collections, and create serving
    configuration that can be easily applied to other Cloud resources
    e.g. Target Proxies.

    Data Model

    The Certificates Manager service exposes the following resources:

    - ``Certificate`` that describes a single TLS certificate.
    - ``CertificateMap`` that describes a collection of certificates
      that can be attached to a target resource.
    - ``CertificateMapEntry`` that describes a single configuration
      entry that consists of a SNI and a group of certificates. It's a
      subresource of CertificateMap.

    Certificate, CertificateMap and CertificateMapEntry IDs have to
    fully match the regexp ``[a-z0-9-]{1,63}``. In other words,

    - only lower case letters, digits, and hyphen are allowed
    - length of the resource ID has to be in [1,63] range.

    Provides methods to manage Cloud Certificate Manager entities.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "certificatemanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CertificateManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'certificatemanager.googleapis.com').
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
            interceptor (Optional[CertificateManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CertificateManagerRestInterceptor()
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

    class _CreateCertificate(
        _BaseCertificateManagerRestTransport._BaseCreateCertificate,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.CreateCertificate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.CreateCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create certificate method over HTTP.

            Args:
                request (~.certificate_manager.CreateCertificateRequest):
                    The request object. Request for the ``CreateCertificate`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseCreateCertificate._get_http_options()
            request, metadata = self._interceptor.pre_create_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCreateCertificate,
                    "_BaseCreateCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CreateCertificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._CreateCertificate._get_response(
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

            resp = self._interceptor.post_create_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_certificate_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.create_certificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCertificateIssuanceConfig(
        _BaseCertificateManagerRestTransport._BaseCreateCertificateIssuanceConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash(
                "CertificateManagerRestTransport.CreateCertificateIssuanceConfig"
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
            request: gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create certificate
            issuance config method over HTTP.

                Args:
                    request (~.gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest):
                        The request object. Request for the ``CreateCertificateIssuanceConfig``
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

            http_options = _BaseCertificateManagerRestTransport._BaseCreateCertificateIssuanceConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_certificate_issuance_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCreateCertificateIssuanceConfig,
                    "_BaseCreateCertificateIssuanceConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CreateCertificateIssuanceConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificateIssuanceConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._CreateCertificateIssuanceConfig._get_response(
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

            resp = self._interceptor.post_create_certificate_issuance_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_certificate_issuance_config_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.create_certificate_issuance_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificateIssuanceConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCertificateMap(
        _BaseCertificateManagerRestTransport._BaseCreateCertificateMap,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.CreateCertificateMap")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.CreateCertificateMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create certificate map method over HTTP.

            Args:
                request (~.certificate_manager.CreateCertificateMapRequest):
                    The request object. Request for the ``CreateCertificateMap`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseCreateCertificateMap._get_http_options()
            request, metadata = self._interceptor.pre_create_certificate_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCreateCertificateMap,
                    "_BaseCreateCertificateMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CreateCertificateMap",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificateMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._CreateCertificateMap._get_response(
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

            resp = self._interceptor.post_create_certificate_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_certificate_map_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.create_certificate_map",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificateMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCertificateMapEntry(
        _BaseCertificateManagerRestTransport._BaseCreateCertificateMapEntry,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.CreateCertificateMapEntry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.CreateCertificateMapEntryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create certificate map
            entry method over HTTP.

                Args:
                    request (~.certificate_manager.CreateCertificateMapEntryRequest):
                        The request object. Request for the ``CreateCertificateMapEntry`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseCreateCertificateMapEntry._get_http_options()
            request, metadata = self._interceptor.pre_create_certificate_map_entry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCreateCertificateMapEntry,
                    "_BaseCreateCertificateMapEntry__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CreateCertificateMapEntry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificateMapEntry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._CreateCertificateMapEntry._get_response(
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

            resp = self._interceptor.post_create_certificate_map_entry(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_certificate_map_entry_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.create_certificate_map_entry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateCertificateMapEntry",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDnsAuthorization(
        _BaseCertificateManagerRestTransport._BaseCreateDnsAuthorization,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.CreateDnsAuthorization")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.CreateDnsAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create dns authorization method over HTTP.

            Args:
                request (~.certificate_manager.CreateDnsAuthorizationRequest):
                    The request object. Request for the ``CreateDnsAuthorization`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseCreateDnsAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_create_dns_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCreateDnsAuthorization,
                    "_BaseCreateDnsAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CreateDnsAuthorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateDnsAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._CreateDnsAuthorization._get_response(
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

            resp = self._interceptor.post_create_dns_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dns_authorization_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.create_dns_authorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateDnsAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTrustConfig(
        _BaseCertificateManagerRestTransport._BaseCreateTrustConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.CreateTrustConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcc_trust_config.CreateTrustConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create trust config method over HTTP.

            Args:
                request (~.gcc_trust_config.CreateTrustConfigRequest):
                    The request object. Request for the ``CreateTrustConfig`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseCreateTrustConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_trust_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCreateTrustConfig,
                    "_BaseCreateTrustConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CreateTrustConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateTrustConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._CreateTrustConfig._get_response(
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

            resp = self._interceptor.post_create_trust_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_trust_config_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.create_trust_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CreateTrustConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCertificate(
        _BaseCertificateManagerRestTransport._BaseDeleteCertificate,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.DeleteCertificate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.DeleteCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete certificate method over HTTP.

            Args:
                request (~.certificate_manager.DeleteCertificateRequest):
                    The request object. Request for the ``DeleteCertificate`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteCertificate._get_http_options()
            request, metadata = self._interceptor.pre_delete_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteCertificate,
                    "_BaseDeleteCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteCertificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._DeleteCertificate._get_response(
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

            resp = self._interceptor.post_delete_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_certificate_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.delete_certificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCertificateIssuanceConfig(
        _BaseCertificateManagerRestTransport._BaseDeleteCertificateIssuanceConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash(
                "CertificateManagerRestTransport.DeleteCertificateIssuanceConfig"
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
            )
            return response

        def __call__(
            self,
            request: certificate_issuance_config.DeleteCertificateIssuanceConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete certificate
            issuance config method over HTTP.

                Args:
                    request (~.certificate_issuance_config.DeleteCertificateIssuanceConfigRequest):
                        The request object. Request for the ``DeleteCertificateIssuanceConfig``
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteCertificateIssuanceConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_certificate_issuance_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteCertificateIssuanceConfig,
                    "_BaseDeleteCertificateIssuanceConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteCertificateIssuanceConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificateIssuanceConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._DeleteCertificateIssuanceConfig._get_response(
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

            resp = self._interceptor.post_delete_certificate_issuance_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_certificate_issuance_config_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.delete_certificate_issuance_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificateIssuanceConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCertificateMap(
        _BaseCertificateManagerRestTransport._BaseDeleteCertificateMap,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.DeleteCertificateMap")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.DeleteCertificateMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete certificate map method over HTTP.

            Args:
                request (~.certificate_manager.DeleteCertificateMapRequest):
                    The request object. Request for the ``DeleteCertificateMap`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteCertificateMap._get_http_options()
            request, metadata = self._interceptor.pre_delete_certificate_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteCertificateMap,
                    "_BaseDeleteCertificateMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteCertificateMap",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificateMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._DeleteCertificateMap._get_response(
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

            resp = self._interceptor.post_delete_certificate_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_certificate_map_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.delete_certificate_map",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificateMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCertificateMapEntry(
        _BaseCertificateManagerRestTransport._BaseDeleteCertificateMapEntry,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.DeleteCertificateMapEntry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.DeleteCertificateMapEntryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete certificate map
            entry method over HTTP.

                Args:
                    request (~.certificate_manager.DeleteCertificateMapEntryRequest):
                        The request object. Request for the ``DeleteCertificateMapEntry`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteCertificateMapEntry._get_http_options()
            request, metadata = self._interceptor.pre_delete_certificate_map_entry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteCertificateMapEntry,
                    "_BaseDeleteCertificateMapEntry__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteCertificateMapEntry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificateMapEntry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._DeleteCertificateMapEntry._get_response(
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

            resp = self._interceptor.post_delete_certificate_map_entry(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_certificate_map_entry_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.delete_certificate_map_entry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteCertificateMapEntry",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDnsAuthorization(
        _BaseCertificateManagerRestTransport._BaseDeleteDnsAuthorization,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.DeleteDnsAuthorization")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.DeleteDnsAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete dns authorization method over HTTP.

            Args:
                request (~.certificate_manager.DeleteDnsAuthorizationRequest):
                    The request object. Request for the ``DeleteDnsAuthorization`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteDnsAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_delete_dns_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteDnsAuthorization,
                    "_BaseDeleteDnsAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteDnsAuthorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteDnsAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._DeleteDnsAuthorization._get_response(
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

            resp = self._interceptor.post_delete_dns_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_dns_authorization_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.delete_dns_authorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteDnsAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTrustConfig(
        _BaseCertificateManagerRestTransport._BaseDeleteTrustConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.DeleteTrustConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: trust_config.DeleteTrustConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete trust config method over HTTP.

            Args:
                request (~.trust_config.DeleteTrustConfigRequest):
                    The request object. Request for the ``DeleteTrustConfig`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteTrustConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_trust_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteTrustConfig,
                    "_BaseDeleteTrustConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteTrustConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteTrustConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._DeleteTrustConfig._get_response(
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

            resp = self._interceptor.post_delete_trust_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_trust_config_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.delete_trust_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteTrustConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCertificate(
        _BaseCertificateManagerRestTransport._BaseGetCertificate,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetCertificate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.GetCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.Certificate:
            r"""Call the get certificate method over HTTP.

            Args:
                request (~.certificate_manager.GetCertificateRequest):
                    The request object. Request for the ``GetCertificate`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.Certificate:
                    Defines TLS certificate.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseGetCertificate._get_http_options()
            request, metadata = self._interceptor.pre_get_certificate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetCertificate,
                    "_BaseGetCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetCertificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._GetCertificate._get_response(
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
            resp = certificate_manager.Certificate()
            pb_resp = certificate_manager.Certificate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_certificate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = certificate_manager.Certificate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.get_certificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCertificateIssuanceConfig(
        _BaseCertificateManagerRestTransport._BaseGetCertificateIssuanceConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetCertificateIssuanceConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_issuance_config.GetCertificateIssuanceConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_issuance_config.CertificateIssuanceConfig:
            r"""Call the get certificate issuance
            config method over HTTP.

                Args:
                    request (~.certificate_issuance_config.GetCertificateIssuanceConfigRequest):
                        The request object. Request for the ``GetCertificateIssuanceConfig`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.certificate_issuance_config.CertificateIssuanceConfig:
                        CertificateIssuanceConfig specifies
                    how to issue and manage a certificate.

            """

            http_options = _BaseCertificateManagerRestTransport._BaseGetCertificateIssuanceConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_certificate_issuance_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetCertificateIssuanceConfig,
                    "_BaseGetCertificateIssuanceConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetCertificateIssuanceConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificateIssuanceConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._GetCertificateIssuanceConfig._get_response(
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
            resp = certificate_issuance_config.CertificateIssuanceConfig()
            pb_resp = certificate_issuance_config.CertificateIssuanceConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_certificate_issuance_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_certificate_issuance_config_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        certificate_issuance_config.CertificateIssuanceConfig.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.get_certificate_issuance_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificateIssuanceConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCertificateMap(
        _BaseCertificateManagerRestTransport._BaseGetCertificateMap,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetCertificateMap")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.GetCertificateMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.CertificateMap:
            r"""Call the get certificate map method over HTTP.

            Args:
                request (~.certificate_manager.GetCertificateMapRequest):
                    The request object. Request for the ``GetCertificateMap`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.CertificateMap:
                    Defines a collection of certificate
                configurations.

            """

            http_options = _BaseCertificateManagerRestTransport._BaseGetCertificateMap._get_http_options()
            request, metadata = self._interceptor.pre_get_certificate_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetCertificateMap,
                    "_BaseGetCertificateMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetCertificateMap",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificateMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._GetCertificateMap._get_response(
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
            resp = certificate_manager.CertificateMap()
            pb_resp = certificate_manager.CertificateMap.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_certificate_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_certificate_map_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = certificate_manager.CertificateMap.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.get_certificate_map",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificateMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCertificateMapEntry(
        _BaseCertificateManagerRestTransport._BaseGetCertificateMapEntry,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetCertificateMapEntry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.GetCertificateMapEntryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.CertificateMapEntry:
            r"""Call the get certificate map entry method over HTTP.

            Args:
                request (~.certificate_manager.GetCertificateMapEntryRequest):
                    The request object. Request for the ``GetCertificateMapEntry`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.CertificateMapEntry:
                    Defines a certificate map entry.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseGetCertificateMapEntry._get_http_options()
            request, metadata = self._interceptor.pre_get_certificate_map_entry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetCertificateMapEntry,
                    "_BaseGetCertificateMapEntry__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetCertificateMapEntry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificateMapEntry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._GetCertificateMapEntry._get_response(
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
            resp = certificate_manager.CertificateMapEntry()
            pb_resp = certificate_manager.CertificateMapEntry.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_certificate_map_entry(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_certificate_map_entry_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = certificate_manager.CertificateMapEntry.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.get_certificate_map_entry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetCertificateMapEntry",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDnsAuthorization(
        _BaseCertificateManagerRestTransport._BaseGetDnsAuthorization,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetDnsAuthorization")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.GetDnsAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.DnsAuthorization:
            r"""Call the get dns authorization method over HTTP.

            Args:
                request (~.certificate_manager.GetDnsAuthorizationRequest):
                    The request object. Request for the ``GetDnsAuthorization`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.DnsAuthorization:
                    A DnsAuthorization resource describes
                a way to perform domain authorization
                for certificate issuance.

            """

            http_options = _BaseCertificateManagerRestTransport._BaseGetDnsAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_get_dns_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetDnsAuthorization,
                    "_BaseGetDnsAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetDnsAuthorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetDnsAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._GetDnsAuthorization._get_response(
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
            resp = certificate_manager.DnsAuthorization()
            pb_resp = certificate_manager.DnsAuthorization.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dns_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dns_authorization_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = certificate_manager.DnsAuthorization.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.get_dns_authorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetDnsAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTrustConfig(
        _BaseCertificateManagerRestTransport._BaseGetTrustConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetTrustConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: trust_config.GetTrustConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> trust_config.TrustConfig:
            r"""Call the get trust config method over HTTP.

            Args:
                request (~.trust_config.GetTrustConfigRequest):
                    The request object. Request for the ``GetTrustConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.trust_config.TrustConfig:
                    Defines a trust config.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseGetTrustConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_trust_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetTrustConfig,
                    "_BaseGetTrustConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetTrustConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetTrustConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._GetTrustConfig._get_response(
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
            resp = trust_config.TrustConfig()
            pb_resp = trust_config.TrustConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_trust_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_trust_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = trust_config.TrustConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.get_trust_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetTrustConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCertificateIssuanceConfigs(
        _BaseCertificateManagerRestTransport._BaseListCertificateIssuanceConfigs,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash(
                "CertificateManagerRestTransport.ListCertificateIssuanceConfigs"
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
            )
            return response

        def __call__(
            self,
            request: certificate_issuance_config.ListCertificateIssuanceConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_issuance_config.ListCertificateIssuanceConfigsResponse:
            r"""Call the list certificate issuance
            configs method over HTTP.

                Args:
                    request (~.certificate_issuance_config.ListCertificateIssuanceConfigsRequest):
                        The request object. Request for the ``ListCertificateIssuanceConfigs``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.certificate_issuance_config.ListCertificateIssuanceConfigsResponse:
                        Response for the ``ListCertificateIssuanceConfigs``
                    method.

            """

            http_options = _BaseCertificateManagerRestTransport._BaseListCertificateIssuanceConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_certificate_issuance_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListCertificateIssuanceConfigs,
                    "_BaseListCertificateIssuanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListCertificateIssuanceConfigs",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificateIssuanceConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._ListCertificateIssuanceConfigs._get_response(
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
            resp = certificate_issuance_config.ListCertificateIssuanceConfigsResponse()
            pb_resp = (
                certificate_issuance_config.ListCertificateIssuanceConfigsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_certificate_issuance_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_certificate_issuance_configs_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = certificate_issuance_config.ListCertificateIssuanceConfigsResponse.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.list_certificate_issuance_configs",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificateIssuanceConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCertificateMapEntries(
        _BaseCertificateManagerRestTransport._BaseListCertificateMapEntries,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListCertificateMapEntries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.ListCertificateMapEntriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.ListCertificateMapEntriesResponse:
            r"""Call the list certificate map
            entries method over HTTP.

                Args:
                    request (~.certificate_manager.ListCertificateMapEntriesRequest):
                        The request object. Request for the ``ListCertificateMapEntries`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.certificate_manager.ListCertificateMapEntriesResponse:
                        Response for the ``ListCertificateMapEntries`` method.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseListCertificateMapEntries._get_http_options()
            request, metadata = self._interceptor.pre_list_certificate_map_entries(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListCertificateMapEntries,
                    "_BaseListCertificateMapEntries__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListCertificateMapEntries",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificateMapEntries",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._ListCertificateMapEntries._get_response(
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
            resp = certificate_manager.ListCertificateMapEntriesResponse()
            pb_resp = certificate_manager.ListCertificateMapEntriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_certificate_map_entries(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_certificate_map_entries_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        certificate_manager.ListCertificateMapEntriesResponse.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.list_certificate_map_entries",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificateMapEntries",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCertificateMaps(
        _BaseCertificateManagerRestTransport._BaseListCertificateMaps,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListCertificateMaps")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.ListCertificateMapsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.ListCertificateMapsResponse:
            r"""Call the list certificate maps method over HTTP.

            Args:
                request (~.certificate_manager.ListCertificateMapsRequest):
                    The request object. Request for the ``ListCertificateMaps`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.ListCertificateMapsResponse:
                    Response for the ``ListCertificateMaps`` method.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseListCertificateMaps._get_http_options()
            request, metadata = self._interceptor.pre_list_certificate_maps(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListCertificateMaps,
                    "_BaseListCertificateMaps__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListCertificateMaps",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificateMaps",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._ListCertificateMaps._get_response(
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
            resp = certificate_manager.ListCertificateMapsResponse()
            pb_resp = certificate_manager.ListCertificateMapsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_certificate_maps(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_certificate_maps_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        certificate_manager.ListCertificateMapsResponse.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.list_certificate_maps",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificateMaps",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCertificates(
        _BaseCertificateManagerRestTransport._BaseListCertificates,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListCertificates")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.ListCertificatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.ListCertificatesResponse:
            r"""Call the list certificates method over HTTP.

            Args:
                request (~.certificate_manager.ListCertificatesRequest):
                    The request object. Request for the ``ListCertificates`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.ListCertificatesResponse:
                    Response for the ``ListCertificates`` method.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseListCertificates._get_http_options()
            request, metadata = self._interceptor.pre_list_certificates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListCertificates,
                    "_BaseListCertificates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListCertificates",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._ListCertificates._get_response(
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
            resp = certificate_manager.ListCertificatesResponse()
            pb_resp = certificate_manager.ListCertificatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_certificates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_certificates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        certificate_manager.ListCertificatesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.list_certificates",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListCertificates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDnsAuthorizations(
        _BaseCertificateManagerRestTransport._BaseListDnsAuthorizations,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListDnsAuthorizations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.ListDnsAuthorizationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> certificate_manager.ListDnsAuthorizationsResponse:
            r"""Call the list dns authorizations method over HTTP.

            Args:
                request (~.certificate_manager.ListDnsAuthorizationsRequest):
                    The request object. Request for the ``ListDnsAuthorizations`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.certificate_manager.ListDnsAuthorizationsResponse:
                    Response for the ``ListDnsAuthorizations`` method.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseListDnsAuthorizations._get_http_options()
            request, metadata = self._interceptor.pre_list_dns_authorizations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListDnsAuthorizations,
                    "_BaseListDnsAuthorizations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListDnsAuthorizations",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListDnsAuthorizations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._ListDnsAuthorizations._get_response(
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
            resp = certificate_manager.ListDnsAuthorizationsResponse()
            pb_resp = certificate_manager.ListDnsAuthorizationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dns_authorizations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dns_authorizations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        certificate_manager.ListDnsAuthorizationsResponse.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.list_dns_authorizations",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListDnsAuthorizations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTrustConfigs(
        _BaseCertificateManagerRestTransport._BaseListTrustConfigs,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListTrustConfigs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: trust_config.ListTrustConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> trust_config.ListTrustConfigsResponse:
            r"""Call the list trust configs method over HTTP.

            Args:
                request (~.trust_config.ListTrustConfigsRequest):
                    The request object. Request for the ``ListTrustConfigs`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.trust_config.ListTrustConfigsResponse:
                    Response for the ``ListTrustConfigs`` method.
            """

            http_options = _BaseCertificateManagerRestTransport._BaseListTrustConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_trust_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListTrustConfigs,
                    "_BaseListTrustConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListTrustConfigs",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListTrustConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._ListTrustConfigs._get_response(
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
            resp = trust_config.ListTrustConfigsResponse()
            pb_resp = trust_config.ListTrustConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_trust_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_trust_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = trust_config.ListTrustConfigsResponse.to_json(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.list_trust_configs",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListTrustConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCertificate(
        _BaseCertificateManagerRestTransport._BaseUpdateCertificate,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.UpdateCertificate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.UpdateCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update certificate method over HTTP.

            Args:
                request (~.certificate_manager.UpdateCertificateRequest):
                    The request object. Request for the ``UpdateCertificate`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseUpdateCertificate._get_http_options()
            request, metadata = self._interceptor.pre_update_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseUpdateCertificate,
                    "_BaseUpdateCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.UpdateCertificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._UpdateCertificate._get_response(
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

            resp = self._interceptor.post_update_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_certificate_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.update_certificate",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCertificateIssuanceConfig(
        _BaseCertificateManagerRestTransport._BaseUpdateCertificateIssuanceConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash(
                "CertificateManagerRestTransport.UpdateCertificateIssuanceConfig"
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
            request: gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update certificate
            issuance config method over HTTP.

                Args:
                    request (~.gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest):
                        The request object. Request for the ``UpdateCertificateIssuanceConfig``
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

            http_options = _BaseCertificateManagerRestTransport._BaseUpdateCertificateIssuanceConfig._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_certificate_issuance_config(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseUpdateCertificateIssuanceConfig,
                    "_BaseUpdateCertificateIssuanceConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.UpdateCertificateIssuanceConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificateIssuanceConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._UpdateCertificateIssuanceConfig._get_response(
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

            resp = self._interceptor.post_update_certificate_issuance_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_certificate_issuance_config_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.update_certificate_issuance_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificateIssuanceConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCertificateMap(
        _BaseCertificateManagerRestTransport._BaseUpdateCertificateMap,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.UpdateCertificateMap")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.UpdateCertificateMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update certificate map method over HTTP.

            Args:
                request (~.certificate_manager.UpdateCertificateMapRequest):
                    The request object. Request for the ``UpdateCertificateMap`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseUpdateCertificateMap._get_http_options()
            request, metadata = self._interceptor.pre_update_certificate_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseUpdateCertificateMap,
                    "_BaseUpdateCertificateMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.UpdateCertificateMap",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificateMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._UpdateCertificateMap._get_response(
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

            resp = self._interceptor.post_update_certificate_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_certificate_map_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.update_certificate_map",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificateMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCertificateMapEntry(
        _BaseCertificateManagerRestTransport._BaseUpdateCertificateMapEntry,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.UpdateCertificateMapEntry")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.UpdateCertificateMapEntryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update certificate map
            entry method over HTTP.

                Args:
                    request (~.certificate_manager.UpdateCertificateMapEntryRequest):
                        The request object. Request for the ``UpdateCertificateMapEntry`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseUpdateCertificateMapEntry._get_http_options()
            request, metadata = self._interceptor.pre_update_certificate_map_entry(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseUpdateCertificateMapEntry,
                    "_BaseUpdateCertificateMapEntry__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.UpdateCertificateMapEntry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificateMapEntry",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._UpdateCertificateMapEntry._get_response(
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

            resp = self._interceptor.post_update_certificate_map_entry(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_certificate_map_entry_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.update_certificate_map_entry",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateCertificateMapEntry",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDnsAuthorization(
        _BaseCertificateManagerRestTransport._BaseUpdateDnsAuthorization,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.UpdateDnsAuthorization")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: certificate_manager.UpdateDnsAuthorizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update dns authorization method over HTTP.

            Args:
                request (~.certificate_manager.UpdateDnsAuthorizationRequest):
                    The request object. Request for the ``UpdateDnsAuthorization`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseUpdateDnsAuthorization._get_http_options()
            request, metadata = self._interceptor.pre_update_dns_authorization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseUpdateDnsAuthorization,
                    "_BaseUpdateDnsAuthorization__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.UpdateDnsAuthorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateDnsAuthorization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CertificateManagerRestTransport._UpdateDnsAuthorization._get_response(
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

            resp = self._interceptor.post_update_dns_authorization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dns_authorization_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.update_dns_authorization",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateDnsAuthorization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTrustConfig(
        _BaseCertificateManagerRestTransport._BaseUpdateTrustConfig,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.UpdateTrustConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gcc_trust_config.UpdateTrustConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update trust config method over HTTP.

            Args:
                request (~.gcc_trust_config.UpdateTrustConfigRequest):
                    The request object. Request for the ``UpdateTrustConfig`` method.
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

            http_options = _BaseCertificateManagerRestTransport._BaseUpdateTrustConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_trust_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseUpdateTrustConfig,
                    "_BaseUpdateTrustConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.UpdateTrustConfig",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateTrustConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._UpdateTrustConfig._get_response(
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

            resp = self._interceptor.post_update_trust_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_trust_config_with_metadata(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerClient.update_trust_config",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "UpdateTrustConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_certificate(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCertificate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_certificate_issuance_config(
        self,
    ) -> Callable[
        [gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCertificateIssuanceConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateMapRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCertificateMap(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateMapEntryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCertificateMapEntry(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.CreateDnsAuthorizationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDnsAuthorization(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_trust_config(
        self,
    ) -> Callable[
        [gcc_trust_config.CreateTrustConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTrustConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_certificate(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCertificate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_certificate_issuance_config(
        self,
    ) -> Callable[
        [certificate_issuance_config.DeleteCertificateIssuanceConfigRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCertificateIssuanceConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateMapRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCertificateMap(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateMapEntryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCertificateMapEntry(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.DeleteDnsAuthorizationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDnsAuthorization(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_trust_config(
        self,
    ) -> Callable[[trust_config.DeleteTrustConfigRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTrustConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_certificate(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateRequest], certificate_manager.Certificate
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCertificate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_certificate_issuance_config(
        self,
    ) -> Callable[
        [certificate_issuance_config.GetCertificateIssuanceConfigRequest],
        certificate_issuance_config.CertificateIssuanceConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCertificateIssuanceConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateMapRequest],
        certificate_manager.CertificateMap,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCertificateMap(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateMapEntryRequest],
        certificate_manager.CertificateMapEntry,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCertificateMapEntry(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.GetDnsAuthorizationRequest],
        certificate_manager.DnsAuthorization,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDnsAuthorization(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_trust_config(
        self,
    ) -> Callable[[trust_config.GetTrustConfigRequest], trust_config.TrustConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTrustConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_certificate_issuance_configs(
        self,
    ) -> Callable[
        [certificate_issuance_config.ListCertificateIssuanceConfigsRequest],
        certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCertificateIssuanceConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_certificate_map_entries(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificateMapEntriesRequest],
        certificate_manager.ListCertificateMapEntriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCertificateMapEntries(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_certificate_maps(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificateMapsRequest],
        certificate_manager.ListCertificateMapsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCertificateMaps(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_certificates(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificatesRequest],
        certificate_manager.ListCertificatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCertificates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_dns_authorizations(
        self,
    ) -> Callable[
        [certificate_manager.ListDnsAuthorizationsRequest],
        certificate_manager.ListDnsAuthorizationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDnsAuthorizations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_trust_configs(
        self,
    ) -> Callable[
        [trust_config.ListTrustConfigsRequest], trust_config.ListTrustConfigsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTrustConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_certificate(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCertificate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_certificate_issuance_config(
        self,
    ) -> Callable[
        [gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCertificateIssuanceConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateMapRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCertificateMap(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateMapEntryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCertificateMapEntry(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.UpdateDnsAuthorizationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDnsAuthorization(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_trust_config(
        self,
    ) -> Callable[
        [gcc_trust_config.UpdateTrustConfigRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTrustConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseCertificateManagerRestTransport._BaseGetLocation,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCertificateManagerRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
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
        _BaseCertificateManagerRestTransport._BaseListLocations,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCertificateManagerRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
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
        _BaseCertificateManagerRestTransport._BaseCancelOperation,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCertificateManagerRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._CancelOperation._get_response(
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
        _BaseCertificateManagerRestTransport._BaseDeleteOperation,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCertificateManagerRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._DeleteOperation._get_response(
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
        _BaseCertificateManagerRestTransport._BaseGetOperation,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCertificateManagerRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
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
        _BaseCertificateManagerRestTransport._BaseListOperations,
        CertificateManagerRestStub,
    ):
        def __hash__(self):
            return hash("CertificateManagerRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCertificateManagerRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCertificateManagerRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.certificatemanager_v1.CertificateManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CertificateManagerRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.certificatemanager_v1.CertificateManagerAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.certificatemanager.v1.CertificateManager",
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


__all__ = ("CertificateManagerRestTransport",)
