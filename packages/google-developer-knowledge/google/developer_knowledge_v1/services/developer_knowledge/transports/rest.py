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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.developer_knowledge_v1._compat import transcode_request
from google.developer_knowledge_v1.types import developerknowledge

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDeveloperKnowledgeRestTransport

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


class DeveloperKnowledgeRestInterceptor:
    """Interceptor for DeveloperKnowledge.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DeveloperKnowledgeRestTransport.

    .. code-block:: python
        class MyCustomDeveloperKnowledgeInterceptor(DeveloperKnowledgeRestInterceptor):
            def pre_answer_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_answer_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_get_documents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_get_documents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_document_chunks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_document_chunks(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DeveloperKnowledgeRestTransport(interceptor=MyCustomDeveloperKnowledgeInterceptor())
        client = DeveloperKnowledgeClient(transport=transport)


    """

    def pre_answer_query(
        self,
        request: developerknowledge.AnswerQueryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.AnswerQueryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for answer_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperKnowledge server.
        """
        return request, metadata

    def post_answer_query(
        self, response: developerknowledge.AnswerQueryResponse
    ) -> developerknowledge.AnswerQueryResponse:
        """Post-rpc interceptor for answer_query

        DEPRECATED. Please use the `post_answer_query_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperKnowledge server but before
        it is returned to user code. This `post_answer_query` interceptor runs
        before the `post_answer_query_with_metadata` interceptor.
        """
        return response

    def post_answer_query_with_metadata(
        self,
        response: developerknowledge.AnswerQueryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.AnswerQueryResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for answer_query

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperKnowledge server but before it is returned to user code.

        We recommend only using this `post_answer_query_with_metadata`
        interceptor in new development instead of the `post_answer_query` interceptor.
        When both interceptors are used, this `post_answer_query_with_metadata` interceptor runs after the
        `post_answer_query` interceptor. The (possibly modified) response returned by
        `post_answer_query` will be passed to
        `post_answer_query_with_metadata`.
        """
        return response, metadata

    def pre_batch_get_documents(
        self,
        request: developerknowledge.BatchGetDocumentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.BatchGetDocumentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_get_documents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperKnowledge server.
        """
        return request, metadata

    def post_batch_get_documents(
        self, response: developerknowledge.BatchGetDocumentsResponse
    ) -> developerknowledge.BatchGetDocumentsResponse:
        """Post-rpc interceptor for batch_get_documents

        DEPRECATED. Please use the `post_batch_get_documents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperKnowledge server but before
        it is returned to user code. This `post_batch_get_documents` interceptor runs
        before the `post_batch_get_documents_with_metadata` interceptor.
        """
        return response

    def post_batch_get_documents_with_metadata(
        self,
        response: developerknowledge.BatchGetDocumentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.BatchGetDocumentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_get_documents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperKnowledge server but before it is returned to user code.

        We recommend only using this `post_batch_get_documents_with_metadata`
        interceptor in new development instead of the `post_batch_get_documents` interceptor.
        When both interceptors are used, this `post_batch_get_documents_with_metadata` interceptor runs after the
        `post_batch_get_documents` interceptor. The (possibly modified) response returned by
        `post_batch_get_documents` will be passed to
        `post_batch_get_documents_with_metadata`.
        """
        return response, metadata

    def pre_get_document(
        self,
        request: developerknowledge.GetDocumentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.GetDocumentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperKnowledge server.
        """
        return request, metadata

    def post_get_document(
        self, response: developerknowledge.Document
    ) -> developerknowledge.Document:
        """Post-rpc interceptor for get_document

        DEPRECATED. Please use the `post_get_document_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperKnowledge server but before
        it is returned to user code. This `post_get_document` interceptor runs
        before the `post_get_document_with_metadata` interceptor.
        """
        return response

    def post_get_document_with_metadata(
        self,
        response: developerknowledge.Document,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[developerknowledge.Document, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_document

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperKnowledge server but before it is returned to user code.

        We recommend only using this `post_get_document_with_metadata`
        interceptor in new development instead of the `post_get_document` interceptor.
        When both interceptors are used, this `post_get_document_with_metadata` interceptor runs after the
        `post_get_document` interceptor. The (possibly modified) response returned by
        `post_get_document` will be passed to
        `post_get_document_with_metadata`.
        """
        return response, metadata

    def pre_search_document_chunks(
        self,
        request: developerknowledge.SearchDocumentChunksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.SearchDocumentChunksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_document_chunks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperKnowledge server.
        """
        return request, metadata

    def post_search_document_chunks(
        self, response: developerknowledge.SearchDocumentChunksResponse
    ) -> developerknowledge.SearchDocumentChunksResponse:
        """Post-rpc interceptor for search_document_chunks

        DEPRECATED. Please use the `post_search_document_chunks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperKnowledge server but before
        it is returned to user code. This `post_search_document_chunks` interceptor runs
        before the `post_search_document_chunks_with_metadata` interceptor.
        """
        return response

    def post_search_document_chunks_with_metadata(
        self,
        response: developerknowledge.SearchDocumentChunksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerknowledge.SearchDocumentChunksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_document_chunks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperKnowledge server but before it is returned to user code.

        We recommend only using this `post_search_document_chunks_with_metadata`
        interceptor in new development instead of the `post_search_document_chunks` interceptor.
        When both interceptors are used, this `post_search_document_chunks_with_metadata` interceptor runs after the
        `post_search_document_chunks` interceptor. The (possibly modified) response returned by
        `post_search_document_chunks` will be passed to
        `post_search_document_chunks_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DeveloperKnowledgeRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DeveloperKnowledgeRestInterceptor


class DeveloperKnowledgeRestTransport(_BaseDeveloperKnowledgeRestTransport):
    """REST backend synchronous transport for DeveloperKnowledge.

    The Developer Knowledge API provides programmatic access to Google's
    public developer documentation, enabling you to integrate this
    knowledge base into your own applications and workflows.

    The API is designed to be the canonical source for machine-readable
    access to Google's developer documentation.

    A typical use case is to first use
    [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks]
    to find relevant document chunks based on a query, and then use
    [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
    or
    [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments]
    with document resource names (such as
    [DocumentChunk.parent][google.developers.knowledge.v1.DocumentChunk.parent]
    or ``documents/{uri_without_scheme}``) to fetch the full content of
    the top results.

    All document content is provided in Markdown format.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "developerknowledge.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DeveloperKnowledgeRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'developerknowledge.googleapis.com').
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
            interceptor (Optional[DeveloperKnowledgeRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DeveloperKnowledgeRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AnswerQuery(
        _BaseDeveloperKnowledgeRestTransport._BaseAnswerQuery,
        DeveloperKnowledgeRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperKnowledgeRestTransport.AnswerQuery")

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
            request: developerknowledge.AnswerQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerknowledge.AnswerQueryResponse:
            r"""Call the answer query method over HTTP.

            Args:
                request (~.developerknowledge.AnswerQueryRequest):
                    The request object. Request message for
                [DeveloperKnowledge.AnswerQuery][google.developers.knowledge.v1.DeveloperKnowledge.AnswerQuery].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developerknowledge.AnswerQueryResponse:
                    Response message for
                [DeveloperKnowledge.AnswerQuery][google.developers.knowledge.v1.DeveloperKnowledge.AnswerQuery].

            """

            http_options = _BaseDeveloperKnowledgeRestTransport._BaseAnswerQuery._get_http_options()
            request, metadata = self._interceptor.pre_answer_query(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperKnowledgeRestTransport._BaseAnswerQuery,
                    "_BaseAnswerQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.developers.knowledge_v1.DeveloperKnowledgeClient.AnswerQuery",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "AnswerQuery",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperKnowledgeRestTransport._AnswerQuery._get_response(
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
            resp = developerknowledge.AnswerQueryResponse()
            pb_resp = developerknowledge.AnswerQueryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_answer_query(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_answer_query_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developerknowledge.AnswerQueryResponse.to_json(
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
                    "Received response for google.developers.knowledge_v1.DeveloperKnowledgeClient.answer_query",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "AnswerQuery",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchGetDocuments(
        _BaseDeveloperKnowledgeRestTransport._BaseBatchGetDocuments,
        DeveloperKnowledgeRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperKnowledgeRestTransport.BatchGetDocuments")

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
            request: developerknowledge.BatchGetDocumentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerknowledge.BatchGetDocumentsResponse:
            r"""Call the batch get documents method over HTTP.

            Args:
                request (~.developerknowledge.BatchGetDocumentsRequest):
                    The request object. Request message for
                [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developerknowledge.BatchGetDocumentsResponse:
                    Response message for
                [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].

            """

            http_options = _BaseDeveloperKnowledgeRestTransport._BaseBatchGetDocuments._get_http_options()
            request, metadata = self._interceptor.pre_batch_get_documents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperKnowledgeRestTransport._BaseBatchGetDocuments,
                    "_BaseBatchGetDocuments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.developers.knowledge_v1.DeveloperKnowledgeClient.BatchGetDocuments",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "BatchGetDocuments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperKnowledgeRestTransport._BatchGetDocuments._get_response(
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
            resp = developerknowledge.BatchGetDocumentsResponse()
            pb_resp = developerknowledge.BatchGetDocumentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_get_documents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_get_documents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developerknowledge.BatchGetDocumentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.developers.knowledge_v1.DeveloperKnowledgeClient.batch_get_documents",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "BatchGetDocuments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDocument(
        _BaseDeveloperKnowledgeRestTransport._BaseGetDocument,
        DeveloperKnowledgeRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperKnowledgeRestTransport.GetDocument")

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
            request: developerknowledge.GetDocumentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerknowledge.Document:
            r"""Call the get document method over HTTP.

            Args:
                request (~.developerknowledge.GetDocumentRequest):
                    The request object. Request message for
                [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developerknowledge.Document:
                    A Document represents a page of
                documentation in the Developer Knowledge
                corpus, like the page at
                https://docs.cloud.google.com/storage/docs/creating-buckets.

            """

            http_options = _BaseDeveloperKnowledgeRestTransport._BaseGetDocument._get_http_options()
            request, metadata = self._interceptor.pre_get_document(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperKnowledgeRestTransport._BaseGetDocument,
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
                    f"Sending request for google.developers.knowledge_v1.DeveloperKnowledgeClient.GetDocument",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "GetDocument",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperKnowledgeRestTransport._GetDocument._get_response(
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
            resp = developerknowledge.Document()
            pb_resp = developerknowledge.Document.pb(resp)

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
                    response_payload = developerknowledge.Document.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.developers.knowledge_v1.DeveloperKnowledgeClient.get_document",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "GetDocument",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchDocumentChunks(
        _BaseDeveloperKnowledgeRestTransport._BaseSearchDocumentChunks,
        DeveloperKnowledgeRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperKnowledgeRestTransport.SearchDocumentChunks")

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
            request: developerknowledge.SearchDocumentChunksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerknowledge.SearchDocumentChunksResponse:
            r"""Call the search document chunks method over HTTP.

            Args:
                request (~.developerknowledge.SearchDocumentChunksRequest):
                    The request object. Request message for
                [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developerknowledge.SearchDocumentChunksResponse:
                    Response message for
                [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].

            """

            http_options = _BaseDeveloperKnowledgeRestTransport._BaseSearchDocumentChunks._get_http_options()
            request, metadata = self._interceptor.pre_search_document_chunks(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperKnowledgeRestTransport._BaseSearchDocumentChunks,
                    "_BaseSearchDocumentChunks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.developers.knowledge_v1.DeveloperKnowledgeClient.SearchDocumentChunks",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "SearchDocumentChunks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperKnowledgeRestTransport._SearchDocumentChunks._get_response(
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
            resp = developerknowledge.SearchDocumentChunksResponse()
            pb_resp = developerknowledge.SearchDocumentChunksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_document_chunks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_document_chunks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developerknowledge.SearchDocumentChunksResponse.to_json(
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
                    "Received response for google.developers.knowledge_v1.DeveloperKnowledgeClient.search_document_chunks",
                    extra={
                        "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                        "rpcName": "SearchDocumentChunks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def answer_query(
        self,
    ) -> Callable[
        [developerknowledge.AnswerQueryRequest], developerknowledge.AnswerQueryResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnswerQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_get_documents(
        self,
    ) -> Callable[
        [developerknowledge.BatchGetDocumentsRequest],
        developerknowledge.BatchGetDocumentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchGetDocuments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_document(
        self,
    ) -> Callable[[developerknowledge.GetDocumentRequest], developerknowledge.Document]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDocument(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_document_chunks(
        self,
    ) -> Callable[
        [developerknowledge.SearchDocumentChunksRequest],
        developerknowledge.SearchDocumentChunksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchDocumentChunks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DeveloperKnowledgeRestTransport",)
