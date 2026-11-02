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

from google.shopping.merchant_accounts_v1.services.online_return_policy_service import (
    pagers,
)
from google.shopping.merchant_accounts_v1.types import online_return_policy
from google.shopping.merchant_accounts_v1.types import (
    online_return_policy as gsma_online_return_policy,
)

from .client import OnlineReturnPolicyServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, OnlineReturnPolicyServiceTransport
from .transports.grpc_asyncio import OnlineReturnPolicyServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class OnlineReturnPolicyServiceAsyncClient:
    """The service facilitates the management of a business's remorse
    return policy configuration, encompassing return policies for both
    ads and free listings

    programs. This API defines the following resource model:
    --------------------------------------------------------

    [OnlineReturnPolicy][google.shopping.merchant.accounts.v1.OnlineReturnPolicy]
    """

    _client: OnlineReturnPolicyServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = OnlineReturnPolicyServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = OnlineReturnPolicyServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        OnlineReturnPolicyServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = OnlineReturnPolicyServiceClient._DEFAULT_UNIVERSE

    online_return_policy_path = staticmethod(
        OnlineReturnPolicyServiceClient.online_return_policy_path
    )
    parse_online_return_policy_path = staticmethod(
        OnlineReturnPolicyServiceClient.parse_online_return_policy_path
    )
    common_billing_account_path = staticmethod(
        OnlineReturnPolicyServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        OnlineReturnPolicyServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        OnlineReturnPolicyServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        OnlineReturnPolicyServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        OnlineReturnPolicyServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        OnlineReturnPolicyServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        OnlineReturnPolicyServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        OnlineReturnPolicyServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        OnlineReturnPolicyServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        OnlineReturnPolicyServiceClient.parse_common_location_path
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
            OnlineReturnPolicyServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            OnlineReturnPolicyServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(OnlineReturnPolicyServiceAsyncClient, info, *args, **kwargs)

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
            OnlineReturnPolicyServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            OnlineReturnPolicyServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            OnlineReturnPolicyServiceAsyncClient, filename, *args, **kwargs
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
        return OnlineReturnPolicyServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> OnlineReturnPolicyServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            OnlineReturnPolicyServiceTransport: The transport used by the client instance.
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

    get_transport_class = OnlineReturnPolicyServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                OnlineReturnPolicyServiceTransport,
                Callable[..., OnlineReturnPolicyServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the online return policy service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,OnlineReturnPolicyServiceTransport,Callable[..., OnlineReturnPolicyServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the OnlineReturnPolicyServiceTransport constructor.
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
        self._client = OnlineReturnPolicyServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.accounts_v1.OnlineReturnPolicyServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.accounts.v1.OnlineReturnPolicyService",
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
                    "serviceName": "google.shopping.merchant.accounts.v1.OnlineReturnPolicyService",
                    "credentialsType": None,
                },
            )

    async def get_online_return_policy(
        self,
        request: Optional[
            Union[online_return_policy.GetOnlineReturnPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> online_return_policy.OnlineReturnPolicy:
        r"""Gets an existing return policy for a given business.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_get_online_return_policy():
                # Create a client
                client = merchant_accounts_v1.OnlineReturnPolicyServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.GetOnlineReturnPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_online_return_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.GetOnlineReturnPolicyRequest, dict]]):
                The request object. Request message for the ``GetOnlineReturnPolicy``
                method.
            name (:class:`str`):
                Required. The name of the return policy to retrieve.
                Format:
                ``accounts/{account}/onlineReturnPolicies/{return_policy}``

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
            google.shopping.merchant_accounts_v1.types.OnlineReturnPolicy:
                [Online return policy](https://support.google.com/merchants/answer/10220642)
                   object. This is currently used to represent return
                   policies for ads and free listings programs.

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
        if not isinstance(request, online_return_policy.GetOnlineReturnPolicyRequest):
            request = online_return_policy.GetOnlineReturnPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_online_return_policy
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

    async def list_online_return_policies(
        self,
        request: Optional[
            Union[online_return_policy.ListOnlineReturnPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOnlineReturnPoliciesAsyncPager:
        r"""Lists all existing return policies for a given
        business.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_list_online_return_policies():
                # Create a client
                client = merchant_accounts_v1.OnlineReturnPolicyServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ListOnlineReturnPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_online_return_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ListOnlineReturnPoliciesRequest, dict]]):
                The request object. Request message for the ``ListOnlineReturnPolicies``
                method.
            parent (:class:`str`):
                Required. The Merchant Center account for which to list
                return policies. Format: ``accounts/{account}``

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
            google.shopping.merchant_accounts_v1.services.online_return_policy_service.pagers.ListOnlineReturnPoliciesAsyncPager:
                Response message for the ListOnlineReturnPolicies
                method.

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
            request, online_return_policy.ListOnlineReturnPoliciesRequest
        ):
            request = online_return_policy.ListOnlineReturnPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_online_return_policies
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
        response = pagers.ListOnlineReturnPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_online_return_policy(
        self,
        request: Optional[
            Union[gsma_online_return_policy.CreateOnlineReturnPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        online_return_policy: Optional[
            gsma_online_return_policy.OnlineReturnPolicy
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gsma_online_return_policy.OnlineReturnPolicy:
        r"""Creates a new return policy for a given business.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_create_online_return_policy():
                # Create a client
                client = merchant_accounts_v1.OnlineReturnPolicyServiceAsyncClient()

                # Initialize request argument(s)
                online_return_policy = merchant_accounts_v1.OnlineReturnPolicy()
                online_return_policy.countries = ['countries_value1', 'countries_value2']
                online_return_policy.return_policy_uri = "return_policy_uri_value"

                request = merchant_accounts_v1.CreateOnlineReturnPolicyRequest(
                    parent="parent_value",
                    online_return_policy=online_return_policy,
                )

                # Make the request
                response = await client.create_online_return_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.CreateOnlineReturnPolicyRequest, dict]]):
                The request object. Request message for the ``CreateOnlineReturnPolicy``
                method.
            parent (:class:`str`):
                Required. The Merchant Center account for which the
                return policy will be created. Format:
                ``accounts/{account}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            online_return_policy (:class:`google.shopping.merchant_accounts_v1.types.OnlineReturnPolicy`):
                Required. The return policy object to
                create.

                This corresponds to the ``online_return_policy`` field
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
            google.shopping.merchant_accounts_v1.types.OnlineReturnPolicy:
                [Online return policy](https://support.google.com/merchants/answer/10220642)
                   object. This is currently used to represent return
                   policies for ads and free listings programs.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, online_return_policy]
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
            request, gsma_online_return_policy.CreateOnlineReturnPolicyRequest
        ):
            request = gsma_online_return_policy.CreateOnlineReturnPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if online_return_policy is not None:
            request.online_return_policy = online_return_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_online_return_policy
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

    async def delete_online_return_policy(
        self,
        request: Optional[
            Union[online_return_policy.DeleteOnlineReturnPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing return policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_delete_online_return_policy():
                # Create a client
                client = merchant_accounts_v1.OnlineReturnPolicyServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.DeleteOnlineReturnPolicyRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_online_return_policy(request=request)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.DeleteOnlineReturnPolicyRequest, dict]]):
                The request object. Request message for the ``DeleteOnlineReturnPolicy``
                method.
            name (:class:`str`):
                Required. The name of the return policy to delete.
                Format:
                ``accounts/{account}/onlineReturnPolicies/{return_policy}``

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
            request, online_return_policy.DeleteOnlineReturnPolicyRequest
        ):
            request = online_return_policy.DeleteOnlineReturnPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_online_return_policy
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

    async def __aenter__(self) -> "OnlineReturnPolicyServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("OnlineReturnPolicyServiceAsyncClient",)
