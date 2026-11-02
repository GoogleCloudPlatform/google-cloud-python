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

from google.cloud.webrisk_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.webrisk_v1beta1.types import webrisk

from .client import WebRiskServiceV1Beta1Client
from .transports.base import DEFAULT_CLIENT_INFO, WebRiskServiceV1Beta1Transport
from .transports.grpc_asyncio import WebRiskServiceV1Beta1GrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class WebRiskServiceV1Beta1AsyncClient:
    """Web Risk v1beta1 API defines an interface to detect malicious
    URLs on your website and in client applications.
    """

    _client: WebRiskServiceV1Beta1Client

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = WebRiskServiceV1Beta1Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = WebRiskServiceV1Beta1Client.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = WebRiskServiceV1Beta1Client._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = WebRiskServiceV1Beta1Client._DEFAULT_UNIVERSE

    common_billing_account_path = staticmethod(
        WebRiskServiceV1Beta1Client.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        WebRiskServiceV1Beta1Client.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(WebRiskServiceV1Beta1Client.common_folder_path)
    parse_common_folder_path = staticmethod(
        WebRiskServiceV1Beta1Client.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        WebRiskServiceV1Beta1Client.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        WebRiskServiceV1Beta1Client.parse_common_organization_path
    )
    common_project_path = staticmethod(WebRiskServiceV1Beta1Client.common_project_path)
    parse_common_project_path = staticmethod(
        WebRiskServiceV1Beta1Client.parse_common_project_path
    )
    common_location_path = staticmethod(
        WebRiskServiceV1Beta1Client.common_location_path
    )
    parse_common_location_path = staticmethod(
        WebRiskServiceV1Beta1Client.parse_common_location_path
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
            WebRiskServiceV1Beta1AsyncClient: The constructed client.
        """
        sa_info_func = (
            WebRiskServiceV1Beta1Client.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(WebRiskServiceV1Beta1AsyncClient, info, *args, **kwargs)

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
            WebRiskServiceV1Beta1AsyncClient: The constructed client.
        """
        sa_file_func = (
            WebRiskServiceV1Beta1Client.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(WebRiskServiceV1Beta1AsyncClient, filename, *args, **kwargs)

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
        return WebRiskServiceV1Beta1Client.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> WebRiskServiceV1Beta1Transport:
        """Returns the transport used by the client instance.

        Returns:
            WebRiskServiceV1Beta1Transport: The transport used by the client instance.
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

    get_transport_class = WebRiskServiceV1Beta1Client.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                WebRiskServiceV1Beta1Transport,
                Callable[..., WebRiskServiceV1Beta1Transport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the web risk service v1 beta1 async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,WebRiskServiceV1Beta1Transport,Callable[..., WebRiskServiceV1Beta1Transport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the WebRiskServiceV1Beta1Transport constructor.
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
        self._client = WebRiskServiceV1Beta1Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.webrisk_v1beta1.WebRiskServiceV1Beta1AsyncClient`.",
                extra={
                    "serviceName": "google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1",
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
                    "serviceName": "google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1",
                    "credentialsType": None,
                },
            )

    async def compute_threat_list_diff(
        self,
        request: Optional[Union[webrisk.ComputeThreatListDiffRequest, dict]] = None,
        *,
        threat_type: Optional[webrisk.ThreatType] = None,
        version_token: Optional[bytes] = None,
        constraints: Optional[webrisk.ComputeThreatListDiffRequest.Constraints] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> webrisk.ComputeThreatListDiffResponse:
        r"""Gets the most recent threat list diffs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1beta1

            async def sample_compute_threat_list_diff():
                # Create a client
                client = webrisk_v1beta1.WebRiskServiceV1Beta1AsyncClient()

                # Initialize request argument(s)
                request = webrisk_v1beta1.ComputeThreatListDiffRequest(
                    threat_type="UNWANTED_SOFTWARE",
                )

                # Make the request
                response = await client.compute_threat_list_diff(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest, dict]]):
                The request object. Describes an API diff request.
            threat_type (:class:`google.cloud.webrisk_v1beta1.types.ThreatType`):
                The ThreatList to update.
                This corresponds to the ``threat_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            version_token (:class:`bytes`):
                The current version token of the
                client for the requested list (the
                client version that was received from
                the last successful diff).

                This corresponds to the ``version_token`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            constraints (:class:`google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest.Constraints`):
                Required. The constraints associated
                with this request.

                This corresponds to the ``constraints`` field
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
            google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffResponse:

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [threat_type, version_token, constraints]
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
        if not isinstance(request, webrisk.ComputeThreatListDiffRequest):
            request = webrisk.ComputeThreatListDiffRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if threat_type is not None:
            request.threat_type = threat_type
        if version_token is not None:
            request.version_token = version_token
        if constraints is not None:
            request.constraints = constraints

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.compute_threat_list_diff
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

    async def search_uris(
        self,
        request: Optional[Union[webrisk.SearchUrisRequest, dict]] = None,
        *,
        uri: Optional[str] = None,
        threat_types: Optional[MutableSequence[webrisk.ThreatType]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> webrisk.SearchUrisResponse:
        r"""This method is used to check whether a URI is on a
        given threatList.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1beta1

            async def sample_search_uris():
                # Create a client
                client = webrisk_v1beta1.WebRiskServiceV1Beta1AsyncClient()

                # Initialize request argument(s)
                request = webrisk_v1beta1.SearchUrisRequest(
                    uri="uri_value",
                    threat_types=['UNWANTED_SOFTWARE'],
                )

                # Make the request
                response = await client.search_uris(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1beta1.types.SearchUrisRequest, dict]]):
                The request object. Request to check URI entries against
                threatLists.
            uri (:class:`str`):
                Required. The URI to be checked for
                matches.

                This corresponds to the ``uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            threat_types (:class:`MutableSequence[google.cloud.webrisk_v1beta1.types.ThreatType]`):
                Required. The ThreatLists to search
                in.

                This corresponds to the ``threat_types`` field
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
            google.cloud.webrisk_v1beta1.types.SearchUrisResponse:

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [uri, threat_types]
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
        if not isinstance(request, webrisk.SearchUrisRequest):
            request = webrisk.SearchUrisRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if uri is not None:
            request.uri = uri
        if threat_types:
            request.threat_types.extend(threat_types)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_uris
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

    async def search_hashes(
        self,
        request: Optional[Union[webrisk.SearchHashesRequest, dict]] = None,
        *,
        hash_prefix: Optional[bytes] = None,
        threat_types: Optional[MutableSequence[webrisk.ThreatType]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> webrisk.SearchHashesResponse:
        r"""Gets the full hashes that match the requested hash
        prefix. This is used after a hash prefix is looked up in
        a threatList and there is a match. The client side
        threatList only holds partial hashes so the client must
        query this method to determine if there is a full hash
        match of a threat.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import webrisk_v1beta1

            async def sample_search_hashes():
                # Create a client
                client = webrisk_v1beta1.WebRiskServiceV1Beta1AsyncClient()

                # Initialize request argument(s)
                request = webrisk_v1beta1.SearchHashesRequest(
                    threat_types=['UNWANTED_SOFTWARE'],
                )

                # Make the request
                response = await client.search_hashes(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.webrisk_v1beta1.types.SearchHashesRequest, dict]]):
                The request object. Request to return full hashes matched
                by the provided hash prefixes.
            hash_prefix (:class:`bytes`):
                A hash prefix, consisting of the most
                significant 4-32 bytes of a SHA256 hash.
                For JSON requests, this field is
                base64-encoded.

                This corresponds to the ``hash_prefix`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            threat_types (:class:`MutableSequence[google.cloud.webrisk_v1beta1.types.ThreatType]`):
                Required. The ThreatLists to search
                in.

                This corresponds to the ``threat_types`` field
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
            google.cloud.webrisk_v1beta1.types.SearchHashesResponse:

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hash_prefix, threat_types]
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
        if not isinstance(request, webrisk.SearchHashesRequest):
            request = webrisk.SearchHashesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if hash_prefix is not None:
            request.hash_prefix = hash_prefix
        if threat_types:
            request.threat_types.extend(threat_types)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_hashes
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

    async def __aenter__(self) -> "WebRiskServiceV1Beta1AsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("WebRiskServiceV1Beta1AsyncClient",)
