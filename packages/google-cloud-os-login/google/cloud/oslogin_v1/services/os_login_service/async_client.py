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

from google.cloud.oslogin_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore

from google.cloud.oslogin_v1.common.types import common
from google.cloud.oslogin_v1.types import oslogin

from .client import OsLoginServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, OsLoginServiceTransport
from .transports.grpc_asyncio import OsLoginServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class OsLoginServiceAsyncClient:
    """Cloud OS Login API

    The Cloud OS Login API allows you to manage users and their
    associated SSH public keys for logging into virtual machines on
    Google Cloud Platform.
    """

    _client: OsLoginServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = OsLoginServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = OsLoginServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = OsLoginServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = OsLoginServiceClient._DEFAULT_UNIVERSE

    posix_account_path = staticmethod(OsLoginServiceClient.posix_account_path)
    parse_posix_account_path = staticmethod(
        OsLoginServiceClient.parse_posix_account_path
    )
    ssh_public_key_path = staticmethod(OsLoginServiceClient.ssh_public_key_path)
    parse_ssh_public_key_path = staticmethod(
        OsLoginServiceClient.parse_ssh_public_key_path
    )
    common_billing_account_path = staticmethod(
        OsLoginServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        OsLoginServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(OsLoginServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        OsLoginServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        OsLoginServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        OsLoginServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(OsLoginServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        OsLoginServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(OsLoginServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        OsLoginServiceClient.parse_common_location_path
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
            OsLoginServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            OsLoginServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(OsLoginServiceAsyncClient, info, *args, **kwargs)

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
            OsLoginServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            OsLoginServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(OsLoginServiceAsyncClient, filename, *args, **kwargs)

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
        return OsLoginServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> OsLoginServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            OsLoginServiceTransport: The transport used by the client instance.
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

    get_transport_class = OsLoginServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, OsLoginServiceTransport, Callable[..., OsLoginServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the os login service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,OsLoginServiceTransport,Callable[..., OsLoginServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the OsLoginServiceTransport constructor.
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
        self._client = OsLoginServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.oslogin_v1.OsLoginServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.oslogin.v1.OsLoginService",
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
                    "serviceName": "google.cloud.oslogin.v1.OsLoginService",
                    "credentialsType": None,
                },
            )

    async def create_ssh_public_key(
        self,
        request: Optional[Union[oslogin.CreateSshPublicKeyRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        ssh_public_key: Optional[common.SshPublicKey] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common.SshPublicKey:
        r"""Create an SSH public key

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_create_ssh_public_key():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.CreateSshPublicKeyRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_ssh_public_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.CreateSshPublicKeyRequest, dict]]):
                The request object. A request message for creating an SSH
                public key.
            parent (:class:`str`):
                Required. The unique ID for the user in format
                ``users/{user}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ssh_public_key (:class:`google.cloud.oslogin_v1.common.types.SshPublicKey`):
                Required. The SSH public key and
                expiration time.

                This corresponds to the ``ssh_public_key`` field
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
            google.cloud.oslogin_v1.common.types.SshPublicKey:
                The SSH public key information
                associated with a Google account.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, ssh_public_key]
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
        if not isinstance(request, oslogin.CreateSshPublicKeyRequest):
            request = oslogin.CreateSshPublicKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if ssh_public_key is not None:
            request.ssh_public_key = ssh_public_key

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_ssh_public_key
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

    async def delete_posix_account(
        self,
        request: Optional[Union[oslogin.DeletePosixAccountRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a POSIX account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_delete_posix_account():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.DeletePosixAccountRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_posix_account(request=request)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.DeletePosixAccountRequest, dict]]):
                The request object. A request message for deleting a
                POSIX account entry.
            name (:class:`str`):
                Required. A reference to the POSIX account to update.
                POSIX accounts are identified by the project ID they are
                associated with. A reference to the POSIX account is in
                format ``users/{user}/projects/{project}``.

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
        if not isinstance(request, oslogin.DeletePosixAccountRequest):
            request = oslogin.DeletePosixAccountRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_posix_account
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

    async def delete_ssh_public_key(
        self,
        request: Optional[Union[oslogin.DeleteSshPublicKeyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an SSH public key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_delete_ssh_public_key():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.DeleteSshPublicKeyRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_ssh_public_key(request=request)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.DeleteSshPublicKeyRequest, dict]]):
                The request object. A request message for deleting an SSH
                public key.
            name (:class:`str`):
                Required. The fingerprint of the public key to update.
                Public keys are identified by their SHA-256 fingerprint.
                The fingerprint of the public key is in format
                ``users/{user}/sshPublicKeys/{fingerprint}``.

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
        if not isinstance(request, oslogin.DeleteSshPublicKeyRequest):
            request = oslogin.DeleteSshPublicKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_ssh_public_key
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

    async def get_login_profile(
        self,
        request: Optional[Union[oslogin.GetLoginProfileRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> oslogin.LoginProfile:
        r"""Retrieves the profile information used for logging in
        to a virtual machine on Google Compute Engine.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_get_login_profile():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.GetLoginProfileRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_login_profile(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.GetLoginProfileRequest, dict]]):
                The request object. A request message for retrieving the
                login profile information for a user.
            name (:class:`str`):
                Required. The unique ID for the user in format
                ``users/{user}``.

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
            google.cloud.oslogin_v1.types.LoginProfile:
                The user profile information used for
                logging in to a virtual machine on
                Google Compute Engine.

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
        if not isinstance(request, oslogin.GetLoginProfileRequest):
            request = oslogin.GetLoginProfileRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_login_profile
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

    async def get_ssh_public_key(
        self,
        request: Optional[Union[oslogin.GetSshPublicKeyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common.SshPublicKey:
        r"""Retrieves an SSH public key.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_get_ssh_public_key():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.GetSshPublicKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_ssh_public_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.GetSshPublicKeyRequest, dict]]):
                The request object. A request message for retrieving an
                SSH public key.
            name (:class:`str`):
                Required. The fingerprint of the public key to retrieve.
                Public keys are identified by their SHA-256 fingerprint.
                The fingerprint of the public key is in format
                ``users/{user}/sshPublicKeys/{fingerprint}``.

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
            google.cloud.oslogin_v1.common.types.SshPublicKey:
                The SSH public key information
                associated with a Google account.

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
        if not isinstance(request, oslogin.GetSshPublicKeyRequest):
            request = oslogin.GetSshPublicKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_ssh_public_key
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

    async def import_ssh_public_key(
        self,
        request: Optional[Union[oslogin.ImportSshPublicKeyRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        ssh_public_key: Optional[common.SshPublicKey] = None,
        project_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> oslogin.ImportSshPublicKeyResponse:
        r"""Adds an SSH public key and returns the profile
        information. Default POSIX account information is set
        when no username and UID exist as part of the login
        profile.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_import_ssh_public_key():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.ImportSshPublicKeyRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.import_ssh_public_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.ImportSshPublicKeyRequest, dict]]):
                The request object. A request message for importing an
                SSH public key.
            parent (:class:`str`):
                Required. The unique ID for the user in format
                ``users/{user}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ssh_public_key (:class:`google.cloud.oslogin_v1.common.types.SshPublicKey`):
                Optional. The SSH public key and
                expiration time.

                This corresponds to the ``ssh_public_key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            project_id (:class:`str`):
                The project ID of the Google Cloud
                Platform project.

                This corresponds to the ``project_id`` field
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
            google.cloud.oslogin_v1.types.ImportSshPublicKeyResponse:
                A response message for importing an
                SSH public key.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, ssh_public_key, project_id]
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
        if not isinstance(request, oslogin.ImportSshPublicKeyRequest):
            request = oslogin.ImportSshPublicKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if ssh_public_key is not None:
            request.ssh_public_key = ssh_public_key
        if project_id is not None:
            request.project_id = project_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.import_ssh_public_key
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

    async def update_ssh_public_key(
        self,
        request: Optional[Union[oslogin.UpdateSshPublicKeyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        ssh_public_key: Optional[common.SshPublicKey] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common.SshPublicKey:
        r"""Updates an SSH public key and returns the profile
        information. This method supports patch semantics.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oslogin_v1

            async def sample_update_ssh_public_key():
                # Create a client
                client = oslogin_v1.OsLoginServiceAsyncClient()

                # Initialize request argument(s)
                request = oslogin_v1.UpdateSshPublicKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.update_ssh_public_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.oslogin_v1.types.UpdateSshPublicKeyRequest, dict]]):
                The request object. A request message for updating an SSH
                public key.
            name (:class:`str`):
                Required. The fingerprint of the public key to update.
                Public keys are identified by their SHA-256 fingerprint.
                The fingerprint of the public key is in format
                ``users/{user}/sshPublicKeys/{fingerprint}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ssh_public_key (:class:`google.cloud.oslogin_v1.common.types.SshPublicKey`):
                Required. The SSH public key and
                expiration time.

                This corresponds to the ``ssh_public_key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Mask to control which fields get
                updated. Updates all if not present.

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
            google.cloud.oslogin_v1.common.types.SshPublicKey:
                The SSH public key information
                associated with a Google account.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, ssh_public_key, update_mask]
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
        if not isinstance(request, oslogin.UpdateSshPublicKeyRequest):
            request = oslogin.UpdateSshPublicKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if ssh_public_key is not None:
            request.ssh_public_key = ssh_public_key
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_ssh_public_key
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

    async def __aenter__(self) -> "OsLoginServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("OsLoginServiceAsyncClient",)
