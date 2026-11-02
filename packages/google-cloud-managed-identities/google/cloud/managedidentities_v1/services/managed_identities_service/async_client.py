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

from google.cloud.managedidentities_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.managedidentities_v1.services.managed_identities_service import pagers
from google.cloud.managedidentities_v1.types import managed_identities_service, resource

from .client import ManagedIdentitiesServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, ManagedIdentitiesServiceTransport
from .transports.grpc_asyncio import ManagedIdentitiesServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ManagedIdentitiesServiceAsyncClient:
    """API Overview

    The ``managedidentites.googleapis.com`` service implements the
    Google Cloud Managed Identites API for identity services (e.g.
    Microsoft Active Directory).

    The Managed Identities service provides methods to manage
    (create/read/update/delete) domains, reset managed identities admin
    password, add/remove domain controllers in GCP regions and
    add/remove VPC peering.

    Data Model

    The Managed Identities service exposes the following resources:

    - Locations as global, named as follows:
      ``projects/{project_id}/locations/global``.

    - Domains, named as follows:
      ``/projects/{project_id}/locations/global/domain/{domain_name}``.

    The ``{domain_name}`` refers to fully qualified domain name in the
    customer project e.g. mydomain.myorganization.com, with the
    following restrictions:

    - Must contain only lowercase letters, numbers, periods and hyphens.
    - Must start with a letter.
    - Must contain between 2-64 characters.
    - Must end with a number or a letter.
    - Must not start with period.
    - First segement length (mydomain form example above) shouldn't
      exceed 15 chars.
    - The last segment cannot be fully numeric.
    - Must be unique within the customer project.
    """

    _client: ManagedIdentitiesServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ManagedIdentitiesServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ManagedIdentitiesServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        ManagedIdentitiesServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = ManagedIdentitiesServiceClient._DEFAULT_UNIVERSE

    domain_path = staticmethod(ManagedIdentitiesServiceClient.domain_path)
    parse_domain_path = staticmethod(ManagedIdentitiesServiceClient.parse_domain_path)
    common_billing_account_path = staticmethod(
        ManagedIdentitiesServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ManagedIdentitiesServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ManagedIdentitiesServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ManagedIdentitiesServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ManagedIdentitiesServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ManagedIdentitiesServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        ManagedIdentitiesServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        ManagedIdentitiesServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        ManagedIdentitiesServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        ManagedIdentitiesServiceClient.parse_common_location_path
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
            ManagedIdentitiesServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            ManagedIdentitiesServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ManagedIdentitiesServiceAsyncClient, info, *args, **kwargs)

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
            ManagedIdentitiesServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            ManagedIdentitiesServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            ManagedIdentitiesServiceAsyncClient, filename, *args, **kwargs
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
        return ManagedIdentitiesServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> ManagedIdentitiesServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ManagedIdentitiesServiceTransport: The transport used by the client instance.
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

    get_transport_class = ManagedIdentitiesServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                ManagedIdentitiesServiceTransport,
                Callable[..., ManagedIdentitiesServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the managed identities service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ManagedIdentitiesServiceTransport,Callable[..., ManagedIdentitiesServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ManagedIdentitiesServiceTransport constructor.
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
        self._client = ManagedIdentitiesServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.managedidentities_v1.ManagedIdentitiesServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.managedidentities.v1.ManagedIdentitiesService",
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
                    "serviceName": "google.cloud.managedidentities.v1.ManagedIdentitiesService",
                    "credentialsType": None,
                },
            )

    async def create_microsoft_ad_domain(
        self,
        request: Optional[
            Union[managed_identities_service.CreateMicrosoftAdDomainRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        domain_name: Optional[str] = None,
        domain: Optional[resource.Domain] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a Microsoft AD domain.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_create_microsoft_ad_domain():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                domain = managedidentities_v1.Domain()
                domain.name = "name_value"
                domain.reserved_ip_range = "reserved_ip_range_value"
                domain.locations = ['locations_value1', 'locations_value2']

                request = managedidentities_v1.CreateMicrosoftAdDomainRequest(
                    parent="parent_value",
                    domain_name="domain_name_value",
                    domain=domain,
                )

                # Make the request
                operation = await client.create_microsoft_ad_domain(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.CreateMicrosoftAdDomainRequest, dict]]):
                The request object. Request message for
                [CreateMicrosoftAdDomain][google.cloud.managedidentities.v1.CreateMicrosoftAdDomain]
            parent (:class:`str`):
                Required. The resource project name and location using
                the form: ``projects/{project_id}/locations/global``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            domain_name (:class:`str`):
                Required. The fully qualified domain name. e.g.
                mydomain.myorganization.com, with the following
                restrictions:

                - Must contain only lowercase letters, numbers, periods
                  and hyphens.
                - Must start with a letter.
                - Must contain between 2-64 characters.
                - Must end with a number or a letter.
                - Must not start with period.
                - First segement length (mydomain form example above)
                  shouldn't exceed 15 chars.
                - The last segment cannot be fully numeric.
                - Must be unique within the customer project.

                This corresponds to the ``domain_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            domain (:class:`google.cloud.managedidentities_v1.types.Domain`):
                Required. A Managed Identity domain
                resource.

                This corresponds to the ``domain`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.managedidentities_v1.types.Domain`
                Represents a managed Microsoft Active Directory domain.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, domain_name, domain]
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
            request, managed_identities_service.CreateMicrosoftAdDomainRequest
        ):
            request = managed_identities_service.CreateMicrosoftAdDomainRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if domain_name is not None:
            request.domain_name = domain_name
        if domain is not None:
            request.domain = domain

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_microsoft_ad_domain
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resource.Domain,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def reset_admin_password(
        self,
        request: Optional[
            Union[managed_identities_service.ResetAdminPasswordRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> managed_identities_service.ResetAdminPasswordResponse:
        r"""Resets a domain's administrator password.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_reset_admin_password():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                request = managedidentities_v1.ResetAdminPasswordRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.reset_admin_password(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.ResetAdminPasswordRequest, dict]]):
                The request object. Request message for
                [ResetAdminPassword][google.cloud.managedidentities.v1.ResetAdminPassword]
            name (:class:`str`):
                Required. The domain resource name using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

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
            google.cloud.managedidentities_v1.types.ResetAdminPasswordResponse:
                Response message for
                   [ResetAdminPassword][google.cloud.managedidentities.v1.ResetAdminPassword]

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
            request, managed_identities_service.ResetAdminPasswordRequest
        ):
            request = managed_identities_service.ResetAdminPasswordRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reset_admin_password
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

    async def list_domains(
        self,
        request: Optional[
            Union[managed_identities_service.ListDomainsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDomainsAsyncPager:
        r"""Lists domains in a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_list_domains():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                request = managedidentities_v1.ListDomainsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_domains(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.ListDomainsRequest, dict]]):
                The request object. Request message for
                [ListDomains][google.cloud.managedidentities.v1.ListDomains]
            parent (:class:`str`):
                Required. The resource name of the domain location using
                the form: ``projects/{project_id}/locations/global``

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
            google.cloud.managedidentities_v1.services.managed_identities_service.pagers.ListDomainsAsyncPager:
                Response message for
                   [ListDomains][google.cloud.managedidentities.v1.ListDomains]

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
        if not isinstance(request, managed_identities_service.ListDomainsRequest):
            request = managed_identities_service.ListDomainsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_domains
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
        response = pagers.ListDomainsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_domain(
        self,
        request: Optional[
            Union[managed_identities_service.GetDomainRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource.Domain:
        r"""Gets information about a domain.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_get_domain():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                request = managedidentities_v1.GetDomainRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_domain(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.GetDomainRequest, dict]]):
                The request object. Request message for
                [GetDomain][google.cloud.managedidentities.v1.GetDomain]
            name (:class:`str`):
                Required. The domain resource name using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

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
            google.cloud.managedidentities_v1.types.Domain:
                Represents a managed Microsoft Active
                Directory domain.

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
        if not isinstance(request, managed_identities_service.GetDomainRequest):
            request = managed_identities_service.GetDomainRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_domain
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

    async def update_domain(
        self,
        request: Optional[
            Union[managed_identities_service.UpdateDomainRequest, dict]
        ] = None,
        *,
        domain: Optional[resource.Domain] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the metadata and configuration of a domain.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_update_domain():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                domain = managedidentities_v1.Domain()
                domain.name = "name_value"
                domain.reserved_ip_range = "reserved_ip_range_value"
                domain.locations = ['locations_value1', 'locations_value2']

                request = managedidentities_v1.UpdateDomainRequest(
                    domain=domain,
                )

                # Make the request
                operation = await client.update_domain(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.UpdateDomainRequest, dict]]):
                The request object. Request message for
                [UpdateDomain][google.cloud.managedidentities.v1.UpdateDomain]
            domain (:class:`google.cloud.managedidentities_v1.types.Domain`):
                Required. Domain message with updated fields. Only
                supported fields specified in update_mask are updated.

                This corresponds to the ``domain`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. The elements of the
                repeated paths field may only include fields from
                [Domain][google.cloud.managedidentities.v1.Domain]:

                - ``labels``
                - ``locations``
                - ``authorized_networks``

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.managedidentities_v1.types.Domain`
                Represents a managed Microsoft Active Directory domain.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [domain, update_mask]
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
        if not isinstance(request, managed_identities_service.UpdateDomainRequest):
            request = managed_identities_service.UpdateDomainRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if domain is not None:
            request.domain = domain
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_domain
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("domain.name", request.domain.name),)
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resource.Domain,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def delete_domain(
        self,
        request: Optional[
            Union[managed_identities_service.DeleteDomainRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a domain.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_delete_domain():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                request = managedidentities_v1.DeleteDomainRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_domain(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.DeleteDomainRequest, dict]]):
                The request object. Request message for
                [DeleteDomain][google.cloud.managedidentities.v1.DeleteDomain]
            name (:class:`str`):
                Required. The domain resource name using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

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
        if not isinstance(request, managed_identities_service.DeleteDomainRequest):
            request = managed_identities_service.DeleteDomainRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_domain
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def attach_trust(
        self,
        request: Optional[
            Union[managed_identities_service.AttachTrustRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        trust: Optional[resource.Trust] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Adds an AD trust to a domain.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_attach_trust():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                trust = managedidentities_v1.Trust()
                trust.target_domain_name = "target_domain_name_value"
                trust.trust_type = "EXTERNAL"
                trust.trust_direction = "BIDIRECTIONAL"
                trust.target_dns_ip_addresses = ['target_dns_ip_addresses_value1', 'target_dns_ip_addresses_value2']
                trust.trust_handshake_secret = "trust_handshake_secret_value"

                request = managedidentities_v1.AttachTrustRequest(
                    name="name_value",
                    trust=trust,
                )

                # Make the request
                operation = await client.attach_trust(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.AttachTrustRequest, dict]]):
                The request object. Request message for
                [AttachTrust][google.cloud.managedidentities.v1.AttachTrust]
            name (:class:`str`):
                Required. The resource domain name, project name and
                location using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trust (:class:`google.cloud.managedidentities_v1.types.Trust`):
                Required. The domain trust resource.
                This corresponds to the ``trust`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.managedidentities_v1.types.Domain`
                Represents a managed Microsoft Active Directory domain.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, trust]
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
        if not isinstance(request, managed_identities_service.AttachTrustRequest):
            request = managed_identities_service.AttachTrustRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if trust is not None:
            request.trust = trust

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.attach_trust
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resource.Domain,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def reconfigure_trust(
        self,
        request: Optional[
            Union[managed_identities_service.ReconfigureTrustRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        target_domain_name: Optional[str] = None,
        target_dns_ip_addresses: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the DNS conditional forwarder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_reconfigure_trust():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                request = managedidentities_v1.ReconfigureTrustRequest(
                    name="name_value",
                    target_domain_name="target_domain_name_value",
                    target_dns_ip_addresses=['target_dns_ip_addresses_value1', 'target_dns_ip_addresses_value2'],
                )

                # Make the request
                operation = await client.reconfigure_trust(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.ReconfigureTrustRequest, dict]]):
                The request object. Request message for
                [ReconfigureTrust][google.cloud.managedidentities.v1.ReconfigureTrust]
            name (:class:`str`):
                Required. The resource domain name, project name and
                location using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_domain_name (:class:`str`):
                Required. The fully-qualified target
                domain name which will be in trust with
                current domain.

                This corresponds to the ``target_domain_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target_dns_ip_addresses (:class:`MutableSequence[str]`):
                Required. The target DNS server IP
                addresses to resolve the remote domain
                involved in the trust.

                This corresponds to the ``target_dns_ip_addresses`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.managedidentities_v1.types.Domain`
                Represents a managed Microsoft Active Directory domain.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, target_domain_name, target_dns_ip_addresses]
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
        if not isinstance(request, managed_identities_service.ReconfigureTrustRequest):
            request = managed_identities_service.ReconfigureTrustRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if target_domain_name is not None:
            request.target_domain_name = target_domain_name
        if target_dns_ip_addresses:
            request.target_dns_ip_addresses.extend(target_dns_ip_addresses)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reconfigure_trust
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resource.Domain,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def detach_trust(
        self,
        request: Optional[
            Union[managed_identities_service.DetachTrustRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        trust: Optional[resource.Trust] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Removes an AD trust.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_detach_trust():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                trust = managedidentities_v1.Trust()
                trust.target_domain_name = "target_domain_name_value"
                trust.trust_type = "EXTERNAL"
                trust.trust_direction = "BIDIRECTIONAL"
                trust.target_dns_ip_addresses = ['target_dns_ip_addresses_value1', 'target_dns_ip_addresses_value2']
                trust.trust_handshake_secret = "trust_handshake_secret_value"

                request = managedidentities_v1.DetachTrustRequest(
                    name="name_value",
                    trust=trust,
                )

                # Make the request
                operation = await client.detach_trust(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.DetachTrustRequest, dict]]):
                The request object. Request message for
                [DetachTrust][google.cloud.managedidentities.v1.DetachTrust]
            name (:class:`str`):
                Required. The resource domain name, project name, and
                location using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trust (:class:`google.cloud.managedidentities_v1.types.Trust`):
                Required. The domain trust resource
                to removed.

                This corresponds to the ``trust`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.managedidentities_v1.types.Domain`
                Represents a managed Microsoft Active Directory domain.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, trust]
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
        if not isinstance(request, managed_identities_service.DetachTrustRequest):
            request = managed_identities_service.DetachTrustRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if trust is not None:
            request.trust = trust

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.detach_trust
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resource.Domain,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def validate_trust(
        self,
        request: Optional[
            Union[managed_identities_service.ValidateTrustRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        trust: Optional[resource.Trust] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Validates a trust state, that the target domain is
        reachable, and that the target domain is able to accept
        incoming trust requests.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedidentities_v1

            async def sample_validate_trust():
                # Create a client
                client = managedidentities_v1.ManagedIdentitiesServiceAsyncClient()

                # Initialize request argument(s)
                trust = managedidentities_v1.Trust()
                trust.target_domain_name = "target_domain_name_value"
                trust.trust_type = "EXTERNAL"
                trust.trust_direction = "BIDIRECTIONAL"
                trust.target_dns_ip_addresses = ['target_dns_ip_addresses_value1', 'target_dns_ip_addresses_value2']
                trust.trust_handshake_secret = "trust_handshake_secret_value"

                request = managedidentities_v1.ValidateTrustRequest(
                    name="name_value",
                    trust=trust,
                )

                # Make the request
                operation = await client.validate_trust(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedidentities_v1.types.ValidateTrustRequest, dict]]):
                The request object. Request message for
                [ValidateTrust][google.cloud.managedidentities.v1.ValidateTrust]
            name (:class:`str`):
                Required. The resource domain name, project name, and
                location using the form:
                ``projects/{project_id}/locations/global/domains/{domain_name}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trust (:class:`google.cloud.managedidentities_v1.types.Trust`):
                Required. The domain trust to
                validate trust state for.

                This corresponds to the ``trust`` field
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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.managedidentities_v1.types.Domain`
                Represents a managed Microsoft Active Directory domain.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, trust]
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
        if not isinstance(request, managed_identities_service.ValidateTrustRequest):
            request = managed_identities_service.ValidateTrustRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if trust is not None:
            request.trust = trust

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.validate_trust
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            resource.Domain,
            metadata_type=managed_identities_service.OpMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "ManagedIdentitiesServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ManagedIdentitiesServiceAsyncClient",)
