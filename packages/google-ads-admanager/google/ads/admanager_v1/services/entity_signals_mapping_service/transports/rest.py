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
from google.ads.admanager_v1.types import (
    entity_signals_mapping_messages,
    entity_signals_mapping_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseEntitySignalsMappingServiceRestTransport

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


class EntitySignalsMappingServiceRestInterceptor:
    """Interceptor for EntitySignalsMappingService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EntitySignalsMappingServiceRestTransport.

    .. code-block:: python
        class MyCustomEntitySignalsMappingServiceInterceptor(EntitySignalsMappingServiceRestInterceptor):
            def pre_batch_create_entity_signals_mappings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_entity_signals_mappings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_entity_signals_mappings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_entity_signals_mappings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_entity_signals_mapping(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_entity_signals_mapping(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_entity_signals_mapping(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_entity_signals_mapping(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_entity_signals_mappings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_entity_signals_mappings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_entity_signals_mapping(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_entity_signals_mapping(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EntitySignalsMappingServiceRestTransport(interceptor=MyCustomEntitySignalsMappingServiceInterceptor())
        client = EntitySignalsMappingServiceClient(transport=transport)


    """

    def pre_batch_create_entity_signals_mappings(
        self,
        request: entity_signals_mapping_service.BatchCreateEntitySignalsMappingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.BatchCreateEntitySignalsMappingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_entity_signals_mappings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_batch_create_entity_signals_mappings(
        self,
        response: entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse,
    ) -> entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse:
        """Post-rpc interceptor for batch_create_entity_signals_mappings

        DEPRECATED. Please use the `post_batch_create_entity_signals_mappings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code. This `post_batch_create_entity_signals_mappings` interceptor runs
        before the `post_batch_create_entity_signals_mappings_with_metadata` interceptor.
        """
        return response

    def post_batch_create_entity_signals_mappings_with_metadata(
        self,
        response: entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_entity_signals_mappings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EntitySignalsMappingService server but before it is returned to user code.

        We recommend only using this `post_batch_create_entity_signals_mappings_with_metadata`
        interceptor in new development instead of the `post_batch_create_entity_signals_mappings` interceptor.
        When both interceptors are used, this `post_batch_create_entity_signals_mappings_with_metadata` interceptor runs after the
        `post_batch_create_entity_signals_mappings` interceptor. The (possibly modified) response returned by
        `post_batch_create_entity_signals_mappings` will be passed to
        `post_batch_create_entity_signals_mappings_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_entity_signals_mappings(
        self,
        request: entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_entity_signals_mappings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_batch_update_entity_signals_mappings(
        self,
        response: entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse,
    ) -> entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse:
        """Post-rpc interceptor for batch_update_entity_signals_mappings

        DEPRECATED. Please use the `post_batch_update_entity_signals_mappings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code. This `post_batch_update_entity_signals_mappings` interceptor runs
        before the `post_batch_update_entity_signals_mappings_with_metadata` interceptor.
        """
        return response

    def post_batch_update_entity_signals_mappings_with_metadata(
        self,
        response: entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_entity_signals_mappings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EntitySignalsMappingService server but before it is returned to user code.

        We recommend only using this `post_batch_update_entity_signals_mappings_with_metadata`
        interceptor in new development instead of the `post_batch_update_entity_signals_mappings` interceptor.
        When both interceptors are used, this `post_batch_update_entity_signals_mappings_with_metadata` interceptor runs after the
        `post_batch_update_entity_signals_mappings` interceptor. The (possibly modified) response returned by
        `post_batch_update_entity_signals_mappings` will be passed to
        `post_batch_update_entity_signals_mappings_with_metadata`.
        """
        return response, metadata

    def pre_create_entity_signals_mapping(
        self,
        request: entity_signals_mapping_service.CreateEntitySignalsMappingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.CreateEntitySignalsMappingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_entity_signals_mapping

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_create_entity_signals_mapping(
        self, response: entity_signals_mapping_messages.EntitySignalsMapping
    ) -> entity_signals_mapping_messages.EntitySignalsMapping:
        """Post-rpc interceptor for create_entity_signals_mapping

        DEPRECATED. Please use the `post_create_entity_signals_mapping_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code. This `post_create_entity_signals_mapping` interceptor runs
        before the `post_create_entity_signals_mapping_with_metadata` interceptor.
        """
        return response

    def post_create_entity_signals_mapping_with_metadata(
        self,
        response: entity_signals_mapping_messages.EntitySignalsMapping,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_messages.EntitySignalsMapping,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_entity_signals_mapping

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EntitySignalsMappingService server but before it is returned to user code.

        We recommend only using this `post_create_entity_signals_mapping_with_metadata`
        interceptor in new development instead of the `post_create_entity_signals_mapping` interceptor.
        When both interceptors are used, this `post_create_entity_signals_mapping_with_metadata` interceptor runs after the
        `post_create_entity_signals_mapping` interceptor. The (possibly modified) response returned by
        `post_create_entity_signals_mapping` will be passed to
        `post_create_entity_signals_mapping_with_metadata`.
        """
        return response, metadata

    def pre_get_entity_signals_mapping(
        self,
        request: entity_signals_mapping_service.GetEntitySignalsMappingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.GetEntitySignalsMappingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_entity_signals_mapping

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_get_entity_signals_mapping(
        self, response: entity_signals_mapping_messages.EntitySignalsMapping
    ) -> entity_signals_mapping_messages.EntitySignalsMapping:
        """Post-rpc interceptor for get_entity_signals_mapping

        DEPRECATED. Please use the `post_get_entity_signals_mapping_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code. This `post_get_entity_signals_mapping` interceptor runs
        before the `post_get_entity_signals_mapping_with_metadata` interceptor.
        """
        return response

    def post_get_entity_signals_mapping_with_metadata(
        self,
        response: entity_signals_mapping_messages.EntitySignalsMapping,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_messages.EntitySignalsMapping,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_entity_signals_mapping

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EntitySignalsMappingService server but before it is returned to user code.

        We recommend only using this `post_get_entity_signals_mapping_with_metadata`
        interceptor in new development instead of the `post_get_entity_signals_mapping` interceptor.
        When both interceptors are used, this `post_get_entity_signals_mapping_with_metadata` interceptor runs after the
        `post_get_entity_signals_mapping` interceptor. The (possibly modified) response returned by
        `post_get_entity_signals_mapping` will be passed to
        `post_get_entity_signals_mapping_with_metadata`.
        """
        return response, metadata

    def pre_list_entity_signals_mappings(
        self,
        request: entity_signals_mapping_service.ListEntitySignalsMappingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.ListEntitySignalsMappingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_entity_signals_mappings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_list_entity_signals_mappings(
        self, response: entity_signals_mapping_service.ListEntitySignalsMappingsResponse
    ) -> entity_signals_mapping_service.ListEntitySignalsMappingsResponse:
        """Post-rpc interceptor for list_entity_signals_mappings

        DEPRECATED. Please use the `post_list_entity_signals_mappings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code. This `post_list_entity_signals_mappings` interceptor runs
        before the `post_list_entity_signals_mappings_with_metadata` interceptor.
        """
        return response

    def post_list_entity_signals_mappings_with_metadata(
        self,
        response: entity_signals_mapping_service.ListEntitySignalsMappingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.ListEntitySignalsMappingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_entity_signals_mappings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EntitySignalsMappingService server but before it is returned to user code.

        We recommend only using this `post_list_entity_signals_mappings_with_metadata`
        interceptor in new development instead of the `post_list_entity_signals_mappings` interceptor.
        When both interceptors are used, this `post_list_entity_signals_mappings_with_metadata` interceptor runs after the
        `post_list_entity_signals_mappings` interceptor. The (possibly modified) response returned by
        `post_list_entity_signals_mappings` will be passed to
        `post_list_entity_signals_mappings_with_metadata`.
        """
        return response, metadata

    def pre_update_entity_signals_mapping(
        self,
        request: entity_signals_mapping_service.UpdateEntitySignalsMappingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_service.UpdateEntitySignalsMappingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_entity_signals_mapping

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_update_entity_signals_mapping(
        self, response: entity_signals_mapping_messages.EntitySignalsMapping
    ) -> entity_signals_mapping_messages.EntitySignalsMapping:
        """Post-rpc interceptor for update_entity_signals_mapping

        DEPRECATED. Please use the `post_update_entity_signals_mapping_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code. This `post_update_entity_signals_mapping` interceptor runs
        before the `post_update_entity_signals_mapping_with_metadata` interceptor.
        """
        return response

    def post_update_entity_signals_mapping_with_metadata(
        self,
        response: entity_signals_mapping_messages.EntitySignalsMapping,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        entity_signals_mapping_messages.EntitySignalsMapping,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_entity_signals_mapping

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EntitySignalsMappingService server but before it is returned to user code.

        We recommend only using this `post_update_entity_signals_mapping_with_metadata`
        interceptor in new development instead of the `post_update_entity_signals_mapping` interceptor.
        When both interceptors are used, this `post_update_entity_signals_mapping_with_metadata` interceptor runs after the
        `post_update_entity_signals_mapping` interceptor. The (possibly modified) response returned by
        `post_update_entity_signals_mapping` will be passed to
        `post_update_entity_signals_mapping_with_metadata`.
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
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
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
        before they are sent to the EntitySignalsMappingService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the EntitySignalsMappingService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EntitySignalsMappingServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EntitySignalsMappingServiceRestInterceptor


class EntitySignalsMappingServiceRestTransport(
    _BaseEntitySignalsMappingServiceRestTransport
):
    """REST backend synchronous transport for EntitySignalsMappingService.

    Provides methods for handling ``EntitySignalsMapping`` objects.

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
        interceptor: Optional[EntitySignalsMappingServiceRestInterceptor] = None,
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
            interceptor (Optional[EntitySignalsMappingServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or EntitySignalsMappingServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateEntitySignalsMappings(
        _BaseEntitySignalsMappingServiceRestTransport._BaseBatchCreateEntitySignalsMappings,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EntitySignalsMappingServiceRestTransport.BatchCreateEntitySignalsMappings"
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
            request: entity_signals_mapping_service.BatchCreateEntitySignalsMappingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse:
            r"""Call the batch create entity
            signals mappings method over HTTP.

                Args:
                    request (~.entity_signals_mapping_service.BatchCreateEntitySignalsMappingsRequest):
                        The request object. Request object for ``BatchCreateEntitySignalsMappings``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse:
                        Response object for ``BatchCreateEntitySignalsMappings``
                    method.

            """

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseBatchCreateEntitySignalsMappings._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_entity_signals_mappings(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseBatchCreateEntitySignalsMappings,
                    "_BaseBatchCreateEntitySignalsMappings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.BatchCreateEntitySignalsMappings",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "BatchCreateEntitySignalsMappings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EntitySignalsMappingServiceRestTransport._BatchCreateEntitySignalsMappings._get_response(
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
            resp = entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse()
            pb_resp = entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_entity_signals_mappings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_entity_signals_mappings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceClient.batch_create_entity_signals_mappings",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "BatchCreateEntitySignalsMappings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateEntitySignalsMappings(
        _BaseEntitySignalsMappingServiceRestTransport._BaseBatchUpdateEntitySignalsMappings,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EntitySignalsMappingServiceRestTransport.BatchUpdateEntitySignalsMappings"
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
            request: entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse:
            r"""Call the batch update entity
            signals mappings method over HTTP.

                Args:
                    request (~.entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsRequest):
                        The request object. Request object for ``BatchUpdateEntitySignalsMappings``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse:
                        Response object for ``BatchUpdateEntitySignalsMappings``
                    method.

            """

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseBatchUpdateEntitySignalsMappings._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_entity_signals_mappings(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseBatchUpdateEntitySignalsMappings,
                    "_BaseBatchUpdateEntitySignalsMappings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.BatchUpdateEntitySignalsMappings",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "BatchUpdateEntitySignalsMappings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EntitySignalsMappingServiceRestTransport._BatchUpdateEntitySignalsMappings._get_response(
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
            resp = entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse()
            pb_resp = entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_entity_signals_mappings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_entity_signals_mappings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceClient.batch_update_entity_signals_mappings",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "BatchUpdateEntitySignalsMappings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEntitySignalsMapping(
        _BaseEntitySignalsMappingServiceRestTransport._BaseCreateEntitySignalsMapping,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EntitySignalsMappingServiceRestTransport.CreateEntitySignalsMapping"
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
            request: entity_signals_mapping_service.CreateEntitySignalsMappingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> entity_signals_mapping_messages.EntitySignalsMapping:
            r"""Call the create entity signals
            mapping method over HTTP.

                Args:
                    request (~.entity_signals_mapping_service.CreateEntitySignalsMappingRequest):
                        The request object. Request object for ``CreateEntitySignalsMapping``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.entity_signals_mapping_messages.EntitySignalsMapping:
                        The ``EntitySignalsMapping`` resource.
            """

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseCreateEntitySignalsMapping._get_http_options()
            request, metadata = self._interceptor.pre_create_entity_signals_mapping(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseCreateEntitySignalsMapping,
                    "_BaseCreateEntitySignalsMapping__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.CreateEntitySignalsMapping",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "CreateEntitySignalsMapping",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EntitySignalsMappingServiceRestTransport._CreateEntitySignalsMapping._get_response(
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
            resp = entity_signals_mapping_messages.EntitySignalsMapping()
            pb_resp = entity_signals_mapping_messages.EntitySignalsMapping.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_entity_signals_mapping(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_entity_signals_mapping_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        entity_signals_mapping_messages.EntitySignalsMapping.to_json(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceClient.create_entity_signals_mapping",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "CreateEntitySignalsMapping",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEntitySignalsMapping(
        _BaseEntitySignalsMappingServiceRestTransport._BaseGetEntitySignalsMapping,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EntitySignalsMappingServiceRestTransport.GetEntitySignalsMapping"
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
            request: entity_signals_mapping_service.GetEntitySignalsMappingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> entity_signals_mapping_messages.EntitySignalsMapping:
            r"""Call the get entity signals
            mapping method over HTTP.

                Args:
                    request (~.entity_signals_mapping_service.GetEntitySignalsMappingRequest):
                        The request object. Request object for ``GetEntitySignalsMapping`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.entity_signals_mapping_messages.EntitySignalsMapping:
                        The ``EntitySignalsMapping`` resource.
            """

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseGetEntitySignalsMapping._get_http_options()
            request, metadata = self._interceptor.pre_get_entity_signals_mapping(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseGetEntitySignalsMapping,
                    "_BaseGetEntitySignalsMapping__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.GetEntitySignalsMapping",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "GetEntitySignalsMapping",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EntitySignalsMappingServiceRestTransport._GetEntitySignalsMapping._get_response(
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
            resp = entity_signals_mapping_messages.EntitySignalsMapping()
            pb_resp = entity_signals_mapping_messages.EntitySignalsMapping.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_entity_signals_mapping(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_entity_signals_mapping_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        entity_signals_mapping_messages.EntitySignalsMapping.to_json(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceClient.get_entity_signals_mapping",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "GetEntitySignalsMapping",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEntitySignalsMappings(
        _BaseEntitySignalsMappingServiceRestTransport._BaseListEntitySignalsMappings,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EntitySignalsMappingServiceRestTransport.ListEntitySignalsMappings"
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
            request: entity_signals_mapping_service.ListEntitySignalsMappingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> entity_signals_mapping_service.ListEntitySignalsMappingsResponse:
            r"""Call the list entity signals
            mappings method over HTTP.

                Args:
                    request (~.entity_signals_mapping_service.ListEntitySignalsMappingsRequest):
                        The request object. Request object for ``ListEntitySignalsMappings`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.entity_signals_mapping_service.ListEntitySignalsMappingsResponse:
                        Response object for ``ListEntitySignalsMappingsRequest``
                    containing matching ``EntitySignalsMapping`` resources.

            """

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseListEntitySignalsMappings._get_http_options()
            request, metadata = self._interceptor.pre_list_entity_signals_mappings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseListEntitySignalsMappings,
                    "_BaseListEntitySignalsMappings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.ListEntitySignalsMappings",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "ListEntitySignalsMappings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EntitySignalsMappingServiceRestTransport._ListEntitySignalsMappings._get_response(
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
            resp = entity_signals_mapping_service.ListEntitySignalsMappingsResponse()
            pb_resp = (
                entity_signals_mapping_service.ListEntitySignalsMappingsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_entity_signals_mappings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_entity_signals_mappings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = entity_signals_mapping_service.ListEntitySignalsMappingsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceClient.list_entity_signals_mappings",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "ListEntitySignalsMappings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEntitySignalsMapping(
        _BaseEntitySignalsMappingServiceRestTransport._BaseUpdateEntitySignalsMapping,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "EntitySignalsMappingServiceRestTransport.UpdateEntitySignalsMapping"
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
            request: entity_signals_mapping_service.UpdateEntitySignalsMappingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> entity_signals_mapping_messages.EntitySignalsMapping:
            r"""Call the update entity signals
            mapping method over HTTP.

                Args:
                    request (~.entity_signals_mapping_service.UpdateEntitySignalsMappingRequest):
                        The request object. Request object for ``UpdateEntitySignalsMapping``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.entity_signals_mapping_messages.EntitySignalsMapping:
                        The ``EntitySignalsMapping`` resource.
            """

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseUpdateEntitySignalsMapping._get_http_options()
            request, metadata = self._interceptor.pre_update_entity_signals_mapping(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseUpdateEntitySignalsMapping,
                    "_BaseUpdateEntitySignalsMapping__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.UpdateEntitySignalsMapping",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "UpdateEntitySignalsMapping",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EntitySignalsMappingServiceRestTransport._UpdateEntitySignalsMapping._get_response(
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
            resp = entity_signals_mapping_messages.EntitySignalsMapping()
            pb_resp = entity_signals_mapping_messages.EntitySignalsMapping.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_entity_signals_mapping(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_entity_signals_mapping_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        entity_signals_mapping_messages.EntitySignalsMapping.to_json(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceClient.update_entity_signals_mapping",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "UpdateEntitySignalsMapping",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_entity_signals_mappings(
        self,
    ) -> Callable[
        [entity_signals_mapping_service.BatchCreateEntitySignalsMappingsRequest],
        entity_signals_mapping_service.BatchCreateEntitySignalsMappingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateEntitySignalsMappings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_entity_signals_mappings(
        self,
    ) -> Callable[
        [entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsRequest],
        entity_signals_mapping_service.BatchUpdateEntitySignalsMappingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateEntitySignalsMappings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_entity_signals_mapping(
        self,
    ) -> Callable[
        [entity_signals_mapping_service.CreateEntitySignalsMappingRequest],
        entity_signals_mapping_messages.EntitySignalsMapping,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEntitySignalsMapping(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_entity_signals_mapping(
        self,
    ) -> Callable[
        [entity_signals_mapping_service.GetEntitySignalsMappingRequest],
        entity_signals_mapping_messages.EntitySignalsMapping,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEntitySignalsMapping(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_entity_signals_mappings(
        self,
    ) -> Callable[
        [entity_signals_mapping_service.ListEntitySignalsMappingsRequest],
        entity_signals_mapping_service.ListEntitySignalsMappingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEntitySignalsMappings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_entity_signals_mapping(
        self,
    ) -> Callable[
        [entity_signals_mapping_service.UpdateEntitySignalsMappingRequest],
        entity_signals_mapping_messages.EntitySignalsMapping,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEntitySignalsMapping(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseEntitySignalsMappingServiceRestTransport._BaseCancelOperation,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash("EntitySignalsMappingServiceRestTransport.CancelOperation")

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

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EntitySignalsMappingServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseEntitySignalsMappingServiceRestTransport._BaseGetOperation,
        EntitySignalsMappingServiceRestStub,
    ):
        def __hash__(self):
            return hash("EntitySignalsMappingServiceRestTransport.GetOperation")

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

            http_options = _BaseEntitySignalsMappingServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEntitySignalsMappingServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.EntitySignalsMappingServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EntitySignalsMappingServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.EntitySignalsMappingServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.EntitySignalsMappingService",
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


__all__ = ("EntitySignalsMappingServiceRestTransport",)
