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

from google.cloud.recaptchaenterprise_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service import (
    pagers,
)
from google.cloud.recaptchaenterprise_v1.types import recaptchaenterprise

from .client import RecaptchaEnterpriseServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, RecaptchaEnterpriseServiceTransport
from .transports.grpc_asyncio import RecaptchaEnterpriseServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class RecaptchaEnterpriseServiceAsyncClient:
    """Service to determine the likelihood an event is legitimate."""

    _client: RecaptchaEnterpriseServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = RecaptchaEnterpriseServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = RecaptchaEnterpriseServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        RecaptchaEnterpriseServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = RecaptchaEnterpriseServiceClient._DEFAULT_UNIVERSE

    assessment_path = staticmethod(RecaptchaEnterpriseServiceClient.assessment_path)
    parse_assessment_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_assessment_path
    )
    firewall_policy_path = staticmethod(
        RecaptchaEnterpriseServiceClient.firewall_policy_path
    )
    parse_firewall_policy_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_firewall_policy_path
    )
    key_path = staticmethod(RecaptchaEnterpriseServiceClient.key_path)
    parse_key_path = staticmethod(RecaptchaEnterpriseServiceClient.parse_key_path)
    metrics_path = staticmethod(RecaptchaEnterpriseServiceClient.metrics_path)
    parse_metrics_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_metrics_path
    )
    policy_path = staticmethod(RecaptchaEnterpriseServiceClient.policy_path)
    parse_policy_path = staticmethod(RecaptchaEnterpriseServiceClient.parse_policy_path)
    related_account_group_path = staticmethod(
        RecaptchaEnterpriseServiceClient.related_account_group_path
    )
    parse_related_account_group_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_related_account_group_path
    )
    related_account_group_membership_path = staticmethod(
        RecaptchaEnterpriseServiceClient.related_account_group_membership_path
    )
    parse_related_account_group_membership_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_related_account_group_membership_path
    )
    common_billing_account_path = staticmethod(
        RecaptchaEnterpriseServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        RecaptchaEnterpriseServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        RecaptchaEnterpriseServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        RecaptchaEnterpriseServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        RecaptchaEnterpriseServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        RecaptchaEnterpriseServiceClient.parse_common_location_path
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
            RecaptchaEnterpriseServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            RecaptchaEnterpriseServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            RecaptchaEnterpriseServiceAsyncClient, info, *args, **kwargs
        )

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
            RecaptchaEnterpriseServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            RecaptchaEnterpriseServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            RecaptchaEnterpriseServiceAsyncClient, filename, *args, **kwargs
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
        return RecaptchaEnterpriseServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> RecaptchaEnterpriseServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            RecaptchaEnterpriseServiceTransport: The transport used by the client instance.
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

    get_transport_class = RecaptchaEnterpriseServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                RecaptchaEnterpriseServiceTransport,
                Callable[..., RecaptchaEnterpriseServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the recaptcha enterprise service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,RecaptchaEnterpriseServiceTransport,Callable[..., RecaptchaEnterpriseServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the RecaptchaEnterpriseServiceTransport constructor.
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
        self._client = RecaptchaEnterpriseServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService",
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
                    "serviceName": "google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService",
                    "credentialsType": None,
                },
            )

    async def create_assessment(
        self,
        request: Optional[
            Union[recaptchaenterprise.CreateAssessmentRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        assessment: Optional[recaptchaenterprise.Assessment] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Assessment:
        r"""Creates an Assessment of the likelihood an event is
        legitimate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_create_assessment():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.CreateAssessmentRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_assessment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest, dict]]):
                The request object. The create assessment request
                message.
            parent (:class:`str`):
                Required. The name of the project in which the
                assessment is created, in the format
                ``projects/{project}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            assessment (:class:`google.cloud.recaptchaenterprise_v1.types.Assessment`):
                Required. The assessment details.
                This corresponds to the ``assessment`` field
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
            google.cloud.recaptchaenterprise_v1.types.Assessment:
                A reCAPTCHA Enterprise assessment
                resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, assessment]
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
        if not isinstance(request, recaptchaenterprise.CreateAssessmentRequest):
            request = recaptchaenterprise.CreateAssessmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if assessment is not None:
            request.assessment = assessment

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_assessment
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

    async def annotate_assessment(
        self,
        request: Optional[
            Union[recaptchaenterprise.AnnotateAssessmentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        annotation: Optional[
            recaptchaenterprise.AnnotateAssessmentRequest.Annotation
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.AnnotateAssessmentResponse:
        r"""Annotates a previously created Assessment to provide
        additional information on whether the event turned out
        to be authentic or fraudulent.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_annotate_assessment():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.AnnotateAssessmentRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.annotate_assessment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest, dict]]):
                The request object. The request message to annotate an
                Assessment.
            name (:class:`str`):
                Required. The resource name of the Assessment, in the
                format ``projects/{project}/assessments/{assessment}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            annotation (:class:`google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation`):
                Optional. The annotation that is
                assigned to the Event. This field can be
                left empty to provide reasons that apply
                to an event without concluding whether
                the event is legitimate or fraudulent.

                This corresponds to the ``annotation`` field
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
            google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentResponse:
                Empty response for
                AnnotateAssessment.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, annotation]
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
        if not isinstance(request, recaptchaenterprise.AnnotateAssessmentRequest):
            request = recaptchaenterprise.AnnotateAssessmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if annotation is not None:
            request.annotation = annotation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.annotate_assessment
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

    async def create_key(
        self,
        request: Optional[Union[recaptchaenterprise.CreateKeyRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        key: Optional[recaptchaenterprise.Key] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Key:
        r"""Creates a new reCAPTCHA Enterprise key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_create_key():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                key = recaptchaenterprise_v1.Key()
                key.web_settings.integration_type = "POLICY_BASED_CHALLENGE"
                key.display_name = "display_name_value"

                request = recaptchaenterprise_v1.CreateKeyRequest(
                    parent="parent_value",
                    key=key,
                )

                # Make the request
                response = await client.create_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.CreateKeyRequest, dict]]):
                The request object. The create key request message.
            parent (:class:`str`):
                Required. The name of the project in which the key is
                created, in the format ``projects/{project}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            key (:class:`google.cloud.recaptchaenterprise_v1.types.Key`):
                Required. Information to create a
                reCAPTCHA Enterprise key.

                This corresponds to the ``key`` field
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
            google.cloud.recaptchaenterprise_v1.types.Key:
                A key used to identify and configure
                applications (web and/or mobile) that
                use reCAPTCHA Enterprise.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, key]
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
        if not isinstance(request, recaptchaenterprise.CreateKeyRequest):
            request = recaptchaenterprise.CreateKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if key is not None:
            request.key = key

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_key
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

    async def list_keys(
        self,
        request: Optional[Union[recaptchaenterprise.ListKeysRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListKeysAsyncPager:
        r"""Returns the list of all keys that belong to a
        project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_list_keys():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.ListKeysRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_keys(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.ListKeysRequest, dict]]):
                The request object. The list keys request message.
            parent (:class:`str`):
                Required. The name of the project that contains the keys
                that is listed, in the format ``projects/{project}``.

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
            google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysAsyncPager:
                Response to request to list keys in a
                project.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

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
        if not isinstance(request, recaptchaenterprise.ListKeysRequest):
            request = recaptchaenterprise.ListKeysRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_keys
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
        response = pagers.ListKeysAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def retrieve_legacy_secret_key(
        self,
        request: Optional[
            Union[recaptchaenterprise.RetrieveLegacySecretKeyRequest, dict]
        ] = None,
        *,
        key: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.RetrieveLegacySecretKeyResponse:
        r"""Returns the secret key related to the specified
        public key. You must use the legacy secret key only in a
        3rd party integration with legacy reCAPTCHA.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_retrieve_legacy_secret_key():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.RetrieveLegacySecretKeyRequest(
                    key="key_value",
                )

                # Make the request
                response = await client.retrieve_legacy_secret_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyRequest, dict]]):
                The request object. The retrieve legacy secret key
                request message.
            key (:class:`str`):
                Required. The public key name linked to the requested
                secret key in the format
                ``projects/{project}/keys/{key}``.

                This corresponds to the ``key`` field
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
            google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyResponse:
                Secret key is used only in legacy
                reCAPTCHA. It must be used in a 3rd
                party integration with legacy reCAPTCHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [key]
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
        if not isinstance(request, recaptchaenterprise.RetrieveLegacySecretKeyRequest):
            request = recaptchaenterprise.RetrieveLegacySecretKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if key is not None:
            request.key = key

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.retrieve_legacy_secret_key
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("key", request.key),)),
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

    async def get_key(
        self,
        request: Optional[Union[recaptchaenterprise.GetKeyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Key:
        r"""Returns the specified key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_get_key():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.GetKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.GetKeyRequest, dict]]):
                The request object. The get key request message.
            name (:class:`str`):
                Required. The name of the requested key, in the format
                ``projects/{project}/keys/{key}``.

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
            google.cloud.recaptchaenterprise_v1.types.Key:
                A key used to identify and configure
                applications (web and/or mobile) that
                use reCAPTCHA Enterprise.

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
        if not isinstance(request, recaptchaenterprise.GetKeyRequest):
            request = recaptchaenterprise.GetKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_key]

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

    async def update_key(
        self,
        request: Optional[Union[recaptchaenterprise.UpdateKeyRequest, dict]] = None,
        *,
        key: Optional[recaptchaenterprise.Key] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Key:
        r"""Updates the specified key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_update_key():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                key = recaptchaenterprise_v1.Key()
                key.web_settings.integration_type = "POLICY_BASED_CHALLENGE"
                key.display_name = "display_name_value"

                request = recaptchaenterprise_v1.UpdateKeyRequest(
                    key=key,
                )

                # Make the request
                response = await client.update_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.UpdateKeyRequest, dict]]):
                The request object. The update key request message.
            key (:class:`google.cloud.recaptchaenterprise_v1.types.Key`):
                Required. The key to update.
                This corresponds to the ``key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The mask to control which
                fields of the key get updated. If the
                mask is not present, all fields are
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
            google.cloud.recaptchaenterprise_v1.types.Key:
                A key used to identify and configure
                applications (web and/or mobile) that
                use reCAPTCHA Enterprise.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [key, update_mask]
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
        if not isinstance(request, recaptchaenterprise.UpdateKeyRequest):
            request = recaptchaenterprise.UpdateKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if key is not None:
            request.key = key
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_key
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("key.name", request.key.name),)),
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

    async def delete_key(
        self,
        request: Optional[Union[recaptchaenterprise.DeleteKeyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_delete_key():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.DeleteKeyRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_key(request=request)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.DeleteKeyRequest, dict]]):
                The request object. The delete key request message.
            name (:class:`str`):
                Required. The name of the key to be deleted, in the
                format ``projects/{project}/keys/{key}``.

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
        if not isinstance(request, recaptchaenterprise.DeleteKeyRequest):
            request = recaptchaenterprise.DeleteKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_key
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

    async def migrate_key(
        self,
        request: Optional[Union[recaptchaenterprise.MigrateKeyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Key:
        r"""Migrates an existing key from reCAPTCHA to reCAPTCHA
        Enterprise. Once a key is migrated, it can be used from
        either product. SiteVerify requests are billed as
        CreateAssessment calls. You must be authenticated as one
        of the current owners of the reCAPTCHA Key, and your
        user must have the reCAPTCHA Enterprise Admin IAM role
        in the destination project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_migrate_key():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.MigrateKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.migrate_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.MigrateKeyRequest, dict]]):
                The request object. The migrate key request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.recaptchaenterprise_v1.types.Key:
                A key used to identify and configure
                applications (web and/or mobile) that
                use reCAPTCHA Enterprise.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, recaptchaenterprise.MigrateKeyRequest):
            request = recaptchaenterprise.MigrateKeyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.migrate_key
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

    async def add_ip_override(
        self,
        request: Optional[Union[recaptchaenterprise.AddIpOverrideRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        ip_override_data: Optional[recaptchaenterprise.IpOverrideData] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.AddIpOverrideResponse:
        r"""Adds an IP override to a key. The following restrictions hold:

        - The maximum number of IP overrides per key is 1000.
        - For any conflict (such as IP already exists or IP part of an
          existing IP range), an error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_add_ip_override():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                ip_override_data = recaptchaenterprise_v1.IpOverrideData()
                ip_override_data.ip = "ip_value"
                ip_override_data.override_type = "ALLOW"

                request = recaptchaenterprise_v1.AddIpOverrideRequest(
                    name="name_value",
                    ip_override_data=ip_override_data,
                )

                # Make the request
                response = await client.add_ip_override(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.AddIpOverrideRequest, dict]]):
                The request object. The AddIpOverride request message.
            name (:class:`str`):
                Required. The name of the key to which the IP override
                is added, in the format
                ``projects/{project}/keys/{key}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ip_override_data (:class:`google.cloud.recaptchaenterprise_v1.types.IpOverrideData`):
                Required. IP override added to the
                key.

                This corresponds to the ``ip_override_data`` field
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
            google.cloud.recaptchaenterprise_v1.types.AddIpOverrideResponse:
                Response for AddIpOverride.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, ip_override_data]
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
        if not isinstance(request, recaptchaenterprise.AddIpOverrideRequest):
            request = recaptchaenterprise.AddIpOverrideRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if ip_override_data is not None:
            request.ip_override_data = ip_override_data

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_ip_override
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

    async def remove_ip_override(
        self,
        request: Optional[
            Union[recaptchaenterprise.RemoveIpOverrideRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        ip_override_data: Optional[recaptchaenterprise.IpOverrideData] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.RemoveIpOverrideResponse:
        r"""Removes an IP override from a key. The following restrictions
        hold:

        - If the IP isn't found in an existing IP override, a
          ``NOT_FOUND`` error is returned.
        - If the IP is found in an existing IP override, but the
          override type does not match, a ``NOT_FOUND`` error is
          returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_remove_ip_override():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                ip_override_data = recaptchaenterprise_v1.IpOverrideData()
                ip_override_data.ip = "ip_value"
                ip_override_data.override_type = "ALLOW"

                request = recaptchaenterprise_v1.RemoveIpOverrideRequest(
                    name="name_value",
                    ip_override_data=ip_override_data,
                )

                # Make the request
                response = await client.remove_ip_override(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideRequest, dict]]):
                The request object. The RemoveIpOverride request message.
            name (:class:`str`):
                Required. The name of the key from which the IP override
                is removed, in the format
                ``projects/{project}/keys/{key}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ip_override_data (:class:`google.cloud.recaptchaenterprise_v1.types.IpOverrideData`):
                Required. IP override to be removed
                from the key.

                This corresponds to the ``ip_override_data`` field
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
            google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideResponse:
                Response for RemoveIpOverride.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, ip_override_data]
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
        if not isinstance(request, recaptchaenterprise.RemoveIpOverrideRequest):
            request = recaptchaenterprise.RemoveIpOverrideRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if ip_override_data is not None:
            request.ip_override_data = ip_override_data

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_ip_override
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

    async def list_ip_overrides(
        self,
        request: Optional[
            Union[recaptchaenterprise.ListIpOverridesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListIpOverridesAsyncPager:
        r"""Lists all IP overrides for a key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_list_ip_overrides():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.ListIpOverridesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_ip_overrides(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest, dict]]):
                The request object. The ListIpOverrides request message.
            parent (:class:`str`):
                Required. The parent key for which the IP overrides are
                listed, in the format ``projects/{project}/keys/{key}``.

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
            google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesAsyncPager:
                Response for ListIpOverrides.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

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
        if not isinstance(request, recaptchaenterprise.ListIpOverridesRequest):
            request = recaptchaenterprise.ListIpOverridesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_ip_overrides
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
        response = pagers.ListIpOverridesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_metrics(
        self,
        request: Optional[Union[recaptchaenterprise.GetMetricsRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Metrics:
        r"""Get some aggregated metrics for a Key. This data can
        be used to build dashboards.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_get_metrics():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.GetMetricsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_metrics(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.GetMetricsRequest, dict]]):
                The request object. The get metrics request message.
            name (:class:`str`):
                Required. The name of the requested metrics, in the
                format ``projects/{project}/keys/{key}/metrics``.

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
            google.cloud.recaptchaenterprise_v1.types.Metrics:
                Metrics for a single Key.
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
        if not isinstance(request, recaptchaenterprise.GetMetricsRequest):
            request = recaptchaenterprise.GetMetricsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_metrics
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

    async def get_policy(
        self,
        request: Optional[Union[recaptchaenterprise.GetPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Policy:
        r"""Get the policy for a key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_get_policy():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.GetPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.GetPolicyRequest, dict]]):
                The request object. The request message to get a policy.
            name (:class:`str`):
                Required. The name of the policy to get, in the format
                ``projects/{project}/keys/{key}/policy``.

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
            google.cloud.recaptchaenterprise_v1.types.Policy:
                A complete configuration set
                containing multiple grouped rules
                defining the behavior of reCAPTCHA for
                fraud detection and prevention.

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
        if not isinstance(request, recaptchaenterprise.GetPolicyRequest):
            request = recaptchaenterprise.GetPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_policy
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

    async def update_policy(
        self,
        request: Optional[Union[recaptchaenterprise.UpdatePolicyRequest, dict]] = None,
        *,
        policy: Optional[recaptchaenterprise.Policy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.Policy:
        r"""Updates the policy for a key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_update_policy():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.UpdatePolicyRequest(
                )

                # Make the request
                response = await client.update_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.UpdatePolicyRequest, dict]]):
                The request object. The request message to update a
                policy.
            policy (:class:`google.cloud.recaptchaenterprise_v1.types.Policy`):
                Required. The Policy's name is used to identify the
                policy to update, in the format
                ``projects/{project}/keys/{key}/policy``.

                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The mask to control which
                fields of the policy get updated. If the
                mask is not present, all fields are
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
            google.cloud.recaptchaenterprise_v1.types.Policy:
                A complete configuration set
                containing multiple grouped rules
                defining the behavior of reCAPTCHA for
                fraud detection and prevention.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [policy, update_mask]
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
        if not isinstance(request, recaptchaenterprise.UpdatePolicyRequest):
            request = recaptchaenterprise.UpdatePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if policy is not None:
            request.policy = policy
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("policy.name", request.policy.name),)
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

    async def create_firewall_policy(
        self,
        request: Optional[
            Union[recaptchaenterprise.CreateFirewallPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        firewall_policy: Optional[recaptchaenterprise.FirewallPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.FirewallPolicy:
        r"""Creates a new FirewallPolicy, specifying conditions
        at which reCAPTCHA Enterprise actions can be executed. A
        project may have a maximum of 1000 policies.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_create_firewall_policy():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.CreateFirewallPolicyRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_firewall_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.CreateFirewallPolicyRequest, dict]]):
                The request object. The create firewall policy request
                message.
            parent (:class:`str`):
                Required. The name of the project this policy applies
                to, in the format ``projects/{project}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy (:class:`google.cloud.recaptchaenterprise_v1.types.FirewallPolicy`):
                Required. Information to create the
                policy.

                This corresponds to the ``firewall_policy`` field
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
            google.cloud.recaptchaenterprise_v1.types.FirewallPolicy:
                A FirewallPolicy represents a single
                matching pattern and resulting actions
                to take.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, firewall_policy]
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
        if not isinstance(request, recaptchaenterprise.CreateFirewallPolicyRequest):
            request = recaptchaenterprise.CreateFirewallPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if firewall_policy is not None:
            request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_firewall_policy
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

    async def list_firewall_policies(
        self,
        request: Optional[
            Union[recaptchaenterprise.ListFirewallPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListFirewallPoliciesAsyncPager:
        r"""Returns the list of all firewall policies that belong
        to a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_list_firewall_policies():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.ListFirewallPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_firewall_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest, dict]]):
                The request object. The list firewall policies request
                message.
            parent (:class:`str`):
                Required. The name of the project to list the policies
                for, in the format ``projects/{project}``.

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
            google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesAsyncPager:
                Response to request to list firewall
                policies belonging to a project.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

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
        if not isinstance(request, recaptchaenterprise.ListFirewallPoliciesRequest):
            request = recaptchaenterprise.ListFirewallPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_firewall_policies
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
        response = pagers.ListFirewallPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_firewall_policy(
        self,
        request: Optional[
            Union[recaptchaenterprise.GetFirewallPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.FirewallPolicy:
        r"""Returns the specified firewall policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_get_firewall_policy():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.GetFirewallPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_firewall_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.GetFirewallPolicyRequest, dict]]):
                The request object. The get firewall policy request
                message.
            name (:class:`str`):
                Required. The name of the requested policy, in the
                format
                ``projects/{project}/firewallpolicies/{firewallpolicy}``.

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
            google.cloud.recaptchaenterprise_v1.types.FirewallPolicy:
                A FirewallPolicy represents a single
                matching pattern and resulting actions
                to take.

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
        if not isinstance(request, recaptchaenterprise.GetFirewallPolicyRequest):
            request = recaptchaenterprise.GetFirewallPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_firewall_policy
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

    async def update_firewall_policy(
        self,
        request: Optional[
            Union[recaptchaenterprise.UpdateFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[recaptchaenterprise.FirewallPolicy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.FirewallPolicy:
        r"""Updates the specified firewall policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_update_firewall_policy():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.UpdateFirewallPolicyRequest(
                )

                # Make the request
                response = await client.update_firewall_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.UpdateFirewallPolicyRequest, dict]]):
                The request object. The update firewall policy request
                message.
            firewall_policy (:class:`google.cloud.recaptchaenterprise_v1.types.FirewallPolicy`):
                Required. The policy to update.
                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The mask to control which
                fields of the policy get updated. If the
                mask is not present, all fields are
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
            google.cloud.recaptchaenterprise_v1.types.FirewallPolicy:
                A FirewallPolicy represents a single
                matching pattern and resulting actions
                to take.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [firewall_policy, update_mask]
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
        if not isinstance(request, recaptchaenterprise.UpdateFirewallPolicyRequest):
            request = recaptchaenterprise.UpdateFirewallPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if firewall_policy is not None:
            request.firewall_policy = firewall_policy
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_firewall_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy.name", request.firewall_policy.name),)
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

    async def delete_firewall_policy(
        self,
        request: Optional[
            Union[recaptchaenterprise.DeleteFirewallPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified firewall policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_delete_firewall_policy():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.DeleteFirewallPolicyRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_firewall_policy(request=request)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.DeleteFirewallPolicyRequest, dict]]):
                The request object. The delete firewall policy request
                message.
            name (:class:`str`):
                Required. The name of the policy to be deleted, in the
                format
                ``projects/{project}/firewallpolicies/{firewallpolicy}``.

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
        if not isinstance(request, recaptchaenterprise.DeleteFirewallPolicyRequest):
            request = recaptchaenterprise.DeleteFirewallPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_firewall_policy
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

    async def reorder_firewall_policies(
        self,
        request: Optional[
            Union[recaptchaenterprise.ReorderFirewallPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> recaptchaenterprise.ReorderFirewallPoliciesResponse:
        r"""Reorders all firewall policies.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_reorder_firewall_policies():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.ReorderFirewallPoliciesRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = await client.reorder_firewall_policies(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesRequest, dict]]):
                The request object. The reorder firewall policies request
                message.
            parent (:class:`str`):
                Required. The name of the project to list the policies
                for, in the format ``projects/{project}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (:class:`MutableSequence[str]`):
                Required. A list containing all policy names, in the new
                order. Each name is in the format
                ``projects/{project}/firewallpolicies/{firewallpolicy}``.

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
            google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesResponse:
                The reorder firewall policies
                response message.

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
        if not isinstance(request, recaptchaenterprise.ReorderFirewallPoliciesRequest):
            request = recaptchaenterprise.ReorderFirewallPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if names:
            request.names.extend(names)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reorder_firewall_policies
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

    async def list_related_account_groups(
        self,
        request: Optional[
            Union[recaptchaenterprise.ListRelatedAccountGroupsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRelatedAccountGroupsAsyncPager:
        r"""List groups of related accounts.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_list_related_account_groups():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.ListRelatedAccountGroupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_related_account_groups(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest, dict]]):
                The request object. The request message to list related
                account groups.
            parent (:class:`str`):
                Required. The name of the project to list related
                account groups from, in the format
                ``projects/{project}``.

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
            google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsAsyncPager:
                The response to a ListRelatedAccountGroups call.

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
        if not isinstance(request, recaptchaenterprise.ListRelatedAccountGroupsRequest):
            request = recaptchaenterprise.ListRelatedAccountGroupsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_related_account_groups
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
        response = pagers.ListRelatedAccountGroupsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_related_account_group_memberships(
        self,
        request: Optional[
            Union[recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRelatedAccountGroupMembershipsAsyncPager:
        r"""Get memberships in a group of related accounts.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_list_related_account_group_memberships():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.ListRelatedAccountGroupMembershipsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_related_account_group_memberships(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest, dict]]):
                The request object. The request message to list
                memberships in a related account group.
            parent (:class:`str`):
                Required. The resource name for the related account
                group in the format
                ``projects/{project}/relatedaccountgroups/{relatedaccountgroup}``.

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
            google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsAsyncPager:
                The response to a ListRelatedAccountGroupMemberships
                call.

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
            request, recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest
        ):
            request = recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_related_account_group_memberships
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
        response = pagers.ListRelatedAccountGroupMembershipsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_related_account_group_memberships(
        self,
        request: Optional[
            Union[recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest, dict]
        ] = None,
        *,
        project: Optional[str] = None,
        hashed_account_id: Optional[bytes] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchRelatedAccountGroupMembershipsAsyncPager:
        r"""Search group memberships related to a given account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recaptchaenterprise_v1

            async def sample_search_related_account_group_memberships():
                # Create a client
                client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

                # Initialize request argument(s)
                request = recaptchaenterprise_v1.SearchRelatedAccountGroupMembershipsRequest(
                    project="project_value",
                )

                # Make the request
                page_result = client.search_related_account_group_memberships(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest, dict]]):
                The request object. The request message to search related
                account group memberships.
            project (:class:`str`):
                Required. The name of the project to search related
                account group memberships from. Specify the project name
                in the following format: ``projects/{project}``.

                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hashed_account_id (:class:`bytes`):
                Optional. Deprecated: use ``account_id`` instead. The
                unique stable hashed account identifier used to search
                connections. The identifier should correspond to a
                ``hashed_account_id`` provided in a previous
                ``CreateAssessment`` or ``AnnotateAssessment`` call.
                Either hashed_account_id or account_id must be set, but
                not both.

                This corresponds to the ``hashed_account_id`` field
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
            google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsAsyncPager:
                The response to a SearchRelatedAccountGroupMemberships
                call.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project, hashed_account_id]
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
            request, recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest
        ):
            request = recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project is not None:
            request.project = project
        if hashed_account_id is not None:
            request.hashed_account_id = hashed_account_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_related_account_group_memberships
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", request.project),)),
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
        response = pagers.SearchRelatedAccountGroupMembershipsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "RecaptchaEnterpriseServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("RecaptchaEnterpriseServiceAsyncClient",)
