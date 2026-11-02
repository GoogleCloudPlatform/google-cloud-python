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

from google.ads.datamanager_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore

from google.ads.datamanager_v1.services.user_list_global_license_service import pagers
from google.ads.datamanager_v1.types import (
    user_list_global_license,
    user_list_global_license_service,
    user_list_global_license_type,
    user_list_license_metrics,
    user_list_license_pricing,
    user_list_license_status,
)
from google.ads.datamanager_v1.types import (
    user_list_global_license as gad_user_list_global_license,
)

from .client import UserListGlobalLicenseServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, UserListGlobalLicenseServiceTransport
from .transports.grpc_asyncio import UserListGlobalLicenseServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class UserListGlobalLicenseServiceAsyncClient:
    """Service for managing user list global licenses. Delete is not
    a supported operation for UserListGlobalLicenses.  Callers
    should update the license status to DISABLED to instead to
    deactivate a license.

    This feature is only available to data partners.
    """

    _client: UserListGlobalLicenseServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = UserListGlobalLicenseServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = UserListGlobalLicenseServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        UserListGlobalLicenseServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = UserListGlobalLicenseServiceClient._DEFAULT_UNIVERSE

    user_list_global_license_path = staticmethod(
        UserListGlobalLicenseServiceClient.user_list_global_license_path
    )
    parse_user_list_global_license_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_user_list_global_license_path
    )
    user_list_global_license_customer_info_path = staticmethod(
        UserListGlobalLicenseServiceClient.user_list_global_license_customer_info_path
    )
    parse_user_list_global_license_customer_info_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_user_list_global_license_customer_info_path
    )
    common_billing_account_path = staticmethod(
        UserListGlobalLicenseServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        UserListGlobalLicenseServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        UserListGlobalLicenseServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        UserListGlobalLicenseServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        UserListGlobalLicenseServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        UserListGlobalLicenseServiceClient.parse_common_location_path
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
            UserListGlobalLicenseServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            UserListGlobalLicenseServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            UserListGlobalLicenseServiceAsyncClient, info, *args, **kwargs
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
            UserListGlobalLicenseServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            UserListGlobalLicenseServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            UserListGlobalLicenseServiceAsyncClient, filename, *args, **kwargs
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
        return UserListGlobalLicenseServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> UserListGlobalLicenseServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            UserListGlobalLicenseServiceTransport: The transport used by the client instance.
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

    get_transport_class = UserListGlobalLicenseServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                UserListGlobalLicenseServiceTransport,
                Callable[..., UserListGlobalLicenseServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the user list global license service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,UserListGlobalLicenseServiceTransport,Callable[..., UserListGlobalLicenseServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the UserListGlobalLicenseServiceTransport constructor.
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
        self._client = UserListGlobalLicenseServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.ads.datamanager_v1.UserListGlobalLicenseServiceAsyncClient`.",
                extra={
                    "serviceName": "google.ads.datamanager.v1.UserListGlobalLicenseService",
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
                    "serviceName": "google.ads.datamanager.v1.UserListGlobalLicenseService",
                    "credentialsType": None,
                },
            )

    async def create_user_list_global_license(
        self,
        request: Optional[
            Union[
                user_list_global_license_service.CreateUserListGlobalLicenseRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        user_list_global_license: Optional[
            gad_user_list_global_license.UserListGlobalLicense
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gad_user_list_global_license.UserListGlobalLicense:
        r"""Creates a user list global license.

        This feature is only available to data partners.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_create_user_list_global_license():
                # Create a client
                client = datamanager_v1.UserListGlobalLicenseServiceAsyncClient()

                # Initialize request argument(s)
                request = datamanager_v1.CreateUserListGlobalLicenseRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_user_list_global_license(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.CreateUserListGlobalLicenseRequest, dict]]):
                The request object. Request to create a
                [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
                resource.
            parent (:class:`str`):
                Required. The account that owns the user list being
                licensed. Should be in the format
                accountTypes/{ACCOUNT_TYPE}/accounts/{ACCOUNT_ID}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_list_global_license (:class:`google.ads.datamanager_v1.types.UserListGlobalLicense`):
                Required. The user list global
                license to create.

                This corresponds to the ``user_list_global_license`` field
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
            google.ads.datamanager_v1.types.UserListGlobalLicense:
                A user list global license.

                This feature is only available to data
                partners.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_list_global_license]
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
            request, user_list_global_license_service.CreateUserListGlobalLicenseRequest
        ):
            request = (
                user_list_global_license_service.CreateUserListGlobalLicenseRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if user_list_global_license is not None:
            request.user_list_global_license = user_list_global_license

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_user_list_global_license
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

    async def update_user_list_global_license(
        self,
        request: Optional[
            Union[
                user_list_global_license_service.UpdateUserListGlobalLicenseRequest,
                dict,
            ]
        ] = None,
        *,
        user_list_global_license: Optional[
            gad_user_list_global_license.UserListGlobalLicense
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gad_user_list_global_license.UserListGlobalLicense:
        r"""Updates a user list global license.

        This feature is only available to data partners.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_update_user_list_global_license():
                # Create a client
                client = datamanager_v1.UserListGlobalLicenseServiceAsyncClient()

                # Initialize request argument(s)
                request = datamanager_v1.UpdateUserListGlobalLicenseRequest(
                )

                # Make the request
                response = await client.update_user_list_global_license(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.UpdateUserListGlobalLicenseRequest, dict]]):
                The request object. Request to update a
                [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
                resource.
            user_list_global_license (:class:`google.ads.datamanager_v1.types.UserListGlobalLicense`):
                Required. The licenses' ``name`` field is used to
                identify the license to update.

                This corresponds to the ``user_list_global_license`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to update. The special
                character ``*`` is not supported and an
                ``INVALID_UPDATE_MASK`` error will be thrown if used.

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
            google.ads.datamanager_v1.types.UserListGlobalLicense:
                A user list global license.

                This feature is only available to data
                partners.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [user_list_global_license, update_mask]
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
            request, user_list_global_license_service.UpdateUserListGlobalLicenseRequest
        ):
            request = (
                user_list_global_license_service.UpdateUserListGlobalLicenseRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if user_list_global_license is not None:
            request.user_list_global_license = user_list_global_license
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_user_list_global_license
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "user_list_global_license.name",
                        request.user_list_global_license.name,
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

    async def get_user_list_global_license(
        self,
        request: Optional[
            Union[
                user_list_global_license_service.GetUserListGlobalLicenseRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> user_list_global_license.UserListGlobalLicense:
        r"""Retrieves a user list global license.

        This feature is only available to data partners.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_get_user_list_global_license():
                # Create a client
                client = datamanager_v1.UserListGlobalLicenseServiceAsyncClient()

                # Initialize request argument(s)
                request = datamanager_v1.GetUserListGlobalLicenseRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_user_list_global_license(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.GetUserListGlobalLicenseRequest, dict]]):
                The request object. Request to get a
                [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
                resource.
            name (:class:`str`):
                Required. The resource name of the
                user list global license.

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
            google.ads.datamanager_v1.types.UserListGlobalLicense:
                A user list global license.

                This feature is only available to data
                partners.

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
            request, user_list_global_license_service.GetUserListGlobalLicenseRequest
        ):
            request = user_list_global_license_service.GetUserListGlobalLicenseRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_user_list_global_license
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

    async def list_user_list_global_licenses(
        self,
        request: Optional[
            Union[
                user_list_global_license_service.ListUserListGlobalLicensesRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserListGlobalLicensesAsyncPager:
        r"""Lists all user list global licenses owned by the
        parent account.
        This feature is only available to data partners.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_list_user_list_global_licenses():
                # Create a client
                client = datamanager_v1.UserListGlobalLicenseServiceAsyncClient()

                # Initialize request argument(s)
                request = datamanager_v1.ListUserListGlobalLicensesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_list_global_licenses(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.ListUserListGlobalLicensesRequest, dict]]):
                The request object. Request to list all
                [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
                resources for a given account.
            parent (:class:`str`):
                Required. The account whose licenses are being queried.
                Should be in the format
                accountTypes/{ACCOUNT_TYPE}/accounts/{ACCOUNT_ID}

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
            google.ads.datamanager_v1.services.user_list_global_license_service.pagers.ListUserListGlobalLicensesAsyncPager:
                Response from the
                   [ListUserListGlobalLicensesRequest][google.ads.datamanager.v1.ListUserListGlobalLicensesRequest].

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
            request, user_list_global_license_service.ListUserListGlobalLicensesRequest
        ):
            request = (
                user_list_global_license_service.ListUserListGlobalLicensesRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_user_list_global_licenses
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
        response = pagers.ListUserListGlobalLicensesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_user_list_global_license_customer_infos(
        self,
        request: Optional[
            Union[
                user_list_global_license_service.ListUserListGlobalLicenseCustomerInfosRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserListGlobalLicenseCustomerInfosAsyncPager:
        r"""Lists all customer info for a user list global
        license.
        This feature is only available to data partners.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import datamanager_v1

            async def sample_list_user_list_global_license_customer_infos():
                # Create a client
                client = datamanager_v1.UserListGlobalLicenseServiceAsyncClient()

                # Initialize request argument(s)
                request = datamanager_v1.ListUserListGlobalLicenseCustomerInfosRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_list_global_license_customer_infos(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.ads.datamanager_v1.types.ListUserListGlobalLicenseCustomerInfosRequest, dict]]):
                The request object. Request to list all
                [UserListGlobalLicenseCustomerInfo][google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo]
                resources for a given user list global license.
            parent (:class:`str`):
                Required. The global license whose customer info are
                being queried. Should be in the format
                ``accountTypes/{ACCOUNT_TYPE}/accounts/{ACCOUNT_ID}/userListGlobalLicenses/{USER_LIST_GLOBAL_LICENSE_ID}``.
                To list all global license customer info under an
                account, replace the user list global license id with a
                '-' (for example,
                ``accountTypes/DATA_PARTNER/accounts/123/userListGlobalLicenses/-``)

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
            google.ads.datamanager_v1.services.user_list_global_license_service.pagers.ListUserListGlobalLicenseCustomerInfosAsyncPager:
                Response from the
                   [ListUserListGlobalLicensesCustomerInfoRequest][google.ads.datamanager.v1.ListUserListGlobalLicensesCustomerInfoRequest].

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
            request,
            user_list_global_license_service.ListUserListGlobalLicenseCustomerInfosRequest,
        ):
            request = user_list_global_license_service.ListUserListGlobalLicenseCustomerInfosRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_user_list_global_license_customer_infos
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
        response = pagers.ListUserListGlobalLicenseCustomerInfosAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "UserListGlobalLicenseServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("UserListGlobalLicenseServiceAsyncClient",)
