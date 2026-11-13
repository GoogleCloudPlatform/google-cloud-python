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
from google.ads.admanager_v1.types import label_messages, label_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLabelServiceRestTransport

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


class LabelServiceRestInterceptor:
    """Interceptor for LabelService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LabelServiceRestTransport.

    .. code-block:: python
        class MyCustomLabelServiceInterceptor(LabelServiceRestInterceptor):
            def pre_batch_activate_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_label(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LabelServiceRestTransport(interceptor=MyCustomLabelServiceInterceptor())
        client = LabelServiceClient(transport=transport)


    """

    def pre_batch_activate_labels(
        self,
        request: label_service.BatchActivateLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchActivateLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_batch_activate_labels(
        self, response: label_service.BatchActivateLabelsResponse
    ) -> label_service.BatchActivateLabelsResponse:
        """Post-rpc interceptor for batch_activate_labels

        DEPRECATED. Please use the `post_batch_activate_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_batch_activate_labels` interceptor runs
        before the `post_batch_activate_labels_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_labels_with_metadata(
        self,
        response: label_service.BatchActivateLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchActivateLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_labels_with_metadata`
        interceptor in new development instead of the `post_batch_activate_labels` interceptor.
        When both interceptors are used, this `post_batch_activate_labels_with_metadata` interceptor runs after the
        `post_batch_activate_labels` interceptor. The (possibly modified) response returned by
        `post_batch_activate_labels` will be passed to
        `post_batch_activate_labels_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_labels(
        self,
        request: label_service.BatchCreateLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchCreateLabelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_batch_create_labels(
        self, response: label_service.BatchCreateLabelsResponse
    ) -> label_service.BatchCreateLabelsResponse:
        """Post-rpc interceptor for batch_create_labels

        DEPRECATED. Please use the `post_batch_create_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_batch_create_labels` interceptor runs
        before the `post_batch_create_labels_with_metadata` interceptor.
        """
        return response

    def post_batch_create_labels_with_metadata(
        self,
        response: label_service.BatchCreateLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchCreateLabelsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_batch_create_labels_with_metadata`
        interceptor in new development instead of the `post_batch_create_labels` interceptor.
        When both interceptors are used, this `post_batch_create_labels_with_metadata` interceptor runs after the
        `post_batch_create_labels` interceptor. The (possibly modified) response returned by
        `post_batch_create_labels` will be passed to
        `post_batch_create_labels_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_labels(
        self,
        request: label_service.BatchDeactivateLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchDeactivateLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_batch_deactivate_labels(
        self, response: label_service.BatchDeactivateLabelsResponse
    ) -> label_service.BatchDeactivateLabelsResponse:
        """Post-rpc interceptor for batch_deactivate_labels

        DEPRECATED. Please use the `post_batch_deactivate_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_batch_deactivate_labels` interceptor runs
        before the `post_batch_deactivate_labels_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_labels_with_metadata(
        self,
        response: label_service.BatchDeactivateLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchDeactivateLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_labels_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_labels` interceptor.
        When both interceptors are used, this `post_batch_deactivate_labels_with_metadata` interceptor runs after the
        `post_batch_deactivate_labels` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_labels` will be passed to
        `post_batch_deactivate_labels_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_labels(
        self,
        request: label_service.BatchUpdateLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchUpdateLabelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_batch_update_labels(
        self, response: label_service.BatchUpdateLabelsResponse
    ) -> label_service.BatchUpdateLabelsResponse:
        """Post-rpc interceptor for batch_update_labels

        DEPRECATED. Please use the `post_batch_update_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_batch_update_labels` interceptor runs
        before the `post_batch_update_labels_with_metadata` interceptor.
        """
        return response

    def post_batch_update_labels_with_metadata(
        self,
        response: label_service.BatchUpdateLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.BatchUpdateLabelsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_batch_update_labels_with_metadata`
        interceptor in new development instead of the `post_batch_update_labels` interceptor.
        When both interceptors are used, this `post_batch_update_labels_with_metadata` interceptor runs after the
        `post_batch_update_labels` interceptor. The (possibly modified) response returned by
        `post_batch_update_labels` will be passed to
        `post_batch_update_labels_with_metadata`.
        """
        return response, metadata

    def pre_create_label(
        self,
        request: label_service.CreateLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.CreateLabelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_create_label(self, response: label_messages.Label) -> label_messages.Label:
        """Post-rpc interceptor for create_label

        DEPRECATED. Please use the `post_create_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_create_label` interceptor runs
        before the `post_create_label_with_metadata` interceptor.
        """
        return response

    def post_create_label_with_metadata(
        self,
        response: label_messages.Label,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[label_messages.Label, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_create_label_with_metadata`
        interceptor in new development instead of the `post_create_label` interceptor.
        When both interceptors are used, this `post_create_label_with_metadata` interceptor runs after the
        `post_create_label` interceptor. The (possibly modified) response returned by
        `post_create_label` will be passed to
        `post_create_label_with_metadata`.
        """
        return response, metadata

    def pre_get_label(
        self,
        request: label_service.GetLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[label_service.GetLabelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_get_label(self, response: label_messages.Label) -> label_messages.Label:
        """Post-rpc interceptor for get_label

        DEPRECATED. Please use the `post_get_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_get_label` interceptor runs
        before the `post_get_label_with_metadata` interceptor.
        """
        return response

    def post_get_label_with_metadata(
        self,
        response: label_messages.Label,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[label_messages.Label, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_get_label_with_metadata`
        interceptor in new development instead of the `post_get_label` interceptor.
        When both interceptors are used, this `post_get_label_with_metadata` interceptor runs after the
        `post_get_label` interceptor. The (possibly modified) response returned by
        `post_get_label` will be passed to
        `post_get_label_with_metadata`.
        """
        return response, metadata

    def pre_list_labels(
        self,
        request: label_service.ListLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.ListLabelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_list_labels(
        self, response: label_service.ListLabelsResponse
    ) -> label_service.ListLabelsResponse:
        """Post-rpc interceptor for list_labels

        DEPRECATED. Please use the `post_list_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_list_labels` interceptor runs
        before the `post_list_labels_with_metadata` interceptor.
        """
        return response

    def post_list_labels_with_metadata(
        self,
        response: label_service.ListLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.ListLabelsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_list_labels_with_metadata`
        interceptor in new development instead of the `post_list_labels` interceptor.
        When both interceptors are used, this `post_list_labels_with_metadata` interceptor runs after the
        `post_list_labels` interceptor. The (possibly modified) response returned by
        `post_list_labels` will be passed to
        `post_list_labels_with_metadata`.
        """
        return response, metadata

    def pre_update_label(
        self,
        request: label_service.UpdateLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        label_service.UpdateLabelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_update_label(self, response: label_messages.Label) -> label_messages.Label:
        """Post-rpc interceptor for update_label

        DEPRECATED. Please use the `post_update_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code. This `post_update_label` interceptor runs
        before the `post_update_label_with_metadata` interceptor.
        """
        return response

    def post_update_label_with_metadata(
        self,
        response: label_messages.Label,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[label_messages.Label, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LabelService server but before it is returned to user code.

        We recommend only using this `post_update_label_with_metadata`
        interceptor in new development instead of the `post_update_label` interceptor.
        When both interceptors are used, this `post_update_label_with_metadata` interceptor runs after the
        `post_update_label` interceptor. The (possibly modified) response returned by
        `post_update_label` will be passed to
        `post_update_label_with_metadata`.
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
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the LabelService server but before
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
        before they are sent to the LabelService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the LabelService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LabelServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LabelServiceRestInterceptor


class LabelServiceRestTransport(_BaseLabelServiceRestTransport):
    """REST backend synchronous transport for LabelService.

    Provides methods for handling ``Label`` objects.

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
        interceptor: Optional[LabelServiceRestInterceptor] = None,
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
            interceptor (Optional[LabelServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LabelServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateLabels(
        _BaseLabelServiceRestTransport._BaseBatchActivateLabels, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.BatchActivateLabels")

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
            request: label_service.BatchActivateLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_service.BatchActivateLabelsResponse:
            r"""Call the batch activate labels method over HTTP.

            Args:
                request (~.label_service.BatchActivateLabelsRequest):
                    The request object. Request message for ``BatchActivateLabels`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_service.BatchActivateLabelsResponse:
                    Response message for ``BatchActivateLabels`` method.
            """

            http_options = _BaseLabelServiceRestTransport._BaseBatchActivateLabels._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseBatchActivateLabels,
                    "_BaseBatchActivateLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.BatchActivateLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchActivateLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._BatchActivateLabels._get_response(
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
            resp = label_service.BatchActivateLabelsResponse()
            pb_resp = label_service.BatchActivateLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        label_service.BatchActivateLabelsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LabelServiceClient.batch_activate_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchActivateLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateLabels(
        _BaseLabelServiceRestTransport._BaseBatchCreateLabels, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.BatchCreateLabels")

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
            request: label_service.BatchCreateLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_service.BatchCreateLabelsResponse:
            r"""Call the batch create labels method over HTTP.

            Args:
                request (~.label_service.BatchCreateLabelsRequest):
                    The request object. Request object for ``BatchCreateLabels`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_service.BatchCreateLabelsResponse:
                    Response object for ``BatchCreateLabels`` method.
            """

            http_options = _BaseLabelServiceRestTransport._BaseBatchCreateLabels._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseBatchCreateLabels,
                    "_BaseBatchCreateLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.BatchCreateLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchCreateLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._BatchCreateLabels._get_response(
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
            resp = label_service.BatchCreateLabelsResponse()
            pb_resp = label_service.BatchCreateLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = label_service.BatchCreateLabelsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LabelServiceClient.batch_create_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchCreateLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateLabels(
        _BaseLabelServiceRestTransport._BaseBatchDeactivateLabels, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.BatchDeactivateLabels")

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
            request: label_service.BatchDeactivateLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_service.BatchDeactivateLabelsResponse:
            r"""Call the batch deactivate labels method over HTTP.

            Args:
                request (~.label_service.BatchDeactivateLabelsRequest):
                    The request object. Request message for ``BatchDeactivateLabels`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_service.BatchDeactivateLabelsResponse:
                    Response message for ``BatchDeactivateLabels`` method.
            """

            http_options = _BaseLabelServiceRestTransport._BaseBatchDeactivateLabels._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseBatchDeactivateLabels,
                    "_BaseBatchDeactivateLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.BatchDeactivateLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchDeactivateLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._BatchDeactivateLabels._get_response(
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
            resp = label_service.BatchDeactivateLabelsResponse()
            pb_resp = label_service.BatchDeactivateLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        label_service.BatchDeactivateLabelsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LabelServiceClient.batch_deactivate_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchDeactivateLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateLabels(
        _BaseLabelServiceRestTransport._BaseBatchUpdateLabels, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.BatchUpdateLabels")

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
            request: label_service.BatchUpdateLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_service.BatchUpdateLabelsResponse:
            r"""Call the batch update labels method over HTTP.

            Args:
                request (~.label_service.BatchUpdateLabelsRequest):
                    The request object. Request object for ``BatchUpdateLabels`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_service.BatchUpdateLabelsResponse:
                    Response object for ``BatchUpdateLabels`` method.
            """

            http_options = _BaseLabelServiceRestTransport._BaseBatchUpdateLabels._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseBatchUpdateLabels,
                    "_BaseBatchUpdateLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.BatchUpdateLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchUpdateLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._BatchUpdateLabels._get_response(
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
            resp = label_service.BatchUpdateLabelsResponse()
            pb_resp = label_service.BatchUpdateLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = label_service.BatchUpdateLabelsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LabelServiceClient.batch_update_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "BatchUpdateLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLabel(
        _BaseLabelServiceRestTransport._BaseCreateLabel, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.CreateLabel")

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
            request: label_service.CreateLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_messages.Label:
            r"""Call the create label method over HTTP.

            Args:
                request (~.label_service.CreateLabelRequest):
                    The request object. Request object for ``CreateLabel`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_messages.Label:
                    A Label is additional information
                that can be added to an entity.

            """

            http_options = (
                _BaseLabelServiceRestTransport._BaseCreateLabel._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_label(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseCreateLabel,
                    "_BaseCreateLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.CreateLabel",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "CreateLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._CreateLabel._get_response(
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
            resp = label_messages.Label()
            pb_resp = label_messages.Label.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = label_messages.Label.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LabelServiceClient.create_label",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "CreateLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLabel(_BaseLabelServiceRestTransport._BaseGetLabel, LabelServiceRestStub):
        def __hash__(self):
            return hash("LabelServiceRestTransport.GetLabel")

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
            request: label_service.GetLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_messages.Label:
            r"""Call the get label method over HTTP.

            Args:
                request (~.label_service.GetLabelRequest):
                    The request object. Request object for ``GetLabel`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_messages.Label:
                    A Label is additional information
                that can be added to an entity.

            """

            http_options = (
                _BaseLabelServiceRestTransport._BaseGetLabel._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_label(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseGetLabel,
                    "_BaseGetLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.GetLabel",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "GetLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._GetLabel._get_response(
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
            resp = label_messages.Label()
            pb_resp = label_messages.Label.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = label_messages.Label.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LabelServiceClient.get_label",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "GetLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLabels(
        _BaseLabelServiceRestTransport._BaseListLabels, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.ListLabels")

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
            request: label_service.ListLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_service.ListLabelsResponse:
            r"""Call the list labels method over HTTP.

            Args:
                request (~.label_service.ListLabelsRequest):
                    The request object. Request object for ``ListLabels`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_service.ListLabelsResponse:
                    Response object for ``ListLabelsRequest`` containing
                matching ``Label`` objects.

            """

            http_options = (
                _BaseLabelServiceRestTransport._BaseListLabels._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_labels(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseListLabels,
                    "_BaseListLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.ListLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "ListLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._ListLabels._get_response(
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
            resp = label_service.ListLabelsResponse()
            pb_resp = label_service.ListLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = label_service.ListLabelsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.LabelServiceClient.list_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "ListLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLabel(
        _BaseLabelServiceRestTransport._BaseUpdateLabel, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.UpdateLabel")

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
            request: label_service.UpdateLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> label_messages.Label:
            r"""Call the update label method over HTTP.

            Args:
                request (~.label_service.UpdateLabelRequest):
                    The request object. Request object for ``UpdateLabel`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.label_messages.Label:
                    A Label is additional information
                that can be added to an entity.

            """

            http_options = (
                _BaseLabelServiceRestTransport._BaseUpdateLabel._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_label(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseUpdateLabel,
                    "_BaseUpdateLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.UpdateLabel",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "UpdateLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._UpdateLabel._get_response(
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
            resp = label_messages.Label()
            pb_resp = label_messages.Label.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = label_messages.Label.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.LabelServiceClient.update_label",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "UpdateLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_labels(
        self,
    ) -> Callable[
        [label_service.BatchActivateLabelsRequest],
        label_service.BatchActivateLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_labels(
        self,
    ) -> Callable[
        [label_service.BatchCreateLabelsRequest],
        label_service.BatchCreateLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_labels(
        self,
    ) -> Callable[
        [label_service.BatchDeactivateLabelsRequest],
        label_service.BatchDeactivateLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_labels(
        self,
    ) -> Callable[
        [label_service.BatchUpdateLabelsRequest],
        label_service.BatchUpdateLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_label(
        self,
    ) -> Callable[[label_service.CreateLabelRequest], label_messages.Label]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_label(
        self,
    ) -> Callable[[label_service.GetLabelRequest], label_messages.Label]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_labels(
        self,
    ) -> Callable[[label_service.ListLabelsRequest], label_service.ListLabelsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_label(
        self,
    ) -> Callable[[label_service.UpdateLabelRequest], label_messages.Label]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseLabelServiceRestTransport._BaseCancelOperation, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.CancelOperation")

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

            http_options = (
                _BaseLabelServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._CancelOperation._get_response(
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
        _BaseLabelServiceRestTransport._BaseGetOperation, LabelServiceRestStub
    ):
        def __hash__(self):
            return hash("LabelServiceRestTransport.GetOperation")

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
                _BaseLabelServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLabelServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.LabelServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LabelServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.LabelServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LabelService",
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


__all__ = ("LabelServiceRestTransport",)
