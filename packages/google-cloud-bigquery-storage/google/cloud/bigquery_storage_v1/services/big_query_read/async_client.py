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
    AsyncIterable,
    Awaitable,
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

from google.cloud.bigquery_storage_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.bigquery_storage_v1.types import arrow, avro, storage, stream

from .client import BigQueryReadClient
from .transports.base import DEFAULT_CLIENT_INFO, BigQueryReadTransport
from .transports.grpc_asyncio import BigQueryReadGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class BigQueryReadAsyncClient:
    """BigQuery Read API.

    The Read API can be used to read data from BigQuery.
    """

    _client: BigQueryReadClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = BigQueryReadClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = BigQueryReadClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = BigQueryReadClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = BigQueryReadClient._DEFAULT_UNIVERSE

    read_session_path = staticmethod(BigQueryReadClient.read_session_path)
    parse_read_session_path = staticmethod(BigQueryReadClient.parse_read_session_path)
    read_stream_path = staticmethod(BigQueryReadClient.read_stream_path)
    parse_read_stream_path = staticmethod(BigQueryReadClient.parse_read_stream_path)
    table_path = staticmethod(BigQueryReadClient.table_path)
    parse_table_path = staticmethod(BigQueryReadClient.parse_table_path)
    common_billing_account_path = staticmethod(
        BigQueryReadClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        BigQueryReadClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(BigQueryReadClient.common_folder_path)
    parse_common_folder_path = staticmethod(BigQueryReadClient.parse_common_folder_path)
    common_organization_path = staticmethod(BigQueryReadClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        BigQueryReadClient.parse_common_organization_path
    )
    common_project_path = staticmethod(BigQueryReadClient.common_project_path)
    parse_common_project_path = staticmethod(
        BigQueryReadClient.parse_common_project_path
    )
    common_location_path = staticmethod(BigQueryReadClient.common_location_path)
    parse_common_location_path = staticmethod(
        BigQueryReadClient.parse_common_location_path
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
            BigQueryReadAsyncClient: The constructed client.
        """
        sa_info_func = (
            BigQueryReadClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(BigQueryReadAsyncClient, info, *args, **kwargs)

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
            BigQueryReadAsyncClient: The constructed client.
        """
        sa_file_func = (
            BigQueryReadClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(BigQueryReadAsyncClient, filename, *args, **kwargs)

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
        return BigQueryReadClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> BigQueryReadTransport:
        """Returns the transport used by the client instance.

        Returns:
            BigQueryReadTransport: The transport used by the client instance.
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

    get_transport_class = BigQueryReadClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, BigQueryReadTransport, Callable[..., BigQueryReadTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the big query read async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,BigQueryReadTransport,Callable[..., BigQueryReadTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the BigQueryReadTransport constructor.
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
        self._client = BigQueryReadClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.bigquery.storage_v1.BigQueryReadAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.bigquery.storage.v1.BigQueryRead",
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
                    "serviceName": "google.cloud.bigquery.storage.v1.BigQueryRead",
                    "credentialsType": None,
                },
            )

    async def create_read_session(
        self,
        request: Optional[Union[storage.CreateReadSessionRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        read_session: Optional[stream.ReadSession] = None,
        max_stream_count: Optional[int] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> stream.ReadSession:
        r"""Creates a new read session. A read session divides
        the contents of a BigQuery table into one or more
        streams, which can then be used to read data from the
        table. The read session also specifies properties of the
        data to be read, such as a list of columns or a
        push-down filter describing the rows to be returned.

        A particular row can be read by at most one stream. When
        the caller has reached the end of each stream in the
        session, then all the data in the table has been read.

        Data is assigned to each stream such that roughly the
        same number of rows can be read from each stream.
        Because the server-side unit for assigning data is
        collections of rows, the API does not guarantee that
        each stream will return the same number or rows.
        Additionally, the limits are enforced based on the
        number of pre-filtered rows, so some filters can lead to
        lopsided assignments.

        Read sessions automatically expire 6 hours after they
        are created and do not require manual clean-up by the
        caller.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_storage_v1

            async def sample_create_read_session():
                # Create a client
                client = bigquery_storage_v1.BigQueryReadAsyncClient()

                # Initialize request argument(s)
                request = bigquery_storage_v1.CreateReadSessionRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_read_session(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_storage_v1.types.CreateReadSessionRequest, dict]]):
                The request object. Request message for ``CreateReadSession``.
            parent (:class:`str`):
                Required. The request project that owns the session, in
                the form of ``projects/{project_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            read_session (:class:`google.cloud.bigquery_storage_v1.types.ReadSession`):
                Required. Session to be created.
                This corresponds to the ``read_session`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            max_stream_count (:class:`int`):
                Max initial number of streams. If unset or zero, the
                server will provide a value of streams so as to produce
                reasonable throughput. Must be non-negative. The number
                of streams may be lower than the requested number,
                depending on the amount parallelism that is reasonable
                for the table. There is a default system max limit of
                1,000.

                This must be greater than or equal to
                preferred_min_stream_count. Typically, clients should
                either leave this unset to let the system to determine
                an upper bound OR set this a size for the maximum "units
                of work" it can gracefully handle.

                This corresponds to the ``max_stream_count`` field
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
            google.cloud.bigquery_storage_v1.types.ReadSession:
                Information about the ReadSession.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, read_session, max_stream_count]
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
        if not isinstance(request, storage.CreateReadSessionRequest):
            request = storage.CreateReadSessionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if read_session is not None:
            request.read_session = read_session
        if max_stream_count is not None:
            request.max_stream_count = max_stream_count

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_read_session
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("read_session.table", request.read_session.table),)
            ),
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

    def read_rows(
        self,
        request: Optional[Union[storage.ReadRowsRequest, dict]] = None,
        *,
        read_stream: Optional[str] = None,
        offset: Optional[int] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Awaitable[AsyncIterable[storage.ReadRowsResponse]]:
        r"""Reads rows from the stream in the format prescribed
        by the ReadSession. Each response contains one or more
        table rows, up to a maximum of 128 MB per response; read
        requests which attempt to read individual rows larger
        than 128 MB will fail.

        Each request also returns a set of stream statistics
        reflecting the current state of the stream.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_storage_v1

            async def sample_read_rows():
                # Create a client
                client = bigquery_storage_v1.BigQueryReadAsyncClient()

                # Initialize request argument(s)
                request = bigquery_storage_v1.ReadRowsRequest(
                    read_stream="read_stream_value",
                )

                # Make the request
                stream = await client.read_rows(request=request)

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_storage_v1.types.ReadRowsRequest, dict]]):
                The request object. Request message for ``ReadRows``.
            read_stream (:class:`str`):
                Required. Stream to read rows from.
                This corresponds to the ``read_stream`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            offset (:class:`int`):
                The offset requested must be less
                than the last row read from Read.
                Requesting a larger offset is undefined.
                If not specified, start reading from
                offset zero.

                This corresponds to the ``offset`` field
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
            AsyncIterable[google.cloud.bigquery_storage_v1.types.ReadRowsResponse]:
                Response from calling ReadRows may include row data, progress and
                   throttling information.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [read_stream, offset]
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
        if not isinstance(request, storage.ReadRowsRequest):
            request = storage.ReadRowsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if read_stream is not None:
            request.read_stream = read_stream
        if offset is not None:
            request.offset = offset

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.read_rows
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("read_stream", request.read_stream),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def split_read_stream(
        self,
        request: Optional[Union[storage.SplitReadStreamRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage.SplitReadStreamResponse:
        r"""Splits a given ``ReadStream`` into two ``ReadStream`` objects.
        These ``ReadStream`` objects are referred to as the primary and
        the residual streams of the split. The original ``ReadStream``
        can still be read from in the same manner as before. Both of the
        returned ``ReadStream`` objects can also be read from, and the
        rows returned by both child streams will be the same as the rows
        read from the original stream.

        Moreover, the two child streams will be allocated back-to-back
        in the original ``ReadStream``. Concretely, it is guaranteed
        that for streams original, primary, and residual, that
        original[0-j] = primary[0-j] and original[j-n] = residual[0-m]
        once the streams have been read to completion.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_storage_v1

            async def sample_split_read_stream():
                # Create a client
                client = bigquery_storage_v1.BigQueryReadAsyncClient()

                # Initialize request argument(s)
                request = bigquery_storage_v1.SplitReadStreamRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.split_read_stream(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_storage_v1.types.SplitReadStreamRequest, dict]]):
                The request object. Request message for ``SplitReadStream``.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.bigquery_storage_v1.types.SplitReadStreamResponse:
                Response message for SplitReadStream.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, storage.SplitReadStreamRequest):
            request = storage.SplitReadStreamRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.split_read_stream
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

    async def __aenter__(self) -> "BigQueryReadAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("BigQueryReadAsyncClient",)
