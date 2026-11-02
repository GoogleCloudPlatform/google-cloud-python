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

from google.cloud.dialogflow_v2beta1._compat import transcode_request
from google.cloud.dialogflow_v2beta1.types import knowledge_base
from google.cloud.dialogflow_v2beta1.types import knowledge_base as gcd_knowledge_base

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseKnowledgeBasesRestTransport

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


class KnowledgeBasesRestInterceptor:
    """Interceptor for KnowledgeBases.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the KnowledgeBasesRestTransport.

    .. code-block:: python
        class MyCustomKnowledgeBasesInterceptor(KnowledgeBasesRestInterceptor):
            def pre_create_knowledge_base(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_knowledge_base(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_knowledge_base(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_knowledge_base(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_knowledge_base(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_knowledge_bases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_knowledge_bases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_knowledge_base(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_knowledge_base(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = KnowledgeBasesRestTransport(interceptor=MyCustomKnowledgeBasesInterceptor())
        client = KnowledgeBasesClient(transport=transport)


    """

    def pre_create_knowledge_base(
        self,
        request: gcd_knowledge_base.CreateKnowledgeBaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_knowledge_base.CreateKnowledgeBaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_knowledge_base

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_create_knowledge_base(
        self, response: gcd_knowledge_base.KnowledgeBase
    ) -> gcd_knowledge_base.KnowledgeBase:
        """Post-rpc interceptor for create_knowledge_base

        DEPRECATED. Please use the `post_create_knowledge_base_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KnowledgeBases server but before
        it is returned to user code. This `post_create_knowledge_base` interceptor runs
        before the `post_create_knowledge_base_with_metadata` interceptor.
        """
        return response

    def post_create_knowledge_base_with_metadata(
        self,
        response: gcd_knowledge_base.KnowledgeBase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_knowledge_base.KnowledgeBase, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_knowledge_base

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KnowledgeBases server but before it is returned to user code.

        We recommend only using this `post_create_knowledge_base_with_metadata`
        interceptor in new development instead of the `post_create_knowledge_base` interceptor.
        When both interceptors are used, this `post_create_knowledge_base_with_metadata` interceptor runs after the
        `post_create_knowledge_base` interceptor. The (possibly modified) response returned by
        `post_create_knowledge_base` will be passed to
        `post_create_knowledge_base_with_metadata`.
        """
        return response, metadata

    def pre_delete_knowledge_base(
        self,
        request: knowledge_base.DeleteKnowledgeBaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        knowledge_base.DeleteKnowledgeBaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_knowledge_base

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def pre_get_knowledge_base(
        self,
        request: knowledge_base.GetKnowledgeBaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        knowledge_base.GetKnowledgeBaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_knowledge_base

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_get_knowledge_base(
        self, response: knowledge_base.KnowledgeBase
    ) -> knowledge_base.KnowledgeBase:
        """Post-rpc interceptor for get_knowledge_base

        DEPRECATED. Please use the `post_get_knowledge_base_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KnowledgeBases server but before
        it is returned to user code. This `post_get_knowledge_base` interceptor runs
        before the `post_get_knowledge_base_with_metadata` interceptor.
        """
        return response

    def post_get_knowledge_base_with_metadata(
        self,
        response: knowledge_base.KnowledgeBase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[knowledge_base.KnowledgeBase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_knowledge_base

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KnowledgeBases server but before it is returned to user code.

        We recommend only using this `post_get_knowledge_base_with_metadata`
        interceptor in new development instead of the `post_get_knowledge_base` interceptor.
        When both interceptors are used, this `post_get_knowledge_base_with_metadata` interceptor runs after the
        `post_get_knowledge_base` interceptor. The (possibly modified) response returned by
        `post_get_knowledge_base` will be passed to
        `post_get_knowledge_base_with_metadata`.
        """
        return response, metadata

    def pre_list_knowledge_bases(
        self,
        request: knowledge_base.ListKnowledgeBasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        knowledge_base.ListKnowledgeBasesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_knowledge_bases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_list_knowledge_bases(
        self, response: knowledge_base.ListKnowledgeBasesResponse
    ) -> knowledge_base.ListKnowledgeBasesResponse:
        """Post-rpc interceptor for list_knowledge_bases

        DEPRECATED. Please use the `post_list_knowledge_bases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KnowledgeBases server but before
        it is returned to user code. This `post_list_knowledge_bases` interceptor runs
        before the `post_list_knowledge_bases_with_metadata` interceptor.
        """
        return response

    def post_list_knowledge_bases_with_metadata(
        self,
        response: knowledge_base.ListKnowledgeBasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        knowledge_base.ListKnowledgeBasesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_knowledge_bases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KnowledgeBases server but before it is returned to user code.

        We recommend only using this `post_list_knowledge_bases_with_metadata`
        interceptor in new development instead of the `post_list_knowledge_bases` interceptor.
        When both interceptors are used, this `post_list_knowledge_bases_with_metadata` interceptor runs after the
        `post_list_knowledge_bases` interceptor. The (possibly modified) response returned by
        `post_list_knowledge_bases` will be passed to
        `post_list_knowledge_bases_with_metadata`.
        """
        return response, metadata

    def pre_update_knowledge_base(
        self,
        request: gcd_knowledge_base.UpdateKnowledgeBaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_knowledge_base.UpdateKnowledgeBaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_knowledge_base

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_update_knowledge_base(
        self, response: gcd_knowledge_base.KnowledgeBase
    ) -> gcd_knowledge_base.KnowledgeBase:
        """Post-rpc interceptor for update_knowledge_base

        DEPRECATED. Please use the `post_update_knowledge_base_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KnowledgeBases server but before
        it is returned to user code. This `post_update_knowledge_base` interceptor runs
        before the `post_update_knowledge_base_with_metadata` interceptor.
        """
        return response

    def post_update_knowledge_base_with_metadata(
        self,
        response: gcd_knowledge_base.KnowledgeBase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_knowledge_base.KnowledgeBase, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_knowledge_base

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KnowledgeBases server but before it is returned to user code.

        We recommend only using this `post_update_knowledge_base_with_metadata`
        interceptor in new development instead of the `post_update_knowledge_base` interceptor.
        When both interceptors are used, this `post_update_knowledge_base_with_metadata` interceptor runs after the
        `post_update_knowledge_base` interceptor. The (possibly modified) response returned by
        `post_update_knowledge_base` will be passed to
        `post_update_knowledge_base_with_metadata`.
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
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the KnowledgeBases server but before
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
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the KnowledgeBases server but before
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
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the KnowledgeBases server but before
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
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the KnowledgeBases server but before
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
        before they are sent to the KnowledgeBases server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the KnowledgeBases server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class KnowledgeBasesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: KnowledgeBasesRestInterceptor


class KnowledgeBasesRestTransport(_BaseKnowledgeBasesRestTransport):
    """REST backend synchronous transport for KnowledgeBases.

    Service for managing
    [KnowledgeBases][google.cloud.dialogflow.v2beta1.KnowledgeBase].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[KnowledgeBasesRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
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
            interceptor (Optional[KnowledgeBasesRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or KnowledgeBasesRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateKnowledgeBase(
        _BaseKnowledgeBasesRestTransport._BaseCreateKnowledgeBase,
        KnowledgeBasesRestStub,
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.CreateKnowledgeBase")

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
            request: gcd_knowledge_base.CreateKnowledgeBaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_knowledge_base.KnowledgeBase:
            r"""Call the create knowledge base method over HTTP.

            Args:
                request (~.gcd_knowledge_base.CreateKnowledgeBaseRequest):
                    The request object. Request message for
                [KnowledgeBases.CreateKnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBases.CreateKnowledgeBase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_knowledge_base.KnowledgeBase:
                    A knowledge base represents a collection of knowledge
                documents that you provide to Dialogflow. Your knowledge
                documents contain information that may be useful during
                conversations with end-users. Some Dialogflow features
                use knowledge bases when looking for a response to an
                end-user input.

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases`` resource is
                deprecated; only use ``projects.knowledgeBases``.

            """

            http_options = _BaseKnowledgeBasesRestTransport._BaseCreateKnowledgeBase._get_http_options()
            request, metadata = self._interceptor.pre_create_knowledge_base(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseCreateKnowledgeBase,
                    "_BaseCreateKnowledgeBase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.CreateKnowledgeBase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "CreateKnowledgeBase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._CreateKnowledgeBase._get_response(
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
            resp = gcd_knowledge_base.KnowledgeBase()
            pb_resp = gcd_knowledge_base.KnowledgeBase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_knowledge_base(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_knowledge_base_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_knowledge_base.KnowledgeBase.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.create_knowledge_base",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "CreateKnowledgeBase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteKnowledgeBase(
        _BaseKnowledgeBasesRestTransport._BaseDeleteKnowledgeBase,
        KnowledgeBasesRestStub,
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.DeleteKnowledgeBase")

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
            request: knowledge_base.DeleteKnowledgeBaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete knowledge base method over HTTP.

            Args:
                request (~.knowledge_base.DeleteKnowledgeBaseRequest):
                    The request object. Request message for
                [KnowledgeBases.DeleteKnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBases.DeleteKnowledgeBase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseKnowledgeBasesRestTransport._BaseDeleteKnowledgeBase._get_http_options()
            request, metadata = self._interceptor.pre_delete_knowledge_base(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseDeleteKnowledgeBase,
                    "_BaseDeleteKnowledgeBase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.DeleteKnowledgeBase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "DeleteKnowledgeBase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._DeleteKnowledgeBase._get_response(
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

    class _GetKnowledgeBase(
        _BaseKnowledgeBasesRestTransport._BaseGetKnowledgeBase, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.GetKnowledgeBase")

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
            request: knowledge_base.GetKnowledgeBaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> knowledge_base.KnowledgeBase:
            r"""Call the get knowledge base method over HTTP.

            Args:
                request (~.knowledge_base.GetKnowledgeBaseRequest):
                    The request object. Request message for
                [KnowledgeBases.GetKnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBases.GetKnowledgeBase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.knowledge_base.KnowledgeBase:
                    A knowledge base represents a collection of knowledge
                documents that you provide to Dialogflow. Your knowledge
                documents contain information that may be useful during
                conversations with end-users. Some Dialogflow features
                use knowledge bases when looking for a response to an
                end-user input.

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases`` resource is
                deprecated; only use ``projects.knowledgeBases``.

            """

            http_options = _BaseKnowledgeBasesRestTransport._BaseGetKnowledgeBase._get_http_options()
            request, metadata = self._interceptor.pre_get_knowledge_base(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseGetKnowledgeBase,
                    "_BaseGetKnowledgeBase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.GetKnowledgeBase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "GetKnowledgeBase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._GetKnowledgeBase._get_response(
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
            resp = knowledge_base.KnowledgeBase()
            pb_resp = knowledge_base.KnowledgeBase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_knowledge_base(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_knowledge_base_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = knowledge_base.KnowledgeBase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.get_knowledge_base",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "GetKnowledgeBase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListKnowledgeBases(
        _BaseKnowledgeBasesRestTransport._BaseListKnowledgeBases, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.ListKnowledgeBases")

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
            request: knowledge_base.ListKnowledgeBasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> knowledge_base.ListKnowledgeBasesResponse:
            r"""Call the list knowledge bases method over HTTP.

            Args:
                request (~.knowledge_base.ListKnowledgeBasesRequest):
                    The request object. Request message for
                [KnowledgeBases.ListKnowledgeBases][google.cloud.dialogflow.v2beta1.KnowledgeBases.ListKnowledgeBases].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.knowledge_base.ListKnowledgeBasesResponse:
                    Response message for
                [KnowledgeBases.ListKnowledgeBases][google.cloud.dialogflow.v2beta1.KnowledgeBases.ListKnowledgeBases].

            """

            http_options = _BaseKnowledgeBasesRestTransport._BaseListKnowledgeBases._get_http_options()
            request, metadata = self._interceptor.pre_list_knowledge_bases(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseListKnowledgeBases,
                    "_BaseListKnowledgeBases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.ListKnowledgeBases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "ListKnowledgeBases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._ListKnowledgeBases._get_response(
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
            resp = knowledge_base.ListKnowledgeBasesResponse()
            pb_resp = knowledge_base.ListKnowledgeBasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_knowledge_bases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_knowledge_bases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        knowledge_base.ListKnowledgeBasesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.list_knowledge_bases",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "ListKnowledgeBases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateKnowledgeBase(
        _BaseKnowledgeBasesRestTransport._BaseUpdateKnowledgeBase,
        KnowledgeBasesRestStub,
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.UpdateKnowledgeBase")

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
            request: gcd_knowledge_base.UpdateKnowledgeBaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_knowledge_base.KnowledgeBase:
            r"""Call the update knowledge base method over HTTP.

            Args:
                request (~.gcd_knowledge_base.UpdateKnowledgeBaseRequest):
                    The request object. Request message for
                [KnowledgeBases.UpdateKnowledgeBase][google.cloud.dialogflow.v2beta1.KnowledgeBases.UpdateKnowledgeBase].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_knowledge_base.KnowledgeBase:
                    A knowledge base represents a collection of knowledge
                documents that you provide to Dialogflow. Your knowledge
                documents contain information that may be useful during
                conversations with end-users. Some Dialogflow features
                use knowledge bases when looking for a response to an
                end-user input.

                For more information, see the `knowledge base
                guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

                Note: The ``projects.agent.knowledgeBases`` resource is
                deprecated; only use ``projects.knowledgeBases``.

            """

            http_options = _BaseKnowledgeBasesRestTransport._BaseUpdateKnowledgeBase._get_http_options()
            request, metadata = self._interceptor.pre_update_knowledge_base(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseUpdateKnowledgeBase,
                    "_BaseUpdateKnowledgeBase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.UpdateKnowledgeBase",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "UpdateKnowledgeBase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._UpdateKnowledgeBase._get_response(
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
            resp = gcd_knowledge_base.KnowledgeBase()
            pb_resp = gcd_knowledge_base.KnowledgeBase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_knowledge_base(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_knowledge_base_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_knowledge_base.KnowledgeBase.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.update_knowledge_base",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "UpdateKnowledgeBase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_knowledge_base(
        self,
    ) -> Callable[
        [gcd_knowledge_base.CreateKnowledgeBaseRequest],
        gcd_knowledge_base.KnowledgeBase,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateKnowledgeBase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_knowledge_base(
        self,
    ) -> Callable[[knowledge_base.DeleteKnowledgeBaseRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteKnowledgeBase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_knowledge_base(
        self,
    ) -> Callable[
        [knowledge_base.GetKnowledgeBaseRequest], knowledge_base.KnowledgeBase
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKnowledgeBase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_knowledge_bases(
        self,
    ) -> Callable[
        [knowledge_base.ListKnowledgeBasesRequest],
        knowledge_base.ListKnowledgeBasesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListKnowledgeBases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_knowledge_base(
        self,
    ) -> Callable[
        [gcd_knowledge_base.UpdateKnowledgeBaseRequest],
        gcd_knowledge_base.KnowledgeBase,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateKnowledgeBase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseKnowledgeBasesRestTransport._BaseGetLocation, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.GetLocation")

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
                _BaseKnowledgeBasesRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
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
        _BaseKnowledgeBasesRestTransport._BaseListLocations, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.ListLocations")

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
                _BaseKnowledgeBasesRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
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
        _BaseKnowledgeBasesRestTransport._BaseCancelOperation, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.CancelOperation")

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

            http_options = _BaseKnowledgeBasesRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._CancelOperation._get_response(
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
        _BaseKnowledgeBasesRestTransport._BaseGetOperation, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.GetOperation")

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
                _BaseKnowledgeBasesRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
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
        _BaseKnowledgeBasesRestTransport._BaseListOperations, KnowledgeBasesRestStub
    ):
        def __hash__(self):
            return hash("KnowledgeBasesRestTransport.ListOperations")

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
                _BaseKnowledgeBasesRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKnowledgeBasesRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.KnowledgeBasesClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KnowledgeBasesRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.KnowledgeBasesAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.KnowledgeBases",
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


__all__ = ("KnowledgeBasesRestTransport",)
