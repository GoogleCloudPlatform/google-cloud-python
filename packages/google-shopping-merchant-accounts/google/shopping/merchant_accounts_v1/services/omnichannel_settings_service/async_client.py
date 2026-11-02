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

from google.shopping.merchant_accounts_v1.services.omnichannel_settings_service import (
    pagers,
)
from google.shopping.merchant_accounts_v1.types import omnichannelsettings

from .client import OmnichannelSettingsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, OmnichannelSettingsServiceTransport
from .transports.grpc_asyncio import OmnichannelSettingsServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class OmnichannelSettingsServiceAsyncClient:
    """The service facilitates the management of a merchant's omnichannel
    settings.

    This API defines the following resource model:
    ----------------------------------------------

    [OmnichannelSetting][google.shopping.merchant.accounts.v1.OmnichannelSetting]
    """

    _client: OmnichannelSettingsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = OmnichannelSettingsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = OmnichannelSettingsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        OmnichannelSettingsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = OmnichannelSettingsServiceClient._DEFAULT_UNIVERSE

    account_path = staticmethod(OmnichannelSettingsServiceClient.account_path)
    parse_account_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_account_path
    )
    omnichannel_setting_path = staticmethod(
        OmnichannelSettingsServiceClient.omnichannel_setting_path
    )
    parse_omnichannel_setting_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_omnichannel_setting_path
    )
    common_billing_account_path = staticmethod(
        OmnichannelSettingsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        OmnichannelSettingsServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        OmnichannelSettingsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        OmnichannelSettingsServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        OmnichannelSettingsServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        OmnichannelSettingsServiceClient.parse_common_location_path
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
            OmnichannelSettingsServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            OmnichannelSettingsServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            OmnichannelSettingsServiceAsyncClient, info, *args, **kwargs
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
            OmnichannelSettingsServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            OmnichannelSettingsServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            OmnichannelSettingsServiceAsyncClient, filename, *args, **kwargs
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
        return OmnichannelSettingsServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> OmnichannelSettingsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            OmnichannelSettingsServiceTransport: The transport used by the client instance.
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

    get_transport_class = OmnichannelSettingsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                OmnichannelSettingsServiceTransport,
                Callable[..., OmnichannelSettingsServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the omnichannel settings service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,OmnichannelSettingsServiceTransport,Callable[..., OmnichannelSettingsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the OmnichannelSettingsServiceTransport constructor.
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
        self._client = OmnichannelSettingsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.accounts_v1.OmnichannelSettingsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
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
                    "serviceName": "google.shopping.merchant.accounts.v1.OmnichannelSettingsService",
                    "credentialsType": None,
                },
            )

    async def get_omnichannel_setting(
        self,
        request: Optional[
            Union[omnichannelsettings.GetOmnichannelSettingRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> omnichannelsettings.OmnichannelSetting:
        r"""Get the omnichannel settings for a given merchant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_get_omnichannel_setting():
                # Create a client
                client = merchant_accounts_v1.OmnichannelSettingsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.GetOmnichannelSettingRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_omnichannel_setting(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.GetOmnichannelSettingRequest, dict]]):
                The request object. Request message for the
                GetOmnichannelSettings method.
            name (:class:`str`):
                Required. The name of the omnichannel setting to
                retrieve. Format:
                ``accounts/{account}/omnichannelSettings/{omnichannel_setting}``

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
            google.shopping.merchant_accounts_v1.types.OmnichannelSetting:
                Collection of information related to
                the omnichannel settings of a merchant.

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
        if not isinstance(request, omnichannelsettings.GetOmnichannelSettingRequest):
            request = omnichannelsettings.GetOmnichannelSettingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_omnichannel_setting
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

    async def list_omnichannel_settings(
        self,
        request: Optional[
            Union[omnichannelsettings.ListOmnichannelSettingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOmnichannelSettingsAsyncPager:
        r"""List all the omnichannel settings for a given
        merchant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_list_omnichannel_settings():
                # Create a client
                client = merchant_accounts_v1.OmnichannelSettingsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.ListOmnichannelSettingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_omnichannel_settings(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.ListOmnichannelSettingsRequest, dict]]):
                The request object. Request message for the
                ListOmnichannelSettings method.
            parent (:class:`str`):
                Required. The parent, which owns this collection of
                omnichannel settings. Format: ``accounts/{account}``

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
            google.shopping.merchant_accounts_v1.services.omnichannel_settings_service.pagers.ListOmnichannelSettingsAsyncPager:
                Response message for the
                ListOmnichannelSettings method.
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
        if not isinstance(request, omnichannelsettings.ListOmnichannelSettingsRequest):
            request = omnichannelsettings.ListOmnichannelSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_omnichannel_settings
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
        response = pagers.ListOmnichannelSettingsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_omnichannel_setting(
        self,
        request: Optional[
            Union[omnichannelsettings.CreateOmnichannelSettingRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        omnichannel_setting: Optional[omnichannelsettings.OmnichannelSetting] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> omnichannelsettings.OmnichannelSetting:
        r"""Create the omnichannel settings for a given merchant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_create_omnichannel_setting():
                # Create a client
                client = merchant_accounts_v1.OmnichannelSettingsServiceAsyncClient()

                # Initialize request argument(s)
                omnichannel_setting = merchant_accounts_v1.OmnichannelSetting()
                omnichannel_setting.region_code = "region_code_value"
                omnichannel_setting.lsf_type = "MHLSF_FULL"

                request = merchant_accounts_v1.CreateOmnichannelSettingRequest(
                    parent="parent_value",
                    omnichannel_setting=omnichannel_setting,
                )

                # Make the request
                response = await client.create_omnichannel_setting(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.CreateOmnichannelSettingRequest, dict]]):
                The request object. Request message for the
                CreateOmnichannelSetting method.
            parent (:class:`str`):
                Required. The parent resource where this omnichannel
                setting will be created. Format: ``accounts/{account}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            omnichannel_setting (:class:`google.shopping.merchant_accounts_v1.types.OmnichannelSetting`):
                Required. The omnichannel setting to
                create.

                This corresponds to the ``omnichannel_setting`` field
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
            google.shopping.merchant_accounts_v1.types.OmnichannelSetting:
                Collection of information related to
                the omnichannel settings of a merchant.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, omnichannel_setting]
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
        if not isinstance(request, omnichannelsettings.CreateOmnichannelSettingRequest):
            request = omnichannelsettings.CreateOmnichannelSettingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if omnichannel_setting is not None:
            request.omnichannel_setting = omnichannel_setting

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_omnichannel_setting
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

    async def update_omnichannel_setting(
        self,
        request: Optional[
            Union[omnichannelsettings.UpdateOmnichannelSettingRequest, dict]
        ] = None,
        *,
        omnichannel_setting: Optional[omnichannelsettings.OmnichannelSetting] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> omnichannelsettings.OmnichannelSetting:
        r"""Update the omnichannel setting for a given merchant
        in a given country.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_update_omnichannel_setting():
                # Create a client
                client = merchant_accounts_v1.OmnichannelSettingsServiceAsyncClient()

                # Initialize request argument(s)
                omnichannel_setting = merchant_accounts_v1.OmnichannelSetting()
                omnichannel_setting.region_code = "region_code_value"
                omnichannel_setting.lsf_type = "MHLSF_FULL"

                request = merchant_accounts_v1.UpdateOmnichannelSettingRequest(
                    omnichannel_setting=omnichannel_setting,
                )

                # Make the request
                response = await client.update_omnichannel_setting(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.UpdateOmnichannelSettingRequest, dict]]):
                The request object. Request message for the
                UpdateOmnichannelSetting method.
            omnichannel_setting (:class:`google.shopping.merchant_accounts_v1.types.OmnichannelSetting`):
                Required. The omnichannel setting to update.

                The omnichannel setting's ``name`` field is used to
                identify the omnichannel setting to be updated.

                This corresponds to the ``omnichannel_setting`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to be updated.

                The following fields are supported in snake_case only:

                - ``lsf_type``
                - ``in_stock``
                - ``pickup``
                - ``odo``
                - ``about``
                - ``inventory_verification``

                Full replacement with wildcard ``*``\ is supported,
                while empty/implied update mask is not.

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
            google.shopping.merchant_accounts_v1.types.OmnichannelSetting:
                Collection of information related to
                the omnichannel settings of a merchant.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [omnichannel_setting, update_mask]
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
        if not isinstance(request, omnichannelsettings.UpdateOmnichannelSettingRequest):
            request = omnichannelsettings.UpdateOmnichannelSettingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if omnichannel_setting is not None:
            request.omnichannel_setting = omnichannel_setting
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_omnichannel_setting
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("omnichannel_setting.name", request.omnichannel_setting.name),)
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

    async def request_inventory_verification(
        self,
        request: Optional[
            Union[omnichannelsettings.RequestInventoryVerificationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> omnichannelsettings.RequestInventoryVerificationResponse:
        r"""Requests inventory verification for a given merchant
        in a given country.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_request_inventory_verification():
                # Create a client
                client = merchant_accounts_v1.OmnichannelSettingsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.RequestInventoryVerificationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.request_inventory_verification(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.RequestInventoryVerificationRequest, dict]]):
                The request object. Request message for the
                RequestInventoryVerification method.
            name (:class:`str`):
                Required. The name of the omnichannel setting to request
                inventory verification. Format:
                ``accounts/{account}/omnichannelSettings/{omnichannel_setting}``

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
            google.shopping.merchant_accounts_v1.types.RequestInventoryVerificationResponse:
                Response message for the
                RequestInventoryVerification method.

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
            request, omnichannelsettings.RequestInventoryVerificationRequest
        ):
            request = omnichannelsettings.RequestInventoryVerificationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.request_inventory_verification
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

    async def __aenter__(self) -> "OmnichannelSettingsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("OmnichannelSettingsServiceAsyncClient",)
