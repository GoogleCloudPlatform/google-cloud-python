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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore

from google.shopping.merchant_accounts_v1.services.accounts_service import pagers
from google.shopping.merchant_accounts_v1.types import accounts

from .client import AccountsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, AccountsServiceTransport
from .transports.grpc_asyncio import AccountsServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AccountsServiceAsyncClient:
    """Service to support Accounts API."""

    _client: AccountsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AccountsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AccountsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AccountsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AccountsServiceClient._DEFAULT_UNIVERSE

    account_path = staticmethod(AccountsServiceClient.account_path)
    parse_account_path = staticmethod(AccountsServiceClient.parse_account_path)
    user_path = staticmethod(AccountsServiceClient.user_path)
    parse_user_path = staticmethod(AccountsServiceClient.parse_user_path)
    common_billing_account_path = staticmethod(
        AccountsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AccountsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AccountsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AccountsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AccountsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AccountsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AccountsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        AccountsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(AccountsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        AccountsServiceClient.parse_common_location_path
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
            AccountsServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            AccountsServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AccountsServiceAsyncClient, info, *args, **kwargs)

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
            AccountsServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            AccountsServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AccountsServiceAsyncClient, filename, *args, **kwargs)

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
        return AccountsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AccountsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            AccountsServiceTransport: The transport used by the client instance.
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

    get_transport_class = AccountsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str, AccountsServiceTransport, Callable[..., AccountsServiceTransport]
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the accounts service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AccountsServiceTransport,Callable[..., AccountsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AccountsServiceTransport constructor.
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
        self._client = AccountsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.accounts_v1.AccountsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.accounts.v1.AccountsService",
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
                    "serviceName": "google.shopping.merchant.accounts.v1.AccountsService",
                    "credentialsType": None,
                },
            )

    async def get_account(
        self,
        request: Optional[Union[accounts.GetAccountRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accounts.Account:
        r"""Retrieves an account from your Merchant Center
        account. After inserting, updating, or deleting an
        account, it may take several minutes before changes take
        effect.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_get_account():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.GetAccountRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.GetAccountRequest, dict]]):
                The request object. Request message for the ``GetAccount`` method.
            name (:class:`str`):
                Required. The name of the account to retrieve. Format:
                ``accounts/{account}``

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
            google.shopping.merchant_accounts_v1.types.Account:
                The Account message represents a business's account within Shopping
                   Ads. It's the primary entity for managing product
                   data, settings, and interactions with Google's
                   services and external providers.

                   Accounts can operate as standalone entities or be
                   part of a advanced account structure. In an advanced
                   account setup the parent account manages multiple
                   sub-accounts.

                   Establishing an account involves configuring
                   attributes like the account name, time zone, and
                   language preferences.

                   The Account message is the parent entity for many
                   other resources, for example, AccountRelationship,
                   Homepage, BusinessInfo and so on.

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
        if not isinstance(request, accounts.GetAccountRequest):
            request = accounts.GetAccountRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_account
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

    async def create_and_configure_account(
        self,
        request: Optional[
            Union[accounts.CreateAndConfigureAccountRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accounts.Account:
        r"""Creates a Merchant Center account with additional
        configuration. Adds the user that makes the request as
        an admin for the new account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_create_and_configure_account():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                account = merchant_accounts_v1.Account()
                account.account_name = "account_name_value"
                account.language_code = "language_code_value"

                request = merchant_accounts_v1.CreateAndConfigureAccountRequest(
                    account=account,
                )

                # Make the request
                response = await client.create_and_configure_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.CreateAndConfigureAccountRequest, dict]]):
                The request object. Request message for the ``CreateAndConfigureAccount``
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.shopping.merchant_accounts_v1.types.Account:
                The Account message represents a business's account within Shopping
                   Ads. It's the primary entity for managing product
                   data, settings, and interactions with Google's
                   services and external providers.

                   Accounts can operate as standalone entities or be
                   part of a advanced account structure. In an advanced
                   account setup the parent account manages multiple
                   sub-accounts.

                   Establishing an account involves configuring
                   attributes like the account name, time zone, and
                   language preferences.

                   The Account message is the parent entity for many
                   other resources, for example, AccountRelationship,
                   Homepage, BusinessInfo and so on.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, accounts.CreateAndConfigureAccountRequest):
            request = accounts.CreateAndConfigureAccountRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_and_configure_account
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

    async def create_test_account(
        self,
        request: Optional[Union[accounts.CreateTestAccountRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        account: Optional[accounts.Account] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accounts.Account:
        r"""Creates a Merchant Center test account.

        Test accounts are intended for development and testing
        purposes, such as validating API integrations or new
        feature behavior.

        Key characteristics and limitations of test accounts:

        - Immutable Type: A test account cannot be converted
          into a regular   (live) Merchant Center account.
          Likewise, a regular account cannot be   converted into
          a test account.
        - Non-Serving Products: Any products, offers, or data
          created within a   test account will not be published
          or made visible to end-users on any   Google surfaces.
          They are strictly for testing environments.
        - Separate Environment: Test accounts operate in a
          sandbox-like manner,   isolated from live serving and
          real user traffic.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_create_test_account():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                account = merchant_accounts_v1.Account()
                account.account_name = "account_name_value"
                account.language_code = "language_code_value"

                request = merchant_accounts_v1.CreateTestAccountRequest(
                    parent="parent_value",
                    account=account,
                )

                # Make the request
                response = await client.create_test_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.CreateTestAccountRequest, dict]]):
                The request object. Request message for the
                CreateTestAccount RPC
            parent (:class:`str`):
                Required. The account resource name
                to create the test account under.
                Format: accounts/{account}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            account (:class:`google.shopping.merchant_accounts_v1.types.Account`):
                Required. The account to be created.
                This corresponds to the ``account`` field
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
            google.shopping.merchant_accounts_v1.types.Account:
                The Account message represents a business's account within Shopping
                   Ads. It's the primary entity for managing product
                   data, settings, and interactions with Google's
                   services and external providers.

                   Accounts can operate as standalone entities or be
                   part of a advanced account structure. In an advanced
                   account setup the parent account manages multiple
                   sub-accounts.

                   Establishing an account involves configuring
                   attributes like the account name, time zone, and
                   language preferences.

                   The Account message is the parent entity for many
                   other resources, for example, AccountRelationship,
                   Homepage, BusinessInfo and so on.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, account]
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
        if not isinstance(request, accounts.CreateTestAccountRequest):
            request = accounts.CreateTestAccountRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if account is not None:
            request.account = account

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_test_account
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

    async def delete_account(
        self,
        request: Optional[Union[accounts.DeleteAccountRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified account regardless of its type:
        standalone, advanced account or sub-account. Deleting an
        advanced account leads to the deletion of all of its
        sub-accounts. This also deletes the account's `developer
        registration
        entity </merchant/api/reference/rest/accounts_v1/accounts.developerRegistration>`__
        and any associated GCP project to the account. Executing this
        method requires admin access. The deletion succeeds only if the
        account does not provide services to any other account and has
        no processed offers. You can use the ``force`` parameter to
        override this.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_delete_account():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.DeleteAccountRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_account(request=request)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.DeleteAccountRequest, dict]]):
                The request object. Request message for the ``DeleteAccount`` method.
            name (:class:`str`):
                Required. The name of the account to delete. Format:
                ``accounts/{account}``

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
        if not isinstance(request, accounts.DeleteAccountRequest):
            request = accounts.DeleteAccountRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_account
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

    async def update_account(
        self,
        request: Optional[Union[accounts.UpdateAccountRequest, dict]] = None,
        *,
        account: Optional[accounts.Account] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accounts.Account:
        r"""Updates an account regardless of its type:
        standalone, advanced account or sub-account. Executing
        this method requires admin access.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_update_account():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                account = merchant_accounts_v1.Account()
                account.account_name = "account_name_value"
                account.language_code = "language_code_value"

                request = merchant_accounts_v1.UpdateAccountRequest(
                    account=account,
                )

                # Make the request
                response = await client.update_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.UpdateAccountRequest, dict]]):
                The request object. Request message for the ``UpdateAccount`` method.
            account (:class:`google.shopping.merchant_accounts_v1.types.Account`):
                Required. The new version of the
                account.

                This corresponds to the ``account`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. List of fields being updated.

                The following fields are supported (in both
                ``snake_case`` and ``lowerCamelCase``):

                - ``account_name``
                - ``adult_content``
                - ``language_code``
                - ``time_zone``

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
            google.shopping.merchant_accounts_v1.types.Account:
                The Account message represents a business's account within Shopping
                   Ads. It's the primary entity for managing product
                   data, settings, and interactions with Google's
                   services and external providers.

                   Accounts can operate as standalone entities or be
                   part of a advanced account structure. In an advanced
                   account setup the parent account manages multiple
                   sub-accounts.

                   Establishing an account involves configuring
                   attributes like the account name, time zone, and
                   language preferences.

                   The Account message is the parent entity for many
                   other resources, for example, AccountRelationship,
                   Homepage, BusinessInfo and so on.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [account, update_mask]
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
        if not isinstance(request, accounts.UpdateAccountRequest):
            request = accounts.UpdateAccountRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if account is not None:
            request.account = account
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_account
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("account.name", request.account.name),)
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

    async def list_accounts(
        self,
        request: Optional[Union[accounts.ListAccountsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAccountsAsyncPager:
        r"""Note: For the ``accounts.list`` method, quota and limits usage
        are charged for each user, and not for the Merchant Center ID or
        the advanced account ID. To list several sub-accounts, you
        should use the ``accounts.listSubaccounts`` method, which is
        more suitable for advanced accounts use case.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_list_accounts():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ListAccountsRequest(
                )

                # Make the request
                page_result = client.list_accounts(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ListAccountsRequest, dict]]):
                The request object. Request message for the ``accounts.list`` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.shopping.merchant_accounts_v1.services.accounts_service.pagers.ListAccountsAsyncPager:
                Response message for the accounts.list method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, accounts.ListAccountsRequest):
            request = accounts.ListAccountsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_accounts
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListAccountsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_sub_accounts(
        self,
        request: Optional[Union[accounts.ListSubAccountsRequest, dict]] = None,
        *,
        provider: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSubAccountsAsyncPager:
        r"""List all sub-accounts for a given advanced account. This is a
        convenience wrapper for the more powerful ``accounts.list``
        method. This method will produce the same results as calling
        ``ListsAccounts`` with the following filter:
        ``relationship(providerId={parent} AND service(type="ACCOUNT_AGGREGATION"))``

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_list_sub_accounts():
                # Create a client
                client = merchant_accounts_v1.AccountsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ListSubAccountsRequest(
                    provider="provider_value",
                )

                # Make the request
                page_result = client.list_sub_accounts(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ListSubAccountsRequest, dict]]):
                The request object. Request message for the ``ListSubAccounts`` method.
            provider (:class:`str`):
                Required. The aggregation service provider. Format:
                ``accounts/{accountId}``

                This corresponds to the ``provider`` field
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
            google.shopping.merchant_accounts_v1.services.accounts_service.pagers.ListSubAccountsAsyncPager:
                Response message for the ListSubAccounts method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [provider]
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
        if not isinstance(request, accounts.ListSubAccountsRequest):
            request = accounts.ListSubAccountsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if provider is not None:
            request.provider = provider

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_sub_accounts
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("provider", request.provider),)),
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
        response = pagers.ListSubAccountsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "AccountsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AccountsServiceAsyncClient",)
