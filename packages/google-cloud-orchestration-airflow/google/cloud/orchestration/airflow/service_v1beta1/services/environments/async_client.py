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

from google.cloud.orchestration.airflow.service_v1beta1 import (
    gapic_version as package_version,
)

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.orchestration.airflow.service_v1beta1.services.environments import (
    pagers,
)
from google.cloud.orchestration.airflow.service_v1beta1.types import (
    environments,
    operations,
)

from .client import EnvironmentsClient
from .transports.base import DEFAULT_CLIENT_INFO, EnvironmentsTransport
from .transports.grpc_asyncio import EnvironmentsGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class EnvironmentsAsyncClient:
    """Managed Apache Airflow Environments."""

    _client: EnvironmentsClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = EnvironmentsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = EnvironmentsClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = EnvironmentsClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = EnvironmentsClient._DEFAULT_UNIVERSE

    environment_path = staticmethod(EnvironmentsClient.environment_path)
    parse_environment_path = staticmethod(EnvironmentsClient.parse_environment_path)
    user_workloads_config_map_path = staticmethod(
        EnvironmentsClient.user_workloads_config_map_path
    )
    parse_user_workloads_config_map_path = staticmethod(
        EnvironmentsClient.parse_user_workloads_config_map_path
    )
    user_workloads_secret_path = staticmethod(
        EnvironmentsClient.user_workloads_secret_path
    )
    parse_user_workloads_secret_path = staticmethod(
        EnvironmentsClient.parse_user_workloads_secret_path
    )
    common_billing_account_path = staticmethod(
        EnvironmentsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        EnvironmentsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(EnvironmentsClient.common_folder_path)
    parse_common_folder_path = staticmethod(EnvironmentsClient.parse_common_folder_path)
    common_organization_path = staticmethod(EnvironmentsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        EnvironmentsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(EnvironmentsClient.common_project_path)
    parse_common_project_path = staticmethod(
        EnvironmentsClient.parse_common_project_path
    )
    common_location_path = staticmethod(EnvironmentsClient.common_location_path)
    parse_common_location_path = staticmethod(
        EnvironmentsClient.parse_common_location_path
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
            EnvironmentsAsyncClient: The constructed client.
        """
        sa_info_func = (
            EnvironmentsClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(EnvironmentsAsyncClient, info, *args, **kwargs)

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
            EnvironmentsAsyncClient: The constructed client.
        """
        sa_file_func = (
            EnvironmentsClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(EnvironmentsAsyncClient, filename, *args, **kwargs)

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
        return EnvironmentsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> EnvironmentsTransport:
        """Returns the transport used by the client instance.

        Returns:
            EnvironmentsTransport: The transport used by the client instance.
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

    get_transport_class = EnvironmentsClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, EnvironmentsTransport, Callable[..., EnvironmentsTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the environments async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,EnvironmentsTransport,Callable[..., EnvironmentsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the EnvironmentsTransport constructor.
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
        self._client = EnvironmentsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.orchestration.airflow.service_v1beta1.EnvironmentsAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.orchestration.airflow.service.v1beta1.Environments",
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
                    "serviceName": "google.cloud.orchestration.airflow.service.v1beta1.Environments",
                    "credentialsType": None,
                },
            )

    async def create_environment(
        self,
        request: Optional[Union[environments.CreateEnvironmentRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        environment: Optional[environments.Environment] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Create a new environment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_create_environment():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.CreateEnvironmentRequest(
                )

                # Make the request
                operation = await client.create_environment(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.CreateEnvironmentRequest, dict]]):
                The request object. Create a new environment.
            parent (:class:`str`):
                The parent must be of the form
                "projects/{projectId}/locations/{locationId}".

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            environment (:class:`google.cloud.orchestration.airflow.service_v1beta1.types.Environment`):
                The environment to create.
                This corresponds to the ``environment`` field
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
                :class:`google.cloud.orchestration.airflow.service_v1beta1.types.Environment`
                An environment for running orchestration tasks.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, environment]
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
        if not isinstance(request, environments.CreateEnvironmentRequest):
            request = environments.CreateEnvironmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if environment is not None:
            request.environment = environment

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_environment
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
            environments.Environment,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_environment(
        self,
        request: Optional[Union[environments.GetEnvironmentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.Environment:
        r"""Get an existing environment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_get_environment():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.GetEnvironmentRequest(
                )

                # Make the request
                response = await client.get_environment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.GetEnvironmentRequest, dict]]):
                The request object. Get an environment.
            name (:class:`str`):
                The resource name of the environment
                to get, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.types.Environment:
                An environment for running
                orchestration tasks.

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
        if not isinstance(request, environments.GetEnvironmentRequest):
            request = environments.GetEnvironmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_environment
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

    async def list_environments(
        self,
        request: Optional[Union[environments.ListEnvironmentsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEnvironmentsAsyncPager:
        r"""List environments.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_list_environments():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.ListEnvironmentsRequest(
                )

                # Make the request
                page_result = client.list_environments(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.ListEnvironmentsRequest, dict]]):
                The request object. List environments in a project and
                location.
            parent (:class:`str`):
                List environments in the given
                project and location, in the form:
                "projects/{projectId}/locations/{locationId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.services.environments.pagers.ListEnvironmentsAsyncPager:
                The environments in a project and
                location.
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
        if not isinstance(request, environments.ListEnvironmentsRequest):
            request = environments.ListEnvironmentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_environments
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
        response = pagers.ListEnvironmentsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_environment(
        self,
        request: Optional[Union[environments.UpdateEnvironmentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        environment: Optional[environments.Environment] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Update an environment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_update_environment():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.UpdateEnvironmentRequest(
                )

                # Make the request
                operation = await client.update_environment(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.UpdateEnvironmentRequest, dict]]):
                The request object. Update an environment.
            name (:class:`str`):
                The relative resource name of the
                environment to update, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            environment (:class:`google.cloud.orchestration.airflow.service_v1beta1.types.Environment`):
                A patch environment. Fields specified by the
                ``updateMask`` will be copied from the patch environment
                into the environment under update.

                This corresponds to the ``environment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. A comma-separated list of paths, relative to
                ``Environment``, of fields to update. For example, to
                set the version of scikit-learn to install in the
                environment to 0.19.0 and to remove an existing
                installation of argparse, the ``updateMask`` parameter
                would include the following two ``paths`` values:
                "config.softwareConfig.pypiPackages.scikit-learn" and
                "config.softwareConfig.pypiPackages.argparse". The
                included patch environment would specify the
                scikit-learn version as follows:

                ::

                    {
                      "config":{
                        "softwareConfig":{
                          "pypiPackages":{
                            "scikit-learn":"==0.19.0"
                          }
                        }
                      }
                    }

                Note that in the above example, any existing PyPI
                packages other than scikit-learn and argparse will be
                unaffected.

                Only one update type may be included in a single
                request's ``updateMask``. For example, one cannot update
                both the PyPI packages and labels in the same request.
                However, it is possible to update multiple members of a
                map field simultaneously in the same request. For
                example, to set the labels "label1" and "label2" while
                clearing "label3" (assuming it already exists), one can
                provide the paths "labels.label1", "labels.label2", and
                "labels.label3" and populate the patch environment as
                follows:

                ::

                    {
                      "labels":{
                        "label1":"new-label1-value"
                        "label2":"new-label2-value"
                      }
                    }

                Note that in the above example, any existing labels that
                are not included in the ``updateMask`` will be
                unaffected.

                It is also possible to replace an entire map field by
                providing the map field's path in the ``updateMask``.
                The new value of the field will be that which is
                provided in the patch environment. For example, to
                delete all pre-existing user-specified PyPI packages and
                install botocore at version 1.7.14, the ``updateMask``
                would contain the path
                "config.softwareConfig.pypiPackages", and the patch
                environment would be the following:

                ::

                    {
                      "config":{
                        "softwareConfig":{
                          "pypiPackages":{
                            "botocore":"==1.7.14"
                          }
                        }
                      }
                    }

                **Note:** Only the following fields can be updated:

                - ``config.softwareConfig.pypiPackages``

                  - Replace all custom custom PyPI packages. If a
                    replacement package map is not included in
                    ``environment``, all custom PyPI packages are
                    cleared. It is an error to provide both this mask
                    and a mask specifying an individual package.

                - ``config.softwareConfig.pypiPackages.``\ packagename

                  - Update the custom PyPI package *packagename*,
                    preserving other packages. To delete the package,
                    include it in ``updateMask``, and omit the mapping
                    for it in
                    ``environment.config.softwareConfig.pypiPackages``.
                    It is an error to provide both a mask of this form
                    and the ``config.softwareConfig.pypiPackages`` mask.

                - ``labels``

                  - Replace all environment labels. If a replacement
                    labels map is not included in ``environment``, all
                    labels are cleared. It is an error to provide both
                    this mask and a mask specifying one or more
                    individual labels.

                - ``labels.``\ labelName

                  - Set the label named *labelName*, while preserving
                    other labels. To delete the label, include it in
                    ``updateMask`` and omit its mapping in
                    ``environment.labels``. It is an error to provide
                    both a mask of this form and the ``labels`` mask.

                - ``config.nodeCount``

                  - Horizontally scale the number of nodes in the
                    environment. An integer greater than or equal to 3
                    must be provided in the ``config.nodeCount`` field.
                    Supported for Cloud Composer environments in
                    versions composer-1.\ *.*-airflow-*.*.\*.

                - ``config.webServerNetworkAccessControl``

                  - Replace the environment's current
                    WebServerNetworkAccessControl.

                - ``config.softwareConfig.airflowConfigOverrides``

                  - Replace all Apache Airflow config overrides. If a
                    replacement config overrides map is not included in
                    ``environment``, all config overrides are cleared.
                    It is an error to provide both this mask and a mask
                    specifying one or more individual config overrides.

                - ``config.softwareConfig.airflowConfigOverrides.``\ section-name

                  - Override the Apache Airflow config property *name*
                    in the section named *section*, preserving other
                    properties. To delete the property override, include
                    it in ``updateMask`` and omit its mapping in
                    ``environment.config.softwareConfig.airflowConfigOverrides``.
                    It is an error to provide both a mask of this form
                    and the
                    ``config.softwareConfig.airflowConfigOverrides``
                    mask.

                - ``config.softwareConfig.envVariables``

                  - Replace all environment variables. If a replacement
                    environment variable map is not included in
                    ``environment``, all custom environment variables
                    are cleared.

                - ``config.softwareConfig.imageVersion``

                  - Upgrade the version of the environment in-place.
                    Refer to ``SoftwareConfig.image_version`` for
                    information on how to format the new image version.
                    Additionally, the new image version cannot effect a
                    version downgrade, and must match the current image
                    version's Composer and Airflow major versions.
                    Consult the `Cloud Composer version
                    list </composer/docs/concepts/versioning/composer-versions>`__
                    for valid values.

                - ``config.softwareConfig.schedulerCount``

                  - Horizontally scale the number of schedulers in
                    Airflow. A positive integer not greater than the
                    number of nodes must be provided in the
                    ``config.softwareConfig.schedulerCount`` field.
                    Supported for Cloud Composer environments in
                    versions composer-1.\ *.*-airflow-2.\ *.*.

                - ``config.softwareConfig.cloudDataLineageIntegration``

                  - Configuration for Cloud Data Lineage integration.

                - ``config.databaseConfig.machineType``

                  - Cloud SQL machine type used by Airflow database. It
                    has to be one of: db-n1-standard-2,
                    db-n1-standard-4, db-n1-standard-8 or
                    db-n1-standard-16. Supported for Cloud Composer
                    environments in versions
                    composer-1.\ *.*-airflow-*.*.\*.

                - ``config.webServerConfig.machineType``

                  - Machine type on which Airflow web server is running.
                    It has to be one of: composer-n1-webserver-2,
                    composer-n1-webserver-4 or composer-n1-webserver-8.
                    Supported for Cloud Composer environments in
                    versions composer-1.\ *.*-airflow-*.*.\*.

                - ``config.maintenanceWindow``

                  - Maintenance window during which Cloud Composer
                    components may be under maintenance.

                - ``config.workloadsConfig``

                  - The workloads configuration settings for the GKE
                    cluster associated with the Cloud Composer
                    environment. Supported for Cloud Composer
                    environments in versions
                    composer-2.\ *.*-airflow-*.*.\* and newer.

                - ``config.environmentSize``

                  - The size of the Cloud Composer environment.
                    Supported for Cloud Composer environments in
                    versions composer-2.\ *.*-airflow-*.*.\* and newer.

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
                :class:`google.cloud.orchestration.airflow.service_v1beta1.types.Environment`
                An environment for running orchestration tasks.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, environment, update_mask]
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
        if not isinstance(request, environments.UpdateEnvironmentRequest):
            request = environments.UpdateEnvironmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if environment is not None:
            request.environment = environment
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_environment
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
            environments.Environment,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_environment(
        self,
        request: Optional[Union[environments.DeleteEnvironmentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Delete an environment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_delete_environment():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.DeleteEnvironmentRequest(
                )

                # Make the request
                operation = await client.delete_environment(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.DeleteEnvironmentRequest, dict]]):
                The request object. Delete an environment.
            name (:class:`str`):
                The environment to delete, in the
                form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

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
        if not isinstance(request, environments.DeleteEnvironmentRequest):
            request = environments.DeleteEnvironmentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_environment
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
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def restart_web_server(
        self,
        request: Optional[Union[environments.RestartWebServerRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Restart Airflow web server.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_restart_web_server():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.RestartWebServerRequest(
                )

                # Make the request
                operation = await client.restart_web_server(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.RestartWebServerRequest, dict]]):
                The request object. Restart Airflow web server.
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
                :class:`google.cloud.orchestration.airflow.service_v1beta1.types.Environment`
                An environment for running orchestration tasks.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.RestartWebServerRequest):
            request = environments.RestartWebServerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.restart_web_server
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
            environments.Environment,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def check_upgrade(
        self,
        request: Optional[Union[environments.CheckUpgradeRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Check if an upgrade operation on the environment will
        succeed.
        In case of problems detailed info can be found in the
        returned Operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_check_upgrade():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.CheckUpgradeRequest(
                )

                # Make the request
                operation = await client.check_upgrade(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.CheckUpgradeRequest, dict]]):
                The request object. Request to check whether image
                upgrade will succeed.
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

                The result type for the operation will be :class:`google.cloud.orchestration.airflow.service_v1beta1.types.CheckUpgradeResponse` Message containing information about the result of an upgrade check
                   operation.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.CheckUpgradeRequest):
            request = environments.CheckUpgradeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.check_upgrade
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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
            environments.CheckUpgradeResponse,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def execute_airflow_command(
        self,
        request: Optional[
            Union[environments.ExecuteAirflowCommandRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.ExecuteAirflowCommandResponse:
        r"""Executes Airflow CLI command.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_execute_airflow_command():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.ExecuteAirflowCommandRequest(
                )

                # Make the request
                response = await client.execute_airflow_command(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.ExecuteAirflowCommandRequest, dict]]):
                The request object. Execute Airflow Command request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.orchestration.airflow.service_v1beta1.types.ExecuteAirflowCommandResponse:
                Response to
                ExecuteAirflowCommandRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.ExecuteAirflowCommandRequest):
            request = environments.ExecuteAirflowCommandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.execute_airflow_command
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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

    async def stop_airflow_command(
        self,
        request: Optional[Union[environments.StopAirflowCommandRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.StopAirflowCommandResponse:
        r"""Stops Airflow CLI command execution.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_stop_airflow_command():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.StopAirflowCommandRequest(
                )

                # Make the request
                response = await client.stop_airflow_command(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.StopAirflowCommandRequest, dict]]):
                The request object. Stop Airflow Command request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.orchestration.airflow.service_v1beta1.types.StopAirflowCommandResponse:
                Response to
                StopAirflowCommandRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.StopAirflowCommandRequest):
            request = environments.StopAirflowCommandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.stop_airflow_command
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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

    async def poll_airflow_command(
        self,
        request: Optional[Union[environments.PollAirflowCommandRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.PollAirflowCommandResponse:
        r"""Polls Airflow CLI command execution and fetches logs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_poll_airflow_command():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.PollAirflowCommandRequest(
                )

                # Make the request
                response = await client.poll_airflow_command(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.PollAirflowCommandRequest, dict]]):
                The request object. Poll Airflow Command request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.orchestration.airflow.service_v1beta1.types.PollAirflowCommandResponse:
                Response to
                PollAirflowCommandRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.PollAirflowCommandRequest):
            request = environments.PollAirflowCommandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.poll_airflow_command
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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

    async def list_workloads(
        self,
        request: Optional[Union[environments.ListWorkloadsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListWorkloadsAsyncPager:
        r"""Lists workloads in a Cloud Composer environment. Workload is a
        unit that runs a single Composer component.

        This method is supported for Cloud Composer environments in
        versions composer-2.\ *.*-airflow-*.*.\* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_list_workloads():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.ListWorkloadsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_workloads(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsRequest, dict]]):
                The request object. Request for listing workloads in a
                Cloud Composer environment.
            parent (:class:`str`):
                Required. The environment name to get
                workloads for, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.services.environments.pagers.ListWorkloadsAsyncPager:
                Response to ListWorkloadsRequest.

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
        if not isinstance(request, environments.ListWorkloadsRequest):
            request = environments.ListWorkloadsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_workloads
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
        response = pagers.ListWorkloadsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_user_workloads_secret(
        self,
        request: Optional[
            Union[environments.CreateUserWorkloadsSecretRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        user_workloads_secret: Optional[environments.UserWorkloadsSecret] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.UserWorkloadsSecret:
        r"""Creates a user workloads Secret.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_create_user_workloads_secret():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.CreateUserWorkloadsSecretRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_user_workloads_secret(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.CreateUserWorkloadsSecretRequest, dict]]):
                The request object. Create user workloads Secret request.
            parent (:class:`str`):
                Required. The environment name to
                create a Secret for, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_workloads_secret (:class:`google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret`):
                Required. User workloads Secret to
                create.

                This corresponds to the ``user_workloads_secret`` field
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
            google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret:
                User workloads Secret used by Airflow
                tasks that run with Kubernetes executor
                or KubernetesPodOperator.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_workloads_secret]
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
        if not isinstance(request, environments.CreateUserWorkloadsSecretRequest):
            request = environments.CreateUserWorkloadsSecretRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if user_workloads_secret is not None:
            request.user_workloads_secret = user_workloads_secret

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_user_workloads_secret
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

    async def get_user_workloads_secret(
        self,
        request: Optional[
            Union[environments.GetUserWorkloadsSecretRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.UserWorkloadsSecret:
        r"""Gets an existing user workloads Secret. Values of the "data"
        field in the response are cleared.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_get_user_workloads_secret():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.GetUserWorkloadsSecretRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_user_workloads_secret(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.GetUserWorkloadsSecretRequest, dict]]):
                The request object. Get user workloads Secret request.
            name (:class:`str`):
                Required. The resource name of the
                Secret to get, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret:
                User workloads Secret used by Airflow
                tasks that run with Kubernetes executor
                or KubernetesPodOperator.

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
        if not isinstance(request, environments.GetUserWorkloadsSecretRequest):
            request = environments.GetUserWorkloadsSecretRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_user_workloads_secret
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

    async def list_user_workloads_secrets(
        self,
        request: Optional[
            Union[environments.ListUserWorkloadsSecretsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserWorkloadsSecretsAsyncPager:
        r"""Lists user workloads Secrets.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_list_user_workloads_secrets():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.ListUserWorkloadsSecretsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_workloads_secrets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.ListUserWorkloadsSecretsRequest, dict]]):
                The request object. List user workloads Secrets request.
            parent (:class:`str`):
                Required. List Secrets in the given
                environment, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.services.environments.pagers.ListUserWorkloadsSecretsAsyncPager:
                The user workloads Secrets for a
                given environment.
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
        if not isinstance(request, environments.ListUserWorkloadsSecretsRequest):
            request = environments.ListUserWorkloadsSecretsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_user_workloads_secrets
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
        response = pagers.ListUserWorkloadsSecretsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_user_workloads_secret(
        self,
        request: Optional[
            Union[environments.UpdateUserWorkloadsSecretRequest, dict]
        ] = None,
        *,
        user_workloads_secret: Optional[environments.UserWorkloadsSecret] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.UserWorkloadsSecret:
        r"""Updates a user workloads Secret.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_update_user_workloads_secret():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.UpdateUserWorkloadsSecretRequest(
                )

                # Make the request
                response = await client.update_user_workloads_secret(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.UpdateUserWorkloadsSecretRequest, dict]]):
                The request object. Update user workloads Secret request.
            user_workloads_secret (:class:`google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret`):
                Optional. User workloads Secret to
                override.

                This corresponds to the ``user_workloads_secret`` field
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
            google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret:
                User workloads Secret used by Airflow
                tasks that run with Kubernetes executor
                or KubernetesPodOperator.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [user_workloads_secret]
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
        if not isinstance(request, environments.UpdateUserWorkloadsSecretRequest):
            request = environments.UpdateUserWorkloadsSecretRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if user_workloads_secret is not None:
            request.user_workloads_secret = user_workloads_secret

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_user_workloads_secret
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("user_workloads_secret.name", request.user_workloads_secret.name),)
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

    async def delete_user_workloads_secret(
        self,
        request: Optional[
            Union[environments.DeleteUserWorkloadsSecretRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a user workloads Secret.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_delete_user_workloads_secret():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.DeleteUserWorkloadsSecretRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_user_workloads_secret(request=request)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.DeleteUserWorkloadsSecretRequest, dict]]):
                The request object. Delete user workloads Secret request.
            name (:class:`str`):
                Required. The Secret to delete, in
                the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"

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
        if not isinstance(request, environments.DeleteUserWorkloadsSecretRequest):
            request = environments.DeleteUserWorkloadsSecretRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_user_workloads_secret
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

    async def create_user_workloads_config_map(
        self,
        request: Optional[
            Union[environments.CreateUserWorkloadsConfigMapRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        user_workloads_config_map: Optional[environments.UserWorkloadsConfigMap] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.UserWorkloadsConfigMap:
        r"""Creates a user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_create_user_workloads_config_map():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.CreateUserWorkloadsConfigMapRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_user_workloads_config_map(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.CreateUserWorkloadsConfigMapRequest, dict]]):
                The request object. Create user workloads ConfigMap
                request.
            parent (:class:`str`):
                Required. The environment name to
                create a ConfigMap for, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_workloads_config_map (:class:`google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap`):
                Required. User workloads ConfigMap to
                create.

                This corresponds to the ``user_workloads_config_map`` field
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
            google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap:
                User workloads ConfigMap used by
                Airflow tasks that run with Kubernetes
                executor or KubernetesPodOperator.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_workloads_config_map]
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
        if not isinstance(request, environments.CreateUserWorkloadsConfigMapRequest):
            request = environments.CreateUserWorkloadsConfigMapRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if user_workloads_config_map is not None:
            request.user_workloads_config_map = user_workloads_config_map

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_user_workloads_config_map
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

    async def get_user_workloads_config_map(
        self,
        request: Optional[
            Union[environments.GetUserWorkloadsConfigMapRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.UserWorkloadsConfigMap:
        r"""Gets an existing user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_get_user_workloads_config_map():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.GetUserWorkloadsConfigMapRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_user_workloads_config_map(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.GetUserWorkloadsConfigMapRequest, dict]]):
                The request object. Get user workloads ConfigMap request.
            name (:class:`str`):
                Required. The resource name of the
                ConfigMap to get, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap:
                User workloads ConfigMap used by
                Airflow tasks that run with Kubernetes
                executor or KubernetesPodOperator.

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
        if not isinstance(request, environments.GetUserWorkloadsConfigMapRequest):
            request = environments.GetUserWorkloadsConfigMapRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_user_workloads_config_map
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

    async def list_user_workloads_config_maps(
        self,
        request: Optional[
            Union[environments.ListUserWorkloadsConfigMapsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserWorkloadsConfigMapsAsyncPager:
        r"""Lists user workloads ConfigMaps.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_list_user_workloads_config_maps():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.ListUserWorkloadsConfigMapsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_workloads_config_maps(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.ListUserWorkloadsConfigMapsRequest, dict]]):
                The request object. List user workloads ConfigMaps
                request.
            parent (:class:`str`):
                Required. List ConfigMaps in the
                given environment, in the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

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
            google.cloud.orchestration.airflow.service_v1beta1.services.environments.pagers.ListUserWorkloadsConfigMapsAsyncPager:
                The user workloads ConfigMaps for a
                given environment.
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
        if not isinstance(request, environments.ListUserWorkloadsConfigMapsRequest):
            request = environments.ListUserWorkloadsConfigMapsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_user_workloads_config_maps
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
        response = pagers.ListUserWorkloadsConfigMapsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_user_workloads_config_map(
        self,
        request: Optional[
            Union[environments.UpdateUserWorkloadsConfigMapRequest, dict]
        ] = None,
        *,
        user_workloads_config_map: Optional[environments.UserWorkloadsConfigMap] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.UserWorkloadsConfigMap:
        r"""Updates a user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_update_user_workloads_config_map():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.UpdateUserWorkloadsConfigMapRequest(
                )

                # Make the request
                response = await client.update_user_workloads_config_map(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.UpdateUserWorkloadsConfigMapRequest, dict]]):
                The request object. Update user workloads ConfigMap
                request.
            user_workloads_config_map (:class:`google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap`):
                Optional. User workloads ConfigMap to
                override.

                This corresponds to the ``user_workloads_config_map`` field
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
            google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap:
                User workloads ConfigMap used by
                Airflow tasks that run with Kubernetes
                executor or KubernetesPodOperator.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [user_workloads_config_map]
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
        if not isinstance(request, environments.UpdateUserWorkloadsConfigMapRequest):
            request = environments.UpdateUserWorkloadsConfigMapRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if user_workloads_config_map is not None:
            request.user_workloads_config_map = user_workloads_config_map

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_user_workloads_config_map
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "user_workloads_config_map.name",
                        request.user_workloads_config_map.name,
                    ),
                )
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

    async def delete_user_workloads_config_map(
        self,
        request: Optional[
            Union[environments.DeleteUserWorkloadsConfigMapRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_delete_user_workloads_config_map():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.DeleteUserWorkloadsConfigMapRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_user_workloads_config_map(request=request)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.DeleteUserWorkloadsConfigMapRequest, dict]]):
                The request object. Delete user workloads ConfigMap
                request.
            name (:class:`str`):
                Required. The ConfigMap to delete, in
                the form:
                "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"

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
        if not isinstance(request, environments.DeleteUserWorkloadsConfigMapRequest):
            request = environments.DeleteUserWorkloadsConfigMapRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_user_workloads_config_map
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

    async def save_snapshot(
        self,
        request: Optional[Union[environments.SaveSnapshotRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a snapshots of a Cloud Composer environment.

        As a result of this operation, snapshot of environment's
        state is stored in a location specified in the
        SaveSnapshotRequest.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_save_snapshot():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.SaveSnapshotRequest(
                )

                # Make the request
                operation = await client.save_snapshot(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.SaveSnapshotRequest, dict]]):
                The request object. Request to create a snapshot of a
                Cloud Composer environment.
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
                :class:`google.cloud.orchestration.airflow.service_v1beta1.types.SaveSnapshotResponse`
                Response to SaveSnapshotRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.SaveSnapshotRequest):
            request = environments.SaveSnapshotRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.save_snapshot
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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
            environments.SaveSnapshotResponse,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def load_snapshot(
        self,
        request: Optional[Union[environments.LoadSnapshotRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Loads a snapshot of a Cloud Composer environment.

        As a result of this operation, a snapshot of
        environment's specified in LoadSnapshotRequest is loaded
        into the environment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_load_snapshot():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.LoadSnapshotRequest(
                )

                # Make the request
                operation = await client.load_snapshot(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.LoadSnapshotRequest, dict]]):
                The request object. Request to load a snapshot into a
                Cloud Composer environment.
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
                :class:`google.cloud.orchestration.airflow.service_v1beta1.types.LoadSnapshotResponse`
                Response to LoadSnapshotRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.LoadSnapshotRequest):
            request = environments.LoadSnapshotRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.load_snapshot
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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
            environments.LoadSnapshotResponse,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def database_failover(
        self,
        request: Optional[Union[environments.DatabaseFailoverRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Triggers database failover (only for highly resilient
        environments).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_database_failover():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.DatabaseFailoverRequest(
                )

                # Make the request
                operation = await client.database_failover(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.DatabaseFailoverRequest, dict]]):
                The request object. Request to trigger database failover
                (only for highly resilient
                environments).
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
                :class:`google.cloud.orchestration.airflow.service_v1beta1.types.DatabaseFailoverResponse`
                Response for DatabaseFailoverRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.DatabaseFailoverRequest):
            request = environments.DatabaseFailoverRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.database_failover
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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
            environments.DatabaseFailoverResponse,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def fetch_database_properties(
        self,
        request: Optional[
            Union[environments.FetchDatabasePropertiesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> environments.FetchDatabasePropertiesResponse:
        r"""Fetches database properties.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.orchestration.airflow import service_v1beta1

            async def sample_fetch_database_properties():
                # Create a client
                client = service_v1beta1.EnvironmentsAsyncClient()

                # Initialize request argument(s)
                request = service_v1beta1.FetchDatabasePropertiesRequest(
                    environment="environment_value",
                )

                # Make the request
                response = await client.fetch_database_properties(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orchestration.airflow.service_v1beta1.types.FetchDatabasePropertiesRequest, dict]]):
                The request object. Request to fetch properties of
                environment's database.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.orchestration.airflow.service_v1beta1.types.FetchDatabasePropertiesResponse:
                Response for
                FetchDatabasePropertiesRequest.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, environments.FetchDatabasePropertiesRequest):
            request = environments.FetchDatabasePropertiesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_database_properties
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("environment", request.environment),)
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

    async def __aenter__(self) -> "EnvironmentsAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("EnvironmentsAsyncClient",)
