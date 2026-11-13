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

from google.apps.meet_v2 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore

from google.apps.meet_v2.services.spaces_service import pagers
from google.apps.meet_v2.types import resource, service

from .client import SpacesServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, SpacesServiceTransport
from .transports.grpc_asyncio import SpacesServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SpacesServiceAsyncClient:
    """REST API for services dealing with spaces."""

    _client: SpacesServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SpacesServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SpacesServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SpacesServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SpacesServiceClient._DEFAULT_UNIVERSE

    conference_record_path = staticmethod(SpacesServiceClient.conference_record_path)
    parse_conference_record_path = staticmethod(
        SpacesServiceClient.parse_conference_record_path
    )
    member_path = staticmethod(SpacesServiceClient.member_path)
    parse_member_path = staticmethod(SpacesServiceClient.parse_member_path)
    space_path = staticmethod(SpacesServiceClient.space_path)
    parse_space_path = staticmethod(SpacesServiceClient.parse_space_path)
    common_billing_account_path = staticmethod(
        SpacesServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SpacesServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SpacesServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        SpacesServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        SpacesServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        SpacesServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(SpacesServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        SpacesServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(SpacesServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        SpacesServiceClient.parse_common_location_path
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
            SpacesServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            SpacesServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SpacesServiceAsyncClient, info, *args, **kwargs)

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
            SpacesServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            SpacesServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(SpacesServiceAsyncClient, filename, *args, **kwargs)

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
        return SpacesServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> SpacesServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            SpacesServiceTransport: The transport used by the client instance.
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

    get_transport_class = SpacesServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, SpacesServiceTransport, Callable[..., SpacesServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the spaces service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SpacesServiceTransport,Callable[..., SpacesServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SpacesServiceTransport constructor.
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
        self._client = SpacesServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.apps.meet_v2.SpacesServiceAsyncClient`.",
                extra={
                    "serviceName": "google.apps.meet.v2.SpacesService",
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
                    "serviceName": "google.apps.meet.v2.SpacesService",
                    "credentialsType": None,
                },
            )

    async def create_space(
        self,
        request: Optional[Union[service.CreateSpaceRequest, dict]] = None,
        *,
        space: Optional[resource.Space] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Space:
        r"""Creates a space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_create_space():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.CreateSpaceRequest(
                )

                # Make the request
                response = await client.create_space(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.CreateSpaceRequest, dict]]):
                The request object. Request to create a space.
            space (:class:`google.apps.meet_v2.types.Space`):
                Space to be created. As of May 2023,
                the input space can be empty. Later on
                the input space can be non-empty when
                space configuration is introduced.

                This corresponds to the ``space`` field
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
            google.apps.meet_v2.types.Space:
                Virtual place where conferences are
                held. Only one active conference can be
                held in one space at any given time.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [space]
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
        if not isinstance(request, service.CreateSpaceRequest):
            request = service.CreateSpaceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if space is not None:
            request.space = space

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_space
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

    async def get_space(
        self,
        request: Optional[Union[service.GetSpaceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Space:
        r"""Gets details about a meeting space.

        For an example, see `Get a meeting
        space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#get-meeting-space>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_get_space():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.GetSpaceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_space(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.GetSpaceRequest, dict]]):
                The request object. Request to get a space.
            name (:class:`str`):
                Required. Resource name of the space.

                Format: ``spaces/{space}`` or ``spaces/{meetingCode}``.

                ``{space}`` is the resource identifier for the space.
                It's a unique, server-generated ID and is case
                sensitive. For example, ``jQCFfuBOdN5z``.

                ``{meetingCode}`` is an alias for the space. It's a
                typeable, unique character string and is non-case
                sensitive. For example, ``abc-mnop-xyz``. The maximum
                length is 128 characters.

                A ``meetingCode`` shouldn't be stored long term as it
                can become dissociated from a meeting space and can be
                reused for different meeting spaces in the future.
                Generally, a ``meetingCode`` expires 365 days after last
                use. For more information, see `Learn about meeting
                codes in Google
                Meet <https://support.google.com/meet/answer/10710509>`__.

                For more information, see `How Meet identifies a meeting
                space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space>`__.

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
            google.apps.meet_v2.types.Space:
                Virtual place where conferences are
                held. Only one active conference can be
                held in one space at any given time.

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
        if not isinstance(request, service.GetSpaceRequest):
            request = service.GetSpaceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_space
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

    async def update_space(
        self,
        request: Optional[Union[service.UpdateSpaceRequest, dict]] = None,
        *,
        space: Optional[resource.Space] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Space:
        r"""Updates details about a meeting space.

        For an example, see `Update a meeting
        space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#update-meeting-space>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_update_space():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.UpdateSpaceRequest(
                )

                # Make the request
                response = await client.update_space(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.UpdateSpaceRequest, dict]]):
                The request object. Request to update a space.
            space (:class:`google.apps.meet_v2.types.Space`):
                Required. Space to be updated.
                This corresponds to the ``space`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask used to specify the fields to be
                updated in the space. If update_mask isn't provided(not
                set, set with empty paths, or only has "" as paths), it
                defaults to update all fields provided with values in
                the request. Using "\*" as update_mask will update all
                fields, including deleting fields not set in the
                request.

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
            google.apps.meet_v2.types.Space:
                Virtual place where conferences are
                held. Only one active conference can be
                held in one space at any given time.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [space, update_mask]
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
        if not isinstance(request, service.UpdateSpaceRequest):
            request = service.UpdateSpaceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if space is not None:
            request.space = space
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_space
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("space.name", request.space.name),)
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

    async def end_active_conference(
        self,
        request: Optional[Union[service.EndActiveConferenceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Ends an active conference (if there's one).

        For an example, see `End active
        conference <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#end-active-conference>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_end_active_conference():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.EndActiveConferenceRequest(
                    name="name_value",
                )

                # Make the request
                await client.end_active_conference(request=request)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.EndActiveConferenceRequest, dict]]):
                The request object. Request to end an ongoing conference
                of a space.
            name (:class:`str`):
                Required. Resource name of the space.

                Format: ``spaces/{space}``.

                ``{space}`` is the resource identifier for the space.
                It's a unique, server-generated ID and is case
                sensitive. For example, ``jQCFfuBOdN5z``.

                For more information, see `How Meet identifies a meeting
                space <https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space>`__.

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
        if not isinstance(request, service.EndActiveConferenceRequest):
            request = service.EndActiveConferenceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.end_active_conference
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

    async def create_member(
        self,
        request: Optional[Union[service.CreateMemberRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        member: Optional[resource.Member] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Member:
        r"""Creates a member.

        This API supports the ``fields`` parameter in
        `SystemParameterContext <https://cloud.google.com/apis/docs/system-parameters>`__.
        When the ``fields`` parameter is omitted, this API response will
        default to "name,email,role".

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_create_member():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.CreateMemberRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_member(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.CreateMemberRequest, dict]]):
                The request object. Request to create a member for a
                space.
            parent (:class:`str`):
                Required. Format: spaces/{space}
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            member (:class:`google.apps.meet_v2.types.Member`):
                Required. The member to be created.
                This corresponds to the ``member`` field
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
            google.apps.meet_v2.types.Member:
                Users who are configured to have a
                role in the space. These users can join
                the space without knocking.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, member]
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
        if not isinstance(request, service.CreateMemberRequest):
            request = service.CreateMemberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if member is not None:
            request.member = member

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_member
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

    async def get_member(
        self,
        request: Optional[Union[service.GetMemberRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Member:
        r"""Gets a member.

        This API supports the ``fields`` parameter in
        `SystemParameterContext <https://cloud.google.com/apis/docs/system-parameters>`__.
        When the ``fields`` parameter is omitted, this API response will
        default to "name,email,role".

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_get_member():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.GetMemberRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_member(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.GetMemberRequest, dict]]):
                The request object. Request to get a member from a space.
            name (:class:`str`):
                Required. Format:
                “spaces/{space}/members/{member}”

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
            google.apps.meet_v2.types.Member:
                Users who are configured to have a
                role in the space. These users can join
                the space without knocking.

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
        if not isinstance(request, service.GetMemberRequest):
            request = service.GetMemberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_member
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

    async def list_members(
        self,
        request: Optional[Union[service.ListMembersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMembersAsyncPager:
        r"""Lists members.

        This API supports the ``fields`` parameter in
        `SystemParameterContext <https://cloud.google.com/apis/docs/system-parameters>`__.
        When the ``fields`` parameter is omitted this API response will
        default to "name,email,role".

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_list_members():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.ListMembersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_members(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.ListMembersRequest, dict]]):
                The request object. Request to list all members of a
                space.
            parent (:class:`str`):
                Required. Format: spaces/{space}
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
            google.apps.meet_v2.services.spaces_service.pagers.ListMembersAsyncPager:
                Response of list members.

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
        if not isinstance(request, service.ListMembersRequest):
            request = service.ListMembersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_members
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
        response = pagers.ListMembersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_member(
        self,
        request: Optional[Union[service.DeleteMemberRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the member who was previously assigned roles
        in the space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_delete_member():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.DeleteMemberRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_member(request=request)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.DeleteMemberRequest, dict]]):
                The request object. Request to delete a member from a
                space.
            name (:class:`str`):
                Required. Format:
                “spaces/{space}/members/{member}”

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
        if not isinstance(request, service.DeleteMemberRequest):
            request = service.DeleteMemberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_member
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

    async def update_member(
        self,
        request: Optional[Union[service.UpdateMemberRequest, dict]] = None,
        *,
        member: Optional[resource.Member] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Member:
        r"""Updates a member.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_update_member():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.UpdateMemberRequest(
                )

                # Make the request
                response = await client.update_member(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.UpdateMemberRequest, dict]]):
                The request object. Request to update a member.
            member (:class:`google.apps.meet_v2.types.Member`):
                Required. The Member to update.
                Format: spaces/{space}/members/{member}

                This corresponds to the ``member`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask used to specify the fields to be
                updated in the member. If update_mask isn't provided(not
                set, set with empty paths, or only has "" as paths), it
                defaults to update all fields provided with values in
                the request. Using "\*" as update_mask will update all
                fields, including deleting fields not set in the
                request. In case of BatchUpdate, it must be absent or
                the same as the update_mask in BatchUpdateMembersRequest
                when UpdateMemberRequest is built as a child request of
                BatchUpdateMembersRequest.

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
            google.apps.meet_v2.types.Member:
                Users who are configured to have a
                role in the space. These users can join
                the space without knocking.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [member, update_mask]
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
        if not isinstance(request, service.UpdateMemberRequest):
            request = service.UpdateMemberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if member is not None:
            request.member = member
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_member
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("member.name", request.member.name),)
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

    async def batch_update_members(
        self,
        request: Optional[Union[service.BatchUpdateMembersRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.BatchUpdateMembersResponse:
        r"""Updates members of one space within a batch.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import meet_v2

            async def sample_batch_update_members():
                # Create a client
                client = meet_v2.SpacesServiceAsyncClient()

                # Initialize request argument(s)
                request = meet_v2.BatchUpdateMembersRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.batch_update_members(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.meet_v2.types.BatchUpdateMembersRequest, dict]]):
                The request object. Request to update members of one
                space within a batch.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.apps.meet_v2.types.BatchUpdateMembersResponse:
                Response of batch update members.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.BatchUpdateMembersRequest):
            request = service.BatchUpdateMembersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_update_members
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

    async def __aenter__(self) -> "SpacesServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SpacesServiceAsyncClient",)
