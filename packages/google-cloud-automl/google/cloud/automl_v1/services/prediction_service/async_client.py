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

from google.cloud.automl_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore

from google.cloud.automl_v1.types import (
    annotation_payload,
    data_items,
    io,
    operations,
    prediction_service,
)

from .client import PredictionServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, PredictionServiceTransport
from .transports.grpc_asyncio import PredictionServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class PredictionServiceAsyncClient:
    """AutoML Prediction API.

    On any input that is documented to expect a string parameter in
    snake_case or dash-case, either of those cases is accepted.
    """

    _client: PredictionServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = PredictionServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PredictionServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = PredictionServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = PredictionServiceClient._DEFAULT_UNIVERSE

    model_path = staticmethod(PredictionServiceClient.model_path)
    parse_model_path = staticmethod(PredictionServiceClient.parse_model_path)
    common_billing_account_path = staticmethod(
        PredictionServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PredictionServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(PredictionServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        PredictionServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        PredictionServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PredictionServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(PredictionServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        PredictionServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(PredictionServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        PredictionServiceClient.parse_common_location_path
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
            PredictionServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            PredictionServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(PredictionServiceAsyncClient, info, *args, **kwargs)

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
            PredictionServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            PredictionServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(PredictionServiceAsyncClient, filename, *args, **kwargs)

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
        return PredictionServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PredictionServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            PredictionServiceTransport: The transport used by the client instance.
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

    get_transport_class = PredictionServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                PredictionServiceTransport,
                Callable[..., PredictionServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the prediction service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,PredictionServiceTransport,Callable[..., PredictionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the PredictionServiceTransport constructor.
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
        self._client = PredictionServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.automl_v1.PredictionServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.automl.v1.PredictionService",
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
                    "serviceName": "google.cloud.automl.v1.PredictionService",
                    "credentialsType": None,
                },
            )

    async def predict(
        self,
        request: Optional[Union[prediction_service.PredictRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        payload: Optional[data_items.ExamplePayload] = None,
        params: Optional[MutableMapping[str, str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> prediction_service.PredictResponse:
        r"""Perform an online prediction. The prediction result is directly
        returned in the response. Available for following ML scenarios,
        and their expected request payloads:

        AutoML Vision Classification

        - An image in .JPEG, .GIF or .PNG format, image_bytes up to
          30MB.

        AutoML Vision Object Detection

        - An image in .JPEG, .GIF or .PNG format, image_bytes up to
          30MB.

        AutoML Natural Language Classification

        - A TextSnippet up to 60,000 characters, UTF-8 encoded or a
          document in .PDF, .TIF or .TIFF format with size upto 2MB.

        AutoML Natural Language Entity Extraction

        - A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a
          document in .PDF, .TIF or .TIFF format with size upto 20MB.

        AutoML Natural Language Sentiment Analysis

        - A TextSnippet up to 60,000 characters, UTF-8 encoded or a
          document in .PDF, .TIF or .TIFF format with size upto 2MB.

        AutoML Translation

        - A TextSnippet up to 25,000 characters, UTF-8 encoded.

        AutoML Tables

        - A row with column values matching the columns of the model, up
          to 5MB. Not available for FORECASTING ``prediction_type``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import automl_v1

            async def sample_predict():
                # Create a client
                client = automl_v1.PredictionServiceAsyncClient()

                # Initialize request argument(s)
                payload = automl_v1.ExamplePayload()
                payload.image.image_bytes = b'image_bytes_blob'

                request = automl_v1.PredictRequest(
                    name="name_value",
                    payload=payload,
                )

                # Make the request
                response = await client.predict(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.automl_v1.types.PredictRequest, dict]]):
                The request object. Request message for
                [PredictionService.Predict][google.cloud.automl.v1.PredictionService.Predict].
            name (:class:`str`):
                Required. Name of the model requested
                to serve the prediction.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            payload (:class:`google.cloud.automl_v1.types.ExamplePayload`):
                Required. Payload to perform a
                prediction on. The payload must match
                the problem type that the model was
                trained to solve.

                This corresponds to the ``payload`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            params (:class:`MutableMapping[str, str]`):
                Additional domain-specific parameters, any string must
                be up to 25000 characters long.

                AutoML Vision Classification

                ``score_threshold`` : (float) A value from 0.0 to 1.0.
                When the model makes predictions for an image, it will
                only produce results that have at least this confidence
                score. The default is 0.5.

                AutoML Vision Object Detection

                ``score_threshold`` : (float) When Model detects objects
                on the image, it will only produce bounding boxes which
                have at least this confidence score. Value in 0 to 1
                range, default is 0.5.

                ``max_bounding_box_count`` : (int64) The maximum number
                of bounding boxes returned. The default is 100. The
                number of returned bounding boxes might be limited by
                the server.

                AutoML Tables

                ``feature_importance`` : (boolean) Whether
                [feature_importance][google.cloud.automl.v1.TablesModelColumnInfo.feature_importance]
                is populated in the returned list of
                [TablesAnnotation][google.cloud.automl.v1.TablesAnnotation]
                objects. The default is false.

                This corresponds to the ``params`` field
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
            google.cloud.automl_v1.types.PredictResponse:
                Response message for
                [PredictionService.Predict][google.cloud.automl.v1.PredictionService.Predict].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, payload, params]
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
        if not isinstance(request, prediction_service.PredictRequest):
            request = prediction_service.PredictRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if payload is not None:
            request.payload = payload

        if params:
            request.params.update(params)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.predict]

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

    async def batch_predict(
        self,
        request: Optional[Union[prediction_service.BatchPredictRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        input_config: Optional[io.BatchPredictInputConfig] = None,
        output_config: Optional[io.BatchPredictOutputConfig] = None,
        params: Optional[MutableMapping[str, str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Perform a batch prediction. Unlike the online
        [Predict][google.cloud.automl.v1.PredictionService.Predict],
        batch prediction result won't be immediately available in the
        response. Instead, a long running operation object is returned.
        User can poll the operation result via
        [GetOperation][google.longrunning.Operations.GetOperation]
        method. Once the operation is done,
        [BatchPredictResult][google.cloud.automl.v1.BatchPredictResult]
        is returned in the
        [response][google.longrunning.Operation.response] field.
        Available for following ML scenarios:

        - AutoML Vision Classification
        - AutoML Vision Object Detection
        - AutoML Video Intelligence Classification
        - AutoML Video Intelligence Object Tracking \* AutoML Natural
          Language Classification
        - AutoML Natural Language Entity Extraction
        - AutoML Natural Language Sentiment Analysis
        - AutoML Tables

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import automl_v1

            async def sample_batch_predict():
                # Create a client
                client = automl_v1.PredictionServiceAsyncClient()

                # Initialize request argument(s)
                input_config = automl_v1.BatchPredictInputConfig()
                input_config.gcs_source.input_uris = ['input_uris_value1', 'input_uris_value2']

                output_config = automl_v1.BatchPredictOutputConfig()
                output_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"

                request = automl_v1.BatchPredictRequest(
                    name="name_value",
                    input_config=input_config,
                    output_config=output_config,
                )

                # Make the request
                operation = await client.batch_predict(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.automl_v1.types.BatchPredictRequest, dict]]):
                The request object. Request message for
                [PredictionService.BatchPredict][google.cloud.automl.v1.PredictionService.BatchPredict].
            name (:class:`str`):
                Required. Name of the model requested
                to serve the batch prediction.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            input_config (:class:`google.cloud.automl_v1.types.BatchPredictInputConfig`):
                Required. The input configuration for
                batch prediction.

                This corresponds to the ``input_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            output_config (:class:`google.cloud.automl_v1.types.BatchPredictOutputConfig`):
                Required. The Configuration
                specifying where output predictions
                should be written.

                This corresponds to the ``output_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            params (:class:`MutableMapping[str, str]`):
                Additional domain-specific parameters for the
                predictions, any string must be up to 25000 characters
                long.

                AutoML Natural Language Classification

                ``score_threshold`` : (float) A value from 0.0 to 1.0.
                When the model makes predictions for a text snippet, it
                will only produce results that have at least this
                confidence score. The default is 0.5.

                AutoML Vision Classification

                ``score_threshold`` : (float) A value from 0.0 to 1.0.
                When the model makes predictions for an image, it will
                only produce results that have at least this confidence
                score. The default is 0.5.

                AutoML Vision Object Detection

                ``score_threshold`` : (float) When Model detects objects
                on the image, it will only produce bounding boxes which
                have at least this confidence score. Value in 0 to 1
                range, default is 0.5.

                ``max_bounding_box_count`` : (int64) The maximum number
                of bounding boxes returned per image. The default is
                100, the number of bounding boxes returned might be
                limited by the server. AutoML Video Intelligence
                Classification

                ``score_threshold`` : (float) A value from 0.0 to 1.0.
                When the model makes predictions for a video, it will
                only produce results that have at least this confidence
                score. The default is 0.5.

                ``segment_classification`` : (boolean) Set to true to
                request segment-level classification. AutoML Video
                Intelligence returns labels and their confidence scores
                for the entire segment of the video that user specified
                in the request configuration. The default is true.

                ``shot_classification`` : (boolean) Set to true to
                request shot-level classification. AutoML Video
                Intelligence determines the boundaries for each camera
                shot in the entire segment of the video that user
                specified in the request configuration. AutoML Video
                Intelligence then returns labels and their confidence
                scores for each detected shot, along with the start and
                end time of the shot. The default is false.

                WARNING: Model evaluation is not done for this
                classification type, the quality of it depends on
                training data, but there are no metrics provided to
                describe that quality.

                ``1s_interval_classification`` : (boolean) Set to true
                to request classification for a video at one-second
                intervals. AutoML Video Intelligence returns labels and
                their confidence scores for each second of the entire
                segment of the video that user specified in the request
                configuration. The default is false.

                WARNING: Model evaluation is not done for this
                classification type, the quality of it depends on
                training data, but there are no metrics provided to
                describe that quality.

                AutoML Video Intelligence Object Tracking

                ``score_threshold`` : (float) When Model detects objects
                on video frames, it will only produce bounding boxes
                which have at least this confidence score. Value in 0 to
                1 range, default is 0.5.

                ``max_bounding_box_count`` : (int64) The maximum number
                of bounding boxes returned per image. The default is
                100, the number of bounding boxes returned might be
                limited by the server.

                ``min_bounding_box_size`` : (float) Only bounding boxes
                with shortest edge at least that long as a relative
                value of video frame size are returned. Value in 0 to 1
                range. Default is 0.

                This corresponds to the ``params`` field
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

                The result type for the operation will be :class:`google.cloud.automl_v1.types.BatchPredictResult` Result of the Batch Predict. This message is returned in
                   [response][google.longrunning.Operation.response] of
                   the operation returned by the
                   [PredictionService.BatchPredict][google.cloud.automl.v1.PredictionService.BatchPredict].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, input_config, output_config, params]
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
        if not isinstance(request, prediction_service.BatchPredictRequest):
            request = prediction_service.BatchPredictRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if input_config is not None:
            request.input_config = input_config
        if output_config is not None:
            request.output_config = output_config

        if params:
            request.params.update(params)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_predict
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
            prediction_service.BatchPredictResult,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "PredictionServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("PredictionServiceAsyncClient",)
