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
from google.cloud.contentwarehouse_v1.types import document as gcc_document
from google.cloud.contentwarehouse_v1.types import (
    document_service,
    document_service_request,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDocumentServiceRestTransport

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


class DocumentServiceRestInterceptor:
    """Interceptor for DocumentService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DocumentServiceRestTransport.

    .. code-block:: python
        class MyCustomDocumentServiceInterceptor(DocumentServiceRestInterceptor):
            def pre_create_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_fetch_acl(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_acl(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lock_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lock_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_documents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_documents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_acl(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_acl(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_document(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DocumentServiceRestTransport(interceptor=MyCustomDocumentServiceInterceptor())
        client = DocumentServiceClient(transport=transport)


    """

    def pre_create_document(
        self,
        request: document_service_request.CreateDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.CreateDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_create_document(
        self, response: document_service.CreateDocumentResponse
    ) -> document_service.CreateDocumentResponse:
        """Post-rpc interceptor for create_document

        DEPRECATED. Please use the `post_create_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_create_document` interceptor runs
        before the `post_create_document_with_metadata` interceptor.
        """
        return response

    def post_create_document_with_metadata(
        self,
        response: document_service.CreateDocumentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service.CreateDocumentResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_create_document_with_metadata`
        interceptor in new development instead of the `post_create_document` interceptor.
        When both interceptors are used, this `post_create_document_with_metadata` interceptor runs after the
        `post_create_document` interceptor. The (possibly modified) response returned by
        `post_create_document` will be passed to
        `post_create_document_with_metadata`.
        """
        return response, metadata

    def pre_delete_document(
        self,
        request: document_service_request.DeleteDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.DeleteDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def pre_fetch_acl(
        self,
        request: document_service_request.FetchAclRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.FetchAclRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_acl

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_fetch_acl(
        self, response: document_service.FetchAclResponse
    ) -> document_service.FetchAclResponse:
        """Post-rpc interceptor for fetch_acl

        DEPRECATED. Please use the `post_fetch_acl_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_fetch_acl` interceptor runs
        before the `post_fetch_acl_with_metadata` interceptor.
        """
        return response

    def post_fetch_acl_with_metadata(
        self,
        response: document_service.FetchAclResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service.FetchAclResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_acl

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_fetch_acl_with_metadata`
        interceptor in new development instead of the `post_fetch_acl` interceptor.
        When both interceptors are used, this `post_fetch_acl_with_metadata` interceptor runs after the
        `post_fetch_acl` interceptor. The (possibly modified) response returned by
        `post_fetch_acl` will be passed to
        `post_fetch_acl_with_metadata`.
        """
        return response, metadata

    def pre_get_document(
        self,
        request: document_service_request.GetDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.GetDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_get_document(
        self, response: gcc_document.Document
    ) -> gcc_document.Document:
        """Post-rpc interceptor for get_document

        DEPRECATED. Please use the `post_get_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_get_document` interceptor runs
        before the `post_get_document_with_metadata` interceptor.
        """
        return response

    def post_get_document_with_metadata(
        self,
        response: gcc_document.Document,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_document.Document, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_get_document_with_metadata`
        interceptor in new development instead of the `post_get_document` interceptor.
        When both interceptors are used, this `post_get_document_with_metadata` interceptor runs after the
        `post_get_document` interceptor. The (possibly modified) response returned by
        `post_get_document` will be passed to
        `post_get_document_with_metadata`.
        """
        return response, metadata

    def pre_lock_document(
        self,
        request: document_service_request.LockDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.LockDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for lock_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_lock_document(
        self, response: gcc_document.Document
    ) -> gcc_document.Document:
        """Post-rpc interceptor for lock_document

        DEPRECATED. Please use the `post_lock_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_lock_document` interceptor runs
        before the `post_lock_document_with_metadata` interceptor.
        """
        return response

    def post_lock_document_with_metadata(
        self,
        response: gcc_document.Document,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_document.Document, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for lock_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_lock_document_with_metadata`
        interceptor in new development instead of the `post_lock_document` interceptor.
        When both interceptors are used, this `post_lock_document_with_metadata` interceptor runs after the
        `post_lock_document` interceptor. The (possibly modified) response returned by
        `post_lock_document` will be passed to
        `post_lock_document_with_metadata`.
        """
        return response, metadata

    def pre_search_documents(
        self,
        request: document_service_request.SearchDocumentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.SearchDocumentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_documents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_search_documents(
        self, response: document_service.SearchDocumentsResponse
    ) -> document_service.SearchDocumentsResponse:
        """Post-rpc interceptor for search_documents

        DEPRECATED. Please use the `post_search_documents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_search_documents` interceptor runs
        before the `post_search_documents_with_metadata` interceptor.
        """
        return response

    def post_search_documents_with_metadata(
        self,
        response: document_service.SearchDocumentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service.SearchDocumentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_documents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_search_documents_with_metadata`
        interceptor in new development instead of the `post_search_documents` interceptor.
        When both interceptors are used, this `post_search_documents_with_metadata` interceptor runs after the
        `post_search_documents` interceptor. The (possibly modified) response returned by
        `post_search_documents` will be passed to
        `post_search_documents_with_metadata`.
        """
        return response, metadata

    def pre_set_acl(
        self,
        request: document_service_request.SetAclRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.SetAclRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_acl

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_set_acl(
        self, response: document_service.SetAclResponse
    ) -> document_service.SetAclResponse:
        """Post-rpc interceptor for set_acl

        DEPRECATED. Please use the `post_set_acl_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_set_acl` interceptor runs
        before the `post_set_acl_with_metadata` interceptor.
        """
        return response

    def post_set_acl_with_metadata(
        self,
        response: document_service.SetAclResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service.SetAclResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for set_acl

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_set_acl_with_metadata`
        interceptor in new development instead of the `post_set_acl` interceptor.
        When both interceptors are used, this `post_set_acl_with_metadata` interceptor runs after the
        `post_set_acl` interceptor. The (possibly modified) response returned by
        `post_set_acl` will be passed to
        `post_set_acl_with_metadata`.
        """
        return response, metadata

    def pre_update_document(
        self,
        request: document_service_request.UpdateDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service_request.UpdateDocumentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_update_document(
        self, response: document_service.UpdateDocumentResponse
    ) -> document_service.UpdateDocumentResponse:
        """Post-rpc interceptor for update_document

        DEPRECATED. Please use the `post_update_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code. This `post_update_document` interceptor runs
        before the `post_update_document_with_metadata` interceptor.
        """
        return response

    def post_update_document_with_metadata(
        self,
        response: document_service.UpdateDocumentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        document_service.UpdateDocumentResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DocumentService server but before it is returned to user code.

        We recommend only using this `post_update_document_with_metadata`
        interceptor in new development instead of the `post_update_document` interceptor.
        When both interceptors are used, this `post_update_document_with_metadata` interceptor runs after the
        `post_update_document` interceptor. The (possibly modified) response returned by
        `post_update_document` will be passed to
        `post_update_document_with_metadata`.
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
        before they are sent to the DocumentService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DocumentService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DocumentServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DocumentServiceRestInterceptor


class DocumentServiceRestTransport(_BaseDocumentServiceRestTransport):
    """REST backend synchronous transport for DocumentService.

    This service lets you manage document.

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
        interceptor: Optional[DocumentServiceRestInterceptor] = None,
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
            interceptor (Optional[DocumentServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DocumentServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateDocument(
        _BaseDocumentServiceRestTransport._BaseCreateDocument, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.CreateDocument")

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
            request: document_service_request.CreateDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_service.CreateDocumentResponse:
            r"""Call the create document method over HTTP.

            Args:
                request (~.document_service_request.CreateDocumentRequest):
                    The request object. Request message for
                DocumentService.CreateDocument.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_service.CreateDocumentResponse:
                    Response message for
                DocumentService.CreateDocument.

            """

            http_options = _BaseDocumentServiceRestTransport._BaseCreateDocument._get_http_options()
            request, metadata = self._interceptor.pre_create_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseCreateDocument,
                    "_BaseCreateDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.CreateDocument",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "CreateDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._CreateDocument._get_response(
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
            resp = document_service.CreateDocumentResponse()
            pb_resp = document_service.CreateDocumentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_document_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_service.CreateDocumentResponse.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.create_document",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "CreateDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDocument(
        _BaseDocumentServiceRestTransport._BaseDeleteDocument, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.DeleteDocument")

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
            request: document_service_request.DeleteDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete document method over HTTP.

            Args:
                request (~.document_service_request.DeleteDocumentRequest):
                    The request object. Request message for
                DocumentService.DeleteDocument.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDocumentServiceRestTransport._BaseDeleteDocument._get_http_options()
            request, metadata = self._interceptor.pre_delete_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseDeleteDocument,
                    "_BaseDeleteDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.DeleteDocument",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "DeleteDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._DeleteDocument._get_response(
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

    class _FetchAcl(
        _BaseDocumentServiceRestTransport._BaseFetchAcl, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.FetchAcl")

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
            request: document_service_request.FetchAclRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_service.FetchAclResponse:
            r"""Call the fetch acl method over HTTP.

            Args:
                request (~.document_service_request.FetchAclRequest):
                    The request object. Request message for
                DocumentService.FetchAcl
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_service.FetchAclResponse:
                    Response message for
                DocumentService.FetchAcl.

            """

            http_options = (
                _BaseDocumentServiceRestTransport._BaseFetchAcl._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_acl(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseFetchAcl,
                    "_BaseFetchAcl__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.FetchAcl",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "FetchAcl",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._FetchAcl._get_response(
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
            resp = document_service.FetchAclResponse()
            pb_resp = document_service.FetchAclResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_acl(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_acl_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_service.FetchAclResponse.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.fetch_acl",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "FetchAcl",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDocument(
        _BaseDocumentServiceRestTransport._BaseGetDocument, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.GetDocument")

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
            request: document_service_request.GetDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_document.Document:
            r"""Call the get document method over HTTP.

            Args:
                request (~.document_service_request.GetDocumentRequest):
                    The request object. Request message for
                DocumentService.GetDocument.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_document.Document:
                    Defines the structure for content
                warehouse document proto.

            """

            http_options = (
                _BaseDocumentServiceRestTransport._BaseGetDocument._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseGetDocument,
                    "_BaseGetDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.GetDocument",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "GetDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._GetDocument._get_response(
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
            resp = gcc_document.Document()
            pb_resp = gcc_document.Document.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_document_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_document.Document.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.get_document",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "GetDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LockDocument(
        _BaseDocumentServiceRestTransport._BaseLockDocument, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.LockDocument")

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
            request: document_service_request.LockDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_document.Document:
            r"""Call the lock document method over HTTP.

            Args:
                request (~.document_service_request.LockDocumentRequest):
                    The request object. Request message for
                DocumentService.LockDocument.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_document.Document:
                    Defines the structure for content
                warehouse document proto.

            """

            http_options = (
                _BaseDocumentServiceRestTransport._BaseLockDocument._get_http_options()
            )
            request, metadata = self._interceptor.pre_lock_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseLockDocument,
                    "_BaseLockDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.LockDocument",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "LockDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._LockDocument._get_response(
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
            resp = gcc_document.Document()
            pb_resp = gcc_document.Document.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lock_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lock_document_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_document.Document.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.lock_document",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "LockDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchDocuments(
        _BaseDocumentServiceRestTransport._BaseSearchDocuments, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.SearchDocuments")

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
            request: document_service_request.SearchDocumentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_service.SearchDocumentsResponse:
            r"""Call the search documents method over HTTP.

            Args:
                request (~.document_service_request.SearchDocumentsRequest):
                    The request object. Request message for
                DocumentService.SearchDocuments.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_service.SearchDocumentsResponse:
                    Response message for
                DocumentService.SearchDocuments.

            """

            http_options = _BaseDocumentServiceRestTransport._BaseSearchDocuments._get_http_options()
            request, metadata = self._interceptor.pre_search_documents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseSearchDocuments,
                    "_BaseSearchDocuments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.SearchDocuments",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "SearchDocuments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._SearchDocuments._get_response(
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
            resp = document_service.SearchDocumentsResponse()
            pb_resp = document_service.SearchDocumentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_documents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_documents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_service.SearchDocumentsResponse.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.search_documents",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "SearchDocuments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetAcl(
        _BaseDocumentServiceRestTransport._BaseSetAcl, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.SetAcl")

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
            request: document_service_request.SetAclRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_service.SetAclResponse:
            r"""Call the set acl method over HTTP.

            Args:
                request (~.document_service_request.SetAclRequest):
                    The request object. Request message for
                DocumentService.SetAcl.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_service.SetAclResponse:
                    Response message for
                DocumentService.SetAcl.

            """

            http_options = (
                _BaseDocumentServiceRestTransport._BaseSetAcl._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_acl(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseSetAcl,
                    "_BaseSetAcl__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.SetAcl",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "SetAcl",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._SetAcl._get_response(
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
            resp = document_service.SetAclResponse()
            pb_resp = document_service.SetAclResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_acl(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_acl_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_service.SetAclResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.set_acl",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "SetAcl",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDocument(
        _BaseDocumentServiceRestTransport._BaseUpdateDocument, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.UpdateDocument")

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
            request: document_service_request.UpdateDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> document_service.UpdateDocumentResponse:
            r"""Call the update document method over HTTP.

            Args:
                request (~.document_service_request.UpdateDocumentRequest):
                    The request object. Request message for
                DocumentService.UpdateDocument.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.document_service.UpdateDocumentResponse:
                    Response message for
                DocumentService.UpdateDocument.

            """

            http_options = _BaseDocumentServiceRestTransport._BaseUpdateDocument._get_http_options()
            request, metadata = self._interceptor.pre_update_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseUpdateDocument,
                    "_BaseUpdateDocument__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.UpdateDocument",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "UpdateDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._UpdateDocument._get_response(
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
            resp = document_service.UpdateDocumentResponse()
            pb_resp = document_service.UpdateDocumentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_document(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_document_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = document_service.UpdateDocumentResponse.to_json(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceClient.update_document",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "UpdateDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_document(
        self,
    ) -> Callable[
        [document_service_request.CreateDocumentRequest],
        document_service.CreateDocumentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_document(
        self,
    ) -> Callable[[document_service_request.DeleteDocumentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_acl(
        self,
    ) -> Callable[
        [document_service_request.FetchAclRequest], document_service.FetchAclResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchAcl(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_document(
        self,
    ) -> Callable[[document_service_request.GetDocumentRequest], gcc_document.Document]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lock_document(
        self,
    ) -> Callable[
        [document_service_request.LockDocumentRequest], gcc_document.Document
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LockDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_documents(
        self,
    ) -> Callable[
        [document_service_request.SearchDocumentsRequest],
        document_service.SearchDocumentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchDocuments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_acl(
        self,
    ) -> Callable[
        [document_service_request.SetAclRequest], document_service.SetAclResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetAcl(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_document(
        self,
    ) -> Callable[
        [document_service_request.UpdateDocumentRequest],
        document_service.UpdateDocumentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDocumentServiceRestTransport._BaseGetOperation, DocumentServiceRestStub
    ):
        def __hash__(self):
            return hash("DocumentServiceRestTransport.GetOperation")

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
                _BaseDocumentServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDocumentServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.contentwarehouse_v1.DocumentServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DocumentServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.contentwarehouse_v1.DocumentServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.contentwarehouse.v1.DocumentService",
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


__all__ = ("DocumentServiceRestTransport",)
