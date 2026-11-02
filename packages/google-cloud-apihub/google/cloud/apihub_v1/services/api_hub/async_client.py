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

from google.cloud.apihub_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.apihub_v1.services.api_hub import pagers
from google.cloud.apihub_v1.types import apihub_service, common_fields

from .client import ApiHubClient
from .transports.base import DEFAULT_CLIENT_INFO, ApiHubTransport
from .transports.grpc_asyncio import ApiHubGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ApiHubAsyncClient:
    """This service provides all methods related to the API hub."""

    _client: ApiHubClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ApiHubClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ApiHubClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ApiHubClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ApiHubClient._DEFAULT_UNIVERSE

    api_path = staticmethod(ApiHubClient.api_path)
    parse_api_path = staticmethod(ApiHubClient.parse_api_path)
    api_operation_path = staticmethod(ApiHubClient.api_operation_path)
    parse_api_operation_path = staticmethod(ApiHubClient.parse_api_operation_path)
    attribute_path = staticmethod(ApiHubClient.attribute_path)
    parse_attribute_path = staticmethod(ApiHubClient.parse_attribute_path)
    definition_path = staticmethod(ApiHubClient.definition_path)
    parse_definition_path = staticmethod(ApiHubClient.parse_definition_path)
    deployment_path = staticmethod(ApiHubClient.deployment_path)
    parse_deployment_path = staticmethod(ApiHubClient.parse_deployment_path)
    external_api_path = staticmethod(ApiHubClient.external_api_path)
    parse_external_api_path = staticmethod(ApiHubClient.parse_external_api_path)
    plugin_instance_path = staticmethod(ApiHubClient.plugin_instance_path)
    parse_plugin_instance_path = staticmethod(ApiHubClient.parse_plugin_instance_path)
    spec_path = staticmethod(ApiHubClient.spec_path)
    parse_spec_path = staticmethod(ApiHubClient.parse_spec_path)
    version_path = staticmethod(ApiHubClient.version_path)
    parse_version_path = staticmethod(ApiHubClient.parse_version_path)
    common_billing_account_path = staticmethod(ApiHubClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(
        ApiHubClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ApiHubClient.common_folder_path)
    parse_common_folder_path = staticmethod(ApiHubClient.parse_common_folder_path)
    common_organization_path = staticmethod(ApiHubClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        ApiHubClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ApiHubClient.common_project_path)
    parse_common_project_path = staticmethod(ApiHubClient.parse_common_project_path)
    common_location_path = staticmethod(ApiHubClient.common_location_path)
    parse_common_location_path = staticmethod(ApiHubClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ApiHubAsyncClient: The constructed client.
        """
        sa_info_func = (
            ApiHubClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ApiHubAsyncClient, info, *args, **kwargs)

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
            ApiHubAsyncClient: The constructed client.
        """
        sa_file_func = (
            ApiHubClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(ApiHubAsyncClient, filename, *args, **kwargs)

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
        return ApiHubClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ApiHubTransport:
        """Returns the transport used by the client instance.

        Returns:
            ApiHubTransport: The transport used by the client instance.
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

    get_transport_class = ApiHubClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, ApiHubTransport, Callable[..., ApiHubTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the api hub async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ApiHubTransport,Callable[..., ApiHubTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ApiHubTransport constructor.
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
        self._client = ApiHubClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.apihub_v1.ApiHubAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.apihub.v1.ApiHub",
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
                    "serviceName": "google.cloud.apihub.v1.ApiHub",
                    "credentialsType": None,
                },
            )

    async def create_api(
        self,
        request: Optional[Union[apihub_service.CreateApiRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        api: Optional[common_fields.Api] = None,
        api_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Api:
        r"""Create an API resource in the API hub.
        Once an API resource is created, versions can be added
        to it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                api = apihub_v1.Api()
                api.display_name = "display_name_value"

                request = apihub_v1.CreateApiRequest(
                    parent="parent_value",
                    api=api,
                )

                # Make the request
                response = await client.create_api(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateApiRequest, dict]]):
                The request object. The [CreateApi][google.cloud.apihub.v1.ApiHub.CreateApi]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for the API resource.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            api (:class:`google.cloud.apihub_v1.types.Api`):
                Required. The API resource to create.
                This corresponds to the ``api`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            api_id (:class:`str`):
                Optional. The ID to use for the API resource, which will
                become the final component of the API's resource name.
                This field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another API resource in the API hub.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``api_id`` field
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
            google.cloud.apihub_v1.types.Api:
                An API resource in the API Hub.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, api, api_id]
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
        if not isinstance(request, apihub_service.CreateApiRequest):
            request = apihub_service.CreateApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if api is not None:
            request.api = api
        if api_id is not None:
            request.api_id = api_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_api
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

    async def get_api(
        self,
        request: Optional[Union[apihub_service.GetApiRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Api:
        r"""Get API resource details including the API versions
        contained in it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetApiRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_api(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetApiRequest, dict]]):
                The request object. The [GetApi][google.cloud.apihub.v1.ApiHub.GetApi]
                method's request.
            name (:class:`str`):
                Required. The name of the API resource to retrieve.
                Format:
                ``projects/{project}/locations/{location}/apis/{api}``

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
            google.cloud.apihub_v1.types.Api:
                An API resource in the API Hub.
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
        if not isinstance(request, apihub_service.GetApiRequest):
            request = apihub_service.GetApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_api]

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

    async def list_apis(
        self,
        request: Optional[Union[apihub_service.ListApisRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApisAsyncPager:
        r"""List API resources in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_apis():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListApisRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_apis(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListApisRequest, dict]]):
                The request object. The [ListApis][google.cloud.apihub.v1.ApiHub.ListApis]
                method's request.
            parent (:class:`str`):
                Required. The parent, which owns this collection of API
                resources. Format:
                ``projects/{project}/locations/{location}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager:
                The [ListApis][google.cloud.apihub.v1.ApiHub.ListApis]
                method's response.

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
        if not isinstance(request, apihub_service.ListApisRequest):
            request = apihub_service.ListApisRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_apis
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
        response = pagers.ListApisAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_api(
        self,
        request: Optional[Union[apihub_service.UpdateApiRequest, dict]] = None,
        *,
        api: Optional[common_fields.Api] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Api:
        r"""Update an API resource in the API hub. The following fields in
        the [API][google.cloud.apihub.v1.Api] can be updated:

        - [display_name][google.cloud.apihub.v1.Api.display_name]
        - [description][google.cloud.apihub.v1.Api.description]
        - [owner][google.cloud.apihub.v1.Api.owner]
        - [documentation][google.cloud.apihub.v1.Api.documentation]
        - [target_user][google.cloud.apihub.v1.Api.target_user]
        - [team][google.cloud.apihub.v1.Api.team]
        - [business_unit][google.cloud.apihub.v1.Api.business_unit]
        - [maturity_level][google.cloud.apihub.v1.Api.maturity_level]
        - [api_style][google.cloud.apihub.v1.Api.api_style]
        - [attributes][google.cloud.apihub.v1.Api.attributes]

        The
        [update_mask][google.cloud.apihub.v1.UpdateApiRequest.update_mask]
        should be used to specify the fields being updated.

        Updating the owner field requires complete owner message and
        updates both owner and email fields.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                api = apihub_v1.Api()
                api.display_name = "display_name_value"

                request = apihub_v1.UpdateApiRequest(
                    api=api,
                )

                # Make the request
                response = await client.update_api(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateApiRequest, dict]]):
                The request object. The [UpdateApi][google.cloud.apihub.v1.ApiHub.UpdateApi]
                method's request.
            api (:class:`google.cloud.apihub_v1.types.Api`):
                Required. The API resource to update.

                The API resource's ``name`` field is used to identify
                the API resource to update. Format:
                ``projects/{project}/locations/{location}/apis/{api}``

                This corresponds to the ``api`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.Api:
                An API resource in the API Hub.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [api, update_mask]
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
        if not isinstance(request, apihub_service.UpdateApiRequest):
            request = apihub_service.UpdateApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if api is not None:
            request.api = api
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_api
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("api.name", request.api.name),)),
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

    async def delete_api(
        self,
        request: Optional[Union[apihub_service.DeleteApiRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete an API resource in the API hub. API can only
        be deleted if all underlying versions are deleted.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteApiRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_api(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteApiRequest, dict]]):
                The request object. The [DeleteApi][google.cloud.apihub.v1.ApiHub.DeleteApi]
                method's request.
            name (:class:`str`):
                Required. The name of the API resource to delete.
                Format:
                ``projects/{project}/locations/{location}/apis/{api}``

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
        if not isinstance(request, apihub_service.DeleteApiRequest):
            request = apihub_service.DeleteApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_api
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

    async def create_version(
        self,
        request: Optional[Union[apihub_service.CreateVersionRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        version: Optional[common_fields.Version] = None,
        version_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Version:
        r"""Create an API version for an API resource in the API
        hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_version():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                version = apihub_v1.Version()
                version.display_name = "display_name_value"

                request = apihub_v1.CreateVersionRequest(
                    parent="parent_value",
                    version=version,
                )

                # Make the request
                response = await client.create_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateVersionRequest, dict]]):
                The request object. The
                [CreateVersion][google.cloud.apihub.v1.ApiHub.CreateVersion]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for API version. Format:
                ``projects/{project}/locations/{location}/apis/{api}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            version (:class:`google.cloud.apihub_v1.types.Version`):
                Required. The version to create.
                This corresponds to the ``version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            version_id (:class:`str`):
                Optional. The ID to use for the API version, which will
                become the final component of the version's resource
                name. This field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another version in the API resource.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, overall resource
                name which will be of format
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``,
                its length is limited to 700 characters and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``version_id`` field
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
            google.cloud.apihub_v1.types.Version:
                Represents a version of the API
                resource in API hub. This is also
                referred to as the API version.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, version, version_id]
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
        if not isinstance(request, apihub_service.CreateVersionRequest):
            request = apihub_service.CreateVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if version is not None:
            request.version = version
        if version_id is not None:
            request.version_id = version_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_version
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

    async def get_version(
        self,
        request: Optional[Union[apihub_service.GetVersionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Version:
        r"""Get details about the API version of an API resource.
        This will include information about the specs and
        operations present in the API version as well as the
        deployments linked to it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_version():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetVersionRequest, dict]]):
                The request object. The
                [GetVersion][google.cloud.apihub.v1.ApiHub.GetVersion]
                method's request.
            name (:class:`str`):
                Required. The name of the API version to retrieve.
                Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

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
            google.cloud.apihub_v1.types.Version:
                Represents a version of the API
                resource in API hub. This is also
                referred to as the API version.

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
        if not isinstance(request, apihub_service.GetVersionRequest):
            request = apihub_service.GetVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_version
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

    async def list_versions(
        self,
        request: Optional[Union[apihub_service.ListVersionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListVersionsAsyncPager:
        r"""List API versions of an API resource in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_versions():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_versions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListVersionsRequest, dict]]):
                The request object. The
                [ListVersions][google.cloud.apihub.v1.ApiHub.ListVersions]
                method's request.
            parent (:class:`str`):
                Required. The parent which owns this collection of API
                versions i.e., the API resource Format:
                ``projects/{project}/locations/{location}/apis/{api}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager:
                The [ListVersions][google.cloud.apihub.v1.ApiHub.ListVersions] method's
                   response.

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
        if not isinstance(request, apihub_service.ListVersionsRequest):
            request = apihub_service.ListVersionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_versions
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
        response = pagers.ListVersionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_version(
        self,
        request: Optional[Union[apihub_service.UpdateVersionRequest, dict]] = None,
        *,
        version: Optional[common_fields.Version] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Version:
        r"""Update API version. The following fields in the
        [version][google.cloud.apihub.v1.Version] can be updated
        currently:

        - [display_name][google.cloud.apihub.v1.Version.display_name]
        - [description][google.cloud.apihub.v1.Version.description]
        - [documentation][google.cloud.apihub.v1.Version.documentation]
        - [deployments][google.cloud.apihub.v1.Version.deployments]
        - [lifecycle][google.cloud.apihub.v1.Version.lifecycle]
        - [compliance][google.cloud.apihub.v1.Version.compliance]
        - [accreditation][google.cloud.apihub.v1.Version.accreditation]
        - [attributes][google.cloud.apihub.v1.Version.attributes]

        The
        [update_mask][google.cloud.apihub.v1.UpdateVersionRequest.update_mask]
        should be used to specify the fields being updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_version():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                version = apihub_v1.Version()
                version.display_name = "display_name_value"

                request = apihub_v1.UpdateVersionRequest(
                    version=version,
                )

                # Make the request
                response = await client.update_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateVersionRequest, dict]]):
                The request object. The
                [UpdateVersion][google.cloud.apihub.v1.ApiHub.UpdateVersion]
                method's request.
            version (:class:`google.cloud.apihub_v1.types.Version`):
                Required. The API version to update.

                The version's ``name`` field is used to identify the API
                version to update. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

                This corresponds to the ``version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.Version:
                Represents a version of the API
                resource in API hub. This is also
                referred to as the API version.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [version, update_mask]
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
        if not isinstance(request, apihub_service.UpdateVersionRequest):
            request = apihub_service.UpdateVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if version is not None:
            request.version = version
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_version
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("version.name", request.version.name),)
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

    async def delete_version(
        self,
        request: Optional[Union[apihub_service.DeleteVersionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete an API version. Version can only be deleted if
        all underlying specs, operations, definitions and linked
        deployments are deleted.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_version():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteVersionRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_version(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteVersionRequest, dict]]):
                The request object. The
                [DeleteVersion][google.cloud.apihub.v1.ApiHub.DeleteVersion]
                method's request.
            name (:class:`str`):
                Required. The name of the version to delete. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

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
        if not isinstance(request, apihub_service.DeleteVersionRequest):
            request = apihub_service.DeleteVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_version
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

    async def create_spec(
        self,
        request: Optional[Union[apihub_service.CreateSpecRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        spec: Optional[common_fields.Spec] = None,
        spec_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Spec:
        r"""Add a spec to an API version in the API hub. Multiple specs can
        be added to an API version. Note, while adding a spec, at least
        one of ``contents`` or ``source_uri`` must be provided. If
        ``contents`` is provided, then ``spec_type`` must also be
        provided.

        On adding a spec with contents to the version, the operations
        present in it will be added to the version.Note that the file
        contents in the spec should be of the same type as defined in
        the
        ``projects/{project}/locations/{location}/attributes/system-spec-type``
        attribute associated with spec resource. Note that specs of
        various types can be uploaded, however parsing of details is
        supported for OpenAPI spec currently.

        In order to access the information parsed from the spec, use the
        [GetSpec][google.cloud.apihub.v1.ApiHub.GetSpec] method. In
        order to access the raw contents for a particular spec, use the
        [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
        method. In order to access the operations parsed from the spec,
        use the
        [ListAPIOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
        method.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_spec():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                spec = apihub_v1.Spec()
                spec.display_name = "display_name_value"
                spec.spec_type.enum_values.values.id = "id_value"
                spec.spec_type.enum_values.values.display_name = "display_name_value"

                request = apihub_v1.CreateSpecRequest(
                    parent="parent_value",
                    spec=spec,
                )

                # Make the request
                response = await client.create_spec(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateSpecRequest, dict]]):
                The request object. The
                [CreateSpec][google.cloud.apihub.v1.ApiHub.CreateSpec]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for Spec. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            spec (:class:`google.cloud.apihub_v1.types.Spec`):
                Required. The spec to create.
                This corresponds to the ``spec`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            spec_id (:class:`str`):
                Optional. The ID to use for the spec, which will become
                the final component of the spec's resource name. This
                field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another spec in the API resource.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, overall resource
                name which will be of format
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``,
                its length is limited to 1000 characters and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``spec_id`` field
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
            google.cloud.apihub_v1.types.Spec:
                Represents a spec associated with an
                API version in the API Hub. Note that
                specs of various types can be uploaded,
                however parsing of details is supported
                for OpenAPI spec currently.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, spec, spec_id]
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
        if not isinstance(request, apihub_service.CreateSpecRequest):
            request = apihub_service.CreateSpecRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if spec is not None:
            request.spec = spec
        if spec_id is not None:
            request.spec_id = spec_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_spec
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

    async def get_spec(
        self,
        request: Optional[Union[apihub_service.GetSpecRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Spec:
        r"""Get details about the information parsed from a spec. Note that
        this method does not return the raw spec contents. Use
        [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
        method to retrieve the same.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_spec():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetSpecRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_spec(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetSpecRequest, dict]]):
                The request object. The [GetSpec][google.cloud.apihub.v1.ApiHub.GetSpec]
                method's request.
            name (:class:`str`):
                Required. The name of the spec to retrieve. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``

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
            google.cloud.apihub_v1.types.Spec:
                Represents a spec associated with an
                API version in the API Hub. Note that
                specs of various types can be uploaded,
                however parsing of details is supported
                for OpenAPI spec currently.

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
        if not isinstance(request, apihub_service.GetSpecRequest):
            request = apihub_service.GetSpecRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_spec]

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

    async def get_spec_contents(
        self,
        request: Optional[Union[apihub_service.GetSpecContentsRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.SpecContents:
        r"""Get spec contents.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_spec_contents():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetSpecContentsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_spec_contents(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetSpecContentsRequest, dict]]):
                The request object. The
                [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
                method's request.
            name (:class:`str`):
                Required. The name of the spec whose contents need to be
                retrieved. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``

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
            google.cloud.apihub_v1.types.SpecContents:
                The spec contents.
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
        if not isinstance(request, apihub_service.GetSpecContentsRequest):
            request = apihub_service.GetSpecContentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_spec_contents
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

    async def list_specs(
        self,
        request: Optional[Union[apihub_service.ListSpecsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSpecsAsyncPager:
        r"""List specs corresponding to a particular API
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_specs():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListSpecsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_specs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListSpecsRequest, dict]]):
                The request object. The [ListSpecs][ListSpecs] method's request.
            parent (:class:`str`):
                Required. The parent, which owns this collection of
                specs. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager:
                The [ListSpecs][google.cloud.apihub.v1.ApiHub.ListSpecs]
                method's response.

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
        if not isinstance(request, apihub_service.ListSpecsRequest):
            request = apihub_service.ListSpecsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_specs
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
        response = pagers.ListSpecsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_spec(
        self,
        request: Optional[Union[apihub_service.UpdateSpecRequest, dict]] = None,
        *,
        spec: Optional[common_fields.Spec] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Spec:
        r"""Update spec. The following fields in the
        [spec][google.cloud.apihub.v1.Spec] can be updated:

        - [display_name][google.cloud.apihub.v1.Spec.display_name]
        - [source_uri][google.cloud.apihub.v1.Spec.source_uri]
        - [lint_response][google.cloud.apihub.v1.Spec.lint_response]
        - [attributes][google.cloud.apihub.v1.Spec.attributes]
        - [contents][google.cloud.apihub.v1.Spec.contents]
        - [spec_type][google.cloud.apihub.v1.Spec.spec_type]

        In case of an OAS spec, updating spec contents can lead to:

        1. Creation, deletion and update of operations.
        2. Creation, deletion and update of definitions.
        3. Update of other info parsed out from the new spec.

        In case of contents or source_uri being present in update mask,
        spec_type must also be present. Also, spec_type can not be
        present in update mask if contents or source_uri is not present.

        The
        [update_mask][google.cloud.apihub.v1.UpdateSpecRequest.update_mask]
        should be used to specify the fields being updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_spec():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                spec = apihub_v1.Spec()
                spec.display_name = "display_name_value"
                spec.spec_type.enum_values.values.id = "id_value"
                spec.spec_type.enum_values.values.display_name = "display_name_value"

                request = apihub_v1.UpdateSpecRequest(
                    spec=spec,
                )

                # Make the request
                response = await client.update_spec(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateSpecRequest, dict]]):
                The request object. The
                [UpdateSpec][google.cloud.apihub.v1.ApiHub.UpdateSpec]
                method's request.
            spec (:class:`google.cloud.apihub_v1.types.Spec`):
                Required. The spec to update.

                The spec's ``name`` field is used to identify the spec
                to update. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``

                This corresponds to the ``spec`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.Spec:
                Represents a spec associated with an
                API version in the API Hub. Note that
                specs of various types can be uploaded,
                however parsing of details is supported
                for OpenAPI spec currently.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [spec, update_mask]
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
        if not isinstance(request, apihub_service.UpdateSpecRequest):
            request = apihub_service.UpdateSpecRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if spec is not None:
            request.spec = spec
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_spec
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("spec.name", request.spec.name),)
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

    async def delete_spec(
        self,
        request: Optional[Union[apihub_service.DeleteSpecRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a spec.
        Deleting a spec will also delete the associated
        operations from the version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_spec():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteSpecRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_spec(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteSpecRequest, dict]]):
                The request object. The
                [DeleteSpec][google.cloud.apihub.v1.ApiHub.DeleteSpec]
                method's request.
            name (:class:`str`):
                Required. The name of the spec to delete. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``

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
        if not isinstance(request, apihub_service.DeleteSpecRequest):
            request = apihub_service.DeleteSpecRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_spec
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

    async def create_api_operation(
        self,
        request: Optional[Union[apihub_service.CreateApiOperationRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        api_operation: Optional[common_fields.ApiOperation] = None,
        api_operation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.ApiOperation:
        r"""Create an apiOperation in an API version.
        An apiOperation can be created only if the version has
        no apiOperations which were created by parsing a spec.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_api_operation():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.CreateApiOperationRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_api_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateApiOperationRequest, dict]]):
                The request object. The
                [CreateApiOperation][google.cloud.apihub.v1.ApiHub.CreateApiOperation]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for the operation
                resource. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            api_operation (:class:`google.cloud.apihub_v1.types.ApiOperation`):
                Required. The operation resource to
                create.

                This corresponds to the ``api_operation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            api_operation_id (:class:`str`):
                Optional. The ID to use for the operation resource,
                which will become the final component of the operation's
                resource name. This field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another operation resource in the API hub.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, overall resource
                name which will be of format
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``,
                its length is limited to 700 characters, and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``api_operation_id`` field
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
            google.cloud.apihub_v1.types.ApiOperation:
                Represents an operation contained in
                an API version in the API Hub. An
                operation is added/updated/deleted in an
                API version when a new spec is added or
                an existing spec is updated/deleted in a
                version. Currently, an operation will be
                created only corresponding to OpenAPI
                spec as parsing is supported for OpenAPI
                spec.
                Alternatively operations can be managed
                via create,update and delete APIs,
                creation of apiOperation can be possible
                only for version with no parsed
                operations and update/delete can be
                possible only for operations created via
                create API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, api_operation, api_operation_id]
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
        if not isinstance(request, apihub_service.CreateApiOperationRequest):
            request = apihub_service.CreateApiOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if api_operation is not None:
            request.api_operation = api_operation
        if api_operation_id is not None:
            request.api_operation_id = api_operation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_api_operation
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

    async def get_api_operation(
        self,
        request: Optional[Union[apihub_service.GetApiOperationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.ApiOperation:
        r"""Get details about a particular operation in API
        version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_api_operation():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetApiOperationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_api_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetApiOperationRequest, dict]]):
                The request object. The
                [GetApiOperation][google.cloud.apihub.v1.ApiHub.GetApiOperation]
                method's request.
            name (:class:`str`):
                Required. The name of the operation to retrieve. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``

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
            google.cloud.apihub_v1.types.ApiOperation:
                Represents an operation contained in
                an API version in the API Hub. An
                operation is added/updated/deleted in an
                API version when a new spec is added or
                an existing spec is updated/deleted in a
                version. Currently, an operation will be
                created only corresponding to OpenAPI
                spec as parsing is supported for OpenAPI
                spec.
                Alternatively operations can be managed
                via create,update and delete APIs,
                creation of apiOperation can be possible
                only for version with no parsed
                operations and update/delete can be
                possible only for operations created via
                create API.

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
        if not isinstance(request, apihub_service.GetApiOperationRequest):
            request = apihub_service.GetApiOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_api_operation
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

    async def list_api_operations(
        self,
        request: Optional[Union[apihub_service.ListApiOperationsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApiOperationsAsyncPager:
        r"""List operations in an API version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_api_operations():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListApiOperationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_api_operations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListApiOperationsRequest, dict]]):
                The request object. The
                [ListApiOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
                method's request.
            parent (:class:`str`):
                Required. The parent which owns this collection of
                operations i.e., the API version. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager:
                The [ListApiOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
                   method's response.

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
        if not isinstance(request, apihub_service.ListApiOperationsRequest):
            request = apihub_service.ListApiOperationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_api_operations
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
        response = pagers.ListApiOperationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_api_operation(
        self,
        request: Optional[Union[apihub_service.UpdateApiOperationRequest, dict]] = None,
        *,
        api_operation: Optional[common_fields.ApiOperation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.ApiOperation:
        r"""Update an operation in an API version. The following fields in
        the [ApiOperation resource][google.cloud.apihub.v1.ApiOperation]
        can be updated:

        - [details.description][ApiOperation.details.description]
        - [details.documentation][ApiOperation.details.documentation]
        - [details.http_operation.path][ApiOperation.details.http_operation.path.path]
        - [details.http_operation.method][ApiOperation.details.http_operation.method]
        - [details.deprecated][ApiOperation.details.deprecated]
        - [attributes][google.cloud.apihub.v1.ApiOperation.attributes]

        The
        [update_mask][google.cloud.apihub.v1.UpdateApiOperationRequest.update_mask]
        should be used to specify the fields being updated.

        An operation can be updated only if the operation was created
        via
        [CreateApiOperation][google.cloud.apihub.v1.ApiHub.CreateApiOperation]
        API. If the operation was created by parsing the spec, then it
        can be edited by updating the spec.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_api_operation():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.UpdateApiOperationRequest(
                )

                # Make the request
                response = await client.update_api_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateApiOperationRequest, dict]]):
                The request object. The
                [UpdateApiOperation][google.cloud.apihub.v1.ApiHub.UpdateApiOperation]
                method's request.
            api_operation (:class:`google.cloud.apihub_v1.types.ApiOperation`):
                Required. The apiOperation resource to update.

                The operation resource's ``name`` field is used to
                identify the operation resource to update. Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``

                This corresponds to the ``api_operation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.ApiOperation:
                Represents an operation contained in
                an API version in the API Hub. An
                operation is added/updated/deleted in an
                API version when a new spec is added or
                an existing spec is updated/deleted in a
                version. Currently, an operation will be
                created only corresponding to OpenAPI
                spec as parsing is supported for OpenAPI
                spec.
                Alternatively operations can be managed
                via create,update and delete APIs,
                creation of apiOperation can be possible
                only for version with no parsed
                operations and update/delete can be
                possible only for operations created via
                create API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [api_operation, update_mask]
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
        if not isinstance(request, apihub_service.UpdateApiOperationRequest):
            request = apihub_service.UpdateApiOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if api_operation is not None:
            request.api_operation = api_operation
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_api_operation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("api_operation.name", request.api_operation.name),)
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

    async def delete_api_operation(
        self,
        request: Optional[Union[apihub_service.DeleteApiOperationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete an operation in an API version and we can
        delete only the operations created via create API. If
        the operation was created by parsing the spec, then it
        can be deleted by editing or deleting the spec.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_api_operation():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteApiOperationRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_api_operation(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteApiOperationRequest, dict]]):
                The request object. The
                [DeleteApiOperation][google.cloud.apihub.v1.ApiHub.DeleteApiOperation]
                method's request.
            name (:class:`str`):
                Required. The name of the operation resource to delete.
                Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``

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
        if not isinstance(request, apihub_service.DeleteApiOperationRequest):
            request = apihub_service.DeleteApiOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_api_operation
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

    async def get_definition(
        self,
        request: Optional[Union[apihub_service.GetDefinitionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Definition:
        r"""Get details about a definition in an API version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_definition():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetDefinitionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_definition(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetDefinitionRequest, dict]]):
                The request object. The
                [GetDefinition][google.cloud.apihub.v1.ApiHub.GetDefinition]
                method's request.
            name (:class:`str`):
                Required. The name of the definition to retrieve.
                Format:
                ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/definitions/{definition}``

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
            google.cloud.apihub_v1.types.Definition:
                Represents a definition for example schema, request, response definitions
                   contained in an API version. A definition is
                   added/updated/deleted in an API version when a new
                   spec is added or an existing spec is updated/deleted
                   in a version. Currently, definition will be created
                   only corresponding to OpenAPI spec as parsing is
                   supported for OpenAPI spec. Also, within OpenAPI
                   spec, only schema object is supported.

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
        if not isinstance(request, apihub_service.GetDefinitionRequest):
            request = apihub_service.GetDefinitionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_definition
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

    async def create_deployment(
        self,
        request: Optional[Union[apihub_service.CreateDeploymentRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        deployment: Optional[common_fields.Deployment] = None,
        deployment_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Deployment:
        r"""Create a deployment resource in the API hub.
        Once a deployment resource is created, it can be
        associated with API versions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_deployment():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                deployment = apihub_v1.Deployment()
                deployment.display_name = "display_name_value"
                deployment.deployment_type.enum_values.values.id = "id_value"
                deployment.deployment_type.enum_values.values.display_name = "display_name_value"
                deployment.resource_uri = "resource_uri_value"
                deployment.endpoints = ['endpoints_value1', 'endpoints_value2']

                request = apihub_v1.CreateDeploymentRequest(
                    parent="parent_value",
                    deployment=deployment,
                )

                # Make the request
                response = await client.create_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateDeploymentRequest, dict]]):
                The request object. The
                [CreateDeployment][google.cloud.apihub.v1.ApiHub.CreateDeployment]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for the deployment
                resource. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deployment (:class:`google.cloud.apihub_v1.types.Deployment`):
                Required. The deployment resource to
                create.

                This corresponds to the ``deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deployment_id (:class:`str`):
                Optional. The ID to use for the deployment resource,
                which will become the final component of the
                deployment's resource name. This field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another deployment resource in the API hub.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``deployment_id`` field
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
            google.cloud.apihub_v1.types.Deployment:
                Details of the deployment where APIs
                are hosted. A deployment could represent
                an Apigee proxy, API gateway, other
                Google Cloud services or non-Google
                Cloud services as well. A deployment
                entity is a root level entity in the API
                hub and exists independent of any API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, deployment, deployment_id]
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
        if not isinstance(request, apihub_service.CreateDeploymentRequest):
            request = apihub_service.CreateDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if deployment is not None:
            request.deployment = deployment
        if deployment_id is not None:
            request.deployment_id = deployment_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_deployment
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

    async def get_deployment(
        self,
        request: Optional[Union[apihub_service.GetDeploymentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Deployment:
        r"""Get details about a deployment and the API versions
        linked to it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_deployment():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetDeploymentRequest, dict]]):
                The request object. The
                [GetDeployment][google.cloud.apihub.v1.ApiHub.GetDeployment]
                method's request.
            name (:class:`str`):
                Required. The name of the deployment resource to
                retrieve. Format:
                ``projects/{project}/locations/{location}/deployments/{deployment}``

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
            google.cloud.apihub_v1.types.Deployment:
                Details of the deployment where APIs
                are hosted. A deployment could represent
                an Apigee proxy, API gateway, other
                Google Cloud services or non-Google
                Cloud services as well. A deployment
                entity is a root level entity in the API
                hub and exists independent of any API.

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
        if not isinstance(request, apihub_service.GetDeploymentRequest):
            request = apihub_service.GetDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_deployment
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

    async def list_deployments(
        self,
        request: Optional[Union[apihub_service.ListDeploymentsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDeploymentsAsyncPager:
        r"""List deployment resources in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_deployments():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListDeploymentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_deployments(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListDeploymentsRequest, dict]]):
                The request object. The
                [ListDeployments][google.cloud.apihub.v1.ApiHub.ListDeployments]
                method's request.
            parent (:class:`str`):
                Required. The parent, which owns this collection of
                deployment resources. Format:
                ``projects/{project}/locations/{location}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager:
                The [ListDeployments][google.cloud.apihub.v1.ApiHub.ListDeployments] method's
                   response.

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
        if not isinstance(request, apihub_service.ListDeploymentsRequest):
            request = apihub_service.ListDeploymentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_deployments
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
        response = pagers.ListDeploymentsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_deployment(
        self,
        request: Optional[Union[apihub_service.UpdateDeploymentRequest, dict]] = None,
        *,
        deployment: Optional[common_fields.Deployment] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Deployment:
        r"""Update a deployment resource in the API hub. The following
        fields in the [deployment
        resource][google.cloud.apihub.v1.Deployment] can be updated:

        - [display_name][google.cloud.apihub.v1.Deployment.display_name]
        - [description][google.cloud.apihub.v1.Deployment.description]
        - [documentation][google.cloud.apihub.v1.Deployment.documentation]
        - [deployment_type][google.cloud.apihub.v1.Deployment.deployment_type]
        - [resource_uri][google.cloud.apihub.v1.Deployment.resource_uri]
        - [endpoints][google.cloud.apihub.v1.Deployment.endpoints]
        - [slo][google.cloud.apihub.v1.Deployment.slo]
        - [environment][google.cloud.apihub.v1.Deployment.environment]
        - [attributes][google.cloud.apihub.v1.Deployment.attributes]
        - [source_project]
          [google.cloud.apihub.v1.Deployment.source_project]
        - [source_environment]
          [google.cloud.apihub.v1.Deployment.source_environment]
        - [management_url][google.cloud.apihub.v1.Deployment.management_url]
        - [source_uri][google.cloud.apihub.v1.Deployment.source_uri] The
          [update_mask][google.cloud.apihub.v1.UpdateDeploymentRequest.update_mask]
          should be used to specify the fields being updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_deployment():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                deployment = apihub_v1.Deployment()
                deployment.display_name = "display_name_value"
                deployment.deployment_type.enum_values.values.id = "id_value"
                deployment.deployment_type.enum_values.values.display_name = "display_name_value"
                deployment.resource_uri = "resource_uri_value"
                deployment.endpoints = ['endpoints_value1', 'endpoints_value2']

                request = apihub_v1.UpdateDeploymentRequest(
                    deployment=deployment,
                )

                # Make the request
                response = await client.update_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateDeploymentRequest, dict]]):
                The request object. The
                [UpdateDeployment][google.cloud.apihub.v1.ApiHub.UpdateDeployment]
                method's request.
            deployment (:class:`google.cloud.apihub_v1.types.Deployment`):
                Required. The deployment resource to update.

                The deployment resource's ``name`` field is used to
                identify the deployment resource to update. Format:
                ``projects/{project}/locations/{location}/deployments/{deployment}``

                This corresponds to the ``deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.Deployment:
                Details of the deployment where APIs
                are hosted. A deployment could represent
                an Apigee proxy, API gateway, other
                Google Cloud services or non-Google
                Cloud services as well. A deployment
                entity is a root level entity in the API
                hub and exists independent of any API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [deployment, update_mask]
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
        if not isinstance(request, apihub_service.UpdateDeploymentRequest):
            request = apihub_service.UpdateDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if deployment is not None:
            request.deployment = deployment
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_deployment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("deployment.name", request.deployment.name),)
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

    async def delete_deployment(
        self,
        request: Optional[Union[apihub_service.DeleteDeploymentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a deployment resource in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_deployment():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_deployment(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteDeploymentRequest, dict]]):
                The request object. The
                [DeleteDeployment][google.cloud.apihub.v1.ApiHub.DeleteDeployment]
                method's request.
            name (:class:`str`):
                Required. The name of the deployment resource to delete.
                Format:
                ``projects/{project}/locations/{location}/deployments/{deployment}``

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
        if not isinstance(request, apihub_service.DeleteDeploymentRequest):
            request = apihub_service.DeleteDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_deployment
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

    async def create_attribute(
        self,
        request: Optional[Union[apihub_service.CreateAttributeRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        attribute: Optional[common_fields.Attribute] = None,
        attribute_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Attribute:
        r"""Create a user defined attribute.

        Certain pre defined attributes are already created by the API
        hub. These attributes will have type as ``SYSTEM_DEFINED`` and
        can be listed via
        [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
        method. Allowed values for the same can be updated via
        [UpdateAttribute][google.cloud.apihub.v1.ApiHub.UpdateAttribute]
        method.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_attribute():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                attribute = apihub_v1.Attribute()
                attribute.display_name = "display_name_value"
                attribute.scope = "PLUGIN"
                attribute.data_type = "URI"

                request = apihub_v1.CreateAttributeRequest(
                    parent="parent_value",
                    attribute=attribute,
                )

                # Make the request
                response = await client.create_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateAttributeRequest, dict]]):
                The request object. The
                [CreateAttribute][google.cloud.apihub.v1.ApiHub.CreateAttribute]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for Attribute. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            attribute (:class:`google.cloud.apihub_v1.types.Attribute`):
                Required. The attribute to create.
                This corresponds to the ``attribute`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            attribute_id (:class:`str`):
                Optional. The ID to use for the attribute, which will
                become the final component of the attribute's resource
                name. This field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another attribute resource in the API hub.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``attribute_id`` field
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
            google.cloud.apihub_v1.types.Attribute:
                An attribute in the API Hub.
                An attribute is a name value pair which
                can be attached to different resources
                in the API hub based on the scope of the
                attribute. Attributes can either be
                pre-defined by the API Hub or created by
                users.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, attribute, attribute_id]
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
        if not isinstance(request, apihub_service.CreateAttributeRequest):
            request = apihub_service.CreateAttributeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if attribute is not None:
            request.attribute = attribute
        if attribute_id is not None:
            request.attribute_id = attribute_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_attribute
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

    async def get_attribute(
        self,
        request: Optional[Union[apihub_service.GetAttributeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Attribute:
        r"""Get details about the attribute.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_attribute():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetAttributeRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetAttributeRequest, dict]]):
                The request object. The
                [GetAttribute][google.cloud.apihub.v1.ApiHub.GetAttribute]
                method's request.
            name (:class:`str`):
                Required. The name of the attribute to retrieve. Format:
                ``projects/{project}/locations/{location}/attributes/{attribute}``

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
            google.cloud.apihub_v1.types.Attribute:
                An attribute in the API Hub.
                An attribute is a name value pair which
                can be attached to different resources
                in the API hub based on the scope of the
                attribute. Attributes can either be
                pre-defined by the API Hub or created by
                users.

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
        if not isinstance(request, apihub_service.GetAttributeRequest):
            request = apihub_service.GetAttributeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_attribute
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

    async def update_attribute(
        self,
        request: Optional[Union[apihub_service.UpdateAttributeRequest, dict]] = None,
        *,
        attribute: Optional[common_fields.Attribute] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.Attribute:
        r"""Update the attribute. The following fields in the [Attribute
        resource][google.cloud.apihub.v1.Attribute] can be updated:

        - [display_name][google.cloud.apihub.v1.Attribute.display_name]
          The display name can be updated for user defined attributes
          only.
        - [description][google.cloud.apihub.v1.Attribute.description]
          The description can be updated for user defined attributes
          only.
        - [allowed_values][google.cloud.apihub.v1.Attribute.allowed_values]
          To update the list of allowed values, clients need to use the
          fetched list of allowed values and add or remove values to or
          from the same list. The mutable allowed values can be updated
          for both user defined and System defined attributes. The
          immutable allowed values cannot be updated or deleted. The
          updated list of allowed values cannot be empty. If an allowed
          value that is already used by some resource's attribute is
          deleted, then the association between the resource and the
          attribute value will also be deleted.
        - [cardinality][google.cloud.apihub.v1.Attribute.cardinality]
          The cardinality can be updated for user defined attributes
          only. Cardinality can only be increased during an update.

        The
        [update_mask][google.cloud.apihub.v1.UpdateAttributeRequest.update_mask]
        should be used to specify the fields being updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_attribute():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                attribute = apihub_v1.Attribute()
                attribute.display_name = "display_name_value"
                attribute.scope = "PLUGIN"
                attribute.data_type = "URI"

                request = apihub_v1.UpdateAttributeRequest(
                    attribute=attribute,
                )

                # Make the request
                response = await client.update_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateAttributeRequest, dict]]):
                The request object. The
                [UpdateAttribute][google.cloud.apihub.v1.ApiHub.UpdateAttribute]
                method's request.
            attribute (:class:`google.cloud.apihub_v1.types.Attribute`):
                Required. The attribute to update.

                The attribute's ``name`` field is used to identify the
                attribute to update. Format:
                ``projects/{project}/locations/{location}/attributes/{attribute}``

                This corresponds to the ``attribute`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.Attribute:
                An attribute in the API Hub.
                An attribute is a name value pair which
                can be attached to different resources
                in the API hub based on the scope of the
                attribute. Attributes can either be
                pre-defined by the API Hub or created by
                users.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [attribute, update_mask]
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
        if not isinstance(request, apihub_service.UpdateAttributeRequest):
            request = apihub_service.UpdateAttributeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if attribute is not None:
            request.attribute = attribute
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_attribute
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attribute.name", request.attribute.name),)
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

    async def delete_attribute(
        self,
        request: Optional[Union[apihub_service.DeleteAttributeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete an attribute.

        Note: System defined attributes cannot be deleted. All
        associations of the attribute being deleted with any API
        hub resource will also get deleted.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_attribute():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteAttributeRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_attribute(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteAttributeRequest, dict]]):
                The request object. The
                [DeleteAttribute][google.cloud.apihub.v1.ApiHub.DeleteAttribute]
                method's request.
            name (:class:`str`):
                Required. The name of the attribute to delete. Format:
                ``projects/{project}/locations/{location}/attributes/{attribute}``

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
        if not isinstance(request, apihub_service.DeleteAttributeRequest):
            request = apihub_service.DeleteAttributeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_attribute
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

    async def list_attributes(
        self,
        request: Optional[Union[apihub_service.ListAttributesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAttributesAsyncPager:
        r"""List all attributes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_attributes():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListAttributesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_attributes(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListAttributesRequest, dict]]):
                The request object. The
                [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for Attribute. Format:
                ``projects/{project}/locations/{location}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager:
                The [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes] method's
                   response.

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
        if not isinstance(request, apihub_service.ListAttributesRequest):
            request = apihub_service.ListAttributesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_attributes
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
        response = pagers.ListAttributesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_resources(
        self,
        request: Optional[Union[apihub_service.SearchResourcesRequest, dict]] = None,
        *,
        location: Optional[str] = None,
        query: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchResourcesAsyncPager:
        r"""Search across API-Hub resources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_search_resources():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.SearchResourcesRequest(
                    location="location_value",
                    query="query_value",
                )

                # Make the request
                page_result = client.search_resources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.SearchResourcesRequest, dict]]):
                The request object. The
                [SearchResources][google.cloud.apihub.v1.ApiHub.SearchResources]
                method's request.
            location (:class:`str`):
                Required. The resource name of the location which will
                be of the type
                ``projects/{project_id}/locations/{location_id}``. This
                field is used to identify the instance of API-Hub in
                which resources should be searched.

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Required. The free text search query.
                This query can contain keywords which
                could be related to any detail of the
                API-Hub resources such display names,
                descriptions, attributes etc.

                This corresponds to the ``query`` field
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
            google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager:
                Response for the
                   [SearchResources][google.cloud.apihub.v1.ApiHub.SearchResources]
                   method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [location, query]
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
        if not isinstance(request, apihub_service.SearchResourcesRequest):
            request = apihub_service.SearchResourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if location is not None:
            request.location = location
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_resources
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
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
        response = pagers.SearchResourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_external_api(
        self,
        request: Optional[Union[apihub_service.CreateExternalApiRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        external_api: Optional[common_fields.ExternalApi] = None,
        external_api_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.ExternalApi:
        r"""Create an External API resource in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_create_external_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                external_api = apihub_v1.ExternalApi()
                external_api.display_name = "display_name_value"

                request = apihub_v1.CreateExternalApiRequest(
                    parent="parent_value",
                    external_api=external_api,
                )

                # Make the request
                response = await client.create_external_api(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.CreateExternalApiRequest, dict]]):
                The request object. The
                [CreateExternalApi][google.cloud.apihub.v1.ApiHub.CreateExternalApi]
                method's request.
            parent (:class:`str`):
                Required. The parent resource for the External API
                resource. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            external_api (:class:`google.cloud.apihub_v1.types.ExternalApi`):
                Required. The External API resource
                to create.

                This corresponds to the ``external_api`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            external_api_id (:class:`str`):
                Optional. The ID to use for the External API resource,
                which will become the final component of the External
                API's resource name. This field is optional.

                - If provided, the same will be used. The service will
                  throw an error if the specified id is already used by
                  another External API resource in the API hub.
                - If not provided, a system generated id will be used.

                This value should be 4-500 characters, and valid
                characters are /[a-z][A-Z][0-9]-\_/.

                This corresponds to the ``external_api_id`` field
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
            google.cloud.apihub_v1.types.ExternalApi:
                An external API represents an API
                being provided by external sources. This
                can be used to model third-party APIs
                and can be used to define dependencies.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, external_api, external_api_id]
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
        if not isinstance(request, apihub_service.CreateExternalApiRequest):
            request = apihub_service.CreateExternalApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if external_api is not None:
            request.external_api = external_api
        if external_api_id is not None:
            request.external_api_id = external_api_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_external_api
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

    async def get_external_api(
        self,
        request: Optional[Union[apihub_service.GetExternalApiRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.ExternalApi:
        r"""Get details about an External API resource in the API
        hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_get_external_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.GetExternalApiRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_external_api(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.GetExternalApiRequest, dict]]):
                The request object. The
                [GetExternalApi][google.cloud.apihub.v1.ApiHub.GetExternalApi]
                method's request.
            name (:class:`str`):
                Required. The name of the External API resource to
                retrieve. Format:
                ``projects/{project}/locations/{location}/externalApis/{externalApi}``

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
            google.cloud.apihub_v1.types.ExternalApi:
                An external API represents an API
                being provided by external sources. This
                can be used to model third-party APIs
                and can be used to define dependencies.

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
        if not isinstance(request, apihub_service.GetExternalApiRequest):
            request = apihub_service.GetExternalApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_external_api
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

    async def update_external_api(
        self,
        request: Optional[Union[apihub_service.UpdateExternalApiRequest, dict]] = None,
        *,
        external_api: Optional[common_fields.ExternalApi] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> common_fields.ExternalApi:
        r"""Update an External API resource in the API hub. The following
        fields can be updated:

        - [display_name][google.cloud.apihub.v1.ExternalApi.display_name]
        - [description][google.cloud.apihub.v1.ExternalApi.description]
        - [documentation][google.cloud.apihub.v1.ExternalApi.documentation]
        - [endpoints][google.cloud.apihub.v1.ExternalApi.endpoints]
        - [paths][google.cloud.apihub.v1.ExternalApi.paths]

        The
        [update_mask][google.cloud.apihub.v1.UpdateExternalApiRequest.update_mask]
        should be used to specify the fields being updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_update_external_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                external_api = apihub_v1.ExternalApi()
                external_api.display_name = "display_name_value"

                request = apihub_v1.UpdateExternalApiRequest(
                    external_api=external_api,
                )

                # Make the request
                response = await client.update_external_api(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.UpdateExternalApiRequest, dict]]):
                The request object. The
                [UpdateExternalApi][google.cloud.apihub.v1.ApiHub.UpdateExternalApi]
                method's request.
            external_api (:class:`google.cloud.apihub_v1.types.ExternalApi`):
                Required. The External API resource to update.

                The External API resource's ``name`` field is used to
                identify the External API resource to update. Format:
                ``projects/{project}/locations/{location}/externalApis/{externalApi}``

                This corresponds to the ``external_api`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.apihub_v1.types.ExternalApi:
                An external API represents an API
                being provided by external sources. This
                can be used to model third-party APIs
                and can be used to define dependencies.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [external_api, update_mask]
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
        if not isinstance(request, apihub_service.UpdateExternalApiRequest):
            request = apihub_service.UpdateExternalApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if external_api is not None:
            request.external_api = external_api
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_external_api
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("external_api.name", request.external_api.name),)
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

    async def delete_external_api(
        self,
        request: Optional[Union[apihub_service.DeleteExternalApiRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete an External API resource in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_delete_external_api():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.DeleteExternalApiRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_external_api(request=request)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.DeleteExternalApiRequest, dict]]):
                The request object. The
                [DeleteExternalApi][google.cloud.apihub.v1.ApiHub.DeleteExternalApi]
                method's request.
            name (:class:`str`):
                Required. The name of the External API resource to
                delete. Format:
                ``projects/{project}/locations/{location}/externalApis/{externalApi}``

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
        if not isinstance(request, apihub_service.DeleteExternalApiRequest):
            request = apihub_service.DeleteExternalApiRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_external_api
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

    async def list_external_apis(
        self,
        request: Optional[Union[apihub_service.ListExternalApisRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListExternalApisAsyncPager:
        r"""List External API resources in the API hub.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import apihub_v1

            async def sample_list_external_apis():
                # Create a client
                client = apihub_v1.ApiHubAsyncClient()

                # Initialize request argument(s)
                request = apihub_v1.ListExternalApisRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_external_apis(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.apihub_v1.types.ListExternalApisRequest, dict]]):
                The request object. The
                [ListExternalApis][google.cloud.apihub.v1.ApiHub.ListExternalApis]
                method's request.
            parent (:class:`str`):
                Required. The parent, which owns this collection of
                External API resources. Format:
                ``projects/{project}/locations/{location}``

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
            google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager:
                The [ListExternalApis][google.cloud.apihub.v1.ApiHub.ListExternalApis]
                   method's response.

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
        if not isinstance(request, apihub_service.ListExternalApisRequest):
            request = apihub_service.ListExternalApisRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_external_apis
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
        response = pagers.ListExternalApisAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[Union[operations_pb2.ListOperationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.ListOperationsRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.ListOperationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_operations]

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

    async def get_operation(
        self,
        request: Optional[Union[operations_pb2.GetOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.GetOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.GetOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_operation]

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

    async def delete_operation(
        self,
        request: Optional[Union[operations_pb2.DeleteOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.DeleteOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.DeleteOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.delete_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: Optional[Union[operations_pb2.CancelOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.CancelOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.CancelOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
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

    async def __aenter__(self) -> "ApiHubAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ApiHubAsyncClient",)
