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

from google.cloud.ces_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.ces_v1beta.services.evaluation_service import pagers
from google.cloud.ces_v1beta.types import (
    agent_service,
    app,
    evaluation,
    evaluation_metrics_config,
    evaluation_service,
    golden_run,
)
from google.cloud.ces_v1beta.types import evaluation as gcc_evaluation

from .client import EvaluationServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, EvaluationServiceTransport
from .transports.grpc_asyncio import EvaluationServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class EvaluationServiceAsyncClient:
    """EvaluationService exposes methods to perform evaluation for
    the CES app.
    """

    _client: EvaluationServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = EvaluationServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = EvaluationServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = EvaluationServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = EvaluationServiceClient._DEFAULT_UNIVERSE

    agent_path = staticmethod(EvaluationServiceClient.agent_path)
    parse_agent_path = staticmethod(EvaluationServiceClient.parse_agent_path)
    app_path = staticmethod(EvaluationServiceClient.app_path)
    parse_app_path = staticmethod(EvaluationServiceClient.parse_app_path)
    app_version_path = staticmethod(EvaluationServiceClient.app_version_path)
    parse_app_version_path = staticmethod(
        EvaluationServiceClient.parse_app_version_path
    )
    changelog_path = staticmethod(EvaluationServiceClient.changelog_path)
    parse_changelog_path = staticmethod(EvaluationServiceClient.parse_changelog_path)
    conversation_path = staticmethod(EvaluationServiceClient.conversation_path)
    parse_conversation_path = staticmethod(
        EvaluationServiceClient.parse_conversation_path
    )
    evaluation_path = staticmethod(EvaluationServiceClient.evaluation_path)
    parse_evaluation_path = staticmethod(EvaluationServiceClient.parse_evaluation_path)
    evaluation_dataset_path = staticmethod(
        EvaluationServiceClient.evaluation_dataset_path
    )
    parse_evaluation_dataset_path = staticmethod(
        EvaluationServiceClient.parse_evaluation_dataset_path
    )
    evaluation_expectation_path = staticmethod(
        EvaluationServiceClient.evaluation_expectation_path
    )
    parse_evaluation_expectation_path = staticmethod(
        EvaluationServiceClient.parse_evaluation_expectation_path
    )
    evaluation_result_path = staticmethod(
        EvaluationServiceClient.evaluation_result_path
    )
    parse_evaluation_result_path = staticmethod(
        EvaluationServiceClient.parse_evaluation_result_path
    )
    evaluation_run_path = staticmethod(EvaluationServiceClient.evaluation_run_path)
    parse_evaluation_run_path = staticmethod(
        EvaluationServiceClient.parse_evaluation_run_path
    )
    guardrail_path = staticmethod(EvaluationServiceClient.guardrail_path)
    parse_guardrail_path = staticmethod(EvaluationServiceClient.parse_guardrail_path)
    scheduled_evaluation_run_path = staticmethod(
        EvaluationServiceClient.scheduled_evaluation_run_path
    )
    parse_scheduled_evaluation_run_path = staticmethod(
        EvaluationServiceClient.parse_scheduled_evaluation_run_path
    )
    tool_path = staticmethod(EvaluationServiceClient.tool_path)
    parse_tool_path = staticmethod(EvaluationServiceClient.parse_tool_path)
    toolset_path = staticmethod(EvaluationServiceClient.toolset_path)
    parse_toolset_path = staticmethod(EvaluationServiceClient.parse_toolset_path)
    common_billing_account_path = staticmethod(
        EvaluationServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        EvaluationServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(EvaluationServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        EvaluationServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        EvaluationServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        EvaluationServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(EvaluationServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        EvaluationServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(EvaluationServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        EvaluationServiceClient.parse_common_location_path
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
            EvaluationServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            EvaluationServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(EvaluationServiceAsyncClient, info, *args, **kwargs)

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
            EvaluationServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            EvaluationServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(EvaluationServiceAsyncClient, filename, *args, **kwargs)

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
        return EvaluationServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> EvaluationServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            EvaluationServiceTransport: The transport used by the client instance.
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

    get_transport_class = EvaluationServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                EvaluationServiceTransport,
                Callable[..., EvaluationServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the evaluation service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,EvaluationServiceTransport,Callable[..., EvaluationServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the EvaluationServiceTransport constructor.
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
        self._client = EvaluationServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.ces_v1beta.EvaluationServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.ces.v1beta.EvaluationService",
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
                    "serviceName": "google.cloud.ces.v1beta.EvaluationService",
                    "credentialsType": None,
                },
            )

    async def run_evaluation(
        self,
        request: Optional[Union[evaluation.RunEvaluationRequest, dict]] = None,
        *,
        app: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Runs an evaluation of the app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_run_evaluation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.RunEvaluationRequest(
                    app="app_value",
                )

                # Make the request
                operation = await client.run_evaluation(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.RunEvaluationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].
            app (:class:`str`):
                Required. The app to evaluate. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``app`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.RunEvaluationResponse` Response message for
                   [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [app]
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
        if not isinstance(request, evaluation.RunEvaluationRequest):
            request = evaluation.RunEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if app is not None:
            request.app = app

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_evaluation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("app", request.app),)),
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation_service.RunEvaluationResponse,
            metadata_type=evaluation_service.RunEvaluationOperationMetadata,
        )

        # Done; return the response.
        return response

    async def upload_evaluation_audio(
        self,
        request: Optional[
            Union[evaluation_service.UploadEvaluationAudioRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        audio_content: Optional[bytes] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation_service.UploadEvaluationAudioResponse:
        r"""Uploads audio for use in Golden Evaluations. Stores the audio in
        the Cloud Storage bucket defined in
        'App.logging_settings.evaluation_audio_recording_config.gcs_bucket'
        and returns a transcript.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_upload_evaluation_audio():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.UploadEvaluationAudioRequest(
                    name="name_value",
                    audio_content=b'audio_content_blob',
                )

                # Make the request
                response = await client.upload_evaluation_audio(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.UploadEvaluationAudioRequest, dict]]):
                The request object. Request message for
                [EvaluationService.UploadEvaluationAudio][google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio].
            name (:class:`str`):
                Required. The resource name of the Evaluation for which
                to upload the evaluation audio. Format:
                ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audio_content (:class:`bytes`):
                Required. The raw audio bytes.
                The format of the audio must be
                single-channel LINEAR16 with a sample
                rate of 16kHz (default
                InputAudioConfig).

                This corresponds to the ``audio_content`` field
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
            google.cloud.ces_v1beta.types.UploadEvaluationAudioResponse:
                Response message for
                   [EvaluationService.UploadEvaluationAudio][google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, audio_content]
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
        if not isinstance(request, evaluation_service.UploadEvaluationAudioRequest):
            request = evaluation_service.UploadEvaluationAudioRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if audio_content is not None:
            request.audio_content = audio_content

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.upload_evaluation_audio
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

    async def create_evaluation(
        self,
        request: Optional[
            Union[evaluation_service.CreateEvaluationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        evaluation: Optional[gcc_evaluation.Evaluation] = None,
        evaluation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcc_evaluation.Evaluation:
        r"""Creates an evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_create_evaluation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                evaluation = ces_v1beta.Evaluation()
                evaluation.golden.turns.steps.user_input.text = "text_value"
                evaluation.display_name = "display_name_value"

                request = ces_v1beta.CreateEvaluationRequest(
                    parent="parent_value",
                    evaluation=evaluation,
                )

                # Make the request
                response = await client.create_evaluation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.CreateEvaluationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.CreateEvaluation][google.cloud.ces.v1beta.EvaluationService.CreateEvaluation].
            parent (:class:`str`):
                Required. The app to create the evaluation for. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            evaluation (:class:`google.cloud.ces_v1beta.types.Evaluation`):
                Required. The evaluation to create.
                This corresponds to the ``evaluation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            evaluation_id (:class:`str`):
                Optional. The ID to use for the
                evaluation, which will become the final
                component of the evaluation's resource
                name. If not provided, a unique ID will
                be automatically assigned for the
                evaluation.

                This corresponds to the ``evaluation_id`` field
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
            google.cloud.ces_v1beta.types.Evaluation:
                An evaluation represents all of the
                information needed to simulate and
                evaluate an agent.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, evaluation, evaluation_id]
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
        if not isinstance(request, evaluation_service.CreateEvaluationRequest):
            request = evaluation_service.CreateEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if evaluation is not None:
            request.evaluation = evaluation
        if evaluation_id is not None:
            request.evaluation_id = evaluation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_evaluation
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

    async def generate_evaluation(
        self,
        request: Optional[
            Union[evaluation_service.GenerateEvaluationRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a golden evaluation from a conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_generate_evaluation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GenerateEvaluationRequest(
                    conversation="conversation_value",
                )

                # Make the request
                operation = await client.generate_evaluation(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GenerateEvaluationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GenerateEvaluation][google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation].
            conversation (:class:`str`):
                Required. The conversation to create the golden
                evaluation for. Format:
                ``projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}``

                This corresponds to the ``conversation`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.Evaluation` An evaluation represents all of the information needed to simulate and
                   evaluate an agent.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation]
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
        if not isinstance(request, evaluation_service.GenerateEvaluationRequest):
            request = evaluation_service.GenerateEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation is not None:
            request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_evaluation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation.Evaluation,
            metadata_type=evaluation_service.GenerateEvaluationOperationMetadata,
        )

        # Done; return the response.
        return response

    async def import_evaluations(
        self,
        request: Optional[
            Union[evaluation_service.ImportEvaluationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Imports evaluations into the app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_import_evaluations():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ImportEvaluationsRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.import_evaluations(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ImportEvaluationsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ImportEvaluations][google.cloud.ces.v1beta.EvaluationService.ImportEvaluations].
            parent (:class:`str`):
                Required. The app to import the evaluations into.
                Format:
                ``projects/{project}/locations/{location}/apps/{app}``

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.ImportEvaluationsResponse` Response message for
                   [EvaluationService.ImportEvaluations][google.cloud.ces.v1beta.EvaluationService.ImportEvaluations].

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
        if not isinstance(request, evaluation_service.ImportEvaluationsRequest):
            request = evaluation_service.ImportEvaluationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.import_evaluations
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation_service.ImportEvaluationsResponse,
            metadata_type=evaluation_service.ImportEvaluationsOperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_evaluation_dataset(
        self,
        request: Optional[
            Union[evaluation_service.CreateEvaluationDatasetRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        evaluation_dataset: Optional[evaluation.EvaluationDataset] = None,
        evaluation_dataset_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationDataset:
        r"""Creates an evaluation dataset.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_create_evaluation_dataset():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                evaluation_dataset = ces_v1beta.EvaluationDataset()
                evaluation_dataset.display_name = "display_name_value"

                request = ces_v1beta.CreateEvaluationDatasetRequest(
                    parent="parent_value",
                    evaluation_dataset=evaluation_dataset,
                )

                # Make the request
                response = await client.create_evaluation_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.CreateEvaluationDatasetRequest, dict]]):
                The request object. Request message for
                [EvaluationService.CreateEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset].
            parent (:class:`str`):
                Required. The app to create the evaluation for. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            evaluation_dataset (:class:`google.cloud.ces_v1beta.types.EvaluationDataset`):
                Required. The evaluation dataset to
                create.

                This corresponds to the ``evaluation_dataset`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            evaluation_dataset_id (:class:`str`):
                Optional. The ID to use for the
                evaluation dataset, which will become
                the final component of the evaluation
                dataset's resource name. If not
                provided, a unique ID will be
                automatically assigned for the
                evaluation.

                This corresponds to the ``evaluation_dataset_id`` field
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
            google.cloud.ces_v1beta.types.EvaluationDataset:
                An evaluation dataset represents a
                set of evaluations that are grouped
                together basaed on shared tags.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, evaluation_dataset, evaluation_dataset_id]
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
        if not isinstance(request, evaluation_service.CreateEvaluationDatasetRequest):
            request = evaluation_service.CreateEvaluationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if evaluation_dataset is not None:
            request.evaluation_dataset = evaluation_dataset
        if evaluation_dataset_id is not None:
            request.evaluation_dataset_id = evaluation_dataset_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_evaluation_dataset
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

    async def update_evaluation(
        self,
        request: Optional[
            Union[evaluation_service.UpdateEvaluationRequest, dict]
        ] = None,
        *,
        evaluation: Optional[gcc_evaluation.Evaluation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcc_evaluation.Evaluation:
        r"""Updates an evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_update_evaluation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                evaluation = ces_v1beta.Evaluation()
                evaluation.golden.turns.steps.user_input.text = "text_value"
                evaluation.display_name = "display_name_value"

                request = ces_v1beta.UpdateEvaluationRequest(
                    evaluation=evaluation,
                )

                # Make the request
                response = await client.update_evaluation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.UpdateEvaluationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.UpdateEvaluation][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation].
            evaluation (:class:`google.cloud.ces_v1beta.types.Evaluation`):
                Required. The evaluation to update.
                This corresponds to the ``evaluation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask is used to
                control which fields get updated. If the
                mask is not present, all fields will be
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
            google.cloud.ces_v1beta.types.Evaluation:
                An evaluation represents all of the
                information needed to simulate and
                evaluate an agent.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [evaluation, update_mask]
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
        if not isinstance(request, evaluation_service.UpdateEvaluationRequest):
            request = evaluation_service.UpdateEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if evaluation is not None:
            request.evaluation = evaluation
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_evaluation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("evaluation.name", request.evaluation.name),)
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

    async def update_evaluation_dataset(
        self,
        request: Optional[
            Union[evaluation_service.UpdateEvaluationDatasetRequest, dict]
        ] = None,
        *,
        evaluation_dataset: Optional[evaluation.EvaluationDataset] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationDataset:
        r"""Updates an evaluation dataset.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_update_evaluation_dataset():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                evaluation_dataset = ces_v1beta.EvaluationDataset()
                evaluation_dataset.display_name = "display_name_value"

                request = ces_v1beta.UpdateEvaluationDatasetRequest(
                    evaluation_dataset=evaluation_dataset,
                )

                # Make the request
                response = await client.update_evaluation_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.UpdateEvaluationDatasetRequest, dict]]):
                The request object. Request message for
                [EvaluationService.UpdateEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset].
            evaluation_dataset (:class:`google.cloud.ces_v1beta.types.EvaluationDataset`):
                Required. The evaluation dataset to
                update.

                This corresponds to the ``evaluation_dataset`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask is used to
                control which fields get updated. If the
                mask is not present, all fields will be
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
            google.cloud.ces_v1beta.types.EvaluationDataset:
                An evaluation dataset represents a
                set of evaluations that are grouped
                together basaed on shared tags.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [evaluation_dataset, update_mask]
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
        if not isinstance(request, evaluation_service.UpdateEvaluationDatasetRequest):
            request = evaluation_service.UpdateEvaluationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if evaluation_dataset is not None:
            request.evaluation_dataset = evaluation_dataset
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_evaluation_dataset
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("evaluation_dataset.name", request.evaluation_dataset.name),)
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

    async def delete_evaluation(
        self,
        request: Optional[
            Union[evaluation_service.DeleteEvaluationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_delete_evaluation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.DeleteEvaluationRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_evaluation(request=request)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.DeleteEvaluationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.DeleteEvaluation][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation].
            name (:class:`str`):
                Required. The resource name of the
                evaluation to delete.

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
        if not isinstance(request, evaluation_service.DeleteEvaluationRequest):
            request = evaluation_service.DeleteEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_evaluation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def delete_evaluation_result(
        self,
        request: Optional[
            Union[evaluation_service.DeleteEvaluationResultRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an evaluation result.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_delete_evaluation_result():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.DeleteEvaluationResultRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_evaluation_result(request=request)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.DeleteEvaluationResultRequest, dict]]):
                The request object. Request message for
                [EvaluationService.DeleteEvaluationResult][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationResult].
            name (:class:`str`):
                Required. The resource name of the
                evaluation result to delete.

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
        if not isinstance(request, evaluation_service.DeleteEvaluationResultRequest):
            request = evaluation_service.DeleteEvaluationResultRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_evaluation_result
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def delete_evaluation_dataset(
        self,
        request: Optional[
            Union[evaluation_service.DeleteEvaluationDatasetRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an evaluation dataset.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_delete_evaluation_dataset():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.DeleteEvaluationDatasetRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_evaluation_dataset(request=request)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.DeleteEvaluationDatasetRequest, dict]]):
                The request object. Request message for
                [EvaluationService.DeleteEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset].
            name (:class:`str`):
                Required. The resource name of the
                evaluation dataset to delete.

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
        if not isinstance(request, evaluation_service.DeleteEvaluationDatasetRequest):
            request = evaluation_service.DeleteEvaluationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_evaluation_dataset
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def delete_evaluation_run(
        self,
        request: Optional[
            Union[evaluation_service.DeleteEvaluationRunRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes an evaluation run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_delete_evaluation_run():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.DeleteEvaluationRunRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_evaluation_run(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.DeleteEvaluationRunRequest, dict]]):
                The request object. Request message for
                [EvaluationService.DeleteEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun].
            name (:class:`str`):
                Required. The resource name of the
                evaluation run to delete.

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

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
        if not isinstance(request, evaluation_service.DeleteEvaluationRunRequest):
            request = evaluation_service.DeleteEvaluationRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_evaluation_run
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=evaluation_service.DeleteEvaluationRunOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_evaluation(
        self,
        request: Optional[Union[evaluation_service.GetEvaluationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.Evaluation:
        r"""Gets details of the specified evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_get_evaluation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GetEvaluationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GetEvaluationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GetEvaluation][google.cloud.ces.v1beta.EvaluationService.GetEvaluation].
            name (:class:`str`):
                Required. The resource name of the
                evaluation to retrieve.

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
            google.cloud.ces_v1beta.types.Evaluation:
                An evaluation represents all of the
                information needed to simulate and
                evaluate an agent.

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
        if not isinstance(request, evaluation_service.GetEvaluationRequest):
            request = evaluation_service.GetEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation
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

    async def get_evaluation_result(
        self,
        request: Optional[
            Union[evaluation_service.GetEvaluationResultRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationResult:
        r"""Gets details of the specified evaluation result.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_get_evaluation_result():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GetEvaluationResultRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation_result(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GetEvaluationResultRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GetEvaluationResult][google.cloud.ces.v1beta.EvaluationService.GetEvaluationResult].
            name (:class:`str`):
                Required. The resource name of the
                evaluation result to retrieve.

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
            google.cloud.ces_v1beta.types.EvaluationResult:
                An evaluation result represents the
                output of running an Evaluation.

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
        if not isinstance(request, evaluation_service.GetEvaluationResultRequest):
            request = evaluation_service.GetEvaluationResultRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation_result
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

    async def get_evaluation_dataset(
        self,
        request: Optional[
            Union[evaluation_service.GetEvaluationDatasetRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationDataset:
        r"""Gets details of the specified evaluation dataset.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_get_evaluation_dataset():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GetEvaluationDatasetRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GetEvaluationDatasetRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GetEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset].
            name (:class:`str`):
                Required. The resource name of the
                evaluation dataset to retrieve.

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
            google.cloud.ces_v1beta.types.EvaluationDataset:
                An evaluation dataset represents a
                set of evaluations that are grouped
                together basaed on shared tags.

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
        if not isinstance(request, evaluation_service.GetEvaluationDatasetRequest):
            request = evaluation_service.GetEvaluationDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation_dataset
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

    async def get_evaluation_run(
        self,
        request: Optional[
            Union[evaluation_service.GetEvaluationRunRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationRun:
        r"""Gets details of the specified evaluation run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_get_evaluation_run():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GetEvaluationRunRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GetEvaluationRunRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GetEvaluationRun][google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun].
            name (:class:`str`):
                Required. The resource name of the
                evaluation run to retrieve.

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
            google.cloud.ces_v1beta.types.EvaluationRun:
                An evaluation run represents an all
                the evaluation results from an
                evaluation execution.

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
        if not isinstance(request, evaluation_service.GetEvaluationRunRequest):
            request = evaluation_service.GetEvaluationRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation_run
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

    async def list_evaluations(
        self,
        request: Optional[
            Union[evaluation_service.ListEvaluationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEvaluationsAsyncPager:
        r"""Lists all evaluations in the given app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_list_evaluations():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ListEvaluationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ListEvaluationsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ListEvaluations][google.cloud.ces.v1beta.EvaluationService.ListEvaluations].
            parent (:class:`str`):
                Required. The resource name of the
                app to list evaluations from.

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
            google.cloud.ces_v1beta.services.evaluation_service.pagers.ListEvaluationsAsyncPager:
                Response message for
                   [EvaluationService.ListEvaluations][google.cloud.ces.v1beta.EvaluationService.ListEvaluations].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
        if not isinstance(request, evaluation_service.ListEvaluationsRequest):
            request = evaluation_service.ListEvaluationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_evaluations
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEvaluationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_evaluation_results(
        self,
        request: Optional[
            Union[evaluation_service.ListEvaluationResultsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEvaluationResultsAsyncPager:
        r"""Lists all evaluation results for a given evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_list_evaluation_results():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ListEvaluationResultsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluation_results(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ListEvaluationResultsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ListEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults].
            parent (:class:`str`):
                Required. The resource name of the evaluation to list
                evaluation results from. To filter by evaluation run,
                use ``-`` as the evaluation ID and specify the
                evaluation run ID in the filter. For example:
                ``projects/{project}/locations/{location}/apps/{app}/evaluations/-``

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
            google.cloud.ces_v1beta.services.evaluation_service.pagers.ListEvaluationResultsAsyncPager:
                Response message for
                   [EvaluationService.ListEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
        if not isinstance(request, evaluation_service.ListEvaluationResultsRequest):
            request = evaluation_service.ListEvaluationResultsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_evaluation_results
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEvaluationResultsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_evaluation_datasets(
        self,
        request: Optional[
            Union[evaluation_service.ListEvaluationDatasetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEvaluationDatasetsAsyncPager:
        r"""Lists all evaluation datasets in the given app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_list_evaluation_datasets():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ListEvaluationDatasetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluation_datasets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ListEvaluationDatasetsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ListEvaluationDatasets][google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets].
            parent (:class:`str`):
                Required. The resource name of the
                app to list evaluation datasets from.

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
            google.cloud.ces_v1beta.services.evaluation_service.pagers.ListEvaluationDatasetsAsyncPager:
                Response message for
                   [EvaluationService.ListEvaluationDatasets][google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
        if not isinstance(request, evaluation_service.ListEvaluationDatasetsRequest):
            request = evaluation_service.ListEvaluationDatasetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_evaluation_datasets
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEvaluationDatasetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_evaluation_runs(
        self,
        request: Optional[
            Union[evaluation_service.ListEvaluationRunsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEvaluationRunsAsyncPager:
        r"""Lists all evaluation runs in the given app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_list_evaluation_runs():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ListEvaluationRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluation_runs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ListEvaluationRunsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ListEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns].
            parent (:class:`str`):
                Required. The resource name of the
                app to list evaluation runs from.

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
            google.cloud.ces_v1beta.services.evaluation_service.pagers.ListEvaluationRunsAsyncPager:
                Response message for
                   [EvaluationService.ListEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
        if not isinstance(request, evaluation_service.ListEvaluationRunsRequest):
            request = evaluation_service.ListEvaluationRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_evaluation_runs
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEvaluationRunsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_evaluation_expectations(
        self,
        request: Optional[
            Union[evaluation_service.ListEvaluationExpectationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEvaluationExpectationsAsyncPager:
        r"""Lists all evaluation expectations in the given app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_list_evaluation_expectations():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ListEvaluationExpectationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluation_expectations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ListEvaluationExpectationsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ListEvaluationExpectations][google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations].
            parent (:class:`str`):
                Required. The resource name of the
                app to list evaluation expectations
                from.

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
            google.cloud.ces_v1beta.services.evaluation_service.pagers.ListEvaluationExpectationsAsyncPager:
                Response message for
                   [EvaluationService.ListEvaluationExpectations][google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            request, evaluation_service.ListEvaluationExpectationsRequest
        ):
            request = evaluation_service.ListEvaluationExpectationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_evaluation_expectations
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEvaluationExpectationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_evaluation_expectation(
        self,
        request: Optional[
            Union[evaluation_service.GetEvaluationExpectationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationExpectation:
        r"""Gets details of the specified evaluation expectation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_get_evaluation_expectation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GetEvaluationExpectationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation_expectation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GetEvaluationExpectationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GetEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation].
            name (:class:`str`):
                Required. The resource name of the
                evaluation expectation to retrieve.

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
            google.cloud.ces_v1beta.types.EvaluationExpectation:
                An evaluation expectation represents
                a specific criteria to evaluate against.

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
        if not isinstance(request, evaluation_service.GetEvaluationExpectationRequest):
            request = evaluation_service.GetEvaluationExpectationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation_expectation
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

    async def create_evaluation_expectation(
        self,
        request: Optional[
            Union[evaluation_service.CreateEvaluationExpectationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        evaluation_expectation: Optional[evaluation.EvaluationExpectation] = None,
        evaluation_expectation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationExpectation:
        r"""Creates an evaluation expectation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_create_evaluation_expectation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                evaluation_expectation = ces_v1beta.EvaluationExpectation()
                evaluation_expectation.llm_criteria.prompt = "prompt_value"
                evaluation_expectation.display_name = "display_name_value"

                request = ces_v1beta.CreateEvaluationExpectationRequest(
                    parent="parent_value",
                    evaluation_expectation=evaluation_expectation,
                )

                # Make the request
                response = await client.create_evaluation_expectation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.CreateEvaluationExpectationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.CreateEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation].
            parent (:class:`str`):
                Required. The app to create the evaluation expectation
                for. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            evaluation_expectation (:class:`google.cloud.ces_v1beta.types.EvaluationExpectation`):
                Required. The evaluation expectation
                to create.

                This corresponds to the ``evaluation_expectation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            evaluation_expectation_id (:class:`str`):
                Optional. The ID to use for the
                evaluation expectation, which will
                become the final component of the
                evaluation expectation's resource name.
                If not provided, a unique ID will be
                automatically assigned for the
                evaluation expectation.

                This corresponds to the ``evaluation_expectation_id`` field
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
            google.cloud.ces_v1beta.types.EvaluationExpectation:
                An evaluation expectation represents
                a specific criteria to evaluate against.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, evaluation_expectation, evaluation_expectation_id]
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
            request, evaluation_service.CreateEvaluationExpectationRequest
        ):
            request = evaluation_service.CreateEvaluationExpectationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if evaluation_expectation is not None:
            request.evaluation_expectation = evaluation_expectation
        if evaluation_expectation_id is not None:
            request.evaluation_expectation_id = evaluation_expectation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_evaluation_expectation
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

    async def update_evaluation_expectation(
        self,
        request: Optional[
            Union[evaluation_service.UpdateEvaluationExpectationRequest, dict]
        ] = None,
        *,
        evaluation_expectation: Optional[evaluation.EvaluationExpectation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.EvaluationExpectation:
        r"""Updates an evaluation expectation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_update_evaluation_expectation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                evaluation_expectation = ces_v1beta.EvaluationExpectation()
                evaluation_expectation.llm_criteria.prompt = "prompt_value"
                evaluation_expectation.display_name = "display_name_value"

                request = ces_v1beta.UpdateEvaluationExpectationRequest(
                    evaluation_expectation=evaluation_expectation,
                )

                # Make the request
                response = await client.update_evaluation_expectation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.UpdateEvaluationExpectationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.UpdateEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation].
            evaluation_expectation (:class:`google.cloud.ces_v1beta.types.EvaluationExpectation`):
                Required. The evaluation expectation
                to update.

                This corresponds to the ``evaluation_expectation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask is used to
                control which fields get updated. If the
                mask is not present, all fields will be
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
            google.cloud.ces_v1beta.types.EvaluationExpectation:
                An evaluation expectation represents
                a specific criteria to evaluate against.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [evaluation_expectation, update_mask]
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
            request, evaluation_service.UpdateEvaluationExpectationRequest
        ):
            request = evaluation_service.UpdateEvaluationExpectationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if evaluation_expectation is not None:
            request.evaluation_expectation = evaluation_expectation
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_evaluation_expectation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("evaluation_expectation.name", request.evaluation_expectation.name),)
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

    async def delete_evaluation_expectation(
        self,
        request: Optional[
            Union[evaluation_service.DeleteEvaluationExpectationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an evaluation expectation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_delete_evaluation_expectation():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.DeleteEvaluationExpectationRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_evaluation_expectation(request=request)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.DeleteEvaluationExpectationRequest, dict]]):
                The request object. Request message for
                [EvaluationService.DeleteEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation].
            name (:class:`str`):
                Required. The resource name of the
                evaluation expectation to delete.

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
        if not isinstance(
            request, evaluation_service.DeleteEvaluationExpectationRequest
        ):
            request = evaluation_service.DeleteEvaluationExpectationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_evaluation_expectation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def create_scheduled_evaluation_run(
        self,
        request: Optional[
            Union[evaluation_service.CreateScheduledEvaluationRunRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        scheduled_evaluation_run: Optional[evaluation.ScheduledEvaluationRun] = None,
        scheduled_evaluation_run_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.ScheduledEvaluationRun:
        r"""Creates a scheduled evaluation run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_create_scheduled_evaluation_run():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                scheduled_evaluation_run = ces_v1beta.ScheduledEvaluationRun()
                scheduled_evaluation_run.display_name = "display_name_value"
                scheduled_evaluation_run.request.app = "app_value"
                scheduled_evaluation_run.scheduling_config.frequency = "BIWEEKLY"

                request = ces_v1beta.CreateScheduledEvaluationRunRequest(
                    parent="parent_value",
                    scheduled_evaluation_run=scheduled_evaluation_run,
                )

                # Make the request
                response = await client.create_scheduled_evaluation_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.CreateScheduledEvaluationRunRequest, dict]]):
                The request object. Request message for
                [EvaluationService.CreateScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun].
            parent (:class:`str`):
                Required. The app to create the scheduled evaluation run
                for. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            scheduled_evaluation_run (:class:`google.cloud.ces_v1beta.types.ScheduledEvaluationRun`):
                Required. The scheduled evaluation
                run to create.

                This corresponds to the ``scheduled_evaluation_run`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            scheduled_evaluation_run_id (:class:`str`):
                Optional. The ID to use for the
                scheduled evaluation run, which will
                become the final component of the
                scheduled evaluation run's resource
                name. If not provided, a unique ID will
                be automatically assigned.

                This corresponds to the ``scheduled_evaluation_run_id`` field
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
            google.cloud.ces_v1beta.types.ScheduledEvaluationRun:
                Represents a scheduled evaluation run
                configuration.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            scheduled_evaluation_run,
            scheduled_evaluation_run_id,
        ]
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
            request, evaluation_service.CreateScheduledEvaluationRunRequest
        ):
            request = evaluation_service.CreateScheduledEvaluationRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if scheduled_evaluation_run is not None:
            request.scheduled_evaluation_run = scheduled_evaluation_run
        if scheduled_evaluation_run_id is not None:
            request.scheduled_evaluation_run_id = scheduled_evaluation_run_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_scheduled_evaluation_run
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

    async def get_scheduled_evaluation_run(
        self,
        request: Optional[
            Union[evaluation_service.GetScheduledEvaluationRunRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.ScheduledEvaluationRun:
        r"""Gets details of the specified scheduled evaluation
        run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_get_scheduled_evaluation_run():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.GetScheduledEvaluationRunRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_scheduled_evaluation_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.GetScheduledEvaluationRunRequest, dict]]):
                The request object. Request message for
                [EvaluationService.GetScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun].
            name (:class:`str`):
                Required. The resource name of the
                scheduled evaluation run to retrieve.

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
            google.cloud.ces_v1beta.types.ScheduledEvaluationRun:
                Represents a scheduled evaluation run
                configuration.

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
        if not isinstance(request, evaluation_service.GetScheduledEvaluationRunRequest):
            request = evaluation_service.GetScheduledEvaluationRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_scheduled_evaluation_run
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

    async def list_scheduled_evaluation_runs(
        self,
        request: Optional[
            Union[evaluation_service.ListScheduledEvaluationRunsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListScheduledEvaluationRunsAsyncPager:
        r"""Lists all scheduled evaluation runs in the given app.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_list_scheduled_evaluation_runs():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ListScheduledEvaluationRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_scheduled_evaluation_runs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ListScheduledEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns].
            parent (:class:`str`):
                Required. The resource name of the
                app to list scheduled evaluation runs
                from.

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
            google.cloud.ces_v1beta.services.evaluation_service.pagers.ListScheduledEvaluationRunsAsyncPager:
                Response message for
                   [EvaluationService.ListScheduledEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            request, evaluation_service.ListScheduledEvaluationRunsRequest
        ):
            request = evaluation_service.ListScheduledEvaluationRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_scheduled_evaluation_runs
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListScheduledEvaluationRunsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_scheduled_evaluation_run(
        self,
        request: Optional[
            Union[evaluation_service.UpdateScheduledEvaluationRunRequest, dict]
        ] = None,
        *,
        scheduled_evaluation_run: Optional[evaluation.ScheduledEvaluationRun] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.ScheduledEvaluationRun:
        r"""Updates a scheduled evaluation run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_update_scheduled_evaluation_run():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                scheduled_evaluation_run = ces_v1beta.ScheduledEvaluationRun()
                scheduled_evaluation_run.display_name = "display_name_value"
                scheduled_evaluation_run.request.app = "app_value"
                scheduled_evaluation_run.scheduling_config.frequency = "BIWEEKLY"

                request = ces_v1beta.UpdateScheduledEvaluationRunRequest(
                    scheduled_evaluation_run=scheduled_evaluation_run,
                )

                # Make the request
                response = await client.update_scheduled_evaluation_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.UpdateScheduledEvaluationRunRequest, dict]]):
                The request object. Request message for
                [EvaluationService.UpdateScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun].
            scheduled_evaluation_run (:class:`google.cloud.ces_v1beta.types.ScheduledEvaluationRun`):
                Required. The scheduled evaluation
                run to update.

                This corresponds to the ``scheduled_evaluation_run`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask is used to
                control which fields get updated. If the
                mask is not present, all fields will be
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
            google.cloud.ces_v1beta.types.ScheduledEvaluationRun:
                Represents a scheduled evaluation run
                configuration.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scheduled_evaluation_run, update_mask]
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
            request, evaluation_service.UpdateScheduledEvaluationRunRequest
        ):
            request = evaluation_service.UpdateScheduledEvaluationRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scheduled_evaluation_run is not None:
            request.scheduled_evaluation_run = scheduled_evaluation_run
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_scheduled_evaluation_run
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "scheduled_evaluation_run.name",
                        request.scheduled_evaluation_run.name,
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

    async def delete_scheduled_evaluation_run(
        self,
        request: Optional[
            Union[evaluation_service.DeleteScheduledEvaluationRunRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a scheduled evaluation run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_delete_scheduled_evaluation_run():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.DeleteScheduledEvaluationRunRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_scheduled_evaluation_run(request=request)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.DeleteScheduledEvaluationRunRequest, dict]]):
                The request object. Request message for
                [EvaluationService.DeleteScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun].
            name (:class:`str`):
                Required. The resource name of the
                scheduled evaluation run to delete.

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
        if not isinstance(
            request, evaluation_service.DeleteScheduledEvaluationRunRequest
        ):
            request = evaluation_service.DeleteScheduledEvaluationRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_scheduled_evaluation_run
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def test_persona_voice(
        self,
        request: Optional[
            Union[evaluation_service.TestPersonaVoiceRequest, dict]
        ] = None,
        *,
        app: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation_service.TestPersonaVoiceResponse:
        r"""Tests the voice of a persona. Also accepts a default
        persona.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_test_persona_voice():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.TestPersonaVoiceRequest(
                    app="app_value",
                    persona_id="persona_id_value",
                    text="text_value",
                )

                # Make the request
                response = await client.test_persona_voice(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.TestPersonaVoiceRequest, dict]]):
                The request object. Request message for
                [EvaluationService.TestPersonaVoice][google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice].
            app (:class:`str`):
                Required. the resource name of the app to test the
                persona voice for. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``app`` field
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
            google.cloud.ces_v1beta.types.TestPersonaVoiceResponse:
                Response message for
                   [EvaluationService.TestPersonaVoice][google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [app]
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
        if not isinstance(request, evaluation_service.TestPersonaVoiceRequest):
            request = evaluation_service.TestPersonaVoiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if app is not None:
            request.app = app

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.test_persona_voice
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("app", request.app),)),
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

    async def export_evaluations(
        self,
        request: Optional[
            Union[evaluation_service.ExportEvaluationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports evaluations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_export_evaluations():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ExportEvaluationsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                operation = await client.export_evaluations(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ExportEvaluationsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ExportEvaluations][google.cloud.ces.v1beta.EvaluationService.ExportEvaluations].
            parent (:class:`str`):
                Required. The resource name of the app to export
                evaluations from. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.ExportEvaluationsResponse` Response message for
                   [EvaluationService.ExportEvaluations][google.cloud.ces.v1beta.EvaluationService.ExportEvaluations].

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
        if not isinstance(request, evaluation_service.ExportEvaluationsRequest):
            request = evaluation_service.ExportEvaluationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_evaluations
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation_service.ExportEvaluationsResponse,
            metadata_type=agent_service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_evaluation_runs(
        self,
        request: Optional[
            Union[evaluation_service.ExportEvaluationRunsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports evaluations runs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_export_evaluation_runs():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ExportEvaluationRunsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                operation = await client.export_evaluation_runs(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ExportEvaluationRunsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ExportEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns].
            parent (:class:`str`):
                Required. The resource name of the app to export
                evaluation runs from. Format:
                ``projects/{project}/locations/{location}/apps/{app}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (:class:`MutableSequence[str]`):
                Required. The resource names of the
                evaluation runs to export.

                This corresponds to the ``names`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.ExportEvaluationRunsResponse` Response message for
                   [EvaluationService.ExportEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, evaluation_service.ExportEvaluationRunsRequest):
            request = evaluation_service.ExportEvaluationRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if names:
            request.names.extend(names)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_evaluation_runs
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation_service.ExportEvaluationRunsResponse,
            metadata_type=evaluation_service.ExportEvaluationRunsOperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_evaluation_results(
        self,
        request: Optional[
            Union[evaluation_service.ExportEvaluationResultsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports evaluations results.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_export_evaluation_results():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.ExportEvaluationResultsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                operation = await client.export_evaluation_results(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.ExportEvaluationResultsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.ExportEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults].
            parent (:class:`str`):
                Required. The resource name of the evaluation to export
                evaluation results from. Format:
                ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (:class:`MutableSequence[str]`):
                Required. The resource names of the
                evaluation results to export.

                This corresponds to the ``names`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.ExportEvaluationResultsResponse` Response message for
                   [EvaluationService.ExportEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, evaluation_service.ExportEvaluationResultsRequest):
            request = evaluation_service.ExportEvaluationResultsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if names:
            request.names.extend(names)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_evaluation_results
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation_service.ExportEvaluationResultsResponse,
            metadata_type=evaluation_service.ExportEvaluationResultsOperationMetadata,
        )

        # Done; return the response.
        return response

    async def run_evaluation_result_metrics(
        self,
        request: Optional[
            Union[evaluation_service.RunEvaluationResultMetricsRequest, dict]
        ] = None,
        *,
        evaluation_result_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Runs metrics on an existing evaluation result.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import ces_v1beta

            async def sample_run_evaluation_result_metrics():
                # Create a client
                client = ces_v1beta.EvaluationServiceAsyncClient()

                # Initialize request argument(s)
                request = ces_v1beta.RunEvaluationResultMetricsRequest(
                    evaluation_result_id="evaluation_result_id_value",
                )

                # Make the request
                operation = await client.run_evaluation_result_metrics(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.ces_v1beta.types.RunEvaluationResultMetricsRequest, dict]]):
                The request object. Request message for
                [EvaluationService.RunEvaluationResultMetrics][google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics].
            evaluation_result_id (:class:`str`):
                Required. The evaluation result to run metrics for.
                Format:
                ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{evaluation_result_id}``

                This corresponds to the ``evaluation_result_id`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.ces_v1beta.types.RunEvaluationResultMetricsResponse` Response message for
                   [EvaluationService.RunEvaluationResultMetrics][google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [evaluation_result_id]
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
            request, evaluation_service.RunEvaluationResultMetricsRequest
        ):
            request = evaluation_service.RunEvaluationResultMetricsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if evaluation_result_id is not None:
            request.evaluation_result_id = evaluation_result_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_evaluation_result_metrics
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("evaluation_result_id", request.evaluation_result_id),)
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            evaluation_service.RunEvaluationResultMetricsResponse,
            metadata_type=evaluation_service.RunEvaluationResultMetricsOperationMetadata,
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

    async def delete_operation(
        self,
        request: Optional[Union[operations_pb2.DeleteOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.DeleteOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.DeleteOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.delete_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: Optional[Union[operations_pb2.CancelOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.CancelOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.CancelOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_location(
        self,
        request: Optional[Union[locations_pb2.GetLocationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.GetLocationRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.GetLocationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_location]

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

    async def list_locations(
        self,
        request: Optional[Union[locations_pb2.ListLocationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.ListLocationsRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.ListLocationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_locations]

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

    async def __aenter__(self) -> "EvaluationServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("EvaluationServiceAsyncClient",)
