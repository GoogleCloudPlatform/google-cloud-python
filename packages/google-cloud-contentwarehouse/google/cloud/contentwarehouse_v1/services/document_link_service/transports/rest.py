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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.contentwarehouse_v1._compat import transcode_request
from google.cloud.contentwarehouse_v1.types import document_link_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDocumentLinkServiceRestTransport

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


class DocumentLinkServiceRestInterceptor:
    """Interceptor for DocumentLinkService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DocumentLinkServiceRestTransport.

    .. code-block:: python
        class MyCustomDocumentLinkServiceInterceptor(DocumentLinkServiceRestInterceptor):
            def pre_create_document_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_document_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_document_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_list_linked_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_linked_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_linked_targets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_linked_targets(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DocumentLinkServiceRestTransport(interceptor=MyCustomDocumentLinkServiceInterceptor())
        client = DocumentLinkServiceClient(transport=transport)


    """

    def pre_create_document_link(
        self,
        request: document_link_service.CreateDocumentLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.CreateDocumentLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_document_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentLinkService server.
        """
        return request, metadata

    def post_create_document_link(
        self, response: document_link_service.DocumentLink
    ) -> document_link_service.DocumentLink:
        """Post-rpc interceptor for create_document_link

        DEPRECATED. Please use the `post_create_document_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentLinkService server but before
        it is returned to user code. This `post_create_document_link` interceptor runs
        before the `post_create_document_link_with_metadata` interceptor.
        """
        return response

    def post_create_document_link_with_metadata(
        self,
        response: document_link_service.DocumentLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.DocumentLink, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_document_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentLinkService server but before it is returned to user code.

        We recommend only using this `post_create_document_link_with_metadata`
        interceptor in new development instead of the `post_create_document_link` interceptor.
        When both interceptors are used, this `post_create_document_link_with_metadata` interceptor runs after the
        `post_create_document_link` interceptor. The (possibly modified) response returned by
        `post_create_document_link` will be passed to
        `post_create_document_link_with_metadata`.
        """
        return response, metadata

    def pre_delete_document_link(
        self,
        request: document_link_service.DeleteDocumentLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.DeleteDocumentLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_document_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentLinkService server.
        """
        return request, metadata

    def pre_list_linked_sources(
        self,
        request: document_link_service.ListLinkedSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.ListLinkedSourcesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_linked_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentLinkService server.
        """
        return request, metadata

    def post_list_linked_sources(
        self, response: document_link_service.ListLinkedSourcesResponse
    ) -> document_link_service.ListLinkedSourcesResponse:
        """Post-rpc interceptor for list_linked_sources

        DEPRECATED. Please use the `post_list_linked_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentLinkService server but before
        it is returned to user code. This `post_list_linked_sources` interceptor runs
        before the `post_list_linked_sources_with_metadata` interceptor.
        """
        return response

    def post_list_linked_sources_with_metadata(
        self,
        response: document_link_service.ListLinkedSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.ListLinkedSourcesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_linked_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentLinkService server but before it is returned to user code.

        We recommend only using this `post_list_linked_sources_with_metadata`
        interceptor in new development instead of the `post_list_linked_sources` interceptor.
        When both interceptors are used, this `post_list_linked_sources_with_metadata` interceptor runs after the
        `post_list_linked_sources` interceptor. The (possibly modified) response returned by
        `post_list_linked_sources` will be passed to
        `post_list_linked_sources_with_metadata`.
        """
        return response, metadata

    def pre_list_linked_targets(
        self,
        request: document_link_service.ListLinkedTargetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.ListLinkedTargetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_linked_targets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentLinkService server.
        """
        return request, metadata

    def post_list_linked_targets(
        self, response: document_link_service.ListLinkedTargetsResponse
    ) -> document_link_service.ListLinkedTargetsResponse:
        """Post-rpc interceptor for list_linked_targets

        DEPRECATED. Please use the `post_list_linked_targets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentLinkService server but before
        it is returned to user code. This `post_list_linked_targets` interceptor runs
        before the `post_list_linked_targets_with_metadata` interceptor.
        """
        return response

    def post_list_linked_targets_with_metadata(
        self,
        response: document_link_service.ListLinkedTargetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_link_service.ListLinkedTargetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_linked_targets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentLinkService server but before it is returned to user code.

        We recommend only using this `post_list_linked_targets_with_metadata`
        interceptor in new development instead of the `post_list_linked_targets` interceptor.
        When both interceptors are used, this `post_list_linked_targets_with_metadata` interceptor runs after the
        `post_list_linked_targets` interceptor. The (possibly modified) response returned by
        `post_list_linked_targets` will be passed to
        `post_list_linked_targets_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentLinkService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DocumentLinkService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DocumentLinkServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DocumentLinkServiceRestInterceptor


class DocumentLinkServiceRestTransport(_BaseDocumentLinkServiceRestTransport):
    """REST backend synchronous transport for DocumentLinkService.

    This service lets you manage document-links.
    Document-Links are treated as sub-resources under source
    documents.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "contentwarehouse.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DocumentLinkServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'contentwarehouse.googleapis.com').
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
            interceptor (Optional[DocumentLinkServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DocumentLinkServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateDocumentLink(
        _BaseDocumentLinkServiceRestTransport._BaseCreateDocumentLink,
        DocumentLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentLinkServiceRestTransport.CreateDocumentLink")

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
            request: document_link_service.CreateDocumentLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_link_service.DocumentLink:
            r"""Call the create document link method over HTTP.

            Args:
                request (~.document_link_service.CreateDocumentLinkRequest):
                    The request object. Request message for
                DocumentLinkService.CreateDocumentLink.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_link_service.DocumentLink:
                    A document-link between source and
                target document.

            """

            http_options = _BaseDocumentLinkServiceRestTransport._BaseCreateDocumentLink._get_http_options()
            request, metadata = self._interceptor.pre_create_document_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentLinkServiceRestTransport._BaseCreateDocumentLink,
                    "_BaseCreateDocumentLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.CreateDocumentLink",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "CreateDocumentLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentLinkServiceRestTransport._CreateDocumentLink._get_response(
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
            resp = document_link_service.DocumentLink()
            pb_resp = document_link_service.DocumentLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_document_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_document_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_link_service.DocumentLink.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.create_document_link",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "CreateDocumentLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDocumentLink(
        _BaseDocumentLinkServiceRestTransport._BaseDeleteDocumentLink,
        DocumentLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentLinkServiceRestTransport.DeleteDocumentLink")

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
            request: document_link_service.DeleteDocumentLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete document link method over HTTP.

            Args:
                request (~.document_link_service.DeleteDocumentLinkRequest):
                    The request object. Request message for
                DocumentLinkService.DeleteDocumentLink.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDocumentLinkServiceRestTransport._BaseDeleteDocumentLink._get_http_options()
            request, metadata = self._interceptor.pre_delete_document_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentLinkServiceRestTransport._BaseDeleteDocumentLink,
                    "_BaseDeleteDocumentLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.DeleteDocumentLink",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "DeleteDocumentLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentLinkServiceRestTransport._DeleteDocumentLink._get_response(
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

    class _ListLinkedSources(
        _BaseDocumentLinkServiceRestTransport._BaseListLinkedSources,
        DocumentLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentLinkServiceRestTransport.ListLinkedSources")

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
            request: document_link_service.ListLinkedSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_link_service.ListLinkedSourcesResponse:
            r"""Call the list linked sources method over HTTP.

            Args:
                request (~.document_link_service.ListLinkedSourcesRequest):
                    The request object. Response message for
                DocumentLinkService.ListLinkedSources.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_link_service.ListLinkedSourcesResponse:
                    Response message for
                DocumentLinkService.ListLinkedSources.

            """

            http_options = _BaseDocumentLinkServiceRestTransport._BaseListLinkedSources._get_http_options()
            request, metadata = self._interceptor.pre_list_linked_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentLinkServiceRestTransport._BaseListLinkedSources,
                    "_BaseListLinkedSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.ListLinkedSources",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "ListLinkedSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentLinkServiceRestTransport._ListLinkedSources._get_response(
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
            resp = document_link_service.ListLinkedSourcesResponse()
            pb_resp = document_link_service.ListLinkedSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_linked_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_linked_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_link_service.ListLinkedSourcesResponse.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.list_linked_sources",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "ListLinkedSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLinkedTargets(
        _BaseDocumentLinkServiceRestTransport._BaseListLinkedTargets,
        DocumentLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentLinkServiceRestTransport.ListLinkedTargets")

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
            request: document_link_service.ListLinkedTargetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_link_service.ListLinkedTargetsResponse:
            r"""Call the list linked targets method over HTTP.

            Args:
                request (~.document_link_service.ListLinkedTargetsRequest):
                    The request object. Request message for
                DocumentLinkService.ListLinkedTargets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_link_service.ListLinkedTargetsResponse:
                    Response message for
                DocumentLinkService.ListLinkedTargets.

            """

            http_options = _BaseDocumentLinkServiceRestTransport._BaseListLinkedTargets._get_http_options()
            request, metadata = self._interceptor.pre_list_linked_targets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentLinkServiceRestTransport._BaseListLinkedTargets,
                    "_BaseListLinkedTargets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.ListLinkedTargets",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "ListLinkedTargets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DocumentLinkServiceRestTransport._ListLinkedTargets._get_response(
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
            resp = document_link_service.ListLinkedTargetsResponse()
            pb_resp = document_link_service.ListLinkedTargetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_linked_targets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_linked_targets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        document_link_service.ListLinkedTargetsResponse.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.list_linked_targets",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "ListLinkedTargets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_document_link(
        self,
    ) -> Callable[
        [document_link_service.CreateDocumentLinkRequest],
        document_link_service.DocumentLink,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDocumentLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_document_link(
        self,
    ) -> Callable[[document_link_service.DeleteDocumentLinkRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDocumentLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_linked_sources(
        self,
    ) -> Callable[
        [document_link_service.ListLinkedSourcesRequest],
        document_link_service.ListLinkedSourcesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLinkedSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_linked_targets(
        self,
    ) -> Callable[
        [document_link_service.ListLinkedTargetsRequest],
        document_link_service.ListLinkedTargetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLinkedTargets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDocumentLinkServiceRestTransport._BaseGetOperation,
        DocumentLinkServiceRestStub,
    ):
        def __hash__(self):
            return hash("DocumentLinkServiceRestTransport.GetOperation")

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

            http_options = _BaseDocumentLinkServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentLinkServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentLinkServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentLinkServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentLinkServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentLinkService",
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


__all__ = ("DocumentLinkServiceRestTransport",)
