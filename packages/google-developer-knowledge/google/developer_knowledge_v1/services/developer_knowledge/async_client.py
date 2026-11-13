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
import logging as std_logging
import re
from collections import OrderedDict
from typing import (
    Callable,
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.developer_knowledge_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.developer_knowledge_v1.services.developer_knowledge import pagers
from google.developer_knowledge_v1.types import developerknowledge

from .client import DeveloperKnowledgeClient
from .transports.base import DEFAULT_CLIENT_INFO, DeveloperKnowledgeTransport
from .transports.grpc_asyncio import DeveloperKnowledgeGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DeveloperKnowledgeAsyncClient:
    """The Developer Knowledge API provides programmatic access to Google's
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
    """

    _client: DeveloperKnowledgeClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DeveloperKnowledgeClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DeveloperKnowledgeClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DeveloperKnowledgeClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DeveloperKnowledgeClient._DEFAULT_UNIVERSE

    document_path = staticmethod(DeveloperKnowledgeClient.document_path)
    parse_document_path = staticmethod(DeveloperKnowledgeClient.parse_document_path)
    common_billing_account_path = staticmethod(
        DeveloperKnowledgeClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DeveloperKnowledgeClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DeveloperKnowledgeClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DeveloperKnowledgeClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DeveloperKnowledgeClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DeveloperKnowledgeClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DeveloperKnowledgeClient.common_project_path)
    parse_common_project_path = staticmethod(
        DeveloperKnowledgeClient.parse_common_project_path
    )
    common_location_path = staticmethod(DeveloperKnowledgeClient.common_location_path)
    parse_common_location_path = staticmethod(
        DeveloperKnowledgeClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DeveloperKnowledgeAsyncClient: The constructed client.
        """
        sa_info_func = (
            DeveloperKnowledgeClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DeveloperKnowledgeAsyncClient, info, *args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DeveloperKnowledgeAsyncClient: The constructed client.
        """
        sa_file_func = (
            DeveloperKnowledgeClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DeveloperKnowledgeAsyncClient, filename, *args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DeveloperKnowledgeClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> DeveloperKnowledgeTransport:
        """Returns the transport used by the client instance.

        Returns:
            DeveloperKnowledgeTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = DeveloperKnowledgeClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DeveloperKnowledgeTransport,
                Callable[..., DeveloperKnowledgeTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the developer knowledge async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DeveloperKnowledgeTransport,Callable[..., DeveloperKnowledgeTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DeveloperKnowledgeTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DeveloperKnowledgeClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.developers.knowledge_v1.DeveloperKnowledgeAsyncClient`.",
                extra={
                    "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                    "universeDomain": getattr(
                        self._client._transport._credentials, "universe_domain", ""
                    ),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(
                        self.transport._credentials, "get_cred_info", lambda: None
                    )(),
                }
                if hasattr(self._client._transport, "_credentials")
                else {
                    "serviceName": "google.developers.knowledge.v1.DeveloperKnowledge",
                    "credentialsType": None,
                },
            )

    async def search_document_chunks(
        self,
        request: Optional[
            Union[developerknowledge.SearchDocumentChunksRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchDocumentChunksAsyncPager:
        r"""Searches for developer knowledge across Google's developer
        documentation. Returns
        [DocumentChunk][google.developers.knowledge.v1.DocumentChunk]s
        based on the user's query. There may be many chunks from the
        same [Document][google.developers.knowledge.v1.Document]. To
        retrieve full documents, use
        [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
        or
        [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments]
        with the
        [DocumentChunk.parent][google.developers.knowledge.v1.DocumentChunk.parent]
        returned in the
        [SearchDocumentChunksResponse.results][google.developers.knowledge.v1.SearchDocumentChunksResponse.results].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google import developer_knowledge_v1

            async def sample_search_document_chunks():
                # Create a client
                client = developer_knowledge_v1.DeveloperKnowledgeAsyncClient()

                # Initialize request argument(s)
                request = developer_knowledge_v1.SearchDocumentChunksRequest(
                    query="query_value",
                )

                # Make the request
                page_result = client.search_document_chunks(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.developer_knowledge_v1.types.SearchDocumentChunksRequest, dict]]):
                The request object. Request message for
                [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.developer_knowledge_v1.services.developer_knowledge.pagers.SearchDocumentChunksAsyncPager:
                Response message for
                   [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, developerknowledge.SearchDocumentChunksRequest):
            request = developerknowledge.SearchDocumentChunksRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_document_chunks
        ]

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.SearchDocumentChunksAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_document(
        self,
        request: Optional[Union[developerknowledge.GetDocumentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> developerknowledge.Document:
        r"""Retrieves a single document with its full Markdown
        content.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google import developer_knowledge_v1

            async def sample_get_document():
                # Create a client
                client = developer_knowledge_v1.DeveloperKnowledgeAsyncClient()

                # Initialize request argument(s)
                request = developer_knowledge_v1.GetDocumentRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.developer_knowledge_v1.types.GetDocumentRequest, dict]]):
                The request object. Request message for
                [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument].
            name (:class:`str`):
                Required. Specifies the name of the document to
                retrieve. Format: ``documents/{uri_without_scheme}``
                Example:
                ``documents/docs.cloud.google.com/storage/docs/creating-buckets``

                The name must not exceed 500 characters; values longer
                than 500 characters will result in an
                ``INVALID_ARGUMENT`` error.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.developer_knowledge_v1.types.Document:
                A Document represents a page of
                documentation in the Developer Knowledge
                corpus, like the page at
                https://docs.cloud.google.com/storage/docs/creating-buckets.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, developerknowledge.GetDocumentRequest):
            request = developerknowledge.GetDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_document
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def batch_get_documents(
        self,
        request: Optional[
            Union[developerknowledge.BatchGetDocumentsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> developerknowledge.BatchGetDocumentsResponse:
        r"""Retrieves multiple documents, each with its full
        Markdown content.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google import developer_knowledge_v1

            async def sample_batch_get_documents():
                # Create a client
                client = developer_knowledge_v1.DeveloperKnowledgeAsyncClient()

                # Initialize request argument(s)
                request = developer_knowledge_v1.BatchGetDocumentsRequest(
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = await client.batch_get_documents(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.developer_knowledge_v1.types.BatchGetDocumentsRequest, dict]]):
                The request object. Request message for
                [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.developer_knowledge_v1.types.BatchGetDocumentsResponse:
                Response message for
                   [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, developerknowledge.BatchGetDocumentsRequest):
            request = developerknowledge.BatchGetDocumentsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_get_documents
        ]

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def answer_query(
        self,
        request: Optional[Union[developerknowledge.AnswerQueryRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> developerknowledge.AnswerQueryResponse:
        r"""Answers a query using grounded generation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google import developer_knowledge_v1

            async def sample_answer_query():
                # Create a client
                client = developer_knowledge_v1.DeveloperKnowledgeAsyncClient()

                # Initialize request argument(s)
                request = developer_knowledge_v1.AnswerQueryRequest(
                    query="query_value",
                )

                # Make the request
                response = await client.answer_query(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.developer_knowledge_v1.types.AnswerQueryRequest, dict]]):
                The request object. Request message for
                [DeveloperKnowledge.AnswerQuery][google.developers.knowledge.v1.DeveloperKnowledge.AnswerQuery].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.developer_knowledge_v1.types.AnswerQueryResponse:
                Response message for
                   [DeveloperKnowledge.AnswerQuery][google.developers.knowledge.v1.DeveloperKnowledge.AnswerQuery].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, developerknowledge.AnswerQueryRequest):
            request = developerknowledge.AnswerQueryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.answer_query
        ]

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "DeveloperKnowledgeAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DeveloperKnowledgeAsyncClient",)
