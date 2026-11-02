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

from google.cloud.retail_v2alpha import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.retail_v2alpha.types import (
    generative_question,
    generative_question_service,
)

from .client import GenerativeQuestionServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, GenerativeQuestionServiceTransport
from .transports.grpc_asyncio import GenerativeQuestionServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class GenerativeQuestionServiceAsyncClient:
    """Service for managing LLM generated questions in search
    serving.
    """

    _client: GenerativeQuestionServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = GenerativeQuestionServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = GenerativeQuestionServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        GenerativeQuestionServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = GenerativeQuestionServiceClient._DEFAULT_UNIVERSE

    catalog_path = staticmethod(GenerativeQuestionServiceClient.catalog_path)
    parse_catalog_path = staticmethod(
        GenerativeQuestionServiceClient.parse_catalog_path
    )
    common_billing_account_path = staticmethod(
        GenerativeQuestionServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        GenerativeQuestionServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        GenerativeQuestionServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        GenerativeQuestionServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        GenerativeQuestionServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        GenerativeQuestionServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        GenerativeQuestionServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        GenerativeQuestionServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        GenerativeQuestionServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        GenerativeQuestionServiceClient.parse_common_location_path
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
            GenerativeQuestionServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            GenerativeQuestionServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(GenerativeQuestionServiceAsyncClient, info, *args, **kwargs)

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
            GenerativeQuestionServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            GenerativeQuestionServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            GenerativeQuestionServiceAsyncClient, filename, *args, **kwargs
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
        return GenerativeQuestionServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> GenerativeQuestionServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            GenerativeQuestionServiceTransport: The transport used by the client instance.
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

    get_transport_class = GenerativeQuestionServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                GenerativeQuestionServiceTransport,
                Callable[..., GenerativeQuestionServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the generative question service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,GenerativeQuestionServiceTransport,Callable[..., GenerativeQuestionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the GenerativeQuestionServiceTransport constructor.
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
        self._client = GenerativeQuestionServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.retail_v2alpha.GenerativeQuestionServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.retail.v2alpha.GenerativeQuestionService",
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
                    "serviceName": "google.cloud.retail.v2alpha.GenerativeQuestionService",
                    "credentialsType": None,
                },
            )

    async def update_generative_questions_feature_config(
        self,
        request: Optional[
            Union[
                generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest,
                dict,
            ]
        ] = None,
        *,
        generative_questions_feature_config: Optional[
            generative_question.GenerativeQuestionsFeatureConfig
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> generative_question.GenerativeQuestionsFeatureConfig:
        r"""Manages overal generative question feature state --
        enables toggling feature on and off.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2alpha

            async def sample_update_generative_questions_feature_config():
                # Create a client
                client = retail_v2alpha.GenerativeQuestionServiceAsyncClient()

                # Initialize request argument(s)
                generative_questions_feature_config = retail_v2alpha.GenerativeQuestionsFeatureConfig()
                generative_questions_feature_config.catalog = "catalog_value"

                request = retail_v2alpha.UpdateGenerativeQuestionsFeatureConfigRequest(
                    generative_questions_feature_config=generative_questions_feature_config,
                )

                # Make the request
                response = await client.update_generative_questions_feature_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2alpha.types.UpdateGenerativeQuestionsFeatureConfigRequest, dict]]):
                The request object. Request for
                UpdateGenerativeQuestionsFeatureConfig
                method.
            generative_questions_feature_config (:class:`google.cloud.retail_v2alpha.types.GenerativeQuestionsFeatureConfig`):
                Required. The configuration managing
                the feature state.

                This corresponds to the ``generative_questions_feature_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Indicates which fields in the provided
                [GenerativeQuestionsFeatureConfig][google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig]
                to update. If not set or empty, all supported fields are
                updated.

                This corresponds to the ``update_mask`` field
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
            google.cloud.retail_v2alpha.types.GenerativeQuestionsFeatureConfig:
                Configuration for overall generative
                question feature state.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [generative_questions_feature_config, update_mask]
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
        if not isinstance(
            request,
            generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest,
        ):
            request = generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if generative_questions_feature_config is not None:
            request.generative_questions_feature_config = (
                generative_questions_feature_config
            )
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_generative_questions_feature_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "generative_questions_feature_config.catalog",
                        request.generative_questions_feature_config.catalog,
                    ),
                )
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

    async def get_generative_questions_feature_config(
        self,
        request: Optional[
            Union[
                generative_question_service.GetGenerativeQuestionsFeatureConfigRequest,
                dict,
            ]
        ] = None,
        *,
        catalog: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> generative_question.GenerativeQuestionsFeatureConfig:
        r"""Manages overal generative question feature state --
        enables toggling feature on and off.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2alpha

            async def sample_get_generative_questions_feature_config():
                # Create a client
                client = retail_v2alpha.GenerativeQuestionServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2alpha.GetGenerativeQuestionsFeatureConfigRequest(
                    catalog="catalog_value",
                )

                # Make the request
                response = await client.get_generative_questions_feature_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2alpha.types.GetGenerativeQuestionsFeatureConfigRequest, dict]]):
                The request object. Request for
                GetGenerativeQuestionsFeatureConfig
                method.
            catalog (:class:`str`):
                Required. Resource name of the parent
                catalog. Format:
                projects/{project}/locations/{location}/catalogs/{catalog}

                This corresponds to the ``catalog`` field
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
            google.cloud.retail_v2alpha.types.GenerativeQuestionsFeatureConfig:
                Configuration for overall generative
                question feature state.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [catalog]
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
        if not isinstance(
            request,
            generative_question_service.GetGenerativeQuestionsFeatureConfigRequest,
        ):
            request = (
                generative_question_service.GetGenerativeQuestionsFeatureConfigRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if catalog is not None:
            request.catalog = catalog

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_generative_questions_feature_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("catalog", request.catalog),)),
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

    async def list_generative_question_configs(
        self,
        request: Optional[
            Union[
                generative_question_service.ListGenerativeQuestionConfigsRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> generative_question_service.ListGenerativeQuestionConfigsResponse:
        r"""Returns all questions for a given catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2alpha

            async def sample_list_generative_question_configs():
                # Create a client
                client = retail_v2alpha.GenerativeQuestionServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2alpha.ListGenerativeQuestionConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_generative_question_configs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2alpha.types.ListGenerativeQuestionConfigsRequest, dict]]):
                The request object. Request for ListQuestions method.
            parent (:class:`str`):
                Required. Resource name of the parent
                catalog. Format:
                projects/{project}/locations/{location}/catalogs/{catalog}

                This corresponds to the ``parent`` field
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
            google.cloud.retail_v2alpha.types.ListGenerativeQuestionConfigsResponse:
                Response for ListQuestions method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
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
        if not isinstance(
            request, generative_question_service.ListGenerativeQuestionConfigsRequest
        ):
            request = generative_question_service.ListGenerativeQuestionConfigsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_generative_question_configs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
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

    async def update_generative_question_config(
        self,
        request: Optional[
            Union[
                generative_question_service.UpdateGenerativeQuestionConfigRequest, dict
            ]
        ] = None,
        *,
        generative_question_config: Optional[
            generative_question.GenerativeQuestionConfig
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> generative_question.GenerativeQuestionConfig:
        r"""Allows management of individual questions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2alpha

            async def sample_update_generative_question_config():
                # Create a client
                client = retail_v2alpha.GenerativeQuestionServiceAsyncClient()

                # Initialize request argument(s)
                generative_question_config = retail_v2alpha.GenerativeQuestionConfig()
                generative_question_config.catalog = "catalog_value"
                generative_question_config.facet = "facet_value"

                request = retail_v2alpha.UpdateGenerativeQuestionConfigRequest(
                    generative_question_config=generative_question_config,
                )

                # Make the request
                response = await client.update_generative_question_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2alpha.types.UpdateGenerativeQuestionConfigRequest, dict]]):
                The request object. Request for
                UpdateGenerativeQuestionConfig method.
            generative_question_config (:class:`google.cloud.retail_v2alpha.types.GenerativeQuestionConfig`):
                Required. The question to update.
                This corresponds to the ``generative_question_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Indicates which fields in the provided
                [GenerativeQuestionConfig][google.cloud.retail.v2alpha.GenerativeQuestionConfig]
                to update. The following are NOT supported:

                - [GenerativeQuestionConfig.frequency][google.cloud.retail.v2alpha.GenerativeQuestionConfig.frequency]

                If not set or empty, all supported fields are updated.

                This corresponds to the ``update_mask`` field
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
            google.cloud.retail_v2alpha.types.GenerativeQuestionConfig:
                Configuration for a single generated
                question.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [generative_question_config, update_mask]
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
        if not isinstance(
            request, generative_question_service.UpdateGenerativeQuestionConfigRequest
        ):
            request = generative_question_service.UpdateGenerativeQuestionConfigRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if generative_question_config is not None:
            request.generative_question_config = generative_question_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_generative_question_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "generative_question_config.catalog",
                        request.generative_question_config.catalog,
                    ),
                )
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

    async def batch_update_generative_question_configs(
        self,
        request: Optional[
            Union[
                generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[
            MutableSequence[
                generative_question_service.UpdateGenerativeQuestionConfigRequest
            ]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse:
        r"""Allows management of multiple questions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2alpha

            async def sample_batch_update_generative_question_configs():
                # Create a client
                client = retail_v2alpha.GenerativeQuestionServiceAsyncClient()

                # Initialize request argument(s)
                requests = retail_v2alpha.UpdateGenerativeQuestionConfigRequest()
                requests.generative_question_config.catalog = "catalog_value"
                requests.generative_question_config.facet = "facet_value"

                request = retail_v2alpha.BatchUpdateGenerativeQuestionConfigsRequest(
                    requests=requests,
                )

                # Make the request
                response = await client.batch_update_generative_question_configs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2alpha.types.BatchUpdateGenerativeQuestionConfigsRequest, dict]]):
                The request object. Request for
                BatchUpdateGenerativeQuestionConfig
                method.
            parent (:class:`str`):
                Optional. Resource name of the parent
                catalog. Format:
                projects/{project}/locations/{location}/catalogs/{catalog}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (:class:`MutableSequence[google.cloud.retail_v2alpha.types.UpdateGenerativeQuestionConfigRequest]`):
                Required. The updates question
                configs.

                This corresponds to the ``requests`` field
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
            google.cloud.retail_v2alpha.types.BatchUpdateGenerativeQuestionConfigsResponse:
                Aggregated response for
                UpdateGenerativeQuestionConfig method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, requests]
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
        if not isinstance(
            request,
            generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest,
        ):
            request = (
                generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if requests:
            request.requests.extend(requests)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_update_generative_question_configs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
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

    async def list_operations(
        self,
        request: Optional[Union[operations_pb2.ListOperationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.ListOperationsRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.ListOperationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_operations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[Union[operations_pb2.GetOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.GetOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.GetOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "GenerativeQuestionServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("GenerativeQuestionServiceAsyncClient",)
