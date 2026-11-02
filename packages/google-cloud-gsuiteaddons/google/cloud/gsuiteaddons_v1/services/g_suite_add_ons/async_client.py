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

from google.cloud.gsuiteaddons_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore

from google.cloud.gsuiteaddons_v1.services.g_suite_add_ons import pagers
from google.cloud.gsuiteaddons_v1.types import gsuiteaddons

from .client import GSuiteAddOnsClient
from .transports.base import DEFAULT_CLIENT_INFO, GSuiteAddOnsTransport
from .transports.grpc_asyncio import GSuiteAddOnsGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class GSuiteAddOnsAsyncClient:
    """A service for managing Google Workspace add-ons deployments.

    A Google Workspace add-on is a third-party embedded component
    that can be installed in Google Workspace Applications like
    Gmail, Calendar, Drive, and the Google Docs, Sheets, and Slides
    editors. Google Workspace add-ons can display UI cards, receive
    contextual information from the host application, and perform
    actions in the host application (See:

    https://developers.google.com/gsuite/add-ons/overview for more
    information).

    A Google Workspace add-on deployment resource specifies metadata
    about the add-on, including a specification of the entry points
    in the host application that trigger add-on executions (see:

    https://developers.google.com/gsuite/add-ons/concepts/gsuite-manifests).
    Add-on deployments defined via the Google Workspace add-ons API
    define their entrypoints using HTTPS URLs (See:

    https://developers.google.com/gsuite/add-ons/guides/alternate-runtimes),

    A Google Workspace add-on deployment can be installed in
    developer mode, which allows an add-on developer to test the
    experience an end-user would see when installing and running the
    add-on in their G Suite applications.  When running in developer
    mode, more detailed error messages are exposed in the add-on UI
    to aid in debugging.

    A Google Workspace add-on deployment can be published to Google
    Workspace Marketplace, which allows other Google Workspace users
    to discover and install the add-on.  See:

    https://developers.google.com/gsuite/add-ons/how-tos/publish-add-on-overview
    for details.
    """

    _client: GSuiteAddOnsClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = GSuiteAddOnsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = GSuiteAddOnsClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = GSuiteAddOnsClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = GSuiteAddOnsClient._DEFAULT_UNIVERSE

    authorization_path = staticmethod(GSuiteAddOnsClient.authorization_path)
    parse_authorization_path = staticmethod(GSuiteAddOnsClient.parse_authorization_path)
    deployment_path = staticmethod(GSuiteAddOnsClient.deployment_path)
    parse_deployment_path = staticmethod(GSuiteAddOnsClient.parse_deployment_path)
    install_status_path = staticmethod(GSuiteAddOnsClient.install_status_path)
    parse_install_status_path = staticmethod(
        GSuiteAddOnsClient.parse_install_status_path
    )
    common_billing_account_path = staticmethod(
        GSuiteAddOnsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        GSuiteAddOnsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(GSuiteAddOnsClient.common_folder_path)
    parse_common_folder_path = staticmethod(GSuiteAddOnsClient.parse_common_folder_path)
    common_organization_path = staticmethod(GSuiteAddOnsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        GSuiteAddOnsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(GSuiteAddOnsClient.common_project_path)
    parse_common_project_path = staticmethod(
        GSuiteAddOnsClient.parse_common_project_path
    )
    common_location_path = staticmethod(GSuiteAddOnsClient.common_location_path)
    parse_common_location_path = staticmethod(
        GSuiteAddOnsClient.parse_common_location_path
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
            GSuiteAddOnsAsyncClient: The constructed client.
        """
        sa_info_func = (
            GSuiteAddOnsClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(GSuiteAddOnsAsyncClient, info, *args, **kwargs)

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
            GSuiteAddOnsAsyncClient: The constructed client.
        """
        sa_file_func = (
            GSuiteAddOnsClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(GSuiteAddOnsAsyncClient, filename, *args, **kwargs)

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
        return GSuiteAddOnsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> GSuiteAddOnsTransport:
        """Returns the transport used by the client instance.

        Returns:
            GSuiteAddOnsTransport: The transport used by the client instance.
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

    get_transport_class = GSuiteAddOnsClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, GSuiteAddOnsTransport, Callable[..., GSuiteAddOnsTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the g suite add ons async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,GSuiteAddOnsTransport,Callable[..., GSuiteAddOnsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the GSuiteAddOnsTransport constructor.
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
        self._client = GSuiteAddOnsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.gsuiteaddons_v1.GSuiteAddOnsAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
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
                    "serviceName": "google.cloud.gsuiteaddons.v1.GSuiteAddOns",
                    "credentialsType": None,
                },
            )

    async def get_authorization(
        self,
        request: Optional[Union[gsuiteaddons.GetAuthorizationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gsuiteaddons.Authorization:
        r"""Gets the authorization information for deployments in
        a given project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_get_authorization():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.GetAuthorizationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_authorization(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.GetAuthorizationRequest, dict]]):
                The request object. Request message to get Google
                Workspace add-ons authorization
                information.
            name (:class:`str`):
                Required. Name of the project for which to get the
                Google Workspace add-ons authorization information.

                Example: ``projects/my_project/authorization``.

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
            google.cloud.gsuiteaddons_v1.types.Authorization:
                The authorization information used
                when invoking deployment endpoints.

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
        if not isinstance(request, gsuiteaddons.GetAuthorizationRequest):
            request = gsuiteaddons.GetAuthorizationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_authorization
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
        request: Optional[Union[gsuiteaddons.CreateDeploymentRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        deployment: Optional[gsuiteaddons.Deployment] = None,
        deployment_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gsuiteaddons.Deployment:
        r"""Creates a deployment with the specified name and
        configuration.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_create_deployment():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.CreateDeploymentRequest(
                    parent="parent_value",
                    deployment_id="deployment_id_value",
                )

                # Make the request
                response = await client.create_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.CreateDeploymentRequest, dict]]):
                The request object. Request message to create a
                deployment.
            parent (:class:`str`):
                Required. Name of the project in which to create the
                deployment.

                Example: ``projects/my_project``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deployment (:class:`google.cloud.gsuiteaddons_v1.types.Deployment`):
                Required. The deployment to create
                (deployment.name cannot be set).

                This corresponds to the ``deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deployment_id (:class:`str`):
                Required. The id to use for this deployment. The full
                name of the created resource will be
                ``projects/<project_number>/deployments/<deployment_id>``.

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
            google.cloud.gsuiteaddons_v1.types.Deployment:
                A Google Workspace add-on deployment
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
        if not isinstance(request, gsuiteaddons.CreateDeploymentRequest):
            request = gsuiteaddons.CreateDeploymentRequest(request)

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

    async def replace_deployment(
        self,
        request: Optional[Union[gsuiteaddons.ReplaceDeploymentRequest, dict]] = None,
        *,
        deployment: Optional[gsuiteaddons.Deployment] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gsuiteaddons.Deployment:
        r"""Creates or replaces a deployment with the specified
        name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_replace_deployment():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.ReplaceDeploymentRequest(
                )

                # Make the request
                response = await client.replace_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.ReplaceDeploymentRequest, dict]]):
                The request object. Request message to create or replace
                a deployment.
            deployment (:class:`google.cloud.gsuiteaddons_v1.types.Deployment`):
                Required. The deployment to create or
                replace.

                This corresponds to the ``deployment`` field
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
            google.cloud.gsuiteaddons_v1.types.Deployment:
                A Google Workspace add-on deployment
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [deployment]
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
        if not isinstance(request, gsuiteaddons.ReplaceDeploymentRequest):
            request = gsuiteaddons.ReplaceDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if deployment is not None:
            request.deployment = deployment

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.replace_deployment
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

    async def get_deployment(
        self,
        request: Optional[Union[gsuiteaddons.GetDeploymentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gsuiteaddons.Deployment:
        r"""Gets the deployment with the specified name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_get_deployment():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.GetDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.GetDeploymentRequest, dict]]):
                The request object. Request message to get a deployment.
            name (:class:`str`):
                Required. The full resource name of the deployment to
                get.

                Example:
                ``projects/my_project/deployments/my_deployment``.

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
            google.cloud.gsuiteaddons_v1.types.Deployment:
                A Google Workspace add-on deployment
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
        if not isinstance(request, gsuiteaddons.GetDeploymentRequest):
            request = gsuiteaddons.GetDeploymentRequest(request)

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
        request: Optional[Union[gsuiteaddons.ListDeploymentsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDeploymentsAsyncPager:
        r"""Lists all deployments in a particular project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_list_deployments():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.ListDeploymentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_deployments(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.ListDeploymentsRequest, dict]]):
                The request object. Request message to list deployments
                for a project.
            parent (:class:`str`):
                Required. Name of the project in which to create the
                deployment.

                Example: ``projects/my_project``.

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
            google.cloud.gsuiteaddons_v1.services.g_suite_add_ons.pagers.ListDeploymentsAsyncPager:
                Response message to list deployments.

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
        if not isinstance(request, gsuiteaddons.ListDeploymentsRequest):
            request = gsuiteaddons.ListDeploymentsRequest(request)

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

    async def delete_deployment(
        self,
        request: Optional[Union[gsuiteaddons.DeleteDeploymentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the deployment with the given name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_delete_deployment():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.DeleteDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_deployment(request=request)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.DeleteDeploymentRequest, dict]]):
                The request object. Request message to delete a
                deployment.
            name (:class:`str`):
                Required. The full resource name of the deployment to
                delete.

                Example:
                ``projects/my_project/deployments/my_deployment``.

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
        if not isinstance(request, gsuiteaddons.DeleteDeploymentRequest):
            request = gsuiteaddons.DeleteDeploymentRequest(request)

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

    async def install_deployment(
        self,
        request: Optional[Union[gsuiteaddons.InstallDeploymentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Installs a deployment in developer mode.
        See:

        https://developers.google.com/gsuite/add-ons/how-tos/testing-gsuite-addons.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_install_deployment():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.InstallDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                await client.install_deployment(request=request)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.InstallDeploymentRequest, dict]]):
                The request object. Request message to install a
                developer mode deployment.
            name (:class:`str`):
                Required. The full resource name of the deployment to
                install.

                Example:
                ``projects/my_project/deployments/my_deployment``.

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
        if not isinstance(request, gsuiteaddons.InstallDeploymentRequest):
            request = gsuiteaddons.InstallDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.install_deployment
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

    async def uninstall_deployment(
        self,
        request: Optional[Union[gsuiteaddons.UninstallDeploymentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Uninstalls a developer mode deployment.
        See:

        https://developers.google.com/gsuite/add-ons/how-tos/testing-gsuite-addons.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_uninstall_deployment():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.UninstallDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                await client.uninstall_deployment(request=request)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.UninstallDeploymentRequest, dict]]):
                The request object. Request message to uninstall a
                developer mode deployment.
            name (:class:`str`):
                Required. The full resource name of the deployment to
                install.

                Example:
                ``projects/my_project/deployments/my_deployment``.

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
        if not isinstance(request, gsuiteaddons.UninstallDeploymentRequest):
            request = gsuiteaddons.UninstallDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.uninstall_deployment
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

    async def get_install_status(
        self,
        request: Optional[Union[gsuiteaddons.GetInstallStatusRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gsuiteaddons.InstallStatus:
        r"""Fetches the install status of a developer mode
        deployment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gsuiteaddons_v1

            async def sample_get_install_status():
                # Create a client
                client = gsuiteaddons_v1.GSuiteAddOnsAsyncClient()

                # Initialize request argument(s)
                request = gsuiteaddons_v1.GetInstallStatusRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_install_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gsuiteaddons_v1.types.GetInstallStatusRequest, dict]]):
                The request object. Request message to get the install
                status of a developer mode deployment.
            name (:class:`str`):
                Required. The full resource name of the deployment.

                Example:
                ``projects/my_project/deployments/my_deployment/installStatus``.

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
            google.cloud.gsuiteaddons_v1.types.InstallStatus:
                Developer mode install status of a
                deployment

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
        if not isinstance(request, gsuiteaddons.GetInstallStatusRequest):
            request = gsuiteaddons.GetInstallStatusRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_install_status
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

    async def __aenter__(self) -> "GSuiteAddOnsAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("GSuiteAddOnsAsyncClient",)
