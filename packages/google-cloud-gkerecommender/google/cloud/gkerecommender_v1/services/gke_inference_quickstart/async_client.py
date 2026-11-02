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

from google.cloud.gkerecommender_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.gkerecommender_v1.services.gke_inference_quickstart import pagers
from google.cloud.gkerecommender_v1.types import gkerecommender

from .client import GkeInferenceQuickstartClient
from .transports.base import DEFAULT_CLIENT_INFO, GkeInferenceQuickstartTransport
from .transports.grpc_asyncio import GkeInferenceQuickstartGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class GkeInferenceQuickstartAsyncClient:
    """GKE Inference Quickstart (GIQ) service provides profiles with
    performance metrics for popular models and model servers across
    multiple accelerators. These profiles help generate optimized
    best practices for running inference on GKE.
    """

    _client: GkeInferenceQuickstartClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = GkeInferenceQuickstartClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = GkeInferenceQuickstartClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = GkeInferenceQuickstartClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = GkeInferenceQuickstartClient._DEFAULT_UNIVERSE

    common_billing_account_path = staticmethod(
        GkeInferenceQuickstartClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        GkeInferenceQuickstartClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(GkeInferenceQuickstartClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        GkeInferenceQuickstartClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        GkeInferenceQuickstartClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        GkeInferenceQuickstartClient.parse_common_organization_path
    )
    common_project_path = staticmethod(GkeInferenceQuickstartClient.common_project_path)
    parse_common_project_path = staticmethod(
        GkeInferenceQuickstartClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        GkeInferenceQuickstartClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        GkeInferenceQuickstartClient.parse_common_location_path
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
            GkeInferenceQuickstartAsyncClient: The constructed client.
        """
        sa_info_func = (
            GkeInferenceQuickstartClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(GkeInferenceQuickstartAsyncClient, info, *args, **kwargs)

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
            GkeInferenceQuickstartAsyncClient: The constructed client.
        """
        sa_file_func = (
            GkeInferenceQuickstartClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            GkeInferenceQuickstartAsyncClient, filename, *args, **kwargs
        )

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
        return GkeInferenceQuickstartClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> GkeInferenceQuickstartTransport:
        """Returns the transport used by the client instance.

        Returns:
            GkeInferenceQuickstartTransport: The transport used by the client instance.
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

    get_transport_class = GkeInferenceQuickstartClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                GkeInferenceQuickstartTransport,
                Callable[..., GkeInferenceQuickstartTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the gke inference quickstart async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,GkeInferenceQuickstartTransport,Callable[..., GkeInferenceQuickstartTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the GkeInferenceQuickstartTransport constructor.
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
        self._client = GkeInferenceQuickstartClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.gkerecommender_v1.GkeInferenceQuickstartAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
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
                    "serviceName": "google.cloud.gkerecommender.v1.GkeInferenceQuickstart",
                    "credentialsType": None,
                },
            )

    async def fetch_models(
        self,
        request: Optional[Union[gkerecommender.FetchModelsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchModelsAsyncPager:
        r"""Fetches available models. Open-source models follow the
        Huggingface Hub ``owner/model_name`` format.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gkerecommender_v1

            async def sample_fetch_models():
                # Create a client
                client = gkerecommender_v1.GkeInferenceQuickstartAsyncClient()

                # Initialize request argument(s)
                request = gkerecommender_v1.FetchModelsRequest(
                )

                # Make the request
                page_result = client.fetch_models(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gkerecommender_v1.types.FetchModelsRequest, dict]]):
                The request object. Request message for
                [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gkerecommender_v1.services.gke_inference_quickstart.pagers.FetchModelsAsyncPager:
                Response message for
                   [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, gkerecommender.FetchModelsRequest):
            request = gkerecommender.FetchModelsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_models
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
        response = pagers.FetchModelsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_model_servers(
        self,
        request: Optional[Union[gkerecommender.FetchModelServersRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchModelServersAsyncPager:
        r"""Fetches available model servers. Open-source model servers use
        simplified, lowercase names (e.g., ``vllm``).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gkerecommender_v1

            async def sample_fetch_model_servers():
                # Create a client
                client = gkerecommender_v1.GkeInferenceQuickstartAsyncClient()

                # Initialize request argument(s)
                request = gkerecommender_v1.FetchModelServersRequest(
                    model="model_value",
                )

                # Make the request
                page_result = client.fetch_model_servers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gkerecommender_v1.types.FetchModelServersRequest, dict]]):
                The request object. Request message for
                [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gkerecommender_v1.services.gke_inference_quickstart.pagers.FetchModelServersAsyncPager:
                Response message for
                   [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, gkerecommender.FetchModelServersRequest):
            request = gkerecommender.FetchModelServersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_model_servers
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
        response = pagers.FetchModelServersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_model_server_versions(
        self,
        request: Optional[
            Union[gkerecommender.FetchModelServerVersionsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchModelServerVersionsAsyncPager:
        r"""Fetches available model server versions. Open-source servers use
        their own versioning schemas (e.g., ``vllm`` uses semver like
        ``v1.0.0``).

        Some model servers have different versioning schemas depending
        on the accelerator. For example, ``vllm`` uses semver on GPUs,
        but returns nightly build tags on TPUs. All available versions
        will be returned when different schemas are present.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gkerecommender_v1

            async def sample_fetch_model_server_versions():
                # Create a client
                client = gkerecommender_v1.GkeInferenceQuickstartAsyncClient()

                # Initialize request argument(s)
                request = gkerecommender_v1.FetchModelServerVersionsRequest(
                    model="model_value",
                    model_server="model_server_value",
                )

                # Make the request
                page_result = client.fetch_model_server_versions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gkerecommender_v1.types.FetchModelServerVersionsRequest, dict]]):
                The request object. Request message for
                [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gkerecommender_v1.services.gke_inference_quickstart.pagers.FetchModelServerVersionsAsyncPager:
                Response message for
                   [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, gkerecommender.FetchModelServerVersionsRequest):
            request = gkerecommender.FetchModelServerVersionsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_model_server_versions
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
        response = pagers.FetchModelServerVersionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_profiles(
        self,
        request: Optional[Union[gkerecommender.FetchProfilesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchProfilesAsyncPager:
        r"""Fetches available profiles. A profile contains performance
        metrics and cost information for a specific model server setup.
        Profiles can be filtered by parameters. If no filters are
        provided, all profiles are returned.

        Profiles display a single value per performance metric based on
        the provided performance requirements. If no requirements are
        given, the metrics represent the inflection point. See `Run best
        practice inference with GKE Inference Quickstart
        recipes <https://cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart#how>`__
        for details.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gkerecommender_v1

            async def sample_fetch_profiles():
                # Create a client
                client = gkerecommender_v1.GkeInferenceQuickstartAsyncClient()

                # Initialize request argument(s)
                request = gkerecommender_v1.FetchProfilesRequest(
                )

                # Make the request
                page_result = client.fetch_profiles(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gkerecommender_v1.types.FetchProfilesRequest, dict]]):
                The request object. Request message for
                [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gkerecommender_v1.services.gke_inference_quickstart.pagers.FetchProfilesAsyncPager:
                Response message for
                   [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, gkerecommender.FetchProfilesRequest):
            request = gkerecommender.FetchProfilesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_profiles
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
        response = pagers.FetchProfilesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def generate_optimized_manifest(
        self,
        request: Optional[
            Union[gkerecommender.GenerateOptimizedManifestRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gkerecommender.GenerateOptimizedManifestResponse:
        r"""Generates an optimized deployment manifest for a given model and
        model server, based on the specified accelerator, performance
        targets, and configurations. See `Run best practice inference
        with GKE Inference Quickstart
        recipes <https://cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart>`__
        for deployment details.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gkerecommender_v1

            async def sample_generate_optimized_manifest():
                # Create a client
                client = gkerecommender_v1.GkeInferenceQuickstartAsyncClient()

                # Initialize request argument(s)
                model_server_info = gkerecommender_v1.ModelServerInfo()
                model_server_info.model = "model_value"
                model_server_info.model_server = "model_server_value"

                request = gkerecommender_v1.GenerateOptimizedManifestRequest(
                    model_server_info=model_server_info,
                    accelerator_type="accelerator_type_value",
                )

                # Make the request
                response = await client.generate_optimized_manifest(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gkerecommender_v1.types.GenerateOptimizedManifestRequest, dict]]):
                The request object. Request message for
                [GkeInferenceQuickstart.GenerateOptimizedManifest][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifest].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gkerecommender_v1.types.GenerateOptimizedManifestResponse:
                Response message for
                   [GkeInferenceQuickstart.GenerateOptimizedManifest][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifest].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, gkerecommender.GenerateOptimizedManifestRequest):
            request = gkerecommender.GenerateOptimizedManifestRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_optimized_manifest
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

    async def fetch_benchmarking_data(
        self,
        request: Optional[
            Union[gkerecommender.FetchBenchmarkingDataRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gkerecommender.FetchBenchmarkingDataResponse:
        r"""Fetches all of the benchmarking data available for a
        profile. Benchmarking data returns all of the
        performance metrics available for a given model server
        setup on a given instance type.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gkerecommender_v1

            async def sample_fetch_benchmarking_data():
                # Create a client
                client = gkerecommender_v1.GkeInferenceQuickstartAsyncClient()

                # Initialize request argument(s)
                model_server_info = gkerecommender_v1.ModelServerInfo()
                model_server_info.model = "model_value"
                model_server_info.model_server = "model_server_value"

                request = gkerecommender_v1.FetchBenchmarkingDataRequest(
                    model_server_info=model_server_info,
                )

                # Make the request
                response = await client.fetch_benchmarking_data(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gkerecommender_v1.types.FetchBenchmarkingDataRequest, dict]]):
                The request object. Request message for
                [GkeInferenceQuickstart.FetchBenchmarkingData][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingData].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gkerecommender_v1.types.FetchBenchmarkingDataResponse:
                Response message for
                   [GkeInferenceQuickstart.FetchBenchmarkingData][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingData].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, gkerecommender.FetchBenchmarkingDataRequest):
            request = gkerecommender.FetchBenchmarkingDataRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_benchmarking_data
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

    async def __aenter__(self) -> "GkeInferenceQuickstartAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("GkeInferenceQuickstartAsyncClient",)
