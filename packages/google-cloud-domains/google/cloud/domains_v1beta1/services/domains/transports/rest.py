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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.domains_v1beta1._compat import transcode_request
from google.cloud.domains_v1beta1.types import domains

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDomainsRestTransport

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


class DomainsRestInterceptor:
    """Interceptor for Domains.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DomainsRestTransport.

    .. code-block:: python
        class MyCustomDomainsInterceptor(DomainsRestInterceptor):
            def pre_configure_contact_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_configure_contact_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_configure_dns_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_configure_dns_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_configure_management_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_configure_management_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_registration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_registration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_registration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_registration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_registration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_registration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_registrations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_registrations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_register_domain(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_register_domain(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_authorization_code(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_authorization_code(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retrieve_authorization_code(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retrieve_authorization_code(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retrieve_register_parameters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retrieve_register_parameters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retrieve_transfer_parameters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retrieve_transfer_parameters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_domains(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_domains(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_transfer_domain(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_transfer_domain(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_registration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_registration(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DomainsRestTransport(interceptor=MyCustomDomainsInterceptor())
        client = DomainsClient(transport=transport)


    """

    def pre_configure_contact_settings(
        self,
        request: domains.ConfigureContactSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ConfigureContactSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for configure_contact_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_configure_contact_settings(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for configure_contact_settings

        DEPRECATED. Please use the `post_configure_contact_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_configure_contact_settings` interceptor runs
        before the `post_configure_contact_settings_with_metadata` interceptor.
        """
        return response

    def post_configure_contact_settings_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for configure_contact_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_configure_contact_settings_with_metadata`
        interceptor in new development instead of the `post_configure_contact_settings` interceptor.
        When both interceptors are used, this `post_configure_contact_settings_with_metadata` interceptor runs after the
        `post_configure_contact_settings` interceptor. The (possibly modified) response returned by
        `post_configure_contact_settings` will be passed to
        `post_configure_contact_settings_with_metadata`.
        """
        return response, metadata

    def pre_configure_dns_settings(
        self,
        request: domains.ConfigureDnsSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ConfigureDnsSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for configure_dns_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_configure_dns_settings(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for configure_dns_settings

        DEPRECATED. Please use the `post_configure_dns_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_configure_dns_settings` interceptor runs
        before the `post_configure_dns_settings_with_metadata` interceptor.
        """
        return response

    def post_configure_dns_settings_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for configure_dns_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_configure_dns_settings_with_metadata`
        interceptor in new development instead of the `post_configure_dns_settings` interceptor.
        When both interceptors are used, this `post_configure_dns_settings_with_metadata` interceptor runs after the
        `post_configure_dns_settings` interceptor. The (possibly modified) response returned by
        `post_configure_dns_settings` will be passed to
        `post_configure_dns_settings_with_metadata`.
        """
        return response, metadata

    def pre_configure_management_settings(
        self,
        request: domains.ConfigureManagementSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ConfigureManagementSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for configure_management_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_configure_management_settings(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for configure_management_settings

        DEPRECATED. Please use the `post_configure_management_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_configure_management_settings` interceptor runs
        before the `post_configure_management_settings_with_metadata` interceptor.
        """
        return response

    def post_configure_management_settings_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for configure_management_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_configure_management_settings_with_metadata`
        interceptor in new development instead of the `post_configure_management_settings` interceptor.
        When both interceptors are used, this `post_configure_management_settings_with_metadata` interceptor runs after the
        `post_configure_management_settings` interceptor. The (possibly modified) response returned by
        `post_configure_management_settings` will be passed to
        `post_configure_management_settings_with_metadata`.
        """
        return response, metadata

    def pre_delete_registration(
        self,
        request: domains.DeleteRegistrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.DeleteRegistrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_delete_registration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_registration

        DEPRECATED. Please use the `post_delete_registration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_delete_registration` interceptor runs
        before the `post_delete_registration_with_metadata` interceptor.
        """
        return response

    def post_delete_registration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_registration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_delete_registration_with_metadata`
        interceptor in new development instead of the `post_delete_registration` interceptor.
        When both interceptors are used, this `post_delete_registration_with_metadata` interceptor runs after the
        `post_delete_registration` interceptor. The (possibly modified) response returned by
        `post_delete_registration` will be passed to
        `post_delete_registration_with_metadata`.
        """
        return response, metadata

    def pre_export_registration(
        self,
        request: domains.ExportRegistrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ExportRegistrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_export_registration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_registration

        DEPRECATED. Please use the `post_export_registration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_export_registration` interceptor runs
        before the `post_export_registration_with_metadata` interceptor.
        """
        return response

    def post_export_registration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_registration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_export_registration_with_metadata`
        interceptor in new development instead of the `post_export_registration` interceptor.
        When both interceptors are used, this `post_export_registration_with_metadata` interceptor runs after the
        `post_export_registration` interceptor. The (possibly modified) response returned by
        `post_export_registration` will be passed to
        `post_export_registration_with_metadata`.
        """
        return response, metadata

    def pre_get_registration(
        self,
        request: domains.GetRegistrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.GetRegistrationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_get_registration(
        self, response: domains.Registration
    ) -> domains.Registration:
        """Post-rpc interceptor for get_registration

        DEPRECATED. Please use the `post_get_registration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_get_registration` interceptor runs
        before the `post_get_registration_with_metadata` interceptor.
        """
        return response

    def post_get_registration_with_metadata(
        self,
        response: domains.Registration,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.Registration, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_registration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_get_registration_with_metadata`
        interceptor in new development instead of the `post_get_registration` interceptor.
        When both interceptors are used, this `post_get_registration_with_metadata` interceptor runs after the
        `post_get_registration` interceptor. The (possibly modified) response returned by
        `post_get_registration` will be passed to
        `post_get_registration_with_metadata`.
        """
        return response, metadata

    def pre_list_registrations(
        self,
        request: domains.ListRegistrationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ListRegistrationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_registrations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_list_registrations(
        self, response: domains.ListRegistrationsResponse
    ) -> domains.ListRegistrationsResponse:
        """Post-rpc interceptor for list_registrations

        DEPRECATED. Please use the `post_list_registrations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_list_registrations` interceptor runs
        before the `post_list_registrations_with_metadata` interceptor.
        """
        return response

    def post_list_registrations_with_metadata(
        self,
        response: domains.ListRegistrationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ListRegistrationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_registrations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_list_registrations_with_metadata`
        interceptor in new development instead of the `post_list_registrations` interceptor.
        When both interceptors are used, this `post_list_registrations_with_metadata` interceptor runs after the
        `post_list_registrations` interceptor. The (possibly modified) response returned by
        `post_list_registrations` will be passed to
        `post_list_registrations_with_metadata`.
        """
        return response, metadata

    def pre_register_domain(
        self,
        request: domains.RegisterDomainRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.RegisterDomainRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for register_domain

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_register_domain(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for register_domain

        DEPRECATED. Please use the `post_register_domain_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_register_domain` interceptor runs
        before the `post_register_domain_with_metadata` interceptor.
        """
        return response

    def post_register_domain_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for register_domain

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_register_domain_with_metadata`
        interceptor in new development instead of the `post_register_domain` interceptor.
        When both interceptors are used, this `post_register_domain_with_metadata` interceptor runs after the
        `post_register_domain` interceptor. The (possibly modified) response returned by
        `post_register_domain` will be passed to
        `post_register_domain_with_metadata`.
        """
        return response, metadata

    def pre_reset_authorization_code(
        self,
        request: domains.ResetAuthorizationCodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.ResetAuthorizationCodeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reset_authorization_code

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_reset_authorization_code(
        self, response: domains.AuthorizationCode
    ) -> domains.AuthorizationCode:
        """Post-rpc interceptor for reset_authorization_code

        DEPRECATED. Please use the `post_reset_authorization_code_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_reset_authorization_code` interceptor runs
        before the `post_reset_authorization_code_with_metadata` interceptor.
        """
        return response

    def post_reset_authorization_code_with_metadata(
        self,
        response: domains.AuthorizationCode,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.AuthorizationCode, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_authorization_code

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_reset_authorization_code_with_metadata`
        interceptor in new development instead of the `post_reset_authorization_code` interceptor.
        When both interceptors are used, this `post_reset_authorization_code_with_metadata` interceptor runs after the
        `post_reset_authorization_code` interceptor. The (possibly modified) response returned by
        `post_reset_authorization_code` will be passed to
        `post_reset_authorization_code_with_metadata`.
        """
        return response, metadata

    def pre_retrieve_authorization_code(
        self,
        request: domains.RetrieveAuthorizationCodeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.RetrieveAuthorizationCodeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for retrieve_authorization_code

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_retrieve_authorization_code(
        self, response: domains.AuthorizationCode
    ) -> domains.AuthorizationCode:
        """Post-rpc interceptor for retrieve_authorization_code

        DEPRECATED. Please use the `post_retrieve_authorization_code_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_retrieve_authorization_code` interceptor runs
        before the `post_retrieve_authorization_code_with_metadata` interceptor.
        """
        return response

    def post_retrieve_authorization_code_with_metadata(
        self,
        response: domains.AuthorizationCode,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.AuthorizationCode, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for retrieve_authorization_code

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_retrieve_authorization_code_with_metadata`
        interceptor in new development instead of the `post_retrieve_authorization_code` interceptor.
        When both interceptors are used, this `post_retrieve_authorization_code_with_metadata` interceptor runs after the
        `post_retrieve_authorization_code` interceptor. The (possibly modified) response returned by
        `post_retrieve_authorization_code` will be passed to
        `post_retrieve_authorization_code_with_metadata`.
        """
        return response, metadata

    def pre_retrieve_register_parameters(
        self,
        request: domains.RetrieveRegisterParametersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.RetrieveRegisterParametersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for retrieve_register_parameters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_retrieve_register_parameters(
        self, response: domains.RetrieveRegisterParametersResponse
    ) -> domains.RetrieveRegisterParametersResponse:
        """Post-rpc interceptor for retrieve_register_parameters

        DEPRECATED. Please use the `post_retrieve_register_parameters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_retrieve_register_parameters` interceptor runs
        before the `post_retrieve_register_parameters_with_metadata` interceptor.
        """
        return response

    def post_retrieve_register_parameters_with_metadata(
        self,
        response: domains.RetrieveRegisterParametersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.RetrieveRegisterParametersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for retrieve_register_parameters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_retrieve_register_parameters_with_metadata`
        interceptor in new development instead of the `post_retrieve_register_parameters` interceptor.
        When both interceptors are used, this `post_retrieve_register_parameters_with_metadata` interceptor runs after the
        `post_retrieve_register_parameters` interceptor. The (possibly modified) response returned by
        `post_retrieve_register_parameters` will be passed to
        `post_retrieve_register_parameters_with_metadata`.
        """
        return response, metadata

    def pre_retrieve_transfer_parameters(
        self,
        request: domains.RetrieveTransferParametersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.RetrieveTransferParametersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for retrieve_transfer_parameters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_retrieve_transfer_parameters(
        self, response: domains.RetrieveTransferParametersResponse
    ) -> domains.RetrieveTransferParametersResponse:
        """Post-rpc interceptor for retrieve_transfer_parameters

        DEPRECATED. Please use the `post_retrieve_transfer_parameters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_retrieve_transfer_parameters` interceptor runs
        before the `post_retrieve_transfer_parameters_with_metadata` interceptor.
        """
        return response

    def post_retrieve_transfer_parameters_with_metadata(
        self,
        response: domains.RetrieveTransferParametersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.RetrieveTransferParametersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for retrieve_transfer_parameters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_retrieve_transfer_parameters_with_metadata`
        interceptor in new development instead of the `post_retrieve_transfer_parameters` interceptor.
        When both interceptors are used, this `post_retrieve_transfer_parameters_with_metadata` interceptor runs after the
        `post_retrieve_transfer_parameters` interceptor. The (possibly modified) response returned by
        `post_retrieve_transfer_parameters` will be passed to
        `post_retrieve_transfer_parameters_with_metadata`.
        """
        return response, metadata

    def pre_search_domains(
        self,
        request: domains.SearchDomainsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.SearchDomainsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_domains

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_search_domains(
        self, response: domains.SearchDomainsResponse
    ) -> domains.SearchDomainsResponse:
        """Post-rpc interceptor for search_domains

        DEPRECATED. Please use the `post_search_domains_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_search_domains` interceptor runs
        before the `post_search_domains_with_metadata` interceptor.
        """
        return response

    def post_search_domains_with_metadata(
        self,
        response: domains.SearchDomainsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.SearchDomainsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_domains

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_search_domains_with_metadata`
        interceptor in new development instead of the `post_search_domains` interceptor.
        When both interceptors are used, this `post_search_domains_with_metadata` interceptor runs after the
        `post_search_domains` interceptor. The (possibly modified) response returned by
        `post_search_domains` will be passed to
        `post_search_domains_with_metadata`.
        """
        return response, metadata

    def pre_transfer_domain(
        self,
        request: domains.TransferDomainRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[domains.TransferDomainRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for transfer_domain

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_transfer_domain(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for transfer_domain

        DEPRECATED. Please use the `post_transfer_domain_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_transfer_domain` interceptor runs
        before the `post_transfer_domain_with_metadata` interceptor.
        """
        return response

    def post_transfer_domain_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for transfer_domain

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_transfer_domain_with_metadata`
        interceptor in new development instead of the `post_transfer_domain` interceptor.
        When both interceptors are used, this `post_transfer_domain_with_metadata` interceptor runs after the
        `post_transfer_domain` interceptor. The (possibly modified) response returned by
        `post_transfer_domain` will be passed to
        `post_transfer_domain_with_metadata`.
        """
        return response, metadata

    def pre_update_registration(
        self,
        request: domains.UpdateRegistrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        domains.UpdateRegistrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Domains server.
        """
        return request, metadata

    def post_update_registration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_registration

        DEPRECATED. Please use the `post_update_registration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Domains server but before
        it is returned to user code. This `post_update_registration` interceptor runs
        before the `post_update_registration_with_metadata` interceptor.
        """
        return response

    def post_update_registration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_registration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Domains server but before it is returned to user code.

        We recommend only using this `post_update_registration_with_metadata`
        interceptor in new development instead of the `post_update_registration` interceptor.
        When both interceptors are used, this `post_update_registration_with_metadata` interceptor runs after the
        `post_update_registration` interceptor. The (possibly modified) response returned by
        `post_update_registration` will be passed to
        `post_update_registration_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DomainsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DomainsRestInterceptor


class DomainsRestTransport(_BaseDomainsRestTransport):
    """REST backend synchronous transport for Domains.

    The Cloud Domains API enables management and configuration of
    domain names.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "domains.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DomainsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'domains.googleapis.com').
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
            interceptor (Optional[DomainsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DomainsRestInterceptor()
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
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _ConfigureContactSettings(
        _BaseDomainsRestTransport._BaseConfigureContactSettings, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.ConfigureContactSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.ConfigureContactSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the configure contact
            settings method over HTTP.

                Args:
                    request (~.domains.ConfigureContactSettingsRequest):
                        The request object. Request for the ``ConfigureContactSettings`` method.
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

            http_options = _BaseDomainsRestTransport._BaseConfigureContactSettings._get_http_options()
            request, metadata = self._interceptor.pre_configure_contact_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseConfigureContactSettings,
                    "_BaseConfigureContactSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.ConfigureContactSettings",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ConfigureContactSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._ConfigureContactSettings._get_response(
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

            resp = self._interceptor.post_configure_contact_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_configure_contact_settings_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.configure_contact_settings",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ConfigureContactSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ConfigureDnsSettings(
        _BaseDomainsRestTransport._BaseConfigureDnsSettings, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.ConfigureDnsSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.ConfigureDnsSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the configure dns settings method over HTTP.

            Args:
                request (~.domains.ConfigureDnsSettingsRequest):
                    The request object. Request for the ``ConfigureDnsSettings`` method.
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
                _BaseDomainsRestTransport._BaseConfigureDnsSettings._get_http_options()
            )
            request, metadata = self._interceptor.pre_configure_dns_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseConfigureDnsSettings,
                    "_BaseConfigureDnsSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.ConfigureDnsSettings",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ConfigureDnsSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._ConfigureDnsSettings._get_response(
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

            resp = self._interceptor.post_configure_dns_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_configure_dns_settings_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.configure_dns_settings",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ConfigureDnsSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ConfigureManagementSettings(
        _BaseDomainsRestTransport._BaseConfigureManagementSettings, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.ConfigureManagementSettings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.ConfigureManagementSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the configure management
            settings method over HTTP.

                Args:
                    request (~.domains.ConfigureManagementSettingsRequest):
                        The request object. Request for the ``ConfigureManagementSettings`` method.
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

            http_options = _BaseDomainsRestTransport._BaseConfigureManagementSettings._get_http_options()
            request, metadata = self._interceptor.pre_configure_management_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseConfigureManagementSettings,
                    "_BaseConfigureManagementSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.ConfigureManagementSettings",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ConfigureManagementSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._ConfigureManagementSettings._get_response(
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

            resp = self._interceptor.post_configure_management_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_configure_management_settings_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.configure_management_settings",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ConfigureManagementSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRegistration(
        _BaseDomainsRestTransport._BaseDeleteRegistration, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.DeleteRegistration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.DeleteRegistrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete registration method over HTTP.

            Args:
                request (~.domains.DeleteRegistrationRequest):
                    The request object. Request for the ``DeleteRegistration`` method.
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
                _BaseDomainsRestTransport._BaseDeleteRegistration._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_registration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseDeleteRegistration,
                    "_BaseDeleteRegistration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.DeleteRegistration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "DeleteRegistration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._DeleteRegistration._get_response(
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

            resp = self._interceptor.post_delete_registration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_registration_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.delete_registration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "DeleteRegistration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportRegistration(
        _BaseDomainsRestTransport._BaseExportRegistration, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.ExportRegistration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.ExportRegistrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export registration method over HTTP.

            Args:
                request (~.domains.ExportRegistrationRequest):
                    The request object. Request for the ``ExportRegistration`` method.
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
                _BaseDomainsRestTransport._BaseExportRegistration._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_registration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseExportRegistration,
                    "_BaseExportRegistration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.ExportRegistration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ExportRegistration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._ExportRegistration._get_response(
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

            resp = self._interceptor.post_export_registration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_registration_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.export_registration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ExportRegistration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRegistration(
        _BaseDomainsRestTransport._BaseGetRegistration, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.GetRegistration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.GetRegistrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.Registration:
            r"""Call the get registration method over HTTP.

            Args:
                request (~.domains.GetRegistrationRequest):
                    The request object. Request for the ``GetRegistration`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.domains.Registration:
                    The ``Registration`` resource facilitates managing and
                configuring domain name registrations.

                There are several ways to create a new ``Registration``
                resource:

                To create a new ``Registration`` resource, find a
                suitable domain name by calling the ``SearchDomains``
                method with a query to see available domain name
                options. After choosing a name, call
                ``RetrieveRegisterParameters`` to ensure availability
                and obtain information like pricing, which is needed to
                build a call to ``RegisterDomain``.

                Another way to create a new ``Registration`` is to
                transfer an existing domain from another registrar.
                First, go to the current registrar to unlock the domain
                for transfer and retrieve the domain's transfer
                authorization code. Then call
                ``RetrieveTransferParameters`` to confirm that the
                domain is unlocked and to get values needed to build a
                call to ``TransferDomain``.

            """

            http_options = (
                _BaseDomainsRestTransport._BaseGetRegistration._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_registration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseGetRegistration,
                    "_BaseGetRegistration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.GetRegistration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "GetRegistration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._GetRegistration._get_response(
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
            resp = domains.Registration()
            pb_resp = domains.Registration.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_registration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_registration_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = domains.Registration.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.get_registration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "GetRegistration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRegistrations(
        _BaseDomainsRestTransport._BaseListRegistrations, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.ListRegistrations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.ListRegistrationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.ListRegistrationsResponse:
            r"""Call the list registrations method over HTTP.

            Args:
                request (~.domains.ListRegistrationsRequest):
                    The request object. Request for the ``ListRegistrations`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.domains.ListRegistrationsResponse:
                    Response for the ``ListRegistrations`` method.
            """

            http_options = (
                _BaseDomainsRestTransport._BaseListRegistrations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_registrations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseListRegistrations,
                    "_BaseListRegistrations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.ListRegistrations",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ListRegistrations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._ListRegistrations._get_response(
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
            resp = domains.ListRegistrationsResponse()
            pb_resp = domains.ListRegistrationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_registrations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_registrations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = domains.ListRegistrationsResponse.to_json(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.list_registrations",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ListRegistrations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RegisterDomain(
        _BaseDomainsRestTransport._BaseRegisterDomain, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.RegisterDomain")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.RegisterDomainRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the register domain method over HTTP.

            Args:
                request (~.domains.RegisterDomainRequest):
                    The request object. Request for the ``RegisterDomain`` method.
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
                _BaseDomainsRestTransport._BaseRegisterDomain._get_http_options()
            )
            request, metadata = self._interceptor.pre_register_domain(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseRegisterDomain,
                    "_BaseRegisterDomain__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.RegisterDomain",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RegisterDomain",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._RegisterDomain._get_response(
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

            resp = self._interceptor.post_register_domain(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_register_domain_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.register_domain",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RegisterDomain",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetAuthorizationCode(
        _BaseDomainsRestTransport._BaseResetAuthorizationCode, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.ResetAuthorizationCode")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.ResetAuthorizationCodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.AuthorizationCode:
            r"""Call the reset authorization code method over HTTP.

            Args:
                request (~.domains.ResetAuthorizationCodeRequest):
                    The request object. Request for the ``ResetAuthorizationCode`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.domains.AuthorizationCode:
                    Defines an authorization code.
            """

            http_options = _BaseDomainsRestTransport._BaseResetAuthorizationCode._get_http_options()
            request, metadata = self._interceptor.pre_reset_authorization_code(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseResetAuthorizationCode,
                    "_BaseResetAuthorizationCode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.ResetAuthorizationCode",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ResetAuthorizationCode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._ResetAuthorizationCode._get_response(
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
            resp = domains.AuthorizationCode()
            pb_resp = domains.AuthorizationCode.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reset_authorization_code(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_authorization_code_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = domains.AuthorizationCode.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.reset_authorization_code",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "ResetAuthorizationCode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetrieveAuthorizationCode(
        _BaseDomainsRestTransport._BaseRetrieveAuthorizationCode, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.RetrieveAuthorizationCode")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.RetrieveAuthorizationCodeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.AuthorizationCode:
            r"""Call the retrieve authorization
            code method over HTTP.

                Args:
                    request (~.domains.RetrieveAuthorizationCodeRequest):
                        The request object. Request for the ``RetrieveAuthorizationCode`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.domains.AuthorizationCode:
                        Defines an authorization code.
            """

            http_options = _BaseDomainsRestTransport._BaseRetrieveAuthorizationCode._get_http_options()
            request, metadata = self._interceptor.pre_retrieve_authorization_code(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseRetrieveAuthorizationCode,
                    "_BaseRetrieveAuthorizationCode__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.RetrieveAuthorizationCode",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RetrieveAuthorizationCode",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._RetrieveAuthorizationCode._get_response(
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
            resp = domains.AuthorizationCode()
            pb_resp = domains.AuthorizationCode.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retrieve_authorization_code(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retrieve_authorization_code_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = domains.AuthorizationCode.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.retrieve_authorization_code",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RetrieveAuthorizationCode",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetrieveRegisterParameters(
        _BaseDomainsRestTransport._BaseRetrieveRegisterParameters, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.RetrieveRegisterParameters")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.RetrieveRegisterParametersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.RetrieveRegisterParametersResponse:
            r"""Call the retrieve register
            parameters method over HTTP.

                Args:
                    request (~.domains.RetrieveRegisterParametersRequest):
                        The request object. Request for the ``RetrieveRegisterParameters`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.domains.RetrieveRegisterParametersResponse:
                        Response for the ``RetrieveRegisterParameters`` method.
            """

            http_options = _BaseDomainsRestTransport._BaseRetrieveRegisterParameters._get_http_options()
            request, metadata = self._interceptor.pre_retrieve_register_parameters(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseRetrieveRegisterParameters,
                    "_BaseRetrieveRegisterParameters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.RetrieveRegisterParameters",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RetrieveRegisterParameters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._RetrieveRegisterParameters._get_response(
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
            resp = domains.RetrieveRegisterParametersResponse()
            pb_resp = domains.RetrieveRegisterParametersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retrieve_register_parameters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retrieve_register_parameters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        domains.RetrieveRegisterParametersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.retrieve_register_parameters",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RetrieveRegisterParameters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetrieveTransferParameters(
        _BaseDomainsRestTransport._BaseRetrieveTransferParameters, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.RetrieveTransferParameters")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.RetrieveTransferParametersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.RetrieveTransferParametersResponse:
            r"""Call the retrieve transfer
            parameters method over HTTP.

                Args:
                    request (~.domains.RetrieveTransferParametersRequest):
                        The request object. Request for the ``RetrieveTransferParameters`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.domains.RetrieveTransferParametersResponse:
                        Response for the ``RetrieveTransferParameters`` method.
            """

            http_options = _BaseDomainsRestTransport._BaseRetrieveTransferParameters._get_http_options()
            request, metadata = self._interceptor.pre_retrieve_transfer_parameters(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseRetrieveTransferParameters,
                    "_BaseRetrieveTransferParameters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.RetrieveTransferParameters",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RetrieveTransferParameters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._RetrieveTransferParameters._get_response(
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
            resp = domains.RetrieveTransferParametersResponse()
            pb_resp = domains.RetrieveTransferParametersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retrieve_transfer_parameters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retrieve_transfer_parameters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        domains.RetrieveTransferParametersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.retrieve_transfer_parameters",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "RetrieveTransferParameters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchDomains(_BaseDomainsRestTransport._BaseSearchDomains, DomainsRestStub):
        def __hash__(self):
            return hash("DomainsRestTransport.SearchDomains")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.SearchDomainsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> domains.SearchDomainsResponse:
            r"""Call the search domains method over HTTP.

            Args:
                request (~.domains.SearchDomainsRequest):
                    The request object. Request for the ``SearchDomains`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.domains.SearchDomainsResponse:
                    Response for the ``SearchDomains`` method.
            """

            http_options = (
                _BaseDomainsRestTransport._BaseSearchDomains._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_domains(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseSearchDomains,
                    "_BaseSearchDomains__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.SearchDomains",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "SearchDomains",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._SearchDomains._get_response(
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
            resp = domains.SearchDomainsResponse()
            pb_resp = domains.SearchDomainsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_domains(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_domains_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = domains.SearchDomainsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.search_domains",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "SearchDomains",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TransferDomain(
        _BaseDomainsRestTransport._BaseTransferDomain, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.TransferDomain")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.TransferDomainRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the transfer domain method over HTTP.

            Args:
                request (~.domains.TransferDomainRequest):
                    The request object. Request for the ``TransferDomain`` method.
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
                _BaseDomainsRestTransport._BaseTransferDomain._get_http_options()
            )
            request, metadata = self._interceptor.pre_transfer_domain(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseTransferDomain,
                    "_BaseTransferDomain__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.TransferDomain",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "TransferDomain",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._TransferDomain._get_response(
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

            resp = self._interceptor.post_transfer_domain(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_transfer_domain_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.transfer_domain",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "TransferDomain",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRegistration(
        _BaseDomainsRestTransport._BaseUpdateRegistration, DomainsRestStub
    ):
        def __hash__(self):
            return hash("DomainsRestTransport.UpdateRegistration")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: domains.UpdateRegistrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update registration method over HTTP.

            Args:
                request (~.domains.UpdateRegistrationRequest):
                    The request object. Request for the ``UpdateRegistration`` method.
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
                _BaseDomainsRestTransport._BaseUpdateRegistration._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_registration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDomainsRestTransport._BaseUpdateRegistration,
                    "_BaseUpdateRegistration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.domains_v1beta1.DomainsClient.UpdateRegistration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "UpdateRegistration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DomainsRestTransport._UpdateRegistration._get_response(
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

            resp = self._interceptor.post_update_registration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_registration_with_metadata(
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
                    "Received response for google.cloud.domains_v1beta1.DomainsClient.update_registration",
                    extra={
                        "serviceName": "google.cloud.domains.v1beta1.Domains",
                        "rpcName": "UpdateRegistration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def configure_contact_settings(
        self,
    ) -> Callable[[domains.ConfigureContactSettingsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ConfigureContactSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def configure_dns_settings(
        self,
    ) -> Callable[[domains.ConfigureDnsSettingsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ConfigureDnsSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def configure_management_settings(
        self,
    ) -> Callable[
        [domains.ConfigureManagementSettingsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ConfigureManagementSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_registration(
        self,
    ) -> Callable[[domains.DeleteRegistrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRegistration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_registration(
        self,
    ) -> Callable[[domains.ExportRegistrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportRegistration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_registration(
        self,
    ) -> Callable[[domains.GetRegistrationRequest], domains.Registration]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRegistration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_registrations(
        self,
    ) -> Callable[
        [domains.ListRegistrationsRequest], domains.ListRegistrationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRegistrations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def register_domain(
        self,
    ) -> Callable[[domains.RegisterDomainRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RegisterDomain(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_authorization_code(
        self,
    ) -> Callable[[domains.ResetAuthorizationCodeRequest], domains.AuthorizationCode]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetAuthorizationCode(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def retrieve_authorization_code(
        self,
    ) -> Callable[
        [domains.RetrieveAuthorizationCodeRequest], domains.AuthorizationCode
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetrieveAuthorizationCode(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def retrieve_register_parameters(
        self,
    ) -> Callable[
        [domains.RetrieveRegisterParametersRequest],
        domains.RetrieveRegisterParametersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetrieveRegisterParameters(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def retrieve_transfer_parameters(
        self,
    ) -> Callable[
        [domains.RetrieveTransferParametersRequest],
        domains.RetrieveTransferParametersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetrieveTransferParameters(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_domains(
        self,
    ) -> Callable[[domains.SearchDomainsRequest], domains.SearchDomainsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchDomains(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def transfer_domain(
        self,
    ) -> Callable[[domains.TransferDomainRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TransferDomain(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_registration(
        self,
    ) -> Callable[[domains.UpdateRegistrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRegistration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DomainsRestTransport",)
