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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import custom_field_messages, custom_field_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCustomFieldServiceRestTransport

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


class CustomFieldServiceRestInterceptor:
    """Interceptor for CustomFieldService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CustomFieldServiceRestTransport.

    .. code-block:: python
        class MyCustomCustomFieldServiceInterceptor(CustomFieldServiceRestInterceptor):
            def pre_batch_activate_custom_fields(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_custom_fields(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_custom_fields(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_custom_fields(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_custom_fields(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_custom_fields(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_custom_fields(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_custom_fields(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_custom_field(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_field(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_custom_field(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_field(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_fields(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_fields(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_field(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_field(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CustomFieldServiceRestTransport(interceptor=MyCustomCustomFieldServiceInterceptor())
        client = CustomFieldServiceClient(transport=transport)


    """

    def pre_batch_activate_custom_fields(
        self,
        request: custom_field_service.BatchActivateCustomFieldsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchActivateCustomFieldsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_custom_fields

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_batch_activate_custom_fields(
        self, response: custom_field_service.BatchActivateCustomFieldsResponse
    ) -> custom_field_service.BatchActivateCustomFieldsResponse:
        """Post-rpc interceptor for batch_activate_custom_fields

        DEPRECATED. Please use the `post_batch_activate_custom_fields_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_batch_activate_custom_fields` interceptor runs
        before the `post_batch_activate_custom_fields_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_custom_fields_with_metadata(
        self,
        response: custom_field_service.BatchActivateCustomFieldsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchActivateCustomFieldsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_custom_fields

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_custom_fields_with_metadata`
        interceptor in new development instead of the `post_batch_activate_custom_fields` interceptor.
        When both interceptors are used, this `post_batch_activate_custom_fields_with_metadata` interceptor runs after the
        `post_batch_activate_custom_fields` interceptor. The (possibly modified) response returned by
        `post_batch_activate_custom_fields` will be passed to
        `post_batch_activate_custom_fields_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_custom_fields(
        self,
        request: custom_field_service.BatchCreateCustomFieldsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchCreateCustomFieldsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_custom_fields

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_batch_create_custom_fields(
        self, response: custom_field_service.BatchCreateCustomFieldsResponse
    ) -> custom_field_service.BatchCreateCustomFieldsResponse:
        """Post-rpc interceptor for batch_create_custom_fields

        DEPRECATED. Please use the `post_batch_create_custom_fields_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_batch_create_custom_fields` interceptor runs
        before the `post_batch_create_custom_fields_with_metadata` interceptor.
        """
        return response

    def post_batch_create_custom_fields_with_metadata(
        self,
        response: custom_field_service.BatchCreateCustomFieldsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchCreateCustomFieldsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_custom_fields

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_batch_create_custom_fields_with_metadata`
        interceptor in new development instead of the `post_batch_create_custom_fields` interceptor.
        When both interceptors are used, this `post_batch_create_custom_fields_with_metadata` interceptor runs after the
        `post_batch_create_custom_fields` interceptor. The (possibly modified) response returned by
        `post_batch_create_custom_fields` will be passed to
        `post_batch_create_custom_fields_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_custom_fields(
        self,
        request: custom_field_service.BatchDeactivateCustomFieldsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchDeactivateCustomFieldsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_custom_fields

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_batch_deactivate_custom_fields(
        self, response: custom_field_service.BatchDeactivateCustomFieldsResponse
    ) -> custom_field_service.BatchDeactivateCustomFieldsResponse:
        """Post-rpc interceptor for batch_deactivate_custom_fields

        DEPRECATED. Please use the `post_batch_deactivate_custom_fields_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_batch_deactivate_custom_fields` interceptor runs
        before the `post_batch_deactivate_custom_fields_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_custom_fields_with_metadata(
        self,
        response: custom_field_service.BatchDeactivateCustomFieldsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchDeactivateCustomFieldsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_custom_fields

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_custom_fields_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_custom_fields` interceptor.
        When both interceptors are used, this `post_batch_deactivate_custom_fields_with_metadata` interceptor runs after the
        `post_batch_deactivate_custom_fields` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_custom_fields` will be passed to
        `post_batch_deactivate_custom_fields_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_custom_fields(
        self,
        request: custom_field_service.BatchUpdateCustomFieldsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchUpdateCustomFieldsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_custom_fields

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_batch_update_custom_fields(
        self, response: custom_field_service.BatchUpdateCustomFieldsResponse
    ) -> custom_field_service.BatchUpdateCustomFieldsResponse:
        """Post-rpc interceptor for batch_update_custom_fields

        DEPRECATED. Please use the `post_batch_update_custom_fields_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_batch_update_custom_fields` interceptor runs
        before the `post_batch_update_custom_fields_with_metadata` interceptor.
        """
        return response

    def post_batch_update_custom_fields_with_metadata(
        self,
        response: custom_field_service.BatchUpdateCustomFieldsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.BatchUpdateCustomFieldsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_custom_fields

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_batch_update_custom_fields_with_metadata`
        interceptor in new development instead of the `post_batch_update_custom_fields` interceptor.
        When both interceptors are used, this `post_batch_update_custom_fields_with_metadata` interceptor runs after the
        `post_batch_update_custom_fields` interceptor. The (possibly modified) response returned by
        `post_batch_update_custom_fields` will be passed to
        `post_batch_update_custom_fields_with_metadata`.
        """
        return response, metadata

    def pre_create_custom_field(
        self,
        request: custom_field_service.CreateCustomFieldRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.CreateCustomFieldRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_custom_field

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_create_custom_field(
        self, response: custom_field_messages.CustomField
    ) -> custom_field_messages.CustomField:
        """Post-rpc interceptor for create_custom_field

        DEPRECATED. Please use the `post_create_custom_field_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_create_custom_field` interceptor runs
        before the `post_create_custom_field_with_metadata` interceptor.
        """
        return response

    def post_create_custom_field_with_metadata(
        self,
        response: custom_field_messages.CustomField,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_messages.CustomField, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_custom_field

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_create_custom_field_with_metadata`
        interceptor in new development instead of the `post_create_custom_field` interceptor.
        When both interceptors are used, this `post_create_custom_field_with_metadata` interceptor runs after the
        `post_create_custom_field` interceptor. The (possibly modified) response returned by
        `post_create_custom_field` will be passed to
        `post_create_custom_field_with_metadata`.
        """
        return response, metadata

    def pre_get_custom_field(
        self,
        request: custom_field_service.GetCustomFieldRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.GetCustomFieldRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_custom_field

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_get_custom_field(
        self, response: custom_field_messages.CustomField
    ) -> custom_field_messages.CustomField:
        """Post-rpc interceptor for get_custom_field

        DEPRECATED. Please use the `post_get_custom_field_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_get_custom_field` interceptor runs
        before the `post_get_custom_field_with_metadata` interceptor.
        """
        return response

    def post_get_custom_field_with_metadata(
        self,
        response: custom_field_messages.CustomField,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_messages.CustomField, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_custom_field

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_get_custom_field_with_metadata`
        interceptor in new development instead of the `post_get_custom_field` interceptor.
        When both interceptors are used, this `post_get_custom_field_with_metadata` interceptor runs after the
        `post_get_custom_field` interceptor. The (possibly modified) response returned by
        `post_get_custom_field` will be passed to
        `post_get_custom_field_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_fields(
        self,
        request: custom_field_service.ListCustomFieldsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.ListCustomFieldsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_custom_fields

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_list_custom_fields(
        self, response: custom_field_service.ListCustomFieldsResponse
    ) -> custom_field_service.ListCustomFieldsResponse:
        """Post-rpc interceptor for list_custom_fields

        DEPRECATED. Please use the `post_list_custom_fields_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_list_custom_fields` interceptor runs
        before the `post_list_custom_fields_with_metadata` interceptor.
        """
        return response

    def post_list_custom_fields_with_metadata(
        self,
        response: custom_field_service.ListCustomFieldsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.ListCustomFieldsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_custom_fields

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_list_custom_fields_with_metadata`
        interceptor in new development instead of the `post_list_custom_fields` interceptor.
        When both interceptors are used, this `post_list_custom_fields_with_metadata` interceptor runs after the
        `post_list_custom_fields` interceptor. The (possibly modified) response returned by
        `post_list_custom_fields` will be passed to
        `post_list_custom_fields_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_field(
        self,
        request: custom_field_service.UpdateCustomFieldRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_service.UpdateCustomFieldRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_custom_field

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_update_custom_field(
        self, response: custom_field_messages.CustomField
    ) -> custom_field_messages.CustomField:
        """Post-rpc interceptor for update_custom_field

        DEPRECATED. Please use the `post_update_custom_field_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code. This `post_update_custom_field` interceptor runs
        before the `post_update_custom_field_with_metadata` interceptor.
        """
        return response

    def post_update_custom_field_with_metadata(
        self,
        response: custom_field_messages.CustomField,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_field_messages.CustomField, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_custom_field

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomFieldService server but before it is returned to user code.

        We recommend only using this `post_update_custom_field_with_metadata`
        interceptor in new development instead of the `post_update_custom_field` interceptor.
        When both interceptors are used, this `post_update_custom_field_with_metadata` interceptor runs after the
        `post_update_custom_field` interceptor. The (possibly modified) response returned by
        `post_update_custom_field` will be passed to
        `post_update_custom_field_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CustomFieldService server but before
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
        before they are sent to the CustomFieldService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CustomFieldService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CustomFieldServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CustomFieldServiceRestInterceptor


class CustomFieldServiceRestTransport(_BaseCustomFieldServiceRestTransport):
    """REST backend synchronous transport for CustomFieldService.

    Provides methods for handling ``CustomField`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CustomFieldServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'admanager.googleapis.com').
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
            interceptor (Optional[CustomFieldServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CustomFieldServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCustomFields(
        _BaseCustomFieldServiceRestTransport._BaseBatchActivateCustomFields,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.BatchActivateCustomFields")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.BatchActivateCustomFieldsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_service.BatchActivateCustomFieldsResponse:
            r"""Call the batch activate custom
            fields method over HTTP.

                Args:
                    request (~.custom_field_service.BatchActivateCustomFieldsRequest):
                        The request object. Request message for ``BatchActivateCustomFields``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_field_service.BatchActivateCustomFieldsResponse:
                        Response object for ``BatchActivateCustomFields``
                    method.

            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseBatchActivateCustomFields._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_custom_fields(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseBatchActivateCustomFields,
                    "_BaseBatchActivateCustomFields__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.BatchActivateCustomFields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchActivateCustomFields",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._BatchActivateCustomFields._get_response(
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
            resp = custom_field_service.BatchActivateCustomFieldsResponse()
            pb_resp = custom_field_service.BatchActivateCustomFieldsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_custom_fields(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_custom_fields_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_field_service.BatchActivateCustomFieldsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.batch_activate_custom_fields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchActivateCustomFields",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateCustomFields(
        _BaseCustomFieldServiceRestTransport._BaseBatchCreateCustomFields,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.BatchCreateCustomFields")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.BatchCreateCustomFieldsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_service.BatchCreateCustomFieldsResponse:
            r"""Call the batch create custom
            fields method over HTTP.

                Args:
                    request (~.custom_field_service.BatchCreateCustomFieldsRequest):
                        The request object. Request object for ``BatchCreateCustomFields`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_field_service.BatchCreateCustomFieldsResponse:
                        Response object for ``BatchCreateCustomFields`` method.
            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseBatchCreateCustomFields._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_custom_fields(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseBatchCreateCustomFields,
                    "_BaseBatchCreateCustomFields__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.BatchCreateCustomFields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchCreateCustomFields",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CustomFieldServiceRestTransport._BatchCreateCustomFields._get_response(
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
            resp = custom_field_service.BatchCreateCustomFieldsResponse()
            pb_resp = custom_field_service.BatchCreateCustomFieldsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_custom_fields(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_custom_fields_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_field_service.BatchCreateCustomFieldsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.batch_create_custom_fields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchCreateCustomFields",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateCustomFields(
        _BaseCustomFieldServiceRestTransport._BaseBatchDeactivateCustomFields,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.BatchDeactivateCustomFields")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.BatchDeactivateCustomFieldsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_service.BatchDeactivateCustomFieldsResponse:
            r"""Call the batch deactivate custom
            fields method over HTTP.

                Args:
                    request (~.custom_field_service.BatchDeactivateCustomFieldsRequest):
                        The request object. Request message for ``BatchDeactivateCustomFields``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_field_service.BatchDeactivateCustomFieldsResponse:
                        Response object for ``BatchDeactivateCustomFields``
                    method.

            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseBatchDeactivateCustomFields._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_custom_fields(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseBatchDeactivateCustomFields,
                    "_BaseBatchDeactivateCustomFields__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.BatchDeactivateCustomFields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchDeactivateCustomFields",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._BatchDeactivateCustomFields._get_response(
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
            resp = custom_field_service.BatchDeactivateCustomFieldsResponse()
            pb_resp = custom_field_service.BatchDeactivateCustomFieldsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_custom_fields(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_custom_fields_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_field_service.BatchDeactivateCustomFieldsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.batch_deactivate_custom_fields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchDeactivateCustomFields",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateCustomFields(
        _BaseCustomFieldServiceRestTransport._BaseBatchUpdateCustomFields,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.BatchUpdateCustomFields")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.BatchUpdateCustomFieldsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_service.BatchUpdateCustomFieldsResponse:
            r"""Call the batch update custom
            fields method over HTTP.

                Args:
                    request (~.custom_field_service.BatchUpdateCustomFieldsRequest):
                        The request object. Request object for ``BatchUpdateCustomFields`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_field_service.BatchUpdateCustomFieldsResponse:
                        Response object for ``BatchUpdateCustomFields`` method.
            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseBatchUpdateCustomFields._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_custom_fields(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseBatchUpdateCustomFields,
                    "_BaseBatchUpdateCustomFields__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.BatchUpdateCustomFields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchUpdateCustomFields",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CustomFieldServiceRestTransport._BatchUpdateCustomFields._get_response(
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
            resp = custom_field_service.BatchUpdateCustomFieldsResponse()
            pb_resp = custom_field_service.BatchUpdateCustomFieldsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_custom_fields(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_custom_fields_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_field_service.BatchUpdateCustomFieldsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.batch_update_custom_fields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "BatchUpdateCustomFields",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCustomField(
        _BaseCustomFieldServiceRestTransport._BaseCreateCustomField,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.CreateCustomField")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.CreateCustomFieldRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_messages.CustomField:
            r"""Call the create custom field method over HTTP.

            Args:
                request (~.custom_field_service.CreateCustomFieldRequest):
                    The request object. Request object for ``CreateCustomField`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.custom_field_messages.CustomField:
                    An additional, user-created field on
                an entity.

            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseCreateCustomField._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_field(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseCreateCustomField,
                    "_BaseCreateCustomField__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.CreateCustomField",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "CreateCustomField",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._CreateCustomField._get_response(
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
            resp = custom_field_messages.CustomField()
            pb_resp = custom_field_messages.CustomField.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_custom_field(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_custom_field_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_field_messages.CustomField.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.create_custom_field",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "CreateCustomField",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCustomField(
        _BaseCustomFieldServiceRestTransport._BaseGetCustomField,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.GetCustomField")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.GetCustomFieldRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_messages.CustomField:
            r"""Call the get custom field method over HTTP.

            Args:
                request (~.custom_field_service.GetCustomFieldRequest):
                    The request object. Request object for ``GetCustomField`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.custom_field_messages.CustomField:
                    An additional, user-created field on
                an entity.

            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseGetCustomField._get_http_options()
            request, metadata = self._interceptor.pre_get_custom_field(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseGetCustomField,
                    "_BaseGetCustomField__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.GetCustomField",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "GetCustomField",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._GetCustomField._get_response(
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
            resp = custom_field_messages.CustomField()
            pb_resp = custom_field_messages.CustomField.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_field(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_field_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_field_messages.CustomField.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.get_custom_field",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "GetCustomField",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomFields(
        _BaseCustomFieldServiceRestTransport._BaseListCustomFields,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.ListCustomFields")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.ListCustomFieldsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_service.ListCustomFieldsResponse:
            r"""Call the list custom fields method over HTTP.

            Args:
                request (~.custom_field_service.ListCustomFieldsRequest):
                    The request object. Request object for ``ListCustomFields`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.custom_field_service.ListCustomFieldsResponse:
                    Response object for ``ListCustomFieldsRequest``
                containing matching ``CustomField`` objects.

            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseListCustomFields._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_fields(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseListCustomFields,
                    "_BaseListCustomFields__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.ListCustomFields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "ListCustomFields",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._ListCustomFields._get_response(
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
            resp = custom_field_service.ListCustomFieldsResponse()
            pb_resp = custom_field_service.ListCustomFieldsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_fields(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_fields_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_field_service.ListCustomFieldsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.list_custom_fields",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "ListCustomFields",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomField(
        _BaseCustomFieldServiceRestTransport._BaseUpdateCustomField,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.UpdateCustomField")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: custom_field_service.UpdateCustomFieldRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_field_messages.CustomField:
            r"""Call the update custom field method over HTTP.

            Args:
                request (~.custom_field_service.UpdateCustomFieldRequest):
                    The request object. Request object for ``UpdateCustomField`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.custom_field_messages.CustomField:
                    An additional, user-created field on
                an entity.

            """

            http_options = _BaseCustomFieldServiceRestTransport._BaseUpdateCustomField._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_field(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseUpdateCustomField,
                    "_BaseUpdateCustomField__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.UpdateCustomField",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "UpdateCustomField",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._UpdateCustomField._get_response(
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
            resp = custom_field_messages.CustomField()
            pb_resp = custom_field_messages.CustomField.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_custom_field(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_custom_field_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_field_messages.CustomField.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceClient.update_custom_field",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "UpdateCustomField",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_custom_fields(
        self,
    ) -> Callable[
        [custom_field_service.BatchActivateCustomFieldsRequest],
        custom_field_service.BatchActivateCustomFieldsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCustomFields(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_custom_fields(
        self,
    ) -> Callable[
        [custom_field_service.BatchCreateCustomFieldsRequest],
        custom_field_service.BatchCreateCustomFieldsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateCustomFields(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_custom_fields(
        self,
    ) -> Callable[
        [custom_field_service.BatchDeactivateCustomFieldsRequest],
        custom_field_service.BatchDeactivateCustomFieldsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateCustomFields(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_custom_fields(
        self,
    ) -> Callable[
        [custom_field_service.BatchUpdateCustomFieldsRequest],
        custom_field_service.BatchUpdateCustomFieldsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateCustomFields(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_custom_field(
        self,
    ) -> Callable[
        [custom_field_service.CreateCustomFieldRequest],
        custom_field_messages.CustomField,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomField(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_custom_field(
        self,
    ) -> Callable[
        [custom_field_service.GetCustomFieldRequest], custom_field_messages.CustomField
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomField(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_custom_fields(
        self,
    ) -> Callable[
        [custom_field_service.ListCustomFieldsRequest],
        custom_field_service.ListCustomFieldsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomFields(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_custom_field(
        self,
    ) -> Callable[
        [custom_field_service.UpdateCustomFieldRequest],
        custom_field_messages.CustomField,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomField(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCustomFieldServiceRestTransport._BaseCancelOperation,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCustomFieldServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCustomFieldServiceRestTransport._BaseGetOperation,
        CustomFieldServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomFieldServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseCustomFieldServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomFieldServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.CustomFieldServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomFieldServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.CustomFieldServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomFieldService",
                        "rpcName": "GetOperation",
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


__all__ = ("CustomFieldServiceRestTransport",)
