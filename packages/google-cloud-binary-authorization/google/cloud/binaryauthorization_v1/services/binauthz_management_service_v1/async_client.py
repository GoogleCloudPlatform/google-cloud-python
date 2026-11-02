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

from google.cloud.binaryauthorization_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)

from google.cloud.binaryauthorization_v1.services.binauthz_management_service_v1 import (
    pagers,
)
from google.cloud.binaryauthorization_v1.types import resources, service

from .client import BinauthzManagementServiceV1Client
from .transports.base import DEFAULT_CLIENT_INFO, BinauthzManagementServiceV1Transport
from .transports.grpc_asyncio import BinauthzManagementServiceV1GrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class BinauthzManagementServiceV1AsyncClient:
    """Google Cloud Management Service for Binary Authorization admission
    policies and attestation authorities.

    This API implements a REST model with the following objects:

    - [Policy][google.cloud.binaryauthorization.v1.Policy]
    - [Attestor][google.cloud.binaryauthorization.v1.Attestor]
    """

    _client: BinauthzManagementServiceV1Client

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = BinauthzManagementServiceV1Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = BinauthzManagementServiceV1Client.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        BinauthzManagementServiceV1Client._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = BinauthzManagementServiceV1Client._DEFAULT_UNIVERSE

    attestor_path = staticmethod(BinauthzManagementServiceV1Client.attestor_path)
    parse_attestor_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_attestor_path
    )
    policy_path = staticmethod(BinauthzManagementServiceV1Client.policy_path)
    parse_policy_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_policy_path
    )
    common_billing_account_path = staticmethod(
        BinauthzManagementServiceV1Client.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        BinauthzManagementServiceV1Client.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        BinauthzManagementServiceV1Client.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_common_organization_path
    )
    common_project_path = staticmethod(
        BinauthzManagementServiceV1Client.common_project_path
    )
    parse_common_project_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_common_project_path
    )
    common_location_path = staticmethod(
        BinauthzManagementServiceV1Client.common_location_path
    )
    parse_common_location_path = staticmethod(
        BinauthzManagementServiceV1Client.parse_common_location_path
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
            BinauthzManagementServiceV1AsyncClient: The constructed client.
        """
        sa_info_func = (
            BinauthzManagementServiceV1Client.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            BinauthzManagementServiceV1AsyncClient, info, *args, **kwargs
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
            BinauthzManagementServiceV1AsyncClient: The constructed client.
        """
        sa_file_func = (
            BinauthzManagementServiceV1Client.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            BinauthzManagementServiceV1AsyncClient, filename, *args, **kwargs
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
        return BinauthzManagementServiceV1Client.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> BinauthzManagementServiceV1Transport:
        """Returns the transport used by the client instance.

        Returns:
            BinauthzManagementServiceV1Transport: The transport used by the client instance.
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

    get_transport_class = BinauthzManagementServiceV1Client.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                BinauthzManagementServiceV1Transport,
                Callable[..., BinauthzManagementServiceV1Transport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the binauthz management service v1 async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,BinauthzManagementServiceV1Transport,Callable[..., BinauthzManagementServiceV1Transport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the BinauthzManagementServiceV1Transport constructor.
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
        self._client = BinauthzManagementServiceV1Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient`.",
                extra={
                    "serviceName": "google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1",
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
                    "serviceName": "google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1",
                    "credentialsType": None,
                },
            )

    async def get_policy(
        self,
        request: Optional[Union[service.GetPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Policy:
        r"""A [policy][google.cloud.binaryauthorization.v1.Policy] specifies
        the [attestors][google.cloud.binaryauthorization.v1.Attestor]
        that must attest to a container image, before the project is
        allowed to deploy that image. There is at most one policy per
        project. All image admission requests are permitted if a project
        has no policy.

        Gets the [policy][google.cloud.binaryauthorization.v1.Policy]
        for this project. Returns a default
        [policy][google.cloud.binaryauthorization.v1.Policy] if the
        project does not have one.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_get_policy():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                request = binaryauthorization_v1.GetPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.GetPolicyRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.GetPolicy][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicy].
            name (:class:`str`):
                Required. The resource name of the
                [policy][google.cloud.binaryauthorization.v1.Policy] to
                retrieve, in the format ``projects/*/policy``.

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
            google.cloud.binaryauthorization_v1.types.Policy:
                A [policy][google.cloud.binaryauthorization.v1.Policy] for container image
                   binary authorization.

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
        if not isinstance(request, service.GetPolicyRequest):
            request = service.GetPolicyRequest(request)

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
        request: Optional[Union[service.UpdatePolicyRequest, dict]] = None,
        *,
        policy: Optional[resources.Policy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Policy:
        r"""Creates or updates a project's
        [policy][google.cloud.binaryauthorization.v1.Policy], and
        returns a copy of the new
        [policy][google.cloud.binaryauthorization.v1.Policy]. A policy
        is always updated as a whole, to avoid race conditions with
        concurrent policy enforcement (or management!) requests. Returns
        ``NOT_FOUND`` if the project does not exist,
        ``INVALID_ARGUMENT`` if the request is malformed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_update_policy():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                policy = binaryauthorization_v1.Policy()
                policy.default_admission_rule.evaluation_mode = "ALWAYS_DENY"
                policy.default_admission_rule.enforcement_mode = "DRYRUN_AUDIT_LOG_ONLY"

                request = binaryauthorization_v1.UpdatePolicyRequest(
                    policy=policy,
                )

                # Make the request
                response = await client.update_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.UpdatePolicyRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.UpdatePolicy][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicy].
            policy (:class:`google.cloud.binaryauthorization_v1.types.Policy`):
                Required. A new or updated
                [policy][google.cloud.binaryauthorization.v1.Policy]
                value. The service will overwrite the [policy
                name][google.cloud.binaryauthorization.v1.Policy.name]
                field with the resource name in the request URL, in the
                format ``projects/*/policy``.

                This corresponds to the ``policy`` field
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
            google.cloud.binaryauthorization_v1.types.Policy:
                A [policy][google.cloud.binaryauthorization.v1.Policy] for container image
                   binary authorization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [policy]
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
        if not isinstance(request, service.UpdatePolicyRequest):
            request = service.UpdatePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if policy is not None:
            request.policy = policy

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

    async def create_attestor(
        self,
        request: Optional[Union[service.CreateAttestorRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        attestor_id: Optional[str] = None,
        attestor: Optional[resources.Attestor] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Attestor:
        r"""Creates an
        [attestor][google.cloud.binaryauthorization.v1.Attestor], and
        returns a copy of the new
        [attestor][google.cloud.binaryauthorization.v1.Attestor].
        Returns ``NOT_FOUND`` if the project does not exist,
        ``INVALID_ARGUMENT`` if the request is malformed,
        ``ALREADY_EXISTS`` if the
        [attestor][google.cloud.binaryauthorization.v1.Attestor] already
        exists.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_create_attestor():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                attestor = binaryauthorization_v1.Attestor()
                attestor.user_owned_grafeas_note.note_reference = "note_reference_value"
                attestor.name = "name_value"

                request = binaryauthorization_v1.CreateAttestorRequest(
                    parent="parent_value",
                    attestor_id="attestor_id_value",
                    attestor=attestor,
                )

                # Make the request
                response = await client.create_attestor(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.CreateAttestorRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.CreateAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestor].
            parent (:class:`str`):
                Required. The parent of this
                [attestor][google.cloud.binaryauthorization.v1.Attestor].

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            attestor_id (:class:`str`):
                Required. The
                [attestors][google.cloud.binaryauthorization.v1.Attestor]
                ID.

                This corresponds to the ``attestor_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            attestor (:class:`google.cloud.binaryauthorization_v1.types.Attestor`):
                Required. The initial
                [attestor][google.cloud.binaryauthorization.v1.Attestor]
                value. The service will overwrite the [attestor
                name][google.cloud.binaryauthorization.v1.Attestor.name]
                field with the resource name, in the format
                ``projects/*/attestors/*``.

                This corresponds to the ``attestor`` field
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
            google.cloud.binaryauthorization_v1.types.Attestor:
                An [attestor][google.cloud.binaryauthorization.v1.Attestor] that attests to
                   container image artifacts. An existing attestor
                   cannot be modified except where indicated.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, attestor_id, attestor]
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
        if not isinstance(request, service.CreateAttestorRequest):
            request = service.CreateAttestorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if attestor_id is not None:
            request.attestor_id = attestor_id
        if attestor is not None:
            request.attestor = attestor

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_attestor
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

    async def get_attestor(
        self,
        request: Optional[Union[service.GetAttestorRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Attestor:
        r"""Gets an
        [attestor][google.cloud.binaryauthorization.v1.Attestor].
        Returns ``NOT_FOUND`` if the
        [attestor][google.cloud.binaryauthorization.v1.Attestor] does
        not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_get_attestor():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                request = binaryauthorization_v1.GetAttestorRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_attestor(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.GetAttestorRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.GetAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestor].
            name (:class:`str`):
                Required. The name of the
                [attestor][google.cloud.binaryauthorization.v1.Attestor]
                to retrieve, in the format ``projects/*/attestors/*``.

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
            google.cloud.binaryauthorization_v1.types.Attestor:
                An [attestor][google.cloud.binaryauthorization.v1.Attestor] that attests to
                   container image artifacts. An existing attestor
                   cannot be modified except where indicated.

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
        if not isinstance(request, service.GetAttestorRequest):
            request = service.GetAttestorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_attestor
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

    async def update_attestor(
        self,
        request: Optional[Union[service.UpdateAttestorRequest, dict]] = None,
        *,
        attestor: Optional[resources.Attestor] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Attestor:
        r"""Updates an
        [attestor][google.cloud.binaryauthorization.v1.Attestor].
        Returns ``NOT_FOUND`` if the
        [attestor][google.cloud.binaryauthorization.v1.Attestor] does
        not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_update_attestor():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                attestor = binaryauthorization_v1.Attestor()
                attestor.user_owned_grafeas_note.note_reference = "note_reference_value"
                attestor.name = "name_value"

                request = binaryauthorization_v1.UpdateAttestorRequest(
                    attestor=attestor,
                )

                # Make the request
                response = await client.update_attestor(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.UpdateAttestorRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.UpdateAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestor].
            attestor (:class:`google.cloud.binaryauthorization_v1.types.Attestor`):
                Required. The updated
                [attestor][google.cloud.binaryauthorization.v1.Attestor]
                value. The service will overwrite the [attestor
                name][google.cloud.binaryauthorization.v1.Attestor.name]
                field with the resource name in the request URL, in the
                format ``projects/*/attestors/*``.

                This corresponds to the ``attestor`` field
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
            google.cloud.binaryauthorization_v1.types.Attestor:
                An [attestor][google.cloud.binaryauthorization.v1.Attestor] that attests to
                   container image artifacts. An existing attestor
                   cannot be modified except where indicated.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [attestor]
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
        if not isinstance(request, service.UpdateAttestorRequest):
            request = service.UpdateAttestorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if attestor is not None:
            request.attestor = attestor

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_attestor
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attestor.name", request.attestor.name),)
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

    async def list_attestors(
        self,
        request: Optional[Union[service.ListAttestorsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAttestorsAsyncPager:
        r"""Lists [attestors][google.cloud.binaryauthorization.v1.Attestor].
        Returns ``INVALID_ARGUMENT`` if the project does not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_list_attestors():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                request = binaryauthorization_v1.ListAttestorsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_attestors(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.ListAttestorsRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].
            parent (:class:`str`):
                Required. The resource name of the project associated
                with the
                [attestors][google.cloud.binaryauthorization.v1.Attestor],
                in the format ``projects/*``.

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
            google.cloud.binaryauthorization_v1.services.binauthz_management_service_v1.pagers.ListAttestorsAsyncPager:
                Response message for
                   [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

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
        if not isinstance(request, service.ListAttestorsRequest):
            request = service.ListAttestorsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_attestors
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
        response = pagers.ListAttestorsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_attestor(
        self,
        request: Optional[Union[service.DeleteAttestorRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an
        [attestor][google.cloud.binaryauthorization.v1.Attestor].
        Returns ``NOT_FOUND`` if the
        [attestor][google.cloud.binaryauthorization.v1.Attestor] does
        not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import binaryauthorization_v1

            async def sample_delete_attestor():
                # Create a client
                client = binaryauthorization_v1.BinauthzManagementServiceV1AsyncClient()

                # Initialize request argument(s)
                request = binaryauthorization_v1.DeleteAttestorRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_attestor(request=request)

        Args:
            request (Optional[Union[google.cloud.binaryauthorization_v1.types.DeleteAttestorRequest, dict]]):
                The request object. Request message for
                [BinauthzManagementServiceV1.DeleteAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestor].
            name (:class:`str`):
                Required. The name of the
                [attestors][google.cloud.binaryauthorization.v1.Attestor]
                to delete, in the format ``projects/*/attestors/*``.

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
        if not isinstance(request, service.DeleteAttestorRequest):
            request = service.DeleteAttestorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_attestor
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

    async def set_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.SetIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the IAM access control policy on the specified function.

        Replaces any existing policy.

        Args:
            request (:class:`~.iam_policy_pb2.SetIamPolicyRequest`):
                The request object. Request message for `SetIamPolicy`
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**

                ::

                    {
                      "bindings": [
                        {
                          "role": "roles/resourcemanager.organizationAdmin",
                          "members": [
                            "user:mike@example.com",
                            "group:admins@example.com",
                            "domain:google.com",
                            "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                          ]
                        },
                        {
                          "role": "roles/resourcemanager.organizationViewer",
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**

                ::

                    bindings:
                    - members:
                      - user:mike@example.com
                      - group:admins@example.com
                      - domain:google.com
                      - serviceAccount:my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin
                    - members:
                      - user:eve@example.com
                      role: roles/resourcemanager.organizationViewer
                      condition:
                        title: expirable access
                        description: Does not grant access after Sep 2020
                        expression: request.time < timestamp('2020-10-01T00:00:00.000Z')

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.SetIamPolicyRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.SetIamPolicyRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.set_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    async def get_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.GetIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the IAM access control policy for a function.

        Returns an empty policy if the function exists and does not have a
        policy set.

        Args:
            request (:class:`~.iam_policy_pb2.GetIamPolicyRequest`):
                The request object. Request message for `GetIamPolicy`
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if
                any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**

                ::

                    {
                      "bindings": [
                        {
                          "role": "roles/resourcemanager.organizationAdmin",
                          "members": [
                            "user:mike@example.com",
                            "group:admins@example.com",
                            "domain:google.com",
                            "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                          ]
                        },
                        {
                          "role": "roles/resourcemanager.organizationViewer",
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**

                ::

                    bindings:
                    - members:
                      - user:mike@example.com
                      - group:admins@example.com
                      - domain:google.com
                      - serviceAccount:my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin
                    - members:
                      - user:eve@example.com
                      role: roles/resourcemanager.organizationViewer
                      condition:
                        title: expirable access
                        description: Does not grant access after Sep 2020
                        expression: request.time < timestamp('2020-10-01T00:00:00.000Z')

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.GetIamPolicyRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.GetIamPolicyRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    async def test_iam_permissions(
        self,
        request: Optional[Union[iam_policy_pb2.TestIamPermissionsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Tests the specified IAM permissions against the IAM access control
            policy for a function.

        If the function does not exist, this will return an empty set
        of permissions, not a NOT_FOUND error.

        Args:
            request (:class:`~.iam_policy_pb2.TestIamPermissionsRequest`):
                The request object. Request message for
                `TestIamPermissions` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for ``TestIamPermissions`` method.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.TestIamPermissionsRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.TestIamPermissionsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[
            self._client._transport.test_iam_permissions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    async def __aenter__(self) -> "BinauthzManagementServiceV1AsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("BinauthzManagementServiceV1AsyncClient",)
