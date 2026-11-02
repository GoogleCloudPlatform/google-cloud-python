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

from google.shopping.merchant_accounts_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.shopping.merchant_accounts_v1.services.account_services_service import (
    pagers,
)
from google.shopping.merchant_accounts_v1.types import accountservices

from .client import AccountServicesServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, AccountServicesServiceTransport
from .transports.grpc_asyncio import AccountServicesServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AccountServicesServiceAsyncClient:
    """Service to support AccountService API."""

    _client: AccountServicesServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AccountServicesServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AccountServicesServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AccountServicesServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AccountServicesServiceClient._DEFAULT_UNIVERSE

    account_path = staticmethod(AccountServicesServiceClient.account_path)
    parse_account_path = staticmethod(AccountServicesServiceClient.parse_account_path)
    account_service_path = staticmethod(
        AccountServicesServiceClient.account_service_path
    )
    parse_account_service_path = staticmethod(
        AccountServicesServiceClient.parse_account_service_path
    )
    common_billing_account_path = staticmethod(
        AccountServicesServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AccountServicesServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AccountServicesServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AccountServicesServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AccountServicesServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AccountServicesServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AccountServicesServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        AccountServicesServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        AccountServicesServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        AccountServicesServiceClient.parse_common_location_path
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
            AccountServicesServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            AccountServicesServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AccountServicesServiceAsyncClient, info, *args, **kwargs)

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
            AccountServicesServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            AccountServicesServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            AccountServicesServiceAsyncClient, filename, *args, **kwargs
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
        return AccountServicesServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> AccountServicesServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            AccountServicesServiceTransport: The transport used by the client instance.
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

    get_transport_class = AccountServicesServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                AccountServicesServiceTransport,
                Callable[..., AccountServicesServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the account services service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AccountServicesServiceTransport,Callable[..., AccountServicesServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AccountServicesServiceTransport constructor.
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
        self._client = AccountServicesServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.accounts_v1.AccountServicesServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
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
                    "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                    "credentialsType": None,
                },
            )

    async def get_account_service(
        self,
        request: Optional[Union[accountservices.GetAccountServiceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accountservices.AccountService:
        r"""Retrieve an account service.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_get_account_service():
                # Create a client
                client = merchant_accounts_v1.AccountServicesServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.GetAccountServiceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_account_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.GetAccountServiceRequest, dict]]):
                The request object. Request to get an account service.
            name (:class:`str`):
                Required. The resource name of the account service to
                get. Format: ``accounts/{account}/services/{service}``

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
            google.shopping.merchant_accounts_v1.types.AccountService:
                The AccountService message represents a specific service that a provider
                   account offers to a Merchant Center account.

                   AccountService defines the permissions and
                   capabilities granted to the provider, allowing for
                   operations such as product management or campaign
                   management.

                   The lifecycle of an AccountService involves a
                   proposal phase, where one party suggests the service,
                   and an approval phase, where the other party accepts
                   or rejects it. This handshake mechanism ensures
                   mutual consent before any access is granted. This
                   mechanism safeguards both parties by ensuring that
                   access rights are granted appropriately and that both
                   the business and provider are aware of the services
                   enabled. In scenarios where a user is an admin of
                   both accounts, the approval can happen automatically.

                   The mutability of a service is also managed through
                   AccountService. Some services might be immutable, for
                   example, if they were established through other
                   systems or APIs, and you cannot alter them through
                   this API.

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
        if not isinstance(request, accountservices.GetAccountServiceRequest):
            request = accountservices.GetAccountServiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_account_service
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

    async def list_account_services(
        self,
        request: Optional[
            Union[accountservices.ListAccountServicesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAccountServicesAsyncPager:
        r"""List account services for the specified accounts.
        Supports filtering.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_list_account_services():
                # Create a client
                client = merchant_accounts_v1.AccountServicesServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ListAccountServicesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_account_services(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ListAccountServicesRequest, dict]]):
                The request object. Request to list account services.
            parent (:class:`str`):
                Required. The parent account of the account service to
                filter by. Format: ``accounts/{account}``

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
            google.shopping.merchant_accounts_v1.services.account_services_service.pagers.ListAccountServicesAsyncPager:
                Response after trying to list account
                services.
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
        if not isinstance(request, accountservices.ListAccountServicesRequest):
            request = accountservices.ListAccountServicesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_account_services
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
        response = pagers.ListAccountServicesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def propose_account_service(
        self,
        request: Optional[
            Union[accountservices.ProposeAccountServiceRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        provider: Optional[str] = None,
        account_service: Optional[accountservices.AccountService] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accountservices.AccountService:
        r"""Propose an account service.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_propose_account_service():
                # Create a client
                client = merchant_accounts_v1.AccountServicesServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ProposeAccountServiceRequest(
                    parent="parent_value",
                    provider="provider_value",
                )

                # Make the request
                response = await client.propose_account_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ProposeAccountServiceRequest, dict]]):
                The request object. Request to propose an account
                service.
            parent (:class:`str`):
                Required. The resource name of the parent account for
                the service. Format: ``accounts/{account}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            provider (:class:`str`):
                Required. The provider of the service. Either the
                reference to an account such as ``providers/123`` or a
                well-known service provider (one of
                ``providers/GOOGLE_ADS`` or
                ``providers/GOOGLE_BUSINESS_PROFILE``).

                This corresponds to the ``provider`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            account_service (:class:`google.shopping.merchant_accounts_v1.types.AccountService`):
                Required. The account service to
                propose.

                This corresponds to the ``account_service`` field
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
            google.shopping.merchant_accounts_v1.types.AccountService:
                The AccountService message represents a specific service that a provider
                   account offers to a Merchant Center account.

                   AccountService defines the permissions and
                   capabilities granted to the provider, allowing for
                   operations such as product management or campaign
                   management.

                   The lifecycle of an AccountService involves a
                   proposal phase, where one party suggests the service,
                   and an approval phase, where the other party accepts
                   or rejects it. This handshake mechanism ensures
                   mutual consent before any access is granted. This
                   mechanism safeguards both parties by ensuring that
                   access rights are granted appropriately and that both
                   the business and provider are aware of the services
                   enabled. In scenarios where a user is an admin of
                   both accounts, the approval can happen automatically.

                   The mutability of a service is also managed through
                   AccountService. Some services might be immutable, for
                   example, if they were established through other
                   systems or APIs, and you cannot alter them through
                   this API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, provider, account_service]
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
        if not isinstance(request, accountservices.ProposeAccountServiceRequest):
            request = accountservices.ProposeAccountServiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if provider is not None:
            request.provider = provider
        if account_service is not None:
            request.account_service = account_service

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.propose_account_service
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

    async def approve_account_service(
        self,
        request: Optional[
            Union[accountservices.ApproveAccountServiceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accountservices.AccountService:
        r"""Approve an account service proposal.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_approve_account_service():
                # Create a client
                client = merchant_accounts_v1.AccountServicesServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ApproveAccountServiceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.approve_account_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ApproveAccountServiceRequest, dict]]):
                The request object. Request to approve an account
                service.
            name (:class:`str`):
                Required. The resource name of the account service to
                approve. Format:
                ``accounts/{account}/services/{service}``

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
            google.shopping.merchant_accounts_v1.types.AccountService:
                The AccountService message represents a specific service that a provider
                   account offers to a Merchant Center account.

                   AccountService defines the permissions and
                   capabilities granted to the provider, allowing for
                   operations such as product management or campaign
                   management.

                   The lifecycle of an AccountService involves a
                   proposal phase, where one party suggests the service,
                   and an approval phase, where the other party accepts
                   or rejects it. This handshake mechanism ensures
                   mutual consent before any access is granted. This
                   mechanism safeguards both parties by ensuring that
                   access rights are granted appropriately and that both
                   the business and provider are aware of the services
                   enabled. In scenarios where a user is an admin of
                   both accounts, the approval can happen automatically.

                   The mutability of a service is also managed through
                   AccountService. Some services might be immutable, for
                   example, if they were established through other
                   systems or APIs, and you cannot alter them through
                   this API.

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
        if not isinstance(request, accountservices.ApproveAccountServiceRequest):
            request = accountservices.ApproveAccountServiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.approve_account_service
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

    async def reject_account_service(
        self,
        request: Optional[
            Union[accountservices.RejectAccountServiceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Reject an account service (both proposed and approve
        services can be rejected).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_reject_account_service():
                # Create a client
                client = merchant_accounts_v1.AccountServicesServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.RejectAccountServiceRequest(
                    name="name_value",
                )

                # Make the request
                await client.reject_account_service(request=request)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.RejectAccountServiceRequest, dict]]):
                The request object. Request to reject an account service.
            name (:class:`str`):
                Required. The resource name of the account service to
                reject. Format:
                ``accounts/{account}/services/{service}``

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
        if not isinstance(request, accountservices.RejectAccountServiceRequest):
            request = accountservices.RejectAccountServiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reject_account_service
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

    async def __aenter__(self) -> "AccountServicesServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AccountServicesServiceAsyncClient",)
