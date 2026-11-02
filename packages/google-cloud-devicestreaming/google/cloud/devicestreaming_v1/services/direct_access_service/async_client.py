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
    AsyncIterator,
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

from google.cloud.devicestreaming_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.devicestreaming_v1.services.direct_access_service import pagers
from google.cloud.devicestreaming_v1.types import adb_service, service

from .client import DirectAccessServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DirectAccessServiceTransport
from .transports.grpc_asyncio import DirectAccessServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DirectAccessServiceAsyncClient:
    """A service for allocating Android devices and interacting with
    the live-allocated devices.

    Each Session will wait for available capacity, at a higher
    priority over Test Execution. When allocated, the session will
    be exposed through a stream for integration.

    DirectAccessService is currently available as a preview to
    select developers. You can register today on behalf of you and
    your team at
    https://developer.android.com/studio/preview/android-device-streaming
    """

    _client: DirectAccessServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DirectAccessServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DirectAccessServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DirectAccessServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DirectAccessServiceClient._DEFAULT_UNIVERSE

    device_session_path = staticmethod(DirectAccessServiceClient.device_session_path)
    parse_device_session_path = staticmethod(
        DirectAccessServiceClient.parse_device_session_path
    )
    common_billing_account_path = staticmethod(
        DirectAccessServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DirectAccessServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DirectAccessServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DirectAccessServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DirectAccessServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DirectAccessServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DirectAccessServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DirectAccessServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DirectAccessServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DirectAccessServiceClient.parse_common_location_path
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
            DirectAccessServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DirectAccessServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DirectAccessServiceAsyncClient, info, *args, **kwargs)

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
            DirectAccessServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DirectAccessServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DirectAccessServiceAsyncClient, filename, *args, **kwargs)

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
        return DirectAccessServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> DirectAccessServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DirectAccessServiceTransport: The transport used by the client instance.
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

    get_transport_class = DirectAccessServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DirectAccessServiceTransport,
                Callable[..., DirectAccessServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the direct access service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DirectAccessServiceTransport,Callable[..., DirectAccessServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DirectAccessServiceTransport constructor.
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
        self._client = DirectAccessServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.devicestreaming_v1.DirectAccessServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.devicestreaming.v1.DirectAccessService",
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
                    "serviceName": "google.cloud.devicestreaming.v1.DirectAccessService",
                    "credentialsType": None,
                },
            )

    async def create_device_session(
        self,
        request: Optional[Union[service.CreateDeviceSessionRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        device_session: Optional[service.DeviceSession] = None,
        device_session_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.DeviceSession:
        r"""Creates a DeviceSession.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import devicestreaming_v1

            async def sample_create_device_session():
                # Create a client
                client = devicestreaming_v1.DirectAccessServiceAsyncClient()

                # Initialize request argument(s)
                device_session = devicestreaming_v1.DeviceSession()
                device_session.android_device.android_model_id = "android_model_id_value"
                device_session.android_device.android_version_id = "android_version_id_value"

                request = devicestreaming_v1.CreateDeviceSessionRequest(
                    parent="parent_value",
                    device_session=device_session,
                )

                # Make the request
                response = await client.create_device_session(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devicestreaming_v1.types.CreateDeviceSessionRequest, dict]]):
                The request object. Request message for
                DirectAccessService.CreateDeviceSession.
            parent (:class:`str`):
                Required. The Compute Engine project under which this
                device will be allocated. "projects/{project_id}"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            device_session (:class:`google.cloud.devicestreaming_v1.types.DeviceSession`):
                Required. A DeviceSession to create.
                This corresponds to the ``device_session`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            device_session_id (:class:`str`):
                Optional. The ID to use for the DeviceSession, which
                will become the final component of the DeviceSession's
                resource name.

                This value should be 4-63 characters, and valid
                characters are /[a-z][0-9]-/.

                This corresponds to the ``device_session_id`` field
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
            google.cloud.devicestreaming_v1.types.DeviceSession:
                Protobuf message describing the
                device message, used from several RPCs.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, device_session, device_session_id]
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
        if not isinstance(request, service.CreateDeviceSessionRequest):
            request = service.CreateDeviceSessionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if device_session is not None:
            request.device_session = device_session
        if device_session_id is not None:
            request.device_session_id = device_session_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_device_session
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

    async def list_device_sessions(
        self,
        request: Optional[Union[service.ListDeviceSessionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDeviceSessionsAsyncPager:
        r"""Lists DeviceSessions owned by the project user.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import devicestreaming_v1

            async def sample_list_device_sessions():
                # Create a client
                client = devicestreaming_v1.DirectAccessServiceAsyncClient()

                # Initialize request argument(s)
                request = devicestreaming_v1.ListDeviceSessionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_device_sessions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.devicestreaming_v1.types.ListDeviceSessionsRequest, dict]]):
                The request object. Request message for
                DirectAccessService.ListDeviceSessions.
            parent (:class:`str`):
                Required. The name of the parent to request, e.g.
                "projects/{project_id}"

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
            google.cloud.devicestreaming_v1.services.direct_access_service.pagers.ListDeviceSessionsAsyncPager:
                Response message for
                DirectAccessService.ListDeviceSessions.
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
        if not isinstance(request, service.ListDeviceSessionsRequest):
            request = service.ListDeviceSessionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_device_sessions
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
        response = pagers.ListDeviceSessionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_device_session(
        self,
        request: Optional[Union[service.GetDeviceSessionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.DeviceSession:
        r"""Gets a DeviceSession, which documents the allocation
        status and whether the device is allocated. Clients
        making requests from this API must poll
        GetDeviceSession.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import devicestreaming_v1

            async def sample_get_device_session():
                # Create a client
                client = devicestreaming_v1.DirectAccessServiceAsyncClient()

                # Initialize request argument(s)
                request = devicestreaming_v1.GetDeviceSessionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_device_session(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devicestreaming_v1.types.GetDeviceSessionRequest, dict]]):
                The request object. Request message for
                DirectAccessService.GetDeviceSession.
            name (:class:`str`):
                Required. Name of the DeviceSession, e.g.
                "projects/{project_id}/deviceSessions/{session_id}"

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
            google.cloud.devicestreaming_v1.types.DeviceSession:
                Protobuf message describing the
                device message, used from several RPCs.

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
        if not isinstance(request, service.GetDeviceSessionRequest):
            request = service.GetDeviceSessionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_device_session
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

    async def cancel_device_session(
        self,
        request: Optional[Union[service.CancelDeviceSessionRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Cancel a DeviceSession.
        This RPC changes the DeviceSession to state FINISHED and
        terminates all connections.
        Canceled sessions are not deleted and can be retrieved
        or listed by the user until they expire based on the 28
        day deletion policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import devicestreaming_v1

            async def sample_cancel_device_session():
                # Create a client
                client = devicestreaming_v1.DirectAccessServiceAsyncClient()

                # Initialize request argument(s)
                request = devicestreaming_v1.CancelDeviceSessionRequest(
                    name="name_value",
                )

                # Make the request
                await client.cancel_device_session(request=request)

        Args:
            request (Optional[Union[google.cloud.devicestreaming_v1.types.CancelDeviceSessionRequest, dict]]):
                The request object. Request message for
                DirectAccessService.CancelDeviceSession.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.CancelDeviceSessionRequest):
            request = service.CancelDeviceSessionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.cancel_device_session
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

    async def update_device_session(
        self,
        request: Optional[Union[service.UpdateDeviceSessionRequest, dict]] = None,
        *,
        device_session: Optional[service.DeviceSession] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.DeviceSession:
        r"""Updates the current DeviceSession to the fields described by the
        update_mask.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import devicestreaming_v1

            async def sample_update_device_session():
                # Create a client
                client = devicestreaming_v1.DirectAccessServiceAsyncClient()

                # Initialize request argument(s)
                device_session = devicestreaming_v1.DeviceSession()
                device_session.android_device.android_model_id = "android_model_id_value"
                device_session.android_device.android_version_id = "android_version_id_value"

                request = devicestreaming_v1.UpdateDeviceSessionRequest(
                    device_session=device_session,
                )

                # Make the request
                response = await client.update_device_session(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devicestreaming_v1.types.UpdateDeviceSessionRequest, dict]]):
                The request object. Request message for
                DirectAccessService.UpdateDeviceSession.
            device_session (:class:`google.cloud.devicestreaming_v1.types.DeviceSession`):
                Required. DeviceSession to update. The DeviceSession's
                ``name`` field is used to identify the session to update
                "projects/{project_id}/deviceSessions/{session_id}"

                This corresponds to the ``device_session`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to
                update.

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
            google.cloud.devicestreaming_v1.types.DeviceSession:
                Protobuf message describing the
                device message, used from several RPCs.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [device_session, update_mask]
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
        if not isinstance(request, service.UpdateDeviceSessionRequest):
            request = service.UpdateDeviceSessionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if device_session is not None:
            request.device_session = device_session
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_device_session
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("device_session.name", request.device_session.name),)
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

    def adb_connect(
        self,
        requests: Optional[AsyncIterator[adb_service.AdbMessage]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Awaitable[AsyncIterable[adb_service.DeviceMessage]]:
        r"""Exposes an ADB connection if the device supports ADB.
        gRPC headers are used to authenticate the Connect RPC,
        as well as associate to a particular DeviceSession.
        In particular, the user must specify the
        "X-Omnilab-Session-Name" header.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import devicestreaming_v1

            async def sample_adb_connect():
                # Create a client
                client = devicestreaming_v1.DirectAccessServiceAsyncClient()

                # Initialize request argument(s)
                open_ = devicestreaming_v1.Open()
                open_.stream_id = 952

                request = devicestreaming_v1.AdbMessage(
                    open_=open_,
                )

                # This method expects an iterator which contains
                # 'devicestreaming_v1.AdbMessage' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = await client.adb_connect(requests=request_generator())

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            requests (AsyncIterator[`google.cloud.devicestreaming_v1.types.AdbMessage`]):
                The request object AsyncIterator. A message to an ADB server.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            AsyncIterable[google.cloud.devicestreaming_v1.types.DeviceMessage]:
                A message returned from a device.
        """

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.adb_connect
        ]

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = rpc(
            requests,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "DirectAccessServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DirectAccessServiceAsyncClient",)
