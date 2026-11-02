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

from google.cloud.saasplatform_saasservicemgmt_v1beta1 import (
    gapic_version as package_version,
)

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments import (
    pagers,
)
from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import (
    common,
    deployments_resources,
    deployments_service,
)

from .client import SaasDeploymentsClient
from .transports.base import DEFAULT_CLIENT_INFO, SaasDeploymentsTransport
from .transports.grpc_asyncio import SaasDeploymentsGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SaasDeploymentsAsyncClient:
    """Manages the deployment of SaaS services."""

    _client: SaasDeploymentsClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SaasDeploymentsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SaasDeploymentsClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SaasDeploymentsClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SaasDeploymentsClient._DEFAULT_UNIVERSE

    application_path = staticmethod(SaasDeploymentsClient.application_path)
    parse_application_path = staticmethod(SaasDeploymentsClient.parse_application_path)
    application_template_path = staticmethod(
        SaasDeploymentsClient.application_template_path
    )
    parse_application_template_path = staticmethod(
        SaasDeploymentsClient.parse_application_template_path
    )
    application_template_revision_path = staticmethod(
        SaasDeploymentsClient.application_template_revision_path
    )
    parse_application_template_revision_path = staticmethod(
        SaasDeploymentsClient.parse_application_template_revision_path
    )
    release_path = staticmethod(SaasDeploymentsClient.release_path)
    parse_release_path = staticmethod(SaasDeploymentsClient.parse_release_path)
    rollout_path = staticmethod(SaasDeploymentsClient.rollout_path)
    parse_rollout_path = staticmethod(SaasDeploymentsClient.parse_rollout_path)
    saas_path = staticmethod(SaasDeploymentsClient.saas_path)
    parse_saas_path = staticmethod(SaasDeploymentsClient.parse_saas_path)
    tenant_path = staticmethod(SaasDeploymentsClient.tenant_path)
    parse_tenant_path = staticmethod(SaasDeploymentsClient.parse_tenant_path)
    unit_path = staticmethod(SaasDeploymentsClient.unit_path)
    parse_unit_path = staticmethod(SaasDeploymentsClient.parse_unit_path)
    unit_kind_path = staticmethod(SaasDeploymentsClient.unit_kind_path)
    parse_unit_kind_path = staticmethod(SaasDeploymentsClient.parse_unit_kind_path)
    unit_operation_path = staticmethod(SaasDeploymentsClient.unit_operation_path)
    parse_unit_operation_path = staticmethod(
        SaasDeploymentsClient.parse_unit_operation_path
    )
    common_billing_account_path = staticmethod(
        SaasDeploymentsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SaasDeploymentsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SaasDeploymentsClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        SaasDeploymentsClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        SaasDeploymentsClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        SaasDeploymentsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(SaasDeploymentsClient.common_project_path)
    parse_common_project_path = staticmethod(
        SaasDeploymentsClient.parse_common_project_path
    )
    common_location_path = staticmethod(SaasDeploymentsClient.common_location_path)
    parse_common_location_path = staticmethod(
        SaasDeploymentsClient.parse_common_location_path
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
            SaasDeploymentsAsyncClient: The constructed client.
        """
        sa_info_func = (
            SaasDeploymentsClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SaasDeploymentsAsyncClient, info, *args, **kwargs)

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
            SaasDeploymentsAsyncClient: The constructed client.
        """
        sa_file_func = (
            SaasDeploymentsClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(SaasDeploymentsAsyncClient, filename, *args, **kwargs)

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
        return SaasDeploymentsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> SaasDeploymentsTransport:
        """Returns the transport used by the client instance.

        Returns:
            SaasDeploymentsTransport: The transport used by the client instance.
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

    get_transport_class = SaasDeploymentsClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str, SaasDeploymentsTransport, Callable[..., SaasDeploymentsTransport]
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the saas deployments async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SaasDeploymentsTransport,Callable[..., SaasDeploymentsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SaasDeploymentsTransport constructor.
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
        self._client = SaasDeploymentsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
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
                    "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments",
                    "credentialsType": None,
                },
            )

    async def list_saas(
        self,
        request: Optional[Union[deployments_service.ListSaasRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSaasAsyncPager:
        r"""Retrieve a collection of saas.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_saas():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListSaasRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_saas(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasRequest, dict]]):
                The request object. The request structure for the
                ListSaas method.
            parent (:class:`str`):
                Required. The parent of the saas.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments.pagers.ListSaasAsyncPager:
                The response structure for the
                ListSaas method.
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
        if not isinstance(request, deployments_service.ListSaasRequest):
            request = deployments_service.ListSaasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_saas
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
        response = pagers.ListSaasAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_saas(
        self,
        request: Optional[Union[deployments_service.GetSaasRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Saas:
        r"""Retrieve a single saas.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_saas():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetSaasRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_saas(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetSaasRequest, dict]]):
                The request object. The request structure for the GetSaas
                method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas:
                Saas is a representation of a SaaS
                service managed by the Producer.

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
        if not isinstance(request, deployments_service.GetSaasRequest):
            request = deployments_service.GetSaasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_saas]

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

    async def create_saas(
        self,
        request: Optional[Union[deployments_service.CreateSaasRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        saas: Optional[deployments_resources.Saas] = None,
        saas_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Saas:
        r"""Create a new saas.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_saas():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.CreateSaasRequest(
                    parent="parent_value",
                    saas_id="saas_id_value",
                )

                # Make the request
                response = await client.create_saas(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateSaasRequest, dict]]):
                The request object. The request structure for the
                CreateSaas method.
            parent (:class:`str`):
                Required. The parent of the saas.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            saas (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas`):
                Required. The desired state for the
                saas.

                This corresponds to the ``saas`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            saas_id (:class:`str`):
                Required. The ID value for the new
                saas.

                This corresponds to the ``saas_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas:
                Saas is a representation of a SaaS
                service managed by the Producer.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, saas, saas_id]
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
        if not isinstance(request, deployments_service.CreateSaasRequest):
            request = deployments_service.CreateSaasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if saas is not None:
            request.saas = saas
        if saas_id is not None:
            request.saas_id = saas_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_saas
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

    async def update_saas(
        self,
        request: Optional[Union[deployments_service.UpdateSaasRequest, dict]] = None,
        *,
        saas: Optional[deployments_resources.Saas] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Saas:
        r"""Update a single saas.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_saas():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.UpdateSaasRequest(
                )

                # Make the request
                response = await client.update_saas(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateSaasRequest, dict]]):
                The request object. The request structure for the
                UpdateSaas method.
            saas (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas`):
                Required. The desired state for the
                saas.

                This corresponds to the ``saas`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the Saas resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the Saas will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Saas:
                Saas is a representation of a SaaS
                service managed by the Producer.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [saas, update_mask]
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
        if not isinstance(request, deployments_service.UpdateSaasRequest):
            request = deployments_service.UpdateSaasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if saas is not None:
            request.saas = saas
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_saas
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("saas.name", request.saas.name),)
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

    async def delete_saas(
        self,
        request: Optional[Union[deployments_service.DeleteSaasRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single saas.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_saas():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteSaasRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_saas(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteSaasRequest, dict]]):
                The request object. The request structure for the
                DeleteSaas method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
        if not isinstance(request, deployments_service.DeleteSaasRequest):
            request = deployments_service.DeleteSaasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_saas
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

    async def list_tenants(
        self,
        request: Optional[Union[deployments_service.ListTenantsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTenantsAsyncPager:
        r"""Retrieve a collection of tenants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_tenants():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListTenantsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_tenants(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsRequest, dict]]):
                The request object. The request structure for the
                ListTenants method.
            parent (:class:`str`):
                Required. The parent of the tenant.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments.pagers.ListTenantsAsyncPager:
                The response structure for the
                ListTenants method.
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
        if not isinstance(request, deployments_service.ListTenantsRequest):
            request = deployments_service.ListTenantsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_tenants
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
        response = pagers.ListTenantsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_tenant(
        self,
        request: Optional[Union[deployments_service.GetTenantRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Tenant:
        r"""Retrieve a single tenant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_tenant():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetTenantRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_tenant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetTenantRequest, dict]]):
                The request object. The request structure for the
                GetTenant method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant:
                Tenant represents the service producer side of an instance of the
                   service created based on a request from a consumer.
                   In a typical scenario a Tenant has a one-to-one
                   mapping with a resource given out to a service
                   consumer.

                   Example:

                      tenant:
                         name:
                         "projects/svc1/locations/loc/tenants/inst-068afff8"
                         consumer_resource:
                         "projects/gshoe/locations/loc/shoes/black-shoe"

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
        if not isinstance(request, deployments_service.GetTenantRequest):
            request = deployments_service.GetTenantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_tenant
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

    async def create_tenant(
        self,
        request: Optional[Union[deployments_service.CreateTenantRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        tenant: Optional[deployments_resources.Tenant] = None,
        tenant_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Tenant:
        r"""Create a new tenant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_tenant():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                tenant = saasplatform_saasservicemgmt_v1beta1.Tenant()
                tenant.saas = "saas_value"

                request = saasplatform_saasservicemgmt_v1beta1.CreateTenantRequest(
                    parent="parent_value",
                    tenant_id="tenant_id_value",
                    tenant=tenant,
                )

                # Make the request
                response = await client.create_tenant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateTenantRequest, dict]]):
                The request object. The request structure for the
                CreateTenant method.
            parent (:class:`str`):
                Required. The parent of the tenant.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tenant (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant`):
                Required. The desired state for the
                tenant.

                This corresponds to the ``tenant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tenant_id (:class:`str`):
                Required. The ID value for the new
                tenant.

                This corresponds to the ``tenant_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant:
                Tenant represents the service producer side of an instance of the
                   service created based on a request from a consumer.
                   In a typical scenario a Tenant has a one-to-one
                   mapping with a resource given out to a service
                   consumer.

                   Example:

                      tenant:
                         name:
                         "projects/svc1/locations/loc/tenants/inst-068afff8"
                         consumer_resource:
                         "projects/gshoe/locations/loc/shoes/black-shoe"

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, tenant, tenant_id]
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
        if not isinstance(request, deployments_service.CreateTenantRequest):
            request = deployments_service.CreateTenantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if tenant is not None:
            request.tenant = tenant
        if tenant_id is not None:
            request.tenant_id = tenant_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_tenant
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

    async def update_tenant(
        self,
        request: Optional[Union[deployments_service.UpdateTenantRequest, dict]] = None,
        *,
        tenant: Optional[deployments_resources.Tenant] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Tenant:
        r"""Update a single tenant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_tenant():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                tenant = saasplatform_saasservicemgmt_v1beta1.Tenant()
                tenant.saas = "saas_value"

                request = saasplatform_saasservicemgmt_v1beta1.UpdateTenantRequest(
                    tenant=tenant,
                )

                # Make the request
                response = await client.update_tenant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateTenantRequest, dict]]):
                The request object. The request structure for the
                UpdateTenant method.
            tenant (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant`):
                Required. The desired state for the
                tenant.

                This corresponds to the ``tenant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the Tenant resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the Tenant will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Tenant:
                Tenant represents the service producer side of an instance of the
                   service created based on a request from a consumer.
                   In a typical scenario a Tenant has a one-to-one
                   mapping with a resource given out to a service
                   consumer.

                   Example:

                      tenant:
                         name:
                         "projects/svc1/locations/loc/tenants/inst-068afff8"
                         consumer_resource:
                         "projects/gshoe/locations/loc/shoes/black-shoe"

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [tenant, update_mask]
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
        if not isinstance(request, deployments_service.UpdateTenantRequest):
            request = deployments_service.UpdateTenantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if tenant is not None:
            request.tenant = tenant
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_tenant
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("tenant.name", request.tenant.name),)
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

    async def delete_tenant(
        self,
        request: Optional[Union[deployments_service.DeleteTenantRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single tenant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_tenant():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteTenantRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_tenant(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteTenantRequest, dict]]):
                The request object. The request structure for the
                DeleteTenant method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
        if not isinstance(request, deployments_service.DeleteTenantRequest):
            request = deployments_service.DeleteTenantRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_tenant
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

    async def list_unit_kinds(
        self,
        request: Optional[Union[deployments_service.ListUnitKindsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUnitKindsAsyncPager:
        r"""Retrieve a collection of unit kinds.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_unit_kinds():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListUnitKindsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_unit_kinds(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsRequest, dict]]):
                The request object. The request structure for the
                ListUnitKinds method.
            parent (:class:`str`):
                Required. The parent of the unit
                kind.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments.pagers.ListUnitKindsAsyncPager:
                The response structure for the
                ListUnitKinds method.
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
        if not isinstance(request, deployments_service.ListUnitKindsRequest):
            request = deployments_service.ListUnitKindsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_unit_kinds
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
        response = pagers.ListUnitKindsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_unit_kind(
        self,
        request: Optional[Union[deployments_service.GetUnitKindRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.UnitKind:
        r"""Retrieve a single unit kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_unit_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetUnitKindRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_unit_kind(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetUnitKindRequest, dict]]):
                The request object. The request structure for the
                GetUnitKind method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind:
                Definition of a Unit. Units belonging
                to the same UnitKind are managed
                together; for example they follow the
                same release model (blueprints, versions
                etc.) and are typically rolled out
                together.

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
        if not isinstance(request, deployments_service.GetUnitKindRequest):
            request = deployments_service.GetUnitKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_unit_kind
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

    async def create_unit_kind(
        self,
        request: Optional[
            Union[deployments_service.CreateUnitKindRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        unit_kind: Optional[deployments_resources.UnitKind] = None,
        unit_kind_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.UnitKind:
        r"""Create a new unit kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_unit_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                unit_kind = saasplatform_saasservicemgmt_v1beta1.UnitKind()
                unit_kind.saas = "saas_value"

                request = saasplatform_saasservicemgmt_v1beta1.CreateUnitKindRequest(
                    parent="parent_value",
                    unit_kind_id="unit_kind_id_value",
                    unit_kind=unit_kind,
                )

                # Make the request
                response = await client.create_unit_kind(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateUnitKindRequest, dict]]):
                The request object. The request structure for the
                CreateUnitKind method.
            parent (:class:`str`):
                Required. The parent of the unit
                kind.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            unit_kind (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind`):
                Required. The desired state for the
                unit kind.

                This corresponds to the ``unit_kind`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            unit_kind_id (:class:`str`):
                Required. The ID value for the new
                unit kind.

                This corresponds to the ``unit_kind_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind:
                Definition of a Unit. Units belonging
                to the same UnitKind are managed
                together; for example they follow the
                same release model (blueprints, versions
                etc.) and are typically rolled out
                together.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, unit_kind, unit_kind_id]
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
        if not isinstance(request, deployments_service.CreateUnitKindRequest):
            request = deployments_service.CreateUnitKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if unit_kind is not None:
            request.unit_kind = unit_kind
        if unit_kind_id is not None:
            request.unit_kind_id = unit_kind_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_unit_kind
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

    async def update_unit_kind(
        self,
        request: Optional[
            Union[deployments_service.UpdateUnitKindRequest, dict]
        ] = None,
        *,
        unit_kind: Optional[deployments_resources.UnitKind] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.UnitKind:
        r"""Update a single unit kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_unit_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                unit_kind = saasplatform_saasservicemgmt_v1beta1.UnitKind()
                unit_kind.saas = "saas_value"

                request = saasplatform_saasservicemgmt_v1beta1.UpdateUnitKindRequest(
                    unit_kind=unit_kind,
                )

                # Make the request
                response = await client.update_unit_kind(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateUnitKindRequest, dict]]):
                The request object. The request structure for the
                UpdateUnitKind method.
            unit_kind (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind`):
                Required. The desired state for the
                unit kind.

                This corresponds to the ``unit_kind`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the UnitKind resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the UnitKind will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitKind:
                Definition of a Unit. Units belonging
                to the same UnitKind are managed
                together; for example they follow the
                same release model (blueprints, versions
                etc.) and are typically rolled out
                together.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [unit_kind, update_mask]
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
        if not isinstance(request, deployments_service.UpdateUnitKindRequest):
            request = deployments_service.UpdateUnitKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if unit_kind is not None:
            request.unit_kind = unit_kind
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_unit_kind
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("unit_kind.name", request.unit_kind.name),)
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

    async def delete_unit_kind(
        self,
        request: Optional[
            Union[deployments_service.DeleteUnitKindRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single unit kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_unit_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteUnitKindRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_unit_kind(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteUnitKindRequest, dict]]):
                The request object. The request structure for the
                DeleteUnitKind method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
        if not isinstance(request, deployments_service.DeleteUnitKindRequest):
            request = deployments_service.DeleteUnitKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_unit_kind
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

    async def list_units(
        self,
        request: Optional[Union[deployments_service.ListUnitsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUnitsAsyncPager:
        r"""Retrieve a collection of units.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_units():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListUnitsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_units(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsRequest, dict]]):
                The request object. The request structure for the
                ListUnits method.
            parent (:class:`str`):
                Required. The parent of the unit.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments.pagers.ListUnitsAsyncPager:
                The response structure for the
                ListUnits method.
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
        if not isinstance(request, deployments_service.ListUnitsRequest):
            request = deployments_service.ListUnitsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_units
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
        response = pagers.ListUnitsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_unit(
        self,
        request: Optional[Union[deployments_service.GetUnitRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Unit:
        r"""Retrieve a single unit.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_unit():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetUnitRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_unit(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetUnitRequest, dict]]):
                The request object. The request structure for the GetUnit
                method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit:
                A unit of deployment that has its
                lifecycle via a CRUD API using an
                actuation engine under the hood (e.g.
                based on Terraform, Helm or a custom
                implementation provided by a service
                producer). A building block of a SaaS
                Tenant.

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
        if not isinstance(request, deployments_service.GetUnitRequest):
            request = deployments_service.GetUnitRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_unit]

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

    async def create_unit(
        self,
        request: Optional[Union[deployments_service.CreateUnitRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        unit: Optional[deployments_resources.Unit] = None,
        unit_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Unit:
        r"""Create a new unit.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_unit():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.CreateUnitRequest(
                    parent="parent_value",
                    unit_id="unit_id_value",
                )

                # Make the request
                response = await client.create_unit(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateUnitRequest, dict]]):
                The request object. The request structure for the
                CreateUnit method.
            parent (:class:`str`):
                Required. The parent of the unit.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            unit (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit`):
                Required. The desired state for the
                unit.

                This corresponds to the ``unit`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            unit_id (:class:`str`):
                Required. The ID value for the new
                unit.

                This corresponds to the ``unit_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit:
                A unit of deployment that has its
                lifecycle via a CRUD API using an
                actuation engine under the hood (e.g.
                based on Terraform, Helm or a custom
                implementation provided by a service
                producer). A building block of a SaaS
                Tenant.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, unit, unit_id]
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
        if not isinstance(request, deployments_service.CreateUnitRequest):
            request = deployments_service.CreateUnitRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if unit is not None:
            request.unit = unit
        if unit_id is not None:
            request.unit_id = unit_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_unit
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

    async def update_unit(
        self,
        request: Optional[Union[deployments_service.UpdateUnitRequest, dict]] = None,
        *,
        unit: Optional[deployments_resources.Unit] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Unit:
        r"""Update a single unit.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_unit():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.UpdateUnitRequest(
                )

                # Make the request
                response = await client.update_unit(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateUnitRequest, dict]]):
                The request object. The request structure for the
                UpdateUnit method.
            unit (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit`):
                Required. The desired state for the
                unit.

                This corresponds to the ``unit`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the Unit resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the Unit will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit:
                A unit of deployment that has its
                lifecycle via a CRUD API using an
                actuation engine under the hood (e.g.
                based on Terraform, Helm or a custom
                implementation provided by a service
                producer). A building block of a SaaS
                Tenant.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [unit, update_mask]
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
        if not isinstance(request, deployments_service.UpdateUnitRequest):
            request = deployments_service.UpdateUnitRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if unit is not None:
            request.unit = unit
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_unit
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("unit.name", request.unit.name),)
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

    async def delete_unit(
        self,
        request: Optional[Union[deployments_service.DeleteUnitRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single unit.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_unit():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteUnitRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_unit(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteUnitRequest, dict]]):
                The request object. The request structure for the
                DeleteUnit method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
        if not isinstance(request, deployments_service.DeleteUnitRequest):
            request = deployments_service.DeleteUnitRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_unit
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

    async def list_unit_operations(
        self,
        request: Optional[
            Union[deployments_service.ListUnitOperationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUnitOperationsAsyncPager:
        r"""Retrieve a collection of unit operations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_unit_operations():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListUnitOperationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_unit_operations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsRequest, dict]]):
                The request object. The request structure for the
                ListUnitOperations method.
            parent (:class:`str`):
                Required. The parent of the unit
                operation.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments.pagers.ListUnitOperationsAsyncPager:
                The response structure for the
                ListUnitOperations method.
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
        if not isinstance(request, deployments_service.ListUnitOperationsRequest):
            request = deployments_service.ListUnitOperationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_unit_operations
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
        response = pagers.ListUnitOperationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_unit_operation(
        self,
        request: Optional[
            Union[deployments_service.GetUnitOperationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.UnitOperation:
        r"""Retrieve a single unit operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_unit_operation():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetUnitOperationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_unit_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetUnitOperationRequest, dict]]):
                The request object. The request structure for the
                GetUnitOperation method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation:
                UnitOperation encapsulates the intent
                of changing/interacting with the service
                component represented by the specific
                Unit. Multiple UnitOperations can be
                created (requested) and scheduled in the
                future, however only one will be allowed
                to execute at a time (that can change in
                the future for non-mutating operations).

                UnitOperations allow different actors
                interacting with the same unit to focus
                only on the change they have requested.

                This is a base object that contains the
                common fields in all unit operations.
                Next: 22

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
        if not isinstance(request, deployments_service.GetUnitOperationRequest):
            request = deployments_service.GetUnitOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_unit_operation
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

    async def create_unit_operation(
        self,
        request: Optional[
            Union[deployments_service.CreateUnitOperationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        unit_operation: Optional[deployments_resources.UnitOperation] = None,
        unit_operation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.UnitOperation:
        r"""Create a new unit operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_unit_operation():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                unit_operation = saasplatform_saasservicemgmt_v1beta1.UnitOperation()
                unit_operation.unit = "unit_value"

                request = saasplatform_saasservicemgmt_v1beta1.CreateUnitOperationRequest(
                    parent="parent_value",
                    unit_operation_id="unit_operation_id_value",
                    unit_operation=unit_operation,
                )

                # Make the request
                response = await client.create_unit_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateUnitOperationRequest, dict]]):
                The request object. The request structure for the
                CreateUnitOperation method.
            parent (:class:`str`):
                Required. The parent of the unit
                operation.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            unit_operation (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation`):
                Required. The desired state for the
                unit operation.

                This corresponds to the ``unit_operation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            unit_operation_id (:class:`str`):
                Required. The ID value for the new
                unit operation.

                This corresponds to the ``unit_operation_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation:
                UnitOperation encapsulates the intent
                of changing/interacting with the service
                component represented by the specific
                Unit. Multiple UnitOperations can be
                created (requested) and scheduled in the
                future, however only one will be allowed
                to execute at a time (that can change in
                the future for non-mutating operations).

                UnitOperations allow different actors
                interacting with the same unit to focus
                only on the change they have requested.

                This is a base object that contains the
                common fields in all unit operations.
                Next: 22

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, unit_operation, unit_operation_id]
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
        if not isinstance(request, deployments_service.CreateUnitOperationRequest):
            request = deployments_service.CreateUnitOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if unit_operation is not None:
            request.unit_operation = unit_operation
        if unit_operation_id is not None:
            request.unit_operation_id = unit_operation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_unit_operation
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

    async def update_unit_operation(
        self,
        request: Optional[
            Union[deployments_service.UpdateUnitOperationRequest, dict]
        ] = None,
        *,
        unit_operation: Optional[deployments_resources.UnitOperation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.UnitOperation:
        r"""Update a single unit operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_unit_operation():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                unit_operation = saasplatform_saasservicemgmt_v1beta1.UnitOperation()
                unit_operation.unit = "unit_value"

                request = saasplatform_saasservicemgmt_v1beta1.UpdateUnitOperationRequest(
                    unit_operation=unit_operation,
                )

                # Make the request
                response = await client.update_unit_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateUnitOperationRequest, dict]]):
                The request object. The request structure for the
                UpdateUnitOperation method.
            unit_operation (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation`):
                Required. The desired state for the
                unit operation.

                This corresponds to the ``unit_operation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the UnitOperation resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the UnitOperation will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UnitOperation:
                UnitOperation encapsulates the intent
                of changing/interacting with the service
                component represented by the specific
                Unit. Multiple UnitOperations can be
                created (requested) and scheduled in the
                future, however only one will be allowed
                to execute at a time (that can change in
                the future for non-mutating operations).

                UnitOperations allow different actors
                interacting with the same unit to focus
                only on the change they have requested.

                This is a base object that contains the
                common fields in all unit operations.
                Next: 22

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [unit_operation, update_mask]
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
        if not isinstance(request, deployments_service.UpdateUnitOperationRequest):
            request = deployments_service.UpdateUnitOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if unit_operation is not None:
            request.unit_operation = unit_operation
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_unit_operation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("unit_operation.name", request.unit_operation.name),)
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

    async def delete_unit_operation(
        self,
        request: Optional[
            Union[deployments_service.DeleteUnitOperationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single unit operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_unit_operation():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteUnitOperationRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_unit_operation(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteUnitOperationRequest, dict]]):
                The request object. The request structure for the
                DeleteUnitOperation method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
        if not isinstance(request, deployments_service.DeleteUnitOperationRequest):
            request = deployments_service.DeleteUnitOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_unit_operation
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

    async def list_releases(
        self,
        request: Optional[Union[deployments_service.ListReleasesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListReleasesAsyncPager:
        r"""Retrieve a collection of releases.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_releases():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListReleasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_releases(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesRequest, dict]]):
                The request object. The request structure for the
                ListReleases method.
            parent (:class:`str`):
                Required. The parent of the release.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_deployments.pagers.ListReleasesAsyncPager:
                The response structure for the
                ListReleases method.
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
        if not isinstance(request, deployments_service.ListReleasesRequest):
            request = deployments_service.ListReleasesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_releases
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
        response = pagers.ListReleasesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_release(
        self,
        request: Optional[Union[deployments_service.GetReleaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Release:
        r"""Retrieve a single release.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_release():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetReleaseRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_release(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetReleaseRequest, dict]]):
                The request object. The request structure for the
                GetRelease method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release:
                A new version to be propagated and
                deployed to units. This includes
                pointers to packaged blueprints for
                actuation (e.g Helm or Terraform
                configuration packages) via artifact
                registry.

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
        if not isinstance(request, deployments_service.GetReleaseRequest):
            request = deployments_service.GetReleaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_release
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

    async def create_release(
        self,
        request: Optional[Union[deployments_service.CreateReleaseRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        release: Optional[deployments_resources.Release] = None,
        release_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Release:
        r"""Create a new release.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_release():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                release = saasplatform_saasservicemgmt_v1beta1.Release()
                release.unit_kind = "unit_kind_value"

                request = saasplatform_saasservicemgmt_v1beta1.CreateReleaseRequest(
                    parent="parent_value",
                    release_id="release_id_value",
                    release=release,
                )

                # Make the request
                response = await client.create_release(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateReleaseRequest, dict]]):
                The request object. The request structure for the
                CreateRelease method.
            parent (:class:`str`):
                Required. The parent of the release.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            release (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release`):
                Required. The desired state for the
                release.

                This corresponds to the ``release`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            release_id (:class:`str`):
                Required. The ID value for the new
                release.

                This corresponds to the ``release_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release:
                A new version to be propagated and
                deployed to units. This includes
                pointers to packaged blueprints for
                actuation (e.g Helm or Terraform
                configuration packages) via artifact
                registry.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, release, release_id]
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
        if not isinstance(request, deployments_service.CreateReleaseRequest):
            request = deployments_service.CreateReleaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if release is not None:
            request.release = release
        if release_id is not None:
            request.release_id = release_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_release
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

    async def update_release(
        self,
        request: Optional[Union[deployments_service.UpdateReleaseRequest, dict]] = None,
        *,
        release: Optional[deployments_resources.Release] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployments_resources.Release:
        r"""Update a single release.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_release():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                release = saasplatform_saasservicemgmt_v1beta1.Release()
                release.unit_kind = "unit_kind_value"

                request = saasplatform_saasservicemgmt_v1beta1.UpdateReleaseRequest(
                    release=release,
                )

                # Make the request
                response = await client.update_release(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateReleaseRequest, dict]]):
                The request object. The request structure for the
                UpdateRelease method.
            release (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release`):
                Required. The desired state for the
                release.

                This corresponds to the ``release`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the Release resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the Release will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Release:
                A new version to be propagated and
                deployed to units. This includes
                pointers to packaged blueprints for
                actuation (e.g Helm or Terraform
                configuration packages) via artifact
                registry.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [release, update_mask]
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
        if not isinstance(request, deployments_service.UpdateReleaseRequest):
            request = deployments_service.UpdateReleaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if release is not None:
            request.release = release
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_release
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("release.name", request.release.name),)
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

    async def delete_release(
        self,
        request: Optional[Union[deployments_service.DeleteReleaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single release.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_release():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasDeploymentsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteReleaseRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_release(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteReleaseRequest, dict]]):
                The request object. The request structure for the
                DeleteRelease method.
            name (:class:`str`):
                Required. The resource name of the
                resource within a service.

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
        if not isinstance(request, deployments_service.DeleteReleaseRequest):
            request = deployments_service.DeleteReleaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_release
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

    async def get_location(
        self,
        request: Optional[Union[locations_pb2.GetLocationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.GetLocationRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.GetLocationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_location]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
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

    async def list_locations(
        self,
        request: Optional[Union[locations_pb2.ListLocationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.ListLocationsRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.ListLocationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_locations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
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

    async def __aenter__(self) -> "SaasDeploymentsAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SaasDeploymentsAsyncClient",)
