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

from google.cloud.managedkafka_schemaregistry_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf.any_pb2 as any_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry,
    schema_registry_resources,
)
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry as gcms_schema_registry,
)

from .client import ManagedSchemaRegistryClient
from .transports.base import DEFAULT_CLIENT_INFO, ManagedSchemaRegistryTransport
from .transports.grpc_asyncio import ManagedSchemaRegistryGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ManagedSchemaRegistryAsyncClient:
    """SchemaRegistry is a service that allows users to manage schemas for
    their Kafka clusters. It provides APIs to register, list, and delete
    schemas, as well as to get the schema for a given schema id or a
    given version id under a subject, to update the global or
    subject-specific compatibility mode, and to check the compatibility
    of a schema against a subject or a version. The main resource
    hierarchy is as follows:

    - SchemaRegistry
    - SchemaRegistry/Context
    - SchemaRegistry/Context/Schema
    - SchemaRegistry/Context/Subject
    - SchemaRegistry/Context/Subject/Version
    - SchemaRegistry/Config
    - SchemaRegistry/Mode

    **SchemaRegistry** is the root resource to represent a schema
    registry instance. A customer can have multiple schema registry
    instances in a project.

    **Context** is a context resource that represents a group of
    schemas, subjects and versions. A schema registry instance can have
    multiple contexts and always has a 'default' context. Contexts are
    independent of each other. Context is optional and if not specified,
    it falls back to the 'default' context.

    **Schema** is a schema resource that represents a unique schema in a
    context of a schema registry instance. Each schema has a unique
    schema id, and can be referenced by a version of a subject.

    **Subject** refers to the name under which the schema is registered.
    A typical subject is the Kafka topic name. A schema registry
    instance can have multiple subjects.

    **Version** represents a version of a subject. A subject can have
    multiple versions. Creation of new version of a subject is guarded
    by the compatibility mode configured globally or for the subject
    specifically.

    **Config** represents a config at global level cross all registry
    instances or at subject level. Currently, only compatibility is
    supported in config.

    **Mode** represents the mode of a schema registry or a specific
    subject. Three modes are supported:

    - READONLY: The schema registry is in read-only mode, no write
      operations allowed..
    - READWRITE: The schema registry is in read-write mode, which allows
      limited write operations on the schema.
    - IMPORT: The schema registry is in import mode, which allows more
      editing operations on the schema for data importing purposes.
    """

    _client: ManagedSchemaRegistryClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ManagedSchemaRegistryClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ManagedSchemaRegistryClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ManagedSchemaRegistryClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ManagedSchemaRegistryClient._DEFAULT_UNIVERSE

    schema_path = staticmethod(ManagedSchemaRegistryClient.schema_path)
    parse_schema_path = staticmethod(ManagedSchemaRegistryClient.parse_schema_path)
    schema_config_path = staticmethod(ManagedSchemaRegistryClient.schema_config_path)
    parse_schema_config_path = staticmethod(
        ManagedSchemaRegistryClient.parse_schema_config_path
    )
    schema_context_path = staticmethod(ManagedSchemaRegistryClient.schema_context_path)
    parse_schema_context_path = staticmethod(
        ManagedSchemaRegistryClient.parse_schema_context_path
    )
    schema_mode_path = staticmethod(ManagedSchemaRegistryClient.schema_mode_path)
    parse_schema_mode_path = staticmethod(
        ManagedSchemaRegistryClient.parse_schema_mode_path
    )
    schema_registry_path = staticmethod(
        ManagedSchemaRegistryClient.schema_registry_path
    )
    parse_schema_registry_path = staticmethod(
        ManagedSchemaRegistryClient.parse_schema_registry_path
    )
    schema_subject_path = staticmethod(ManagedSchemaRegistryClient.schema_subject_path)
    parse_schema_subject_path = staticmethod(
        ManagedSchemaRegistryClient.parse_schema_subject_path
    )
    schema_version_path = staticmethod(ManagedSchemaRegistryClient.schema_version_path)
    parse_schema_version_path = staticmethod(
        ManagedSchemaRegistryClient.parse_schema_version_path
    )
    common_billing_account_path = staticmethod(
        ManagedSchemaRegistryClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ManagedSchemaRegistryClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ManagedSchemaRegistryClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ManagedSchemaRegistryClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ManagedSchemaRegistryClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ManagedSchemaRegistryClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ManagedSchemaRegistryClient.common_project_path)
    parse_common_project_path = staticmethod(
        ManagedSchemaRegistryClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        ManagedSchemaRegistryClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        ManagedSchemaRegistryClient.parse_common_location_path
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
            ManagedSchemaRegistryAsyncClient: The constructed client.
        """
        sa_info_func = (
            ManagedSchemaRegistryClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ManagedSchemaRegistryAsyncClient, info, *args, **kwargs)

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
            ManagedSchemaRegistryAsyncClient: The constructed client.
        """
        sa_file_func = (
            ManagedSchemaRegistryClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(ManagedSchemaRegistryAsyncClient, filename, *args, **kwargs)

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
        return ManagedSchemaRegistryClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> ManagedSchemaRegistryTransport:
        """Returns the transport used by the client instance.

        Returns:
            ManagedSchemaRegistryTransport: The transport used by the client instance.
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

    get_transport_class = ManagedSchemaRegistryClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                ManagedSchemaRegistryTransport,
                Callable[..., ManagedSchemaRegistryTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the managed schema registry async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ManagedSchemaRegistryTransport,Callable[..., ManagedSchemaRegistryTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ManagedSchemaRegistryTransport constructor.
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
        self._client = ManagedSchemaRegistryClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.managedkafka.schemaregistry_v1.ManagedSchemaRegistryAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
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
                    "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                    "credentialsType": None,
                },
            )

    async def get_schema_registry(
        self,
        request: Optional[Union[schema_registry.GetSchemaRegistryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaRegistry:
        r"""Get the schema registry instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_schema_registry():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetSchemaRegistryRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_schema_registry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetSchemaRegistryRequest, dict]]):
                The request object. Request for GetSchemaRegistry.
            name (:class:`str`):
                Required. The name of the schema registry instance to
                return. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``

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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaRegistry:
                SchemaRegistry is a schema registry
                instance.

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
        if not isinstance(request, schema_registry.GetSchemaRegistryRequest):
            request = schema_registry.GetSchemaRegistryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_schema_registry
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

    async def list_schema_registries(
        self,
        request: Optional[
            Union[schema_registry.ListSchemaRegistriesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry.ListSchemaRegistriesResponse:
        r"""List schema registries.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_schema_registries():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListSchemaRegistriesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_schema_registries(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListSchemaRegistriesRequest, dict]]):
                The request object. Request for ListSchemaRegistries.
            parent (:class:`str`):
                Required. The parent whose schema registry instances are
                to be listed. Structured like:
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
            google.cloud.managedkafka_schemaregistry_v1.types.ListSchemaRegistriesResponse:
                Request for ListSchemaRegistries.
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
        if not isinstance(request, schema_registry.ListSchemaRegistriesRequest):
            request = schema_registry.ListSchemaRegistriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_schema_registries
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

    async def create_schema_registry(
        self,
        request: Optional[
            Union[gcms_schema_registry.CreateSchemaRegistryRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        schema_registry: Optional[schema_registry_resources.SchemaRegistry] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaRegistry:
        r"""Create a schema registry instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_create_schema_registry():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.CreateSchemaRegistryRequest(
                    parent="parent_value",
                    schema_registry_id="schema_registry_id_value",
                )

                # Make the request
                response = await client.create_schema_registry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.CreateSchemaRegistryRequest, dict]]):
                The request object. Request to create a schema registry
                instance.
            parent (:class:`str`):
                Required. The parent whose schema registry instance is
                to be created. Structured like:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            schema_registry (:class:`google.cloud.managedkafka_schemaregistry_v1.types.SchemaRegistry`):
                Required. The schema registry
                instance to create. The name field is
                ignored.

                This corresponds to the ``schema_registry`` field
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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaRegistry:
                SchemaRegistry is a schema registry
                instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, schema_registry]
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
        if not isinstance(request, gcms_schema_registry.CreateSchemaRegistryRequest):
            request = gcms_schema_registry.CreateSchemaRegistryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if schema_registry is not None:
            request.schema_registry = schema_registry

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_schema_registry
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

    async def delete_schema_registry(
        self,
        request: Optional[
            Union[schema_registry.DeleteSchemaRegistryRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete a schema registry instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_delete_schema_registry():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.DeleteSchemaRegistryRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_schema_registry(request=request)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.DeleteSchemaRegistryRequest, dict]]):
                The request object. Request for DeleteSchemaRegistry.
            name (:class:`str`):
                Required. The name of the schema registry instance to
                delete. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``

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
        if not isinstance(request, schema_registry.DeleteSchemaRegistryRequest):
            request = schema_registry.DeleteSchemaRegistryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_schema_registry
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

    async def get_context(
        self,
        request: Optional[Union[schema_registry.GetContextRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.Context:
        r"""Get the context.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_context():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetContextRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_context(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetContextRequest, dict]]):
                The request object. Request for GetContext
            name (:class:`str`):
                Required. The name of the context to return. Structured
                like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}``

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
            google.cloud.managedkafka_schemaregistry_v1.types.Context:
                Context represents an independent
                schema grouping in a schema registry
                instance.

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
        if not isinstance(request, schema_registry.GetContextRequest):
            request = schema_registry.GetContextRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_context
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

    async def list_contexts(
        self,
        request: Optional[Union[schema_registry.ListContextsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""List contexts for a schema registry.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_contexts():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListContextsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_contexts(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListContextsRequest, dict]]):
                The request object. Request for ListContexts.
            parent (:class:`str`):
                Required. The parent of the contexts. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.ListContextsRequest):
            request = schema_registry.ListContextsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_contexts
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

    async def get_schema(
        self,
        request: Optional[Union[schema_registry.GetSchemaRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.Schema:
        r"""Get the schema for the given schema id.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_schema():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetSchemaRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_schema(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetSchemaRequest, dict]]):
                The request object. Request for GetSchema.
            name (:class:`str`):
                Required. The name of the schema to return. Structured
                like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``

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
            google.cloud.managedkafka_schemaregistry_v1.types.Schema:
                Schema for a Kafka message.
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
        if not isinstance(request, schema_registry.GetSchemaRequest):
            request = schema_registry.GetSchemaRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_schema
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

    async def get_raw_schema(
        self,
        request: Optional[Union[schema_registry.GetSchemaRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Get the schema string for the given schema id.
        The response will be the schema string.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_raw_schema():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetSchemaRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_raw_schema(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetSchemaRequest, dict]]):
                The request object. Request for GetSchema.
            name (:class:`str`):
                Required. The name of the schema to return. Structured
                like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.GetSchemaRequest):
            request = schema_registry.GetSchemaRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_raw_schema
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

    async def list_schema_versions(
        self,
        request: Optional[
            Union[schema_registry.ListSchemaVersionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""List the schema versions for the given schema id. The response
        will be an array of subject-version pairs as:
        [{"subject":"subject1", "version":1}, {"subject":"subject2",
        "version":2}].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_schema_versions():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListSchemaVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_schema_versions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListSchemaVersionsRequest, dict]]):
                The request object. Request for ListSchemaVersions.
            parent (:class:`str`):
                Required. The schema whose schema versions are to be
                listed. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/schemas/ids/{schema}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.ListSchemaVersionsRequest):
            request = schema_registry.ListSchemaVersionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_schema_versions
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

    async def list_schema_types(
        self,
        request: Optional[Union[schema_registry.ListSchemaTypesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""List the supported schema types.
        The response will be an array of schema types.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_schema_types():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListSchemaTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_schema_types(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListSchemaTypesRequest, dict]]):
                The request object. Request for ListSchemaTypes.
            parent (:class:`str`):
                Required. The parent schema registry whose schema types
                are to be listed. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.ListSchemaTypesRequest):
            request = schema_registry.ListSchemaTypesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_schema_types
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

    async def list_subjects(
        self,
        request: Optional[Union[schema_registry.ListSubjectsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        subject_prefix: Optional[str] = None,
        deleted: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""List subjects in the schema registry.
        The response will be an array of subject names.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_subjects():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListSubjectsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_subjects(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListSubjectsRequest, dict]]):
                The request object. Request for listing subjects.
            parent (:class:`str`):
                Required. The parent schema registry/context whose
                subjects are to be listed. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subject_prefix (:class:`str`):
                Optional. The context to filter the subjects by, in the
                format of ``:.{context}:``. If unset, all subjects in
                the registry are returned. Set to empty string or add as
                '?subjectPrefix=' at the end of this request to list
                subjects in the default context.

                This corresponds to the ``subject_prefix`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deleted (:class:`bool`):
                Optional. If true, the response will
                include soft-deleted subjects. The
                default is false.

                This corresponds to the ``deleted`` field
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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, subject_prefix, deleted]
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
        if not isinstance(request, schema_registry.ListSubjectsRequest):
            request = schema_registry.ListSubjectsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if subject_prefix is not None:
            request.subject_prefix = subject_prefix
        if deleted is not None:
            request.deleted = deleted

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_subjects
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

    async def list_subjects_by_schema_id(
        self,
        request: Optional[
            Union[schema_registry.ListSubjectsBySchemaIdRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        subject: Optional[str] = None,
        deleted: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""List subjects which reference a particular schema id.
        The response will be an array of subject names.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_subjects_by_schema_id():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListSubjectsBySchemaIdRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_subjects_by_schema_id(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListSubjectsBySchemaIdRequest, dict]]):
                The request object. Request for listing subjects.
            parent (:class:`str`):
                Required. The schema resource whose associated subjects
                are to be listed. Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/schemas/ids/{schema}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subject (:class:`str`):
                Optional. The subject to filter the
                subjects by.

                This corresponds to the ``subject`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deleted (:class:`bool`):
                Optional. If true, the response will
                include soft-deleted subjects. The
                default is false.

                This corresponds to the ``deleted`` field
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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, subject, deleted]
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
        if not isinstance(request, schema_registry.ListSubjectsBySchemaIdRequest):
            request = schema_registry.ListSubjectsBySchemaIdRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if subject is not None:
            request.subject = subject
        if deleted is not None:
            request.deleted = deleted

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_subjects_by_schema_id
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

    async def delete_subject(
        self,
        request: Optional[Union[schema_registry.DeleteSubjectRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Delete a subject.
        The response will be an array of versions of the deleted
        subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_delete_subject():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.DeleteSubjectRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.delete_subject(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.DeleteSubjectRequest, dict]]):
                The request object. Request for DeleteSubject.
            name (:class:`str`):
                Required. The name of the subject to delete. Structured
                like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.DeleteSubjectRequest):
            request = schema_registry.DeleteSubjectRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_subject
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

    async def lookup_version(
        self,
        request: Optional[Union[schema_registry.LookupVersionRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        schema: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaVersion:
        r"""Lookup a schema under the specified subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_lookup_version():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.LookupVersionRequest(
                    parent="parent_value",
                    schema="schema_value",
                )

                # Make the request
                response = await client.lookup_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.LookupVersionRequest, dict]]):
                The request object. Request for LookupVersion.
            parent (:class:`str`):
                Required. The subject to lookup the schema in.
                Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            schema (:class:`str`):
                Required. The schema payload
                This corresponds to the ``schema`` field
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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaVersion:
                Version of a schema.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, schema]
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
        if not isinstance(request, schema_registry.LookupVersionRequest):
            request = schema_registry.LookupVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if schema is not None:
            request.schema = schema

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.lookup_version
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
        request: Optional[Union[schema_registry.GetVersionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaVersion:
        r"""Get a versioned schema (schema with subject/version)
        of a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_version():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetVersionRequest, dict]]):
                The request object. Request for GetVersion.
            name (:class:`str`):
                Required. The name of the subject to return versions.
                Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``

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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaVersion:
                Version of a schema.
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
        if not isinstance(request, schema_registry.GetVersionRequest):
            request = schema_registry.GetVersionRequest(request)

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

    async def get_raw_schema_version(
        self,
        request: Optional[Union[schema_registry.GetVersionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Get the schema string only for a version of a
        subject. The response will be the schema string.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_raw_schema_version():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_raw_schema_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetVersionRequest, dict]]):
                The request object. Request for GetVersion.
            name (:class:`str`):
                Required. The name of the subject to return versions.
                Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.GetVersionRequest):
            request = schema_registry.GetVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_raw_schema_version
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
        request: Optional[Union[schema_registry.ListVersionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Get all versions of a subject.
        The response will be an array of versions of the
        subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_versions():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_versions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListVersionsRequest, dict]]):
                The request object. Request for GetVersions.
            parent (:class:`str`):
                Required. The subject whose versions are to be listed.
                Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.ListVersionsRequest):
            request = schema_registry.ListVersionsRequest(request)

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

        # Done; return the response.
        return response

    async def create_version(
        self,
        request: Optional[Union[schema_registry.CreateVersionRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        version: Optional[int] = None,
        id: Optional[int] = None,
        schema_type: Optional[schema_registry_resources.Schema.SchemaType] = None,
        schema: Optional[str] = None,
        references: Optional[
            MutableSequence[schema_registry_resources.Schema.SchemaReference]
        ] = None,
        normalize: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry.CreateVersionResponse:
        r"""Register a new version under a given subject with the
        given schema.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_create_version():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.CreateVersionRequest(
                    parent="parent_value",
                    schema="schema_value",
                )

                # Make the request
                response = await client.create_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.CreateVersionRequest, dict]]):
                The request object. Request for CreateVersion.
            parent (:class:`str`):
                Required. The subject to create the version for.
                Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            version (:class:`int`):
                Optional. The version to create. It
                is optional. If not specified, the
                version will be created with the max
                version ID of the subject increased by
                1. If the version ID is specified, it
                will be used as the new version ID and
                must not be used by an existing version
                of the subject.

                This corresponds to the ``version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (:class:`int`):
                Optional. The schema ID of the
                schema. If not specified, the schema ID
                will be generated by the server. If the
                schema ID is specified, it must not be
                used by an existing schema that is
                different from the schema to be created.

                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            schema_type (:class:`google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType`):
                Optional. The type of the schema. It
                is optional. If not specified, the
                schema type will be AVRO.

                This corresponds to the ``schema_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            schema (:class:`str`):
                Required. The schema payload
                This corresponds to the ``schema`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            references (:class:`MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference]`):
                Optional. The schema references used
                by the schema.

                This corresponds to the ``references`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            normalize (:class:`bool`):
                Optional. If true, the schema will be
                normalized before being stored. The
                default is false.

                This corresponds to the ``normalize`` field
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
            google.cloud.managedkafka_schemaregistry_v1.types.CreateVersionResponse:
                Response for CreateVersion.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            version,
            id,
            schema_type,
            schema,
            references,
            normalize,
        ]
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
        if not isinstance(request, schema_registry.CreateVersionRequest):
            request = schema_registry.CreateVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if version is not None:
            request.version = version
        if id is not None:
            request.id = id
        if schema_type is not None:
            request.schema_type = schema_type
        if schema is not None:
            request.schema = schema
        if normalize is not None:
            request.normalize = normalize
        if references:
            request.references.extend(references)

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

    async def delete_version(
        self,
        request: Optional[Union[schema_registry.DeleteVersionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Delete a version of a subject.
        The response will be the deleted version id.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_delete_version():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.DeleteVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.delete_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.DeleteVersionRequest, dict]]):
                The request object. Request for DeleteVersion.
            name (:class:`str`):
                Required. The name of the subject version to delete.
                Structured like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.DeleteVersionRequest):
            request = schema_registry.DeleteVersionRequest(request)

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
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_referenced_schemas(
        self,
        request: Optional[
            Union[schema_registry.ListReferencedSchemasRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Get a list of IDs of schemas that reference the
        schema with the given subject and version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_list_referenced_schemas():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.ListReferencedSchemasRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_referenced_schemas(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.ListReferencedSchemasRequest, dict]]):
                The request object. Request for ListReferencedSchemas.
            parent (:class:`str`):
                Required. The version to list referenced by. Structured
                like:
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
                or
                ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``

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
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

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
        if not isinstance(request, schema_registry.ListReferencedSchemasRequest):
            request = schema_registry.ListReferencedSchemasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_referenced_schemas
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

    async def check_compatibility(
        self,
        request: Optional[
            Union[schema_registry.CheckCompatibilityRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        schema: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry.CheckCompatibilityResponse:
        r"""Check compatibility of a schema with all versions or
        a specific version of a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_check_compatibility():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.CheckCompatibilityRequest(
                    name="name_value",
                    schema="schema_value",
                )

                # Make the request
                response = await client.check_compatibility(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.CheckCompatibilityRequest, dict]]):
                The request object. Request for CheckCompatibility.
            name (:class:`str`):
                Required. The name of the resource to check
                compatibility for. The format is either of following:

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/\*/versions:
                  Check compatibility with one or more versions of the
                  specified subject.
                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/{subject}/versions/{version}:
                  Check compatibility with a specific version of the
                  subject.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            schema (:class:`str`):
                Required. The schema payload
                This corresponds to the ``schema`` field
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
            google.cloud.managedkafka_schemaregistry_v1.types.CheckCompatibilityResponse:
                Response for CheckCompatibility.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, schema]
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
        if not isinstance(request, schema_registry.CheckCompatibilityRequest):
            request = schema_registry.CheckCompatibilityRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if schema is not None:
            request.schema = schema

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.check_compatibility
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

    async def get_schema_config(
        self,
        request: Optional[Union[schema_registry.GetSchemaConfigRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaConfig:
        r"""Get schema config at global level or for a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_schema_config():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetSchemaConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_schema_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetSchemaConfigRequest, dict]]):
                The request object. Request for getting config.
            name (:class:`str`):
                Required. The resource name to get the config for. It
                can be either of following:

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config:
                  Get config at global level.
                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}:
                  Get config for a specific subject.

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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaConfig:
                SchemaConfig represents configuration
                for a schema registry or a specific
                subject.

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
        if not isinstance(request, schema_registry.GetSchemaConfigRequest):
            request = schema_registry.GetSchemaConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_schema_config
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

    async def update_schema_config(
        self,
        request: Optional[
            Union[schema_registry.UpdateSchemaConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        compatibility: Optional[
            schema_registry_resources.SchemaConfig.CompatibilityType
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaConfig:
        r"""Update config at global level or for a subject.
        Creates a SchemaSubject-level SchemaConfig if it does
        not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_update_schema_config():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.UpdateSchemaConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.update_schema_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.UpdateSchemaConfigRequest, dict]]):
                The request object. Request for updating schema config.
                On a SchemaSubject-level SchemaConfig,
                an unset field will be removed from the
                SchemaConfig.
            name (:class:`str`):
                Required. The resource name to update the config for. It
                can be either of following:

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config:
                  Update config at global level.
                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}:
                  Update config for a specific subject.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            compatibility (:class:`google.cloud.managedkafka_schemaregistry_v1.types.SchemaConfig.CompatibilityType`):
                Required. The compatibility type of
                the schemas. Cannot be unset for a
                SchemaRegistry-level SchemaConfig. If
                unset on a SchemaSubject-level
                SchemaConfig, removes the compatibility
                field for the SchemaConfig.

                This corresponds to the ``compatibility`` field
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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaConfig:
                SchemaConfig represents configuration
                for a schema registry or a specific
                subject.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, compatibility]
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
        if not isinstance(request, schema_registry.UpdateSchemaConfigRequest):
            request = schema_registry.UpdateSchemaConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if compatibility is not None:
            request.compatibility = compatibility

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_schema_config
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

    async def delete_schema_config(
        self,
        request: Optional[
            Union[schema_registry.DeleteSchemaConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaConfig:
        r"""Delete schema config for a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_delete_schema_config():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.DeleteSchemaConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.delete_schema_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.DeleteSchemaConfigRequest, dict]]):
                The request object. Request for deleting schema config.
            name (:class:`str`):
                Required. The resource name of subject to delete the
                config for. The format is

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}

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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaConfig:
                SchemaConfig represents configuration
                for a schema registry or a specific
                subject.

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
        if not isinstance(request, schema_registry.DeleteSchemaConfigRequest):
            request = schema_registry.DeleteSchemaConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_schema_config
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

    async def get_schema_mode(
        self,
        request: Optional[Union[schema_registry.GetSchemaModeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaMode:
        r"""Get mode at global level or for a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_get_schema_mode():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.GetSchemaModeRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_schema_mode(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.GetSchemaModeRequest, dict]]):
                The request object. Request for getting schema registry
                or subject mode.
            name (:class:`str`):
                Required. The resource name of the mode. The format is

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}:
                  mode for a schema registry, or
                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}:
                  mode for a specific subject in a specific context

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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaMode:
                SchemaMode represents the mode of a schema registry or a specific subject.
                   Four modes are supported: \* NONE: deprecated. This
                   was the default mode for a subject, but now the
                   default is unset (which means use the global schema
                   registry setting) \* READONLY: The schema registry is
                   in read-only mode. \* READWRITE: The schema registry
                   is in read-write mode, which allows limited write
                   operations on the schema. \* IMPORT: The schema
                   registry is in import mode, which allows more editing
                   operations on the schema for data importing purposes.

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
        if not isinstance(request, schema_registry.GetSchemaModeRequest):
            request = schema_registry.GetSchemaModeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_schema_mode
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

    async def update_schema_mode(
        self,
        request: Optional[Union[schema_registry.UpdateSchemaModeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        mode: Optional[schema_registry_resources.SchemaMode.ModeType] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaMode:
        r"""Update mode at global level or for a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_update_schema_mode():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.UpdateSchemaModeRequest(
                    name="name_value",
                    mode="IMPORT",
                )

                # Make the request
                response = await client.update_schema_mode(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.UpdateSchemaModeRequest, dict]]):
                The request object. Request for updating schema registry
                or subject mode.
            name (:class:`str`):
                Required. The resource name of the mode. The format is

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}:
                  mode for a schema registry, or
                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}:
                  mode for a specific subject in a specific context

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            mode (:class:`google.cloud.managedkafka_schemaregistry_v1.types.SchemaMode.ModeType`):
                Required. The mode type.
                This corresponds to the ``mode`` field
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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaMode:
                SchemaMode represents the mode of a schema registry or a specific subject.
                   Four modes are supported: \* NONE: deprecated. This
                   was the default mode for a subject, but now the
                   default is unset (which means use the global schema
                   registry setting) \* READONLY: The schema registry is
                   in read-only mode. \* READWRITE: The schema registry
                   is in read-write mode, which allows limited write
                   operations on the schema. \* IMPORT: The schema
                   registry is in import mode, which allows more editing
                   operations on the schema for data importing purposes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, mode]
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
        if not isinstance(request, schema_registry.UpdateSchemaModeRequest):
            request = schema_registry.UpdateSchemaModeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if mode is not None:
            request.mode = mode

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_schema_mode
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

    async def delete_schema_mode(
        self,
        request: Optional[Union[schema_registry.DeleteSchemaModeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> schema_registry_resources.SchemaMode:
        r"""Delete schema mode for a subject.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import managedkafka_schemaregistry_v1

            async def sample_delete_schema_mode():
                # Create a client
                client = managedkafka_schemaregistry_v1.ManagedSchemaRegistryAsyncClient()

                # Initialize request argument(s)
                request = managedkafka_schemaregistry_v1.DeleteSchemaModeRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.delete_schema_mode(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.managedkafka_schemaregistry_v1.types.DeleteSchemaModeRequest, dict]]):
                The request object. Request for deleting schema mode.
            name (:class:`str`):
                Required. The resource name of subject to delete the
                mode for. The format is

                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}
                - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}

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
            google.cloud.managedkafka_schemaregistry_v1.types.SchemaMode:
                SchemaMode represents the mode of a schema registry or a specific subject.
                   Four modes are supported: \* NONE: deprecated. This
                   was the default mode for a subject, but now the
                   default is unset (which means use the global schema
                   registry setting) \* READONLY: The schema registry is
                   in read-only mode. \* READWRITE: The schema registry
                   is in read-write mode, which allows limited write
                   operations on the schema. \* IMPORT: The schema
                   registry is in import mode, which allows more editing
                   operations on the schema for data importing purposes.

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
        if not isinstance(request, schema_registry.DeleteSchemaModeRequest):
            request = schema_registry.DeleteSchemaModeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_schema_mode
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

    async def __aenter__(self) -> "ManagedSchemaRegistryAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ManagedSchemaRegistryAsyncClient",)
