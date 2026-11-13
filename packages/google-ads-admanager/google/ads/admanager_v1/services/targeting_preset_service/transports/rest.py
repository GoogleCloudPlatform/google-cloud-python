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
    targeting_preset_messages,
    targeting_preset_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTargetingPresetServiceRestTransport

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


class TargetingPresetServiceRestInterceptor:
    """Interceptor for TargetingPresetService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TargetingPresetServiceRestTransport.

    .. code-block:: python
        class MyCustomTargetingPresetServiceInterceptor(TargetingPresetServiceRestInterceptor):
            def pre_batch_create_targeting_presets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_targeting_presets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_targeting_presets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_targeting_presets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_targeting_presets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_targeting_presets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_targeting_preset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_targeting_preset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_targeting_preset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_targeting_preset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_targeting_presets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_targeting_presets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_targeting_preset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_targeting_preset(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TargetingPresetServiceRestTransport(interceptor=MyCustomTargetingPresetServiceInterceptor())
        client = TargetingPresetServiceClient(transport=transport)


    """

    def pre_batch_create_targeting_presets(
        self,
        request: targeting_preset_service.BatchCreateTargetingPresetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.BatchCreateTargetingPresetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_targeting_presets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_batch_create_targeting_presets(
        self, response: targeting_preset_service.BatchCreateTargetingPresetsResponse
    ) -> targeting_preset_service.BatchCreateTargetingPresetsResponse:
        """Post-rpc interceptor for batch_create_targeting_presets

        DEPRECATED. Please use the `post_batch_create_targeting_presets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_batch_create_targeting_presets` interceptor runs
        before the `post_batch_create_targeting_presets_with_metadata` interceptor.
        """
        return response

    def post_batch_create_targeting_presets_with_metadata(
        self,
        response: targeting_preset_service.BatchCreateTargetingPresetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.BatchCreateTargetingPresetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_targeting_presets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_batch_create_targeting_presets_with_metadata`
        interceptor in new development instead of the `post_batch_create_targeting_presets` interceptor.
        When both interceptors are used, this `post_batch_create_targeting_presets_with_metadata` interceptor runs after the
        `post_batch_create_targeting_presets` interceptor. The (possibly modified) response returned by
        `post_batch_create_targeting_presets` will be passed to
        `post_batch_create_targeting_presets_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_targeting_presets(
        self,
        request: targeting_preset_service.BatchDeactivateTargetingPresetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.BatchDeactivateTargetingPresetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_targeting_presets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_batch_deactivate_targeting_presets(
        self, response: targeting_preset_service.BatchDeactivateTargetingPresetsResponse
    ) -> targeting_preset_service.BatchDeactivateTargetingPresetsResponse:
        """Post-rpc interceptor for batch_deactivate_targeting_presets

        DEPRECATED. Please use the `post_batch_deactivate_targeting_presets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_batch_deactivate_targeting_presets` interceptor runs
        before the `post_batch_deactivate_targeting_presets_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_targeting_presets_with_metadata(
        self,
        response: targeting_preset_service.BatchDeactivateTargetingPresetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.BatchDeactivateTargetingPresetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_targeting_presets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_targeting_presets_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_targeting_presets` interceptor.
        When both interceptors are used, this `post_batch_deactivate_targeting_presets_with_metadata` interceptor runs after the
        `post_batch_deactivate_targeting_presets` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_targeting_presets` will be passed to
        `post_batch_deactivate_targeting_presets_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_targeting_presets(
        self,
        request: targeting_preset_service.BatchUpdateTargetingPresetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.BatchUpdateTargetingPresetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_targeting_presets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_batch_update_targeting_presets(
        self, response: targeting_preset_service.BatchUpdateTargetingPresetsResponse
    ) -> targeting_preset_service.BatchUpdateTargetingPresetsResponse:
        """Post-rpc interceptor for batch_update_targeting_presets

        DEPRECATED. Please use the `post_batch_update_targeting_presets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_batch_update_targeting_presets` interceptor runs
        before the `post_batch_update_targeting_presets_with_metadata` interceptor.
        """
        return response

    def post_batch_update_targeting_presets_with_metadata(
        self,
        response: targeting_preset_service.BatchUpdateTargetingPresetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.BatchUpdateTargetingPresetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_targeting_presets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_batch_update_targeting_presets_with_metadata`
        interceptor in new development instead of the `post_batch_update_targeting_presets` interceptor.
        When both interceptors are used, this `post_batch_update_targeting_presets_with_metadata` interceptor runs after the
        `post_batch_update_targeting_presets` interceptor. The (possibly modified) response returned by
        `post_batch_update_targeting_presets` will be passed to
        `post_batch_update_targeting_presets_with_metadata`.
        """
        return response, metadata

    def pre_create_targeting_preset(
        self,
        request: targeting_preset_service.CreateTargetingPresetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.CreateTargetingPresetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_targeting_preset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_create_targeting_preset(
        self, response: targeting_preset_messages.TargetingPreset
    ) -> targeting_preset_messages.TargetingPreset:
        """Post-rpc interceptor for create_targeting_preset

        DEPRECATED. Please use the `post_create_targeting_preset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_create_targeting_preset` interceptor runs
        before the `post_create_targeting_preset_with_metadata` interceptor.
        """
        return response

    def post_create_targeting_preset_with_metadata(
        self,
        response: targeting_preset_messages.TargetingPreset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_messages.TargetingPreset,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_targeting_preset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_create_targeting_preset_with_metadata`
        interceptor in new development instead of the `post_create_targeting_preset` interceptor.
        When both interceptors are used, this `post_create_targeting_preset_with_metadata` interceptor runs after the
        `post_create_targeting_preset` interceptor. The (possibly modified) response returned by
        `post_create_targeting_preset` will be passed to
        `post_create_targeting_preset_with_metadata`.
        """
        return response, metadata

    def pre_get_targeting_preset(
        self,
        request: targeting_preset_service.GetTargetingPresetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.GetTargetingPresetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_targeting_preset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_get_targeting_preset(
        self, response: targeting_preset_messages.TargetingPreset
    ) -> targeting_preset_messages.TargetingPreset:
        """Post-rpc interceptor for get_targeting_preset

        DEPRECATED. Please use the `post_get_targeting_preset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_get_targeting_preset` interceptor runs
        before the `post_get_targeting_preset_with_metadata` interceptor.
        """
        return response

    def post_get_targeting_preset_with_metadata(
        self,
        response: targeting_preset_messages.TargetingPreset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_messages.TargetingPreset,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_targeting_preset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_get_targeting_preset_with_metadata`
        interceptor in new development instead of the `post_get_targeting_preset` interceptor.
        When both interceptors are used, this `post_get_targeting_preset_with_metadata` interceptor runs after the
        `post_get_targeting_preset` interceptor. The (possibly modified) response returned by
        `post_get_targeting_preset` will be passed to
        `post_get_targeting_preset_with_metadata`.
        """
        return response, metadata

    def pre_list_targeting_presets(
        self,
        request: targeting_preset_service.ListTargetingPresetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.ListTargetingPresetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_targeting_presets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_list_targeting_presets(
        self, response: targeting_preset_service.ListTargetingPresetsResponse
    ) -> targeting_preset_service.ListTargetingPresetsResponse:
        """Post-rpc interceptor for list_targeting_presets

        DEPRECATED. Please use the `post_list_targeting_presets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_list_targeting_presets` interceptor runs
        before the `post_list_targeting_presets_with_metadata` interceptor.
        """
        return response

    def post_list_targeting_presets_with_metadata(
        self,
        response: targeting_preset_service.ListTargetingPresetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.ListTargetingPresetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_targeting_presets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_list_targeting_presets_with_metadata`
        interceptor in new development instead of the `post_list_targeting_presets` interceptor.
        When both interceptors are used, this `post_list_targeting_presets_with_metadata` interceptor runs after the
        `post_list_targeting_presets` interceptor. The (possibly modified) response returned by
        `post_list_targeting_presets` will be passed to
        `post_list_targeting_presets_with_metadata`.
        """
        return response, metadata

    def pre_update_targeting_preset(
        self,
        request: targeting_preset_service.UpdateTargetingPresetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_service.UpdateTargetingPresetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_targeting_preset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_update_targeting_preset(
        self, response: targeting_preset_messages.TargetingPreset
    ) -> targeting_preset_messages.TargetingPreset:
        """Post-rpc interceptor for update_targeting_preset

        DEPRECATED. Please use the `post_update_targeting_preset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code. This `post_update_targeting_preset` interceptor runs
        before the `post_update_targeting_preset_with_metadata` interceptor.
        """
        return response

    def post_update_targeting_preset_with_metadata(
        self,
        response: targeting_preset_messages.TargetingPreset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        targeting_preset_messages.TargetingPreset,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_targeting_preset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetingPresetService server but before it is returned to user code.

        We recommend only using this `post_update_targeting_preset_with_metadata`
        interceptor in new development instead of the `post_update_targeting_preset` interceptor.
        When both interceptors are used, this `post_update_targeting_preset_with_metadata` interceptor runs after the
        `post_update_targeting_preset` interceptor. The (possibly modified) response returned by
        `post_update_targeting_preset` will be passed to
        `post_update_targeting_preset_with_metadata`.
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
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the TargetingPresetService server but before
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
        before they are sent to the TargetingPresetService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TargetingPresetService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TargetingPresetServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TargetingPresetServiceRestInterceptor


class TargetingPresetServiceRestTransport(_BaseTargetingPresetServiceRestTransport):
    """REST backend synchronous transport for TargetingPresetService.

    Provides methods for handling ``TargetingPreset`` objects.

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
        interceptor: Optional[TargetingPresetServiceRestInterceptor] = None,
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
            interceptor (Optional[TargetingPresetServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TargetingPresetServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateTargetingPresets(
        _BaseTargetingPresetServiceRestTransport._BaseBatchCreateTargetingPresets,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TargetingPresetServiceRestTransport.BatchCreateTargetingPresets"
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
            request: targeting_preset_service.BatchCreateTargetingPresetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_service.BatchCreateTargetingPresetsResponse:
            r"""Call the batch create targeting
            presets method over HTTP.

                Args:
                    request (~.targeting_preset_service.BatchCreateTargetingPresetsRequest):
                        The request object. Request object for ``BatchCreateTargetingPresets``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.targeting_preset_service.BatchCreateTargetingPresetsResponse:
                        Response object for ``BatchCreateTargetingPresets``
                    method.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseBatchCreateTargetingPresets._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_targeting_presets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseBatchCreateTargetingPresets,
                    "_BaseBatchCreateTargetingPresets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.BatchCreateTargetingPresets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "BatchCreateTargetingPresets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetingPresetServiceRestTransport._BatchCreateTargetingPresets._get_response(
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
            resp = targeting_preset_service.BatchCreateTargetingPresetsResponse()
            pb_resp = targeting_preset_service.BatchCreateTargetingPresetsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_targeting_presets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_targeting_presets_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = targeting_preset_service.BatchCreateTargetingPresetsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.batch_create_targeting_presets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "BatchCreateTargetingPresets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateTargetingPresets(
        _BaseTargetingPresetServiceRestTransport._BaseBatchDeactivateTargetingPresets,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TargetingPresetServiceRestTransport.BatchDeactivateTargetingPresets"
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
            request: targeting_preset_service.BatchDeactivateTargetingPresetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_service.BatchDeactivateTargetingPresetsResponse:
            r"""Call the batch deactivate
            targeting presets method over HTTP.

                Args:
                    request (~.targeting_preset_service.BatchDeactivateTargetingPresetsRequest):
                        The request object. Request message for ``BatchDeactivateTargetingPresets``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.targeting_preset_service.BatchDeactivateTargetingPresetsResponse:
                        Response message for ``DeactivateTargetingPresets``
                    method.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseBatchDeactivateTargetingPresets._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_targeting_presets(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseBatchDeactivateTargetingPresets,
                    "_BaseBatchDeactivateTargetingPresets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.BatchDeactivateTargetingPresets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "BatchDeactivateTargetingPresets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetingPresetServiceRestTransport._BatchDeactivateTargetingPresets._get_response(
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
            resp = targeting_preset_service.BatchDeactivateTargetingPresetsResponse()
            pb_resp = (
                targeting_preset_service.BatchDeactivateTargetingPresetsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_targeting_presets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_targeting_presets_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = targeting_preset_service.BatchDeactivateTargetingPresetsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.batch_deactivate_targeting_presets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "BatchDeactivateTargetingPresets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateTargetingPresets(
        _BaseTargetingPresetServiceRestTransport._BaseBatchUpdateTargetingPresets,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TargetingPresetServiceRestTransport.BatchUpdateTargetingPresets"
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
            request: targeting_preset_service.BatchUpdateTargetingPresetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_service.BatchUpdateTargetingPresetsResponse:
            r"""Call the batch update targeting
            presets method over HTTP.

                Args:
                    request (~.targeting_preset_service.BatchUpdateTargetingPresetsRequest):
                        The request object. Request object for ``BatchUpdateTargetingPresets``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.targeting_preset_service.BatchUpdateTargetingPresetsResponse:
                        Response object for ``BatchUpdateTargetingPresets``
                    method.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseBatchUpdateTargetingPresets._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_targeting_presets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseBatchUpdateTargetingPresets,
                    "_BaseBatchUpdateTargetingPresets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.BatchUpdateTargetingPresets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "BatchUpdateTargetingPresets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetingPresetServiceRestTransport._BatchUpdateTargetingPresets._get_response(
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
            resp = targeting_preset_service.BatchUpdateTargetingPresetsResponse()
            pb_resp = targeting_preset_service.BatchUpdateTargetingPresetsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_targeting_presets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_targeting_presets_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = targeting_preset_service.BatchUpdateTargetingPresetsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.batch_update_targeting_presets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "BatchUpdateTargetingPresets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTargetingPreset(
        _BaseTargetingPresetServiceRestTransport._BaseCreateTargetingPreset,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash("TargetingPresetServiceRestTransport.CreateTargetingPreset")

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
            request: targeting_preset_service.CreateTargetingPresetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_messages.TargetingPreset:
            r"""Call the create targeting preset method over HTTP.

            Args:
                request (~.targeting_preset_service.CreateTargetingPresetRequest):
                    The request object. Request object for ``CreateTargetingPreset`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.targeting_preset_messages.TargetingPreset:
                    User-defined preset targeting
                criteria.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseCreateTargetingPreset._get_http_options()
            request, metadata = self._interceptor.pre_create_targeting_preset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseCreateTargetingPreset,
                    "_BaseCreateTargetingPreset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.CreateTargetingPreset",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "CreateTargetingPreset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetingPresetServiceRestTransport._CreateTargetingPreset._get_response(
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
            resp = targeting_preset_messages.TargetingPreset()
            pb_resp = targeting_preset_messages.TargetingPreset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_targeting_preset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_targeting_preset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        targeting_preset_messages.TargetingPreset.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.create_targeting_preset",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "CreateTargetingPreset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTargetingPreset(
        _BaseTargetingPresetServiceRestTransport._BaseGetTargetingPreset,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash("TargetingPresetServiceRestTransport.GetTargetingPreset")

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
            request: targeting_preset_service.GetTargetingPresetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_messages.TargetingPreset:
            r"""Call the get targeting preset method over HTTP.

            Args:
                request (~.targeting_preset_service.GetTargetingPresetRequest):
                    The request object. Request object for ``GetTargetingPreset`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.targeting_preset_messages.TargetingPreset:
                    User-defined preset targeting
                criteria.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseGetTargetingPreset._get_http_options()
            request, metadata = self._interceptor.pre_get_targeting_preset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseGetTargetingPreset,
                    "_BaseGetTargetingPreset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.GetTargetingPreset",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "GetTargetingPreset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TargetingPresetServiceRestTransport._GetTargetingPreset._get_response(
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
            resp = targeting_preset_messages.TargetingPreset()
            pb_resp = targeting_preset_messages.TargetingPreset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_targeting_preset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_targeting_preset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        targeting_preset_messages.TargetingPreset.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.get_targeting_preset",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "GetTargetingPreset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTargetingPresets(
        _BaseTargetingPresetServiceRestTransport._BaseListTargetingPresets,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash("TargetingPresetServiceRestTransport.ListTargetingPresets")

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
            request: targeting_preset_service.ListTargetingPresetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_service.ListTargetingPresetsResponse:
            r"""Call the list targeting presets method over HTTP.

            Args:
                request (~.targeting_preset_service.ListTargetingPresetsRequest):
                    The request object. Request object for ``ListTargetingPresets`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.targeting_preset_service.ListTargetingPresetsResponse:
                    Response object for ``ListTargetingPresetsRequest``
                containing matching ``TargetingPreset`` objects.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseListTargetingPresets._get_http_options()
            request, metadata = self._interceptor.pre_list_targeting_presets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseListTargetingPresets,
                    "_BaseListTargetingPresets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.ListTargetingPresets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "ListTargetingPresets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TargetingPresetServiceRestTransport._ListTargetingPresets._get_response(
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
            resp = targeting_preset_service.ListTargetingPresetsResponse()
            pb_resp = targeting_preset_service.ListTargetingPresetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_targeting_presets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_targeting_presets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        targeting_preset_service.ListTargetingPresetsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.list_targeting_presets",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "ListTargetingPresets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTargetingPreset(
        _BaseTargetingPresetServiceRestTransport._BaseUpdateTargetingPreset,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash("TargetingPresetServiceRestTransport.UpdateTargetingPreset")

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
            request: targeting_preset_service.UpdateTargetingPresetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> targeting_preset_messages.TargetingPreset:
            r"""Call the update targeting preset method over HTTP.

            Args:
                request (~.targeting_preset_service.UpdateTargetingPresetRequest):
                    The request object. Request object for ``UpdateTargetingPreset`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.targeting_preset_messages.TargetingPreset:
                    User-defined preset targeting
                criteria.

            """

            http_options = _BaseTargetingPresetServiceRestTransport._BaseUpdateTargetingPreset._get_http_options()
            request, metadata = self._interceptor.pre_update_targeting_preset(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseUpdateTargetingPreset,
                    "_BaseUpdateTargetingPreset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.UpdateTargetingPreset",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "UpdateTargetingPreset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetingPresetServiceRestTransport._UpdateTargetingPreset._get_response(
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
            resp = targeting_preset_messages.TargetingPreset()
            pb_resp = targeting_preset_messages.TargetingPreset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_targeting_preset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_targeting_preset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        targeting_preset_messages.TargetingPreset.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceClient.update_targeting_preset",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "UpdateTargetingPreset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_targeting_presets(
        self,
    ) -> Callable[
        [targeting_preset_service.BatchCreateTargetingPresetsRequest],
        targeting_preset_service.BatchCreateTargetingPresetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateTargetingPresets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_targeting_presets(
        self,
    ) -> Callable[
        [targeting_preset_service.BatchDeactivateTargetingPresetsRequest],
        targeting_preset_service.BatchDeactivateTargetingPresetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateTargetingPresets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_targeting_presets(
        self,
    ) -> Callable[
        [targeting_preset_service.BatchUpdateTargetingPresetsRequest],
        targeting_preset_service.BatchUpdateTargetingPresetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateTargetingPresets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_targeting_preset(
        self,
    ) -> Callable[
        [targeting_preset_service.CreateTargetingPresetRequest],
        targeting_preset_messages.TargetingPreset,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTargetingPreset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_targeting_preset(
        self,
    ) -> Callable[
        [targeting_preset_service.GetTargetingPresetRequest],
        targeting_preset_messages.TargetingPreset,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTargetingPreset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_targeting_presets(
        self,
    ) -> Callable[
        [targeting_preset_service.ListTargetingPresetsRequest],
        targeting_preset_service.ListTargetingPresetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTargetingPresets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_targeting_preset(
        self,
    ) -> Callable[
        [targeting_preset_service.UpdateTargetingPresetRequest],
        targeting_preset_messages.TargetingPreset,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTargetingPreset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseTargetingPresetServiceRestTransport._BaseCancelOperation,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash("TargetingPresetServiceRestTransport.CancelOperation")

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

            http_options = _BaseTargetingPresetServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TargetingPresetServiceRestTransport._CancelOperation._get_response(
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
        _BaseTargetingPresetServiceRestTransport._BaseGetOperation,
        TargetingPresetServiceRestStub,
    ):
        def __hash__(self):
            return hash("TargetingPresetServiceRestTransport.GetOperation")

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

            http_options = _BaseTargetingPresetServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetingPresetServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.TargetingPresetServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetingPresetServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.TargetingPresetServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TargetingPresetService",
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


__all__ = ("TargetingPresetServiceRestTransport",)
