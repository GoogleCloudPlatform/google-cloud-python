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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts import (
    pagers,
)
from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import (
    rollouts_resources,
    rollouts_service,
)

from .client import SaasRolloutsClient
from .transports.base import DEFAULT_CLIENT_INFO, SaasRolloutsTransport
from .transports.grpc_asyncio import SaasRolloutsGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SaasRolloutsAsyncClient:
    """Manages the rollout of SaaS services."""

    _client: SaasRolloutsClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SaasRolloutsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SaasRolloutsClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SaasRolloutsClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SaasRolloutsClient._DEFAULT_UNIVERSE

    release_path = staticmethod(SaasRolloutsClient.release_path)
    parse_release_path = staticmethod(SaasRolloutsClient.parse_release_path)
    rollout_path = staticmethod(SaasRolloutsClient.rollout_path)
    parse_rollout_path = staticmethod(SaasRolloutsClient.parse_rollout_path)
    rollout_kind_path = staticmethod(SaasRolloutsClient.rollout_kind_path)
    parse_rollout_kind_path = staticmethod(SaasRolloutsClient.parse_rollout_kind_path)
    unit_kind_path = staticmethod(SaasRolloutsClient.unit_kind_path)
    parse_unit_kind_path = staticmethod(SaasRolloutsClient.parse_unit_kind_path)
    common_billing_account_path = staticmethod(
        SaasRolloutsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SaasRolloutsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SaasRolloutsClient.common_folder_path)
    parse_common_folder_path = staticmethod(SaasRolloutsClient.parse_common_folder_path)
    common_organization_path = staticmethod(SaasRolloutsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        SaasRolloutsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(SaasRolloutsClient.common_project_path)
    parse_common_project_path = staticmethod(
        SaasRolloutsClient.parse_common_project_path
    )
    common_location_path = staticmethod(SaasRolloutsClient.common_location_path)
    parse_common_location_path = staticmethod(
        SaasRolloutsClient.parse_common_location_path
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
            SaasRolloutsAsyncClient: The constructed client.
        """
        sa_info_func = (
            SaasRolloutsClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SaasRolloutsAsyncClient, info, *args, **kwargs)

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
            SaasRolloutsAsyncClient: The constructed client.
        """
        sa_file_func = (
            SaasRolloutsClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(SaasRolloutsAsyncClient, filename, *args, **kwargs)

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
        return SaasRolloutsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> SaasRolloutsTransport:
        """Returns the transport used by the client instance.

        Returns:
            SaasRolloutsTransport: The transport used by the client instance.
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

    get_transport_class = SaasRolloutsClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, SaasRolloutsTransport, Callable[..., SaasRolloutsTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the saas rollouts async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SaasRolloutsTransport,Callable[..., SaasRolloutsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SaasRolloutsTransport constructor.
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
        self._client = SaasRolloutsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
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
                    "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                    "credentialsType": None,
                },
            )

    async def list_rollouts(
        self,
        request: Optional[Union[rollouts_service.ListRolloutsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRolloutsAsyncPager:
        r"""Retrieve a collection of rollouts.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_rollouts():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListRolloutsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_rollouts(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutsRequest, dict]]):
                The request object. The request structure for the
                ListRollouts method.
            parent (:class:`str`):
                Required. The parent of the rollout.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutsAsyncPager:
                The response structure for the
                ListRollouts method.
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
        if not isinstance(request, rollouts_service.ListRolloutsRequest):
            request = rollouts_service.ListRolloutsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_rollouts
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
        response = pagers.ListRolloutsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_rollout(
        self,
        request: Optional[Union[rollouts_service.GetRolloutRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> rollouts_resources.Rollout:
        r"""Retrieve a single rollout.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_rollout():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetRolloutRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_rollout(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutRequest, dict]]):
                The request object. The request structure for the
                GetRollout method.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout:
                Represents a single rollout execution
                and its results

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
        if not isinstance(request, rollouts_service.GetRolloutRequest):
            request = rollouts_service.GetRolloutRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_rollout
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

    async def create_rollout(
        self,
        request: Optional[Union[rollouts_service.CreateRolloutRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        rollout: Optional[rollouts_resources.Rollout] = None,
        rollout_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> rollouts_resources.Rollout:
        r"""Create a new rollout.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_rollout():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                rollout = saasplatform_saasservicemgmt_v1beta1.Rollout()
                rollout.rollout_kind = "rollout_kind_value"

                request = saasplatform_saasservicemgmt_v1beta1.CreateRolloutRequest(
                    parent="parent_value",
                    rollout_id="rollout_id_value",
                    rollout=rollout,
                )

                # Make the request
                response = await client.create_rollout(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutRequest, dict]]):
                The request object. The request structure for the
                CreateRollout method.
            parent (:class:`str`):
                Required. The parent of the rollout.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            rollout (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout`):
                Required. The desired state for the
                rollout.

                This corresponds to the ``rollout`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            rollout_id (:class:`str`):
                Required. The ID value for the new
                rollout.

                This corresponds to the ``rollout_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout:
                Represents a single rollout execution
                and its results

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, rollout, rollout_id]
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
        if not isinstance(request, rollouts_service.CreateRolloutRequest):
            request = rollouts_service.CreateRolloutRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if rollout is not None:
            request.rollout = rollout
        if rollout_id is not None:
            request.rollout_id = rollout_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_rollout
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

    async def update_rollout(
        self,
        request: Optional[Union[rollouts_service.UpdateRolloutRequest, dict]] = None,
        *,
        rollout: Optional[rollouts_resources.Rollout] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> rollouts_resources.Rollout:
        r"""Update a single rollout.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_rollout():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                rollout = saasplatform_saasservicemgmt_v1beta1.Rollout()
                rollout.rollout_kind = "rollout_kind_value"

                request = saasplatform_saasservicemgmt_v1beta1.UpdateRolloutRequest(
                    rollout=rollout,
                )

                # Make the request
                response = await client.update_rollout(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutRequest, dict]]):
                The request object. The request structure for the
                UpdateRollout method.
            rollout (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout`):
                Required. The desired state for the
                rollout.

                This corresponds to the ``rollout`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the Rollout resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the Rollout will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout:
                Represents a single rollout execution
                and its results

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [rollout, update_mask]
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
        if not isinstance(request, rollouts_service.UpdateRolloutRequest):
            request = rollouts_service.UpdateRolloutRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if rollout is not None:
            request.rollout = rollout
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_rollout
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("rollout.name", request.rollout.name),)
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

    async def delete_rollout(
        self,
        request: Optional[Union[rollouts_service.DeleteRolloutRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single rollout.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_rollout():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteRolloutRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_rollout(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutRequest, dict]]):
                The request object. The request structure for the
                DeleteRollout method.
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
        if not isinstance(request, rollouts_service.DeleteRolloutRequest):
            request = rollouts_service.DeleteRolloutRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_rollout
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

    async def list_rollout_kinds(
        self,
        request: Optional[Union[rollouts_service.ListRolloutKindsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRolloutKindsAsyncPager:
        r"""Retrieve a collection of rollout kinds.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_list_rollout_kinds():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.ListRolloutKindsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_rollout_kinds(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutKindsRequest, dict]]):
                The request object. The request structure for the
                ListRolloutKinds method.
            parent (:class:`str`):
                Required. The parent of the rollout
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutKindsAsyncPager:
                The response structure for the
                ListRolloutKinds method.
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
        if not isinstance(request, rollouts_service.ListRolloutKindsRequest):
            request = rollouts_service.ListRolloutKindsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_rollout_kinds
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
        response = pagers.ListRolloutKindsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_rollout_kind(
        self,
        request: Optional[Union[rollouts_service.GetRolloutKindRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> rollouts_resources.RolloutKind:
        r"""Retrieve a single rollout kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_get_rollout_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.GetRolloutKindRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_rollout_kind(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutKindRequest, dict]]):
                The request object. The request structure for the
                GetRolloutKind method.
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind:
                An object that describes various
                settings of Rollout execution. Includes
                built-in policies across GCP and GDC,
                and customizable policies.

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
        if not isinstance(request, rollouts_service.GetRolloutKindRequest):
            request = rollouts_service.GetRolloutKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_rollout_kind
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

    async def create_rollout_kind(
        self,
        request: Optional[
            Union[rollouts_service.CreateRolloutKindRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        rollout_kind: Optional[rollouts_resources.RolloutKind] = None,
        rollout_kind_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> rollouts_resources.RolloutKind:
        r"""Create a new rollout kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_create_rollout_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                rollout_kind = saasplatform_saasservicemgmt_v1beta1.RolloutKind()
                rollout_kind.unit_kind = "unit_kind_value"

                request = saasplatform_saasservicemgmt_v1beta1.CreateRolloutKindRequest(
                    parent="parent_value",
                    rollout_kind_id="rollout_kind_id_value",
                    rollout_kind=rollout_kind,
                )

                # Make the request
                response = await client.create_rollout_kind(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutKindRequest, dict]]):
                The request object. The request structure for the
                CreateRolloutKind method.
            parent (:class:`str`):
                Required. The parent of the rollout
                kind.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            rollout_kind (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind`):
                Required. The desired state for the
                rollout kind.

                This corresponds to the ``rollout_kind`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            rollout_kind_id (:class:`str`):
                Required. The ID value for the new
                rollout kind.

                This corresponds to the ``rollout_kind_id`` field
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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind:
                An object that describes various
                settings of Rollout execution. Includes
                built-in policies across GCP and GDC,
                and customizable policies.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, rollout_kind, rollout_kind_id]
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
        if not isinstance(request, rollouts_service.CreateRolloutKindRequest):
            request = rollouts_service.CreateRolloutKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if rollout_kind is not None:
            request.rollout_kind = rollout_kind
        if rollout_kind_id is not None:
            request.rollout_kind_id = rollout_kind_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_rollout_kind
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

    async def update_rollout_kind(
        self,
        request: Optional[
            Union[rollouts_service.UpdateRolloutKindRequest, dict]
        ] = None,
        *,
        rollout_kind: Optional[rollouts_resources.RolloutKind] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> rollouts_resources.RolloutKind:
        r"""Update a single rollout kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_update_rollout_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                rollout_kind = saasplatform_saasservicemgmt_v1beta1.RolloutKind()
                rollout_kind.unit_kind = "unit_kind_value"

                request = saasplatform_saasservicemgmt_v1beta1.UpdateRolloutKindRequest(
                    rollout_kind=rollout_kind,
                )

                # Make the request
                response = await client.update_rollout_kind(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutKindRequest, dict]]):
                The request object. The request structure for the
                UpdateRolloutKind method.
            rollout_kind (:class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind`):
                Required. The desired state for the
                rollout kind.

                This corresponds to the ``rollout_kind`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Field mask is used to specify the fields to be
                overwritten in the RolloutKind resource by the update.

                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask.

                If the user does not provide a mask then all fields in
                the RolloutKind will be overwritten.

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
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind:
                An object that describes various
                settings of Rollout execution. Includes
                built-in policies across GCP and GDC,
                and customizable policies.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [rollout_kind, update_mask]
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
        if not isinstance(request, rollouts_service.UpdateRolloutKindRequest):
            request = rollouts_service.UpdateRolloutKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if rollout_kind is not None:
            request.rollout_kind = rollout_kind
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_rollout_kind
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("rollout_kind.name", request.rollout_kind.name),)
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

    async def delete_rollout_kind(
        self,
        request: Optional[
            Union[rollouts_service.DeleteRolloutKindRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a single rollout kind.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import saasplatform_saasservicemgmt_v1beta1

            async def sample_delete_rollout_kind():
                # Create a client
                client = saasplatform_saasservicemgmt_v1beta1.SaasRolloutsAsyncClient()

                # Initialize request argument(s)
                request = saasplatform_saasservicemgmt_v1beta1.DeleteRolloutKindRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_rollout_kind(request=request)

        Args:
            request (Optional[Union[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutKindRequest, dict]]):
                The request object. The request structure for the
                DeleteRolloutKind method.
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
        if not isinstance(request, rollouts_service.DeleteRolloutKindRequest):
            request = rollouts_service.DeleteRolloutKindRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_rollout_kind
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

    async def __aenter__(self) -> "SaasRolloutsAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SaasRolloutsAsyncClient",)
