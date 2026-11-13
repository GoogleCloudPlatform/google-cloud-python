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

from google.cloud.backupdr_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.backupdr_v1.services.backup_dr import pagers
from google.cloud.backupdr_v1.types import (
    appliedautoprotectionpolicy,
    autoprotectionpolicy,
    autoprotectionpolicybinding,
    backupdr,
    backupplan,
    backupplanassociation,
    backupvault,
    backupvault_alloydb,
    backupvault_ba,
    backupvault_cloudsql,
    backupvault_disk,
    backupvault_gce,
    bindingmatchingresource,
    datasourcereference,
    restore_template,
    restore_template_common,
    restore_template_execution,
    restore_verification_plan,
    restore_verification_plan_association,
)
from google.cloud.backupdr_v1.types import restore_template as gcb_restore_template
from google.cloud.backupdr_v1.types import (
    restore_verification_plan as gcb_restore_verification_plan,
)
from google.cloud.backupdr_v1.types import (
    restore_verification_plan_association as gcb_restore_verification_plan_association,
)

from .client import BackupDRClient
from .transports.base import DEFAULT_CLIENT_INFO, BackupDRTransport
from .transports.grpc_asyncio import BackupDRGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class BackupDRAsyncClient:
    """The BackupDR Service"""

    _client: BackupDRClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = BackupDRClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = BackupDRClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = BackupDRClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = BackupDRClient._DEFAULT_UNIVERSE

    applied_auto_protection_policy_path = staticmethod(
        BackupDRClient.applied_auto_protection_policy_path
    )
    parse_applied_auto_protection_policy_path = staticmethod(
        BackupDRClient.parse_applied_auto_protection_policy_path
    )
    auto_protection_policy_path = staticmethod(
        BackupDRClient.auto_protection_policy_path
    )
    parse_auto_protection_policy_path = staticmethod(
        BackupDRClient.parse_auto_protection_policy_path
    )
    auto_protection_policy_binding_path = staticmethod(
        BackupDRClient.auto_protection_policy_binding_path
    )
    parse_auto_protection_policy_binding_path = staticmethod(
        BackupDRClient.parse_auto_protection_policy_binding_path
    )
    backup_path = staticmethod(BackupDRClient.backup_path)
    parse_backup_path = staticmethod(BackupDRClient.parse_backup_path)
    backup_plan_path = staticmethod(BackupDRClient.backup_plan_path)
    parse_backup_plan_path = staticmethod(BackupDRClient.parse_backup_plan_path)
    backup_plan_association_path = staticmethod(
        BackupDRClient.backup_plan_association_path
    )
    parse_backup_plan_association_path = staticmethod(
        BackupDRClient.parse_backup_plan_association_path
    )
    backup_plan_revision_path = staticmethod(BackupDRClient.backup_plan_revision_path)
    parse_backup_plan_revision_path = staticmethod(
        BackupDRClient.parse_backup_plan_revision_path
    )
    backup_vault_path = staticmethod(BackupDRClient.backup_vault_path)
    parse_backup_vault_path = staticmethod(BackupDRClient.parse_backup_vault_path)
    binding_matching_resource_path = staticmethod(
        BackupDRClient.binding_matching_resource_path
    )
    parse_binding_matching_resource_path = staticmethod(
        BackupDRClient.parse_binding_matching_resource_path
    )
    cluster_path = staticmethod(BackupDRClient.cluster_path)
    parse_cluster_path = staticmethod(BackupDRClient.parse_cluster_path)
    crypto_key_path = staticmethod(BackupDRClient.crypto_key_path)
    parse_crypto_key_path = staticmethod(BackupDRClient.parse_crypto_key_path)
    crypto_key_version_path = staticmethod(BackupDRClient.crypto_key_version_path)
    parse_crypto_key_version_path = staticmethod(
        BackupDRClient.parse_crypto_key_version_path
    )
    data_source_path = staticmethod(BackupDRClient.data_source_path)
    parse_data_source_path = staticmethod(BackupDRClient.parse_data_source_path)
    data_source_reference_path = staticmethod(BackupDRClient.data_source_reference_path)
    parse_data_source_reference_path = staticmethod(
        BackupDRClient.parse_data_source_reference_path
    )
    execution_path = staticmethod(BackupDRClient.execution_path)
    parse_execution_path = staticmethod(BackupDRClient.parse_execution_path)
    instance_path = staticmethod(BackupDRClient.instance_path)
    parse_instance_path = staticmethod(BackupDRClient.parse_instance_path)
    job_path = staticmethod(BackupDRClient.job_path)
    parse_job_path = staticmethod(BackupDRClient.parse_job_path)
    management_server_path = staticmethod(BackupDRClient.management_server_path)
    parse_management_server_path = staticmethod(
        BackupDRClient.parse_management_server_path
    )
    restore_template_path = staticmethod(BackupDRClient.restore_template_path)
    parse_restore_template_path = staticmethod(
        BackupDRClient.parse_restore_template_path
    )
    restore_template_execution_path = staticmethod(
        BackupDRClient.restore_template_execution_path
    )
    parse_restore_template_execution_path = staticmethod(
        BackupDRClient.parse_restore_template_execution_path
    )
    restore_verification_plan_path = staticmethod(
        BackupDRClient.restore_verification_plan_path
    )
    parse_restore_verification_plan_path = staticmethod(
        BackupDRClient.parse_restore_verification_plan_path
    )
    restore_verification_plan_association_path = staticmethod(
        BackupDRClient.restore_verification_plan_association_path
    )
    parse_restore_verification_plan_association_path = staticmethod(
        BackupDRClient.parse_restore_verification_plan_association_path
    )
    storage_pool_path = staticmethod(BackupDRClient.storage_pool_path)
    parse_storage_pool_path = staticmethod(BackupDRClient.parse_storage_pool_path)
    common_billing_account_path = staticmethod(
        BackupDRClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        BackupDRClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(BackupDRClient.common_folder_path)
    parse_common_folder_path = staticmethod(BackupDRClient.parse_common_folder_path)
    common_organization_path = staticmethod(BackupDRClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        BackupDRClient.parse_common_organization_path
    )
    common_project_path = staticmethod(BackupDRClient.common_project_path)
    parse_common_project_path = staticmethod(BackupDRClient.parse_common_project_path)
    common_location_path = staticmethod(BackupDRClient.common_location_path)
    parse_common_location_path = staticmethod(BackupDRClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            BackupDRAsyncClient: The constructed client.
        """
        sa_info_func = (
            BackupDRClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(BackupDRAsyncClient, info, *args, **kwargs)

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
            BackupDRAsyncClient: The constructed client.
        """
        sa_file_func = (
            BackupDRClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(BackupDRAsyncClient, filename, *args, **kwargs)

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
        return BackupDRClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> BackupDRTransport:
        """Returns the transport used by the client instance.

        Returns:
            BackupDRTransport: The transport used by the client instance.
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

    get_transport_class = BackupDRClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, BackupDRTransport, Callable[..., BackupDRTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the backup dr async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,BackupDRTransport,Callable[..., BackupDRTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the BackupDRTransport constructor.
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
        self._client = BackupDRClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.backupdr_v1.BackupDRAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.backupdr.v1.BackupDR",
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
                    "serviceName": "google.cloud.backupdr.v1.BackupDR",
                    "credentialsType": None,
                },
            )

    async def list_management_servers(
        self,
        request: Optional[Union[backupdr.ListManagementServersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListManagementServersAsyncPager:
        r"""Lists ManagementServers in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_management_servers():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListManagementServersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_management_servers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListManagementServersRequest, dict]]):
                The request object. Request message for listing
                management servers.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                management servers information, in the format
                'projects/{project_id}/locations/{location}'. In Cloud
                BackupDR, locations map to Google Cloud regions, for
                example **us-central1**. To retrieve management servers
                for all locations, use "-" for the '{location}' value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager:
                Response message for listing
                management servers.
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
        if not isinstance(request, backupdr.ListManagementServersRequest):
            request = backupdr.ListManagementServersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_management_servers
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
        response = pagers.ListManagementServersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_management_server(
        self,
        request: Optional[Union[backupdr.GetManagementServerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupdr.ManagementServer:
        r"""Gets details of a single ManagementServer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_management_server():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetManagementServerRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_management_server(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetManagementServerRequest, dict]]):
                The request object. Request message for getting a
                management server instance.
            name (:class:`str`):
                Required. Name of the management server resource name,
                in the format
                'projects/{project_id}/locations/{location}/managementServers/{resource_name}'

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
            google.cloud.backupdr_v1.types.ManagementServer:
                ManagementServer describes a single
                BackupDR ManagementServer instance.

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
        if not isinstance(request, backupdr.GetManagementServerRequest):
            request = backupdr.GetManagementServerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_management_server
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

    async def create_management_server(
        self,
        request: Optional[Union[backupdr.CreateManagementServerRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        management_server: Optional[backupdr.ManagementServer] = None,
        management_server_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new ManagementServer in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_management_server():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.CreateManagementServerRequest(
                    parent="parent_value",
                    management_server_id="management_server_id_value",
                )

                # Make the request
                operation = await client.create_management_server(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateManagementServerRequest, dict]]):
                The request object. Request message for creating a
                management server instance.
            parent (:class:`str`):
                Required. The management server project and location in
                the format 'projects/{project_id}/locations/{location}'.
                In Cloud Backup and DR locations map to Google Cloud
                regions, for example **us-central1**.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            management_server (:class:`google.cloud.backupdr_v1.types.ManagementServer`):
                Required. A [management server
                resource][google.cloud.backupdr.v1.ManagementServer]

                This corresponds to the ``management_server`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            management_server_id (:class:`str`):
                Required. The name of the management
                server to create. The name must be
                unique for the specified project and
                location.

                This corresponds to the ``management_server_id`` field
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
                :class:`google.cloud.backupdr_v1.types.ManagementServer`
                ManagementServer describes a single BackupDR
                ManagementServer instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, management_server, management_server_id]
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
        if not isinstance(request, backupdr.CreateManagementServerRequest):
            request = backupdr.CreateManagementServerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if management_server is not None:
            request.management_server = management_server
        if management_server_id is not None:
            request.management_server_id = management_server_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_management_server
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
            backupdr.ManagementServer,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_management_server(
        self,
        request: Optional[Union[backupdr.DeleteManagementServerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single ManagementServer.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_management_server():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteManagementServerRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_management_server(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteManagementServerRequest, dict]]):
                The request object. Request message for deleting a
                management server instance.
            name (:class:`str`):
                Required. Name of the resource
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
        if not isinstance(request, backupdr.DeleteManagementServerRequest):
            request = backupdr.DeleteManagementServerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_management_server
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_backup_vault(
        self,
        request: Optional[Union[backupvault.CreateBackupVaultRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        backup_vault: Optional[backupvault.BackupVault] = None,
        backup_vault_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new BackupVault in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_backup_vault():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.CreateBackupVaultRequest(
                    parent="parent_value",
                    backup_vault_id="backup_vault_id_value",
                )

                # Make the request
                operation = await client.create_backup_vault(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateBackupVaultRequest, dict]]):
                The request object. Message for creating a BackupVault.
            parent (:class:`str`):
                Required. Value for parent.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backup_vault (:class:`google.cloud.backupdr_v1.types.BackupVault`):
                Required. The resource being created
                This corresponds to the ``backup_vault`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backup_vault_id (:class:`str`):
                Required. ID of the requesting object If auto-generating
                ID server-side, remove this field and backup_vault_id
                from the method_signature of Create RPC

                This corresponds to the ``backup_vault_id`` field
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
                :class:`google.cloud.backupdr_v1.types.BackupVault`
                Message describing a BackupVault object.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, backup_vault, backup_vault_id]
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
        if not isinstance(request, backupvault.CreateBackupVaultRequest):
            request = backupvault.CreateBackupVaultRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if backup_vault is not None:
            request.backup_vault = backup_vault
        if backup_vault_id is not None:
            request.backup_vault_id = backup_vault_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_backup_vault
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
            backupvault.BackupVault,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_backup_vaults(
        self,
        request: Optional[Union[backupvault.ListBackupVaultsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupVaultsAsyncPager:
        r"""Lists BackupVaults in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_backup_vaults():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListBackupVaultsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backup_vaults(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListBackupVaultsRequest, dict]]):
                The request object. Request message for listing
                backupvault stores.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                backupvault stores information, in the format
                'projects/{project_id}/locations/{location}'. In Cloud
                Backup and DR, locations map to Google Cloud regions,
                for example **us-central1**. To retrieve backupvault
                stores for all locations, use "-" for the '{location}'
                value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager:
                Response message for listing
                BackupVaults.
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
        if not isinstance(request, backupvault.ListBackupVaultsRequest):
            request = backupvault.ListBackupVaultsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_backup_vaults
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
        response = pagers.ListBackupVaultsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_usable_backup_vaults(
        self,
        request: Optional[
            Union[backupvault.FetchUsableBackupVaultsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchUsableBackupVaultsAsyncPager:
        r"""FetchUsableBackupVaults lists usable BackupVaults in
        a given project and location. Usable BackupVault are the
        ones that user has backupdr.backupVaults.get permission.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_fetch_usable_backup_vaults():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.FetchUsableBackupVaultsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.fetch_usable_backup_vaults(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest, dict]]):
                The request object. Request message for fetching usable
                BackupVaults.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                backupvault stores information, in the format
                'projects/{project_id}/locations/{location}'. In Cloud
                Backup and DR, locations map to Google Cloud regions,
                for example **us-central1**. To retrieve backupvault
                stores for all locations, use "-" for the '{location}'
                value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager:
                Response message for fetching usable
                BackupVaults.
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
        if not isinstance(request, backupvault.FetchUsableBackupVaultsRequest):
            request = backupvault.FetchUsableBackupVaultsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_usable_backup_vaults
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
        response = pagers.FetchUsableBackupVaultsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_backup_vault(
        self,
        request: Optional[Union[backupvault.GetBackupVaultRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupvault.BackupVault:
        r"""Gets details of a BackupVault.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_backup_vault():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetBackupVaultRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_backup_vault(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetBackupVaultRequest, dict]]):
                The request object. Request message for getting a
                BackupVault.
            name (:class:`str`):
                Required. Name of the backupvault store resource name,
                in the format
                'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'

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
            google.cloud.backupdr_v1.types.BackupVault:
                Message describing a BackupVault
                object.

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
        if not isinstance(request, backupvault.GetBackupVaultRequest):
            request = backupvault.GetBackupVaultRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_backup_vault
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

    async def update_backup_vault(
        self,
        request: Optional[Union[backupvault.UpdateBackupVaultRequest, dict]] = None,
        *,
        backup_vault: Optional[backupvault.BackupVault] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the settings of a BackupVault.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_backup_vault():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.UpdateBackupVaultRequest(
                )

                # Make the request
                operation = await client.update_backup_vault(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateBackupVaultRequest, dict]]):
                The request object. Request message for updating a
                BackupVault.
            backup_vault (:class:`google.cloud.backupdr_v1.types.BackupVault`):
                Required. The resource being updated
                This corresponds to the ``backup_vault`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Field mask is used to specify the fields to be
                overwritten in the BackupVault resource by the update.
                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask. If the user does not
                provide a mask then the request will fail.

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
                :class:`google.cloud.backupdr_v1.types.BackupVault`
                Message describing a BackupVault object.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [backup_vault, update_mask]
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
        if not isinstance(request, backupvault.UpdateBackupVaultRequest):
            request = backupvault.UpdateBackupVaultRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if backup_vault is not None:
            request.backup_vault = backup_vault
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_backup_vault
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("backup_vault.name", request.backup_vault.name),)
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
            backupvault.BackupVault,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_backup_vault(
        self,
        request: Optional[Union[backupvault.DeleteBackupVaultRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a BackupVault.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_backup_vault():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteBackupVaultRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_backup_vault(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteBackupVaultRequest, dict]]):
                The request object. Message for deleting a BackupVault.
            name (:class:`str`):
                Required. Name of the resource.
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
        if not isinstance(request, backupvault.DeleteBackupVaultRequest):
            request = backupvault.DeleteBackupVaultRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_backup_vault
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_data_sources(
        self,
        request: Optional[Union[backupvault.ListDataSourcesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDataSourcesAsyncPager:
        r"""Lists DataSources in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_data_sources():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListDataSourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_data_sources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListDataSourcesRequest, dict]]):
                The request object. Request message for listing
                DataSources.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                data sources information, in the format
                'projects/{project_id}/locations/{location}'. In Cloud
                Backup and DR, locations map to Google Cloud regions,
                for example **us-central1**. To retrieve data sources
                for all locations, use "-" for the '{location}' value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager:
                Response message for listing
                DataSources.
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
        if not isinstance(request, backupvault.ListDataSourcesRequest):
            request = backupvault.ListDataSourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_data_sources
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
        response = pagers.ListDataSourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_data_source(
        self,
        request: Optional[Union[backupvault.GetDataSourceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupvault.DataSource:
        r"""Gets details of a DataSource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_data_source():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetDataSourceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_data_source(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetDataSourceRequest, dict]]):
                The request object. Request message for getting a
                DataSource instance.
            name (:class:`str`):
                Required. Name of the data source resource name, in the
                format
                'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}'

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
            google.cloud.backupdr_v1.types.DataSource:
                Message describing a DataSource
                object. Datasource object used to
                represent Datasource details for both
                admin and basic view.

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
        if not isinstance(request, backupvault.GetDataSourceRequest):
            request = backupvault.GetDataSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_data_source
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

    async def update_data_source(
        self,
        request: Optional[Union[backupvault.UpdateDataSourceRequest, dict]] = None,
        *,
        data_source: Optional[backupvault.DataSource] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the settings of a DataSource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_data_source():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.UpdateDataSourceRequest(
                )

                # Make the request
                operation = await client.update_data_source(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateDataSourceRequest, dict]]):
                The request object. Request message for updating a data
                source instance.
            data_source (:class:`google.cloud.backupdr_v1.types.DataSource`):
                Required. The resource being updated
                This corresponds to the ``data_source`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Field mask is used to specify the fields to be
                overwritten in the DataSource resource by the update.
                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask. If the user does not
                provide a mask then the request will fail.

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.DataSource` Message describing a DataSource object.
                   Datasource object used to represent Datasource
                   details for both admin and basic view.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [data_source, update_mask]
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
        if not isinstance(request, backupvault.UpdateDataSourceRequest):
            request = backupvault.UpdateDataSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if data_source is not None:
            request.data_source = data_source
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_data_source
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("data_source.name", request.data_source.name),)
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
            backupvault.DataSource,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_backups(
        self,
        request: Optional[Union[backupvault.ListBackupsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupsAsyncPager:
        r"""Lists Backups in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_backups():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListBackupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backups(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListBackupsRequest, dict]]):
                The request object. Request message for listing Backups.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                backup information, in the format
                'projects/{project_id}/locations/{location}'. In Cloud
                Backup and DR, locations map to Google Cloud regions,
                for example **us-central1**. To retrieve data sources
                for all locations, use "-" for the '{location}' value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager:
                Response message for listing Backups.

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
        if not isinstance(request, backupvault.ListBackupsRequest):
            request = backupvault.ListBackupsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_backups
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
        response = pagers.ListBackupsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_backups_for_resource_type(
        self,
        request: Optional[
            Union[backupvault.FetchBackupsForResourceTypeRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        resource_type: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchBackupsForResourceTypeAsyncPager:
        r"""Fetch Backups for a given resource type.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_fetch_backups_for_resource_type():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.FetchBackupsForResourceTypeRequest(
                    parent="parent_value",
                    resource_type="resource_type_value",
                )

                # Make the request
                page_result = client.fetch_backups_for_resource_type(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest, dict]]):
                The request object. Request for the
                FetchBackupsForResourceType method.
            parent (:class:`str`):
                Required. Datasources are the parent
                resource for the backups. Format:

                projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource_type (:class:`str`):
                Required. The type of the GCP
                resource. Ex:
                sqladmin.googleapis.com/Instance

                This corresponds to the ``resource_type`` field
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
            google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager:
                Response for the
                FetchBackupsForResourceType method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, resource_type]
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
        if not isinstance(request, backupvault.FetchBackupsForResourceTypeRequest):
            request = backupvault.FetchBackupsForResourceTypeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if resource_type is not None:
            request.resource_type = resource_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_backups_for_resource_type
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
        response = pagers.FetchBackupsForResourceTypeAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_backup(
        self,
        request: Optional[Union[backupvault.GetBackupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupvault.Backup:
        r"""Gets details of a Backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_backup():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetBackupRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_backup(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetBackupRequest, dict]]):
                The request object. Request message for getting a Backup.
            name (:class:`str`):
                Required. Name of the data source resource name, in the
                format
                'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}'

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
            google.cloud.backupdr_v1.types.Backup:
                Message describing a Backup object.
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
        if not isinstance(request, backupvault.GetBackupRequest):
            request = backupvault.GetBackupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_backup
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

    async def update_backup(
        self,
        request: Optional[Union[backupvault.UpdateBackupRequest, dict]] = None,
        *,
        backup: Optional[backupvault.Backup] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the settings of a Backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_backup():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.UpdateBackupRequest(
                )

                # Make the request
                operation = await client.update_backup(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateBackupRequest, dict]]):
                The request object. Request message for updating a
                Backup.
            backup (:class:`google.cloud.backupdr_v1.types.Backup`):
                Required. The resource being updated
                This corresponds to the ``backup`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Field mask is used to specify the fields to be
                overwritten in the Backup resource by the update. The
                fields specified in the update_mask are relative to the
                resource, not the full request. A field will be
                overwritten if it is in the mask. If the user does not
                provide a mask then the request will fail.

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
                :class:`google.cloud.backupdr_v1.types.Backup` Message
                describing a Backup object.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [backup, update_mask]
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
        if not isinstance(request, backupvault.UpdateBackupRequest):
            request = backupvault.UpdateBackupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if backup is not None:
            request.backup = backup
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_backup
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("backup.name", request.backup.name),)
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
            backupvault.Backup,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_backup(
        self,
        request: Optional[Union[backupvault.DeleteBackupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a Backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_backup():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteBackupRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_backup(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteBackupRequest, dict]]):
                The request object. Message for deleting a Backup.
            name (:class:`str`):
                Required. Name of the resource.
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

                The result type for the operation will be
                :class:`google.cloud.backupdr_v1.types.Backup` Message
                describing a Backup object.

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
        if not isinstance(request, backupvault.DeleteBackupRequest):
            request = backupvault.DeleteBackupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_backup
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
            backupvault.Backup,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def restore_backup(
        self,
        request: Optional[Union[backupvault.RestoreBackupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Restore from a Backup

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_restore_backup():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                compute_instance_target_environment = backupdr_v1.ComputeInstanceTargetEnvironment()
                compute_instance_target_environment.project = "project_value"
                compute_instance_target_environment.zone = "zone_value"

                request = backupdr_v1.RestoreBackupRequest(
                    compute_instance_target_environment=compute_instance_target_environment,
                    name="name_value",
                )

                # Make the request
                operation = await client.restore_backup(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.RestoreBackupRequest, dict]]):
                The request object. Request message for restoring from a
                Backup.
            name (:class:`str`):
                Required. The resource name of the Backup instance, in
                the format
                'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.

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

                The result type for the operation will be
                :class:`google.cloud.backupdr_v1.types.RestoreBackupResponse`
                Response message for restoring from a Backup.

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
        if not isinstance(request, backupvault.RestoreBackupRequest):
            request = backupvault.RestoreBackupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.restore_backup
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
            backupvault.RestoreBackupResponse,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_backup_plan(
        self,
        request: Optional[Union[backupplan.CreateBackupPlanRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        backup_plan: Optional[backupplan.BackupPlan] = None,
        backup_plan_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Create a BackupPlan

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_backup_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                backup_plan = backupdr_v1.BackupPlan()
                backup_plan.backup_rules.standard_schedule.recurrence_type = "YEARLY"
                backup_plan.backup_rules.standard_schedule.backup_window.start_hour_of_day = 1820
                backup_plan.backup_rules.standard_schedule.backup_window.end_hour_of_day = 1573
                backup_plan.backup_rules.standard_schedule.time_zone = "time_zone_value"
                backup_plan.backup_rules.rule_id = "rule_id_value"
                backup_plan.backup_rules.backup_retention_days = 2237
                backup_plan.resource_type = "resource_type_value"
                backup_plan.backup_vault = "backup_vault_value"

                request = backupdr_v1.CreateBackupPlanRequest(
                    parent="parent_value",
                    backup_plan_id="backup_plan_id_value",
                    backup_plan=backup_plan,
                )

                # Make the request
                operation = await client.create_backup_plan(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateBackupPlanRequest, dict]]):
                The request object. The request message for creating a ``BackupPlan``.
            parent (:class:`str`):
                Required. The ``BackupPlan`` project and location in the
                format ``projects/{project}/locations/{location}``. In
                Cloud BackupDR locations map to GCP regions, for example
                **us-central1**.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backup_plan (:class:`google.cloud.backupdr_v1.types.BackupPlan`):
                Required. The ``BackupPlan`` resource object to create.
                This corresponds to the ``backup_plan`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backup_plan_id (:class:`str`):
                Required. The name of the ``BackupPlan`` to create. The
                name must be unique for the specified project and
                location.The name must start with a lowercase letter
                followed by up to 62 lowercase letters, numbers, or
                hyphens. Pattern, /[a-z][a-z0-9-]{,62}/.

                This corresponds to the ``backup_plan_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.BackupPlan` A BackupPlan specifies some common fields, such as description as well
                   as one or more BackupRule messages. Each BackupRule
                   has a retention policy and defines a schedule by
                   which the system is to perform backup workloads.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, backup_plan, backup_plan_id]
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
        if not isinstance(request, backupplan.CreateBackupPlanRequest):
            request = backupplan.CreateBackupPlanRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if backup_plan is not None:
            request.backup_plan = backup_plan
        if backup_plan_id is not None:
            request.backup_plan_id = backup_plan_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_backup_plan
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
            backupplan.BackupPlan,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_backup_plan(
        self,
        request: Optional[Union[backupplan.UpdateBackupPlanRequest, dict]] = None,
        *,
        backup_plan: Optional[backupplan.BackupPlan] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Update a BackupPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_backup_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                backup_plan = backupdr_v1.BackupPlan()
                backup_plan.backup_rules.standard_schedule.recurrence_type = "YEARLY"
                backup_plan.backup_rules.standard_schedule.backup_window.start_hour_of_day = 1820
                backup_plan.backup_rules.standard_schedule.backup_window.end_hour_of_day = 1573
                backup_plan.backup_rules.standard_schedule.time_zone = "time_zone_value"
                backup_plan.backup_rules.rule_id = "rule_id_value"
                backup_plan.backup_rules.backup_retention_days = 2237
                backup_plan.resource_type = "resource_type_value"
                backup_plan.backup_vault = "backup_vault_value"

                request = backupdr_v1.UpdateBackupPlanRequest(
                    backup_plan=backup_plan,
                )

                # Make the request
                operation = await client.update_backup_plan(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateBackupPlanRequest, dict]]):
                The request object. Request message for updating a backup
                plan.
            backup_plan (:class:`google.cloud.backupdr_v1.types.BackupPlan`):
                Required. The resource being updated
                This corresponds to the ``backup_plan`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to update. Field mask is
                used to specify the fields to be overwritten in the
                BackupPlan resource by the update. The fields specified
                in the update_mask are relative to the resource, not the
                full request. A field will be overwritten if it is in
                the mask. If the user does not provide a mask then the
                request will fail. Currently, these fields are supported
                in update: description, schedules, retention period,
                adding and removing Backup Rules.

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.BackupPlan` A BackupPlan specifies some common fields, such as description as well
                   as one or more BackupRule messages. Each BackupRule
                   has a retention policy and defines a schedule by
                   which the system is to perform backup workloads.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [backup_plan, update_mask]
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
        if not isinstance(request, backupplan.UpdateBackupPlanRequest):
            request = backupplan.UpdateBackupPlanRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if backup_plan is not None:
            request.backup_plan = backup_plan
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_backup_plan
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("backup_plan.name", request.backup_plan.name),)
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
            backupplan.BackupPlan,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_backup_plan(
        self,
        request: Optional[Union[backupplan.GetBackupPlanRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupplan.BackupPlan:
        r"""Gets details of a single BackupPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_backup_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetBackupPlanRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_backup_plan(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetBackupPlanRequest, dict]]):
                The request object. The request message for getting a ``BackupPlan``.
            name (:class:`str`):
                Required. The resource name of the ``BackupPlan`` to
                retrieve.

                Format:
                ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``

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
            google.cloud.backupdr_v1.types.BackupPlan:
                A BackupPlan specifies some common fields, such as description as well
                   as one or more BackupRule messages. Each BackupRule
                   has a retention policy and defines a schedule by
                   which the system is to perform backup workloads.

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
        if not isinstance(request, backupplan.GetBackupPlanRequest):
            request = backupplan.GetBackupPlanRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_backup_plan
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

    async def list_backup_plans(
        self,
        request: Optional[Union[backupplan.ListBackupPlansRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupPlansAsyncPager:
        r"""Lists BackupPlans in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_backup_plans():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListBackupPlansRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backup_plans(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListBackupPlansRequest, dict]]):
                The request object. The request message for getting a list ``BackupPlan``.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                ``BackupPlans`` information. Format:
                ``projects/{project}/locations/{location}``. In Cloud
                BackupDR, locations map to GCP regions, for e.g.
                **us-central1**. To retrieve backup plans for all
                locations, use "-" for the ``{location}`` value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager:
                The response message for getting a list of BackupPlan.

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
        if not isinstance(request, backupplan.ListBackupPlansRequest):
            request = backupplan.ListBackupPlansRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_backup_plans
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
        response = pagers.ListBackupPlansAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_backup_plan(
        self,
        request: Optional[Union[backupplan.DeleteBackupPlanRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single BackupPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_backup_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteBackupPlanRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_backup_plan(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteBackupPlanRequest, dict]]):
                The request object. The request message for deleting a ``BackupPlan``.
            name (:class:`str`):
                Required. The resource name of the ``BackupPlan`` to
                delete.

                Format:
                ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``

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
        if not isinstance(request, backupplan.DeleteBackupPlanRequest):
            request = backupplan.DeleteBackupPlanRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_backup_plan
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_backup_plan_revision(
        self,
        request: Optional[Union[backupplan.GetBackupPlanRevisionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupplan.BackupPlanRevision:
        r"""Gets details of a single BackupPlanRevision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_backup_plan_revision():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetBackupPlanRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_backup_plan_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetBackupPlanRevisionRequest, dict]]):
                The request object. The request message for getting a
                ``BackupPlanRevision``.
            name (:class:`str`):
                Required. The resource name of the
                ``BackupPlanRevision`` to retrieve.

                Format:
                ``projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}``

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
            google.cloud.backupdr_v1.types.BackupPlanRevision:
                BackupPlanRevision represents a snapshot of a BackupPlan at a point in
                   time.

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
        if not isinstance(request, backupplan.GetBackupPlanRevisionRequest):
            request = backupplan.GetBackupPlanRevisionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_backup_plan_revision
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

    async def list_backup_plan_revisions(
        self,
        request: Optional[
            Union[backupplan.ListBackupPlanRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupPlanRevisionsAsyncPager:
        r"""Lists BackupPlanRevisions in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_backup_plan_revisions():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListBackupPlanRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backup_plan_revisions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest, dict]]):
                The request object. The request message for getting a list of
                ``BackupPlanRevision``.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                ``BackupPlanRevisions`` information. Format:
                ``projects/{project}/locations/{location}/backupPlans/{backup_plan}``.
                In Cloud BackupDR, locations map to GCP regions, for
                e.g. **us-central1**.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager:
                The response message for getting a list of
                BackupPlanRevision.

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
        if not isinstance(request, backupplan.ListBackupPlanRevisionsRequest):
            request = backupplan.ListBackupPlanRevisionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_backup_plan_revisions
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
        response = pagers.ListBackupPlanRevisionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_backup_plan_association(
        self,
        request: Optional[
            Union[backupplanassociation.CreateBackupPlanAssociationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        backup_plan_association: Optional[
            backupplanassociation.BackupPlanAssociation
        ] = None,
        backup_plan_association_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Create a BackupPlanAssociation

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_backup_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                backup_plan_association = backupdr_v1.BackupPlanAssociation()
                backup_plan_association.resource_type = "resource_type_value"
                backup_plan_association.resource = "resource_value"
                backup_plan_association.backup_plan = "backup_plan_value"

                request = backupdr_v1.CreateBackupPlanAssociationRequest(
                    parent="parent_value",
                    backup_plan_association_id="backup_plan_association_id_value",
                    backup_plan_association=backup_plan_association,
                )

                # Make the request
                operation = await client.create_backup_plan_association(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateBackupPlanAssociationRequest, dict]]):
                The request object. Request message for creating a backup
                plan.
            parent (:class:`str`):
                Required. The backup plan association project and
                location in the format
                ``projects/{project_id}/locations/{location}``. In Cloud
                BackupDR locations map to GCP regions, for example
                **us-central1**.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backup_plan_association (:class:`google.cloud.backupdr_v1.types.BackupPlanAssociation`):
                Required. The resource being created
                This corresponds to the ``backup_plan_association`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backup_plan_association_id (:class:`str`):
                Required. The name of the backup plan
                association to create. The name must be
                unique for the specified project and
                location.

                This corresponds to the ``backup_plan_association_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.BackupPlanAssociation` A BackupPlanAssociation represents a single BackupPlanAssociation which
                   contains details like workload, backup plan etc

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, backup_plan_association, backup_plan_association_id]
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
            request, backupplanassociation.CreateBackupPlanAssociationRequest
        ):
            request = backupplanassociation.CreateBackupPlanAssociationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if backup_plan_association is not None:
            request.backup_plan_association = backup_plan_association
        if backup_plan_association_id is not None:
            request.backup_plan_association_id = backup_plan_association_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_backup_plan_association
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
            backupplanassociation.BackupPlanAssociation,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_backup_plan_association(
        self,
        request: Optional[
            Union[backupplanassociation.UpdateBackupPlanAssociationRequest, dict]
        ] = None,
        *,
        backup_plan_association: Optional[
            backupplanassociation.BackupPlanAssociation
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Update a BackupPlanAssociation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_backup_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                backup_plan_association = backupdr_v1.BackupPlanAssociation()
                backup_plan_association.resource_type = "resource_type_value"
                backup_plan_association.resource = "resource_value"
                backup_plan_association.backup_plan = "backup_plan_value"

                request = backupdr_v1.UpdateBackupPlanAssociationRequest(
                    backup_plan_association=backup_plan_association,
                )

                # Make the request
                operation = await client.update_backup_plan_association(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateBackupPlanAssociationRequest, dict]]):
                The request object. Request message for updating a backup
                plan association.
            backup_plan_association (:class:`google.cloud.backupdr_v1.types.BackupPlanAssociation`):
                Required. The resource being updated
                This corresponds to the ``backup_plan_association`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to update. Field mask is
                used to specify the fields to be overwritten in the
                BackupPlanAssociation resource by the update. The fields
                specified in the update_mask are relative to the
                resource, not the full request. A field will be
                overwritten if it is in the mask. If the user does not
                provide a mask then the request will fail. Currently
                backup_plan_association.backup_plan is the only
                supported field.

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.BackupPlanAssociation` A BackupPlanAssociation represents a single BackupPlanAssociation which
                   contains details like workload, backup plan etc

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [backup_plan_association, update_mask]
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
            request, backupplanassociation.UpdateBackupPlanAssociationRequest
        ):
            request = backupplanassociation.UpdateBackupPlanAssociationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if backup_plan_association is not None:
            request.backup_plan_association = backup_plan_association
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_backup_plan_association
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "backup_plan_association.name",
                        request.backup_plan_association.name,
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            backupplanassociation.BackupPlanAssociation,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_backup_plan_association(
        self,
        request: Optional[
            Union[backupplanassociation.GetBackupPlanAssociationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backupplanassociation.BackupPlanAssociation:
        r"""Gets details of a single BackupPlanAssociation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_backup_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetBackupPlanAssociationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_backup_plan_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetBackupPlanAssociationRequest, dict]]):
                The request object. Request message for getting a
                BackupPlanAssociation resource.
            name (:class:`str`):
                Required. Name of the backup plan association resource,
                in the format
                ``projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}``

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
            google.cloud.backupdr_v1.types.BackupPlanAssociation:
                A BackupPlanAssociation represents a
                single BackupPlanAssociation which
                contains details like workload, backup
                plan etc

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
            request, backupplanassociation.GetBackupPlanAssociationRequest
        ):
            request = backupplanassociation.GetBackupPlanAssociationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_backup_plan_association
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

    async def list_backup_plan_associations(
        self,
        request: Optional[
            Union[backupplanassociation.ListBackupPlanAssociationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupPlanAssociationsAsyncPager:
        r"""Lists BackupPlanAssociations in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_backup_plan_associations():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListBackupPlanAssociationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backup_plan_associations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest, dict]]):
                The request object. Request message for List
                BackupPlanAssociation
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                backup Plan Associations information, in the format
                ``projects/{project_id}/locations/{location}``. In Cloud
                BackupDR, locations map to GCP regions, for example
                **us-central1**. To retrieve backup plan associations
                for all locations, use "-" for the ``{location}`` value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager:
                Response message for List
                BackupPlanAssociation
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
        if not isinstance(
            request, backupplanassociation.ListBackupPlanAssociationsRequest
        ):
            request = backupplanassociation.ListBackupPlanAssociationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_backup_plan_associations
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
        response = pagers.ListBackupPlanAssociationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_backup_plan_associations_for_resource_type(
        self,
        request: Optional[
            Union[
                backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        resource_type: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager:
        r"""List BackupPlanAssociations for a given resource
        type.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_fetch_backup_plan_associations_for_resource_type():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.FetchBackupPlanAssociationsForResourceTypeRequest(
                    parent="parent_value",
                    resource_type="resource_type_value",
                )

                # Make the request
                page_result = client.fetch_backup_plan_associations_for_resource_type(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest, dict]]):
                The request object. Request for the
                FetchBackupPlanAssociationsForResourceType
                method.
            parent (:class:`str`):
                Required. The parent resource name.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource_type (:class:`str`):
                Required. The type of the GCP
                resource. Ex:
                sql.googleapis.com/Instance

                This corresponds to the ``resource_type`` field
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
            google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager:
                Response for the
                FetchBackupPlanAssociationsForResourceType
                method.  Iterating over this object will
                yield results and resolve additional
                pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, resource_type]
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
            request,
            backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        ):
            request = (
                backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if resource_type is not None:
            request.resource_type = resource_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_backup_plan_associations_for_resource_type
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
        response = pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_backup_plan_association(
        self,
        request: Optional[
            Union[backupplanassociation.DeleteBackupPlanAssociationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single BackupPlanAssociation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_backup_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteBackupPlanAssociationRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_backup_plan_association(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteBackupPlanAssociationRequest, dict]]):
                The request object. Request message for deleting a backup
                plan association.
            name (:class:`str`):
                Required. Name of the backup plan association resource,
                in the format
                ``projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}``

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
        if not isinstance(
            request, backupplanassociation.DeleteBackupPlanAssociationRequest
        ):
            request = backupplanassociation.DeleteBackupPlanAssociationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_backup_plan_association
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def trigger_backup(
        self,
        request: Optional[
            Union[backupplanassociation.TriggerBackupRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        rule_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Triggers a new Backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_trigger_backup():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.TriggerBackupRequest(
                    name="name_value",
                    rule_id="rule_id_value",
                )

                # Make the request
                operation = await client.trigger_backup(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.TriggerBackupRequest, dict]]):
                The request object. Request message for triggering a
                backup.
            name (:class:`str`):
                Required. Name of the backup plan association resource,
                in the format
                ``projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            rule_id (:class:`str`):
                Required. backup rule_id for which a backup needs to be
                triggered.

                This corresponds to the ``rule_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.BackupPlanAssociation` A BackupPlanAssociation represents a single BackupPlanAssociation which
                   contains details like workload, backup plan etc

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, rule_id]
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
        if not isinstance(request, backupplanassociation.TriggerBackupRequest):
            request = backupplanassociation.TriggerBackupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if rule_id is not None:
            request.rule_id = rule_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.trigger_backup
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
            backupplanassociation.BackupPlanAssociation,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_data_source_reference(
        self,
        request: Optional[
            Union[datasourcereference.GetDataSourceReferenceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datasourcereference.DataSourceReference:
        r"""Gets details of a single DataSourceReference.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_data_source_reference():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetDataSourceReferenceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_data_source_reference(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetDataSourceReferenceRequest, dict]]):
                The request object. Request for the
                GetDataSourceReference method.
            name (:class:`str`):
                Required. The name of the DataSourceReference to
                retrieve. Format:
                projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}

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
            google.cloud.backupdr_v1.types.DataSourceReference:
                DataSourceReference is a reference to
                a DataSource resource.

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
        if not isinstance(request, datasourcereference.GetDataSourceReferenceRequest):
            request = datasourcereference.GetDataSourceReferenceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_data_source_reference
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

    async def list_data_source_references(
        self,
        request: Optional[
            Union[datasourcereference.ListDataSourceReferencesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDataSourceReferencesAsyncPager:
        r"""Lists DataSourceReferences for a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_data_source_references():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListDataSourceReferencesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_data_source_references(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest, dict]]):
                The request object. Request for the
                ListDataSourceReferences method.
            parent (:class:`str`):
                Required. The parent resource name.
                Format:
                projects/{project}/locations/{location}

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager:
                Response for the
                ListDataSourceReferences method.
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
        if not isinstance(request, datasourcereference.ListDataSourceReferencesRequest):
            request = datasourcereference.ListDataSourceReferencesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_data_source_references
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
        response = pagers.ListDataSourceReferencesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def fetch_data_source_references_for_resource_type(
        self,
        request: Optional[
            Union[
                datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        resource_type: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchDataSourceReferencesForResourceTypeAsyncPager:
        r"""Fetch DataSourceReferences for a given project,
        location and resource type.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_fetch_data_source_references_for_resource_type():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.FetchDataSourceReferencesForResourceTypeRequest(
                    parent="parent_value",
                    resource_type="resource_type_value",
                )

                # Make the request
                page_result = client.fetch_data_source_references_for_resource_type(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest, dict]]):
                The request object. Request for the
                FetchDataSourceReferencesForResourceType
                method.
            parent (:class:`str`):
                Required. The parent resource name.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource_type (:class:`str`):
                Required. The type of the GCP
                resource. Ex:
                sql.googleapis.com/Instance

                This corresponds to the ``resource_type`` field
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
            google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager:
                Response for the
                FetchDataSourceReferencesForResourceType
                method.  Iterating over this object will
                yield results and resolve additional
                pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, resource_type]
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
            request, datasourcereference.FetchDataSourceReferencesForResourceTypeRequest
        ):
            request = (
                datasourcereference.FetchDataSourceReferencesForResourceTypeRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if resource_type is not None:
            request.resource_type = resource_type

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.fetch_data_source_references_for_resource_type
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
        response = pagers.FetchDataSourceReferencesForResourceTypeAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def initialize_service(
        self,
        request: Optional[Union[backupdr.InitializeServiceRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Initializes the service related config for a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_initialize_service():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                cloud_sql_instance_initialization_config = backupdr_v1.CloudSqlInstanceInitializationConfig()
                cloud_sql_instance_initialization_config.edition = "ENTERPRISE_PLUS"

                request = backupdr_v1.InitializeServiceRequest(
                    cloud_sql_instance_initialization_config=cloud_sql_instance_initialization_config,
                    name="name_value",
                    resource_type="resource_type_value",
                )

                # Make the request
                operation = await client.initialize_service(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.InitializeServiceRequest, dict]]):
                The request object. Request message for initializing the
                service.
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
                :class:`google.cloud.backupdr_v1.types.InitializeServiceResponse`
                Response message for initializing the service.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, backupdr.InitializeServiceRequest):
            request = backupdr.InitializeServiceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.initialize_service
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
            backupdr.InitializeServiceResponse,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_auto_protection_policy(
        self,
        request: Optional[
            Union[autoprotectionpolicy.CreateAutoProtectionPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        auto_protection_policy: Optional[
            autoprotectionpolicy.AutoProtectionPolicy
        ] = None,
        auto_protection_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new AutoProtectionPolicy in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_auto_protection_policy():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                auto_protection_policy = backupdr_v1.AutoProtectionPolicy()
                auto_protection_policy.backup_plan_details.resource_type = "resource_type_value"
                auto_protection_policy.backup_plan_details.backup_plan = "backup_plan_value"
                auto_protection_policy.criteria.matching_conditions.label_condition.key = "key_value"
                auto_protection_policy.criteria.matching_conditions.label_condition.values = ['values_value1', 'values_value2']

                request = backupdr_v1.CreateAutoProtectionPolicyRequest(
                    parent="parent_value",
                    auto_protection_policy_id="auto_protection_policy_id_value",
                    auto_protection_policy=auto_protection_policy,
                )

                # Make the request
                operation = await client.create_auto_protection_policy(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateAutoProtectionPolicyRequest, dict]]):
                The request object. Request message for creating an
                AutoProtectionPolicy.
            parent (:class:`str`):
                Required. The parent resource where
                this policy will be created. Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            auto_protection_policy (:class:`google.cloud.backupdr_v1.types.AutoProtectionPolicy`):
                Required. The AutoProtectionPolicy
                resource to create.

                This corresponds to the ``auto_protection_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            auto_protection_policy_id (:class:`str`):
                Required. The ID to use for the
                policy. This will become the final
                component of the policy's resource name.

                This value must start with a lowercase
                letter followed by up to 62 lowercase
                letters, numbers, or hyphens, and cannot
                end with a hyphen.

                This corresponds to the ``auto_protection_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.AutoProtectionPolicy` An AutoprotectionPolicy is a policy resource designed to automate backup
                   management, moving from manual per-resource
                   protection to a bulk approach. The policy dynamically
                   discovers and applies a specified backup plan to all
                   eligible resources that match its defined scope and
                   criteria.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, auto_protection_policy, auto_protection_policy_id]
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
            request, autoprotectionpolicy.CreateAutoProtectionPolicyRequest
        ):
            request = autoprotectionpolicy.CreateAutoProtectionPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if auto_protection_policy is not None:
            request.auto_protection_policy = auto_protection_policy
        if auto_protection_policy_id is not None:
            request.auto_protection_policy_id = auto_protection_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_auto_protection_policy
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
            autoprotectionpolicy.AutoProtectionPolicy,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_auto_protection_policies(
        self,
        request: Optional[
            Union[autoprotectionpolicy.ListAutoProtectionPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAutoProtectionPoliciesAsyncPager:
        r"""Lists AutoProtectionPolicies for a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_auto_protection_policies():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListAutoProtectionPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_auto_protection_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesRequest, dict]]):
                The request object. Request message for
                ListAutoProtectionPolicies.
            parent (:class:`str`):
                Required. The project and location
                for which to retrieve the list of
                policies. Format:
                projects/{project}/locations/{location}

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListAutoProtectionPoliciesAsyncPager:
                Response message for
                ListAutoProtectionPolicies.
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
        if not isinstance(
            request, autoprotectionpolicy.ListAutoProtectionPoliciesRequest
        ):
            request = autoprotectionpolicy.ListAutoProtectionPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_auto_protection_policies
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
        response = pagers.ListAutoProtectionPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_auto_protection_policy(
        self,
        request: Optional[
            Union[autoprotectionpolicy.GetAutoProtectionPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> autoprotectionpolicy.AutoProtectionPolicy:
        r"""Gets details of a single AutoProtectionPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_auto_protection_policy():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetAutoProtectionPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_auto_protection_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetAutoProtectionPolicyRequest, dict]]):
                The request object. Request message for getting an
                AutoProtectionPolicy.
            name (:class:`str`):
                Required. The name of the policy to retrieve. Format:
                projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}

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
            google.cloud.backupdr_v1.types.AutoProtectionPolicy:
                An AutoprotectionPolicy is a policy
                resource designed to automate backup
                management, moving from manual
                per-resource protection to a bulk
                approach. The policy dynamically
                discovers and applies a specified backup
                plan to all eligible resources that
                match its defined scope and criteria.

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
        if not isinstance(request, autoprotectionpolicy.GetAutoProtectionPolicyRequest):
            request = autoprotectionpolicy.GetAutoProtectionPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_auto_protection_policy
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

    async def update_auto_protection_policy(
        self,
        request: Optional[
            Union[autoprotectionpolicy.UpdateAutoProtectionPolicyRequest, dict]
        ] = None,
        *,
        auto_protection_policy: Optional[
            autoprotectionpolicy.AutoProtectionPolicy
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the parameters of a single
        AutoProtectionPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_auto_protection_policy():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                auto_protection_policy = backupdr_v1.AutoProtectionPolicy()
                auto_protection_policy.backup_plan_details.resource_type = "resource_type_value"
                auto_protection_policy.backup_plan_details.backup_plan = "backup_plan_value"
                auto_protection_policy.criteria.matching_conditions.label_condition.key = "key_value"
                auto_protection_policy.criteria.matching_conditions.label_condition.values = ['values_value1', 'values_value2']

                request = backupdr_v1.UpdateAutoProtectionPolicyRequest(
                    auto_protection_policy=auto_protection_policy,
                )

                # Make the request
                operation = await client.update_auto_protection_policy(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateAutoProtectionPolicyRequest, dict]]):
                The request object. Request message for updating an
                AutoProtectionPolicy.
            auto_protection_policy (:class:`google.cloud.backupdr_v1.types.AutoProtectionPolicy`):
                Required. The policy to update.
                This corresponds to the ``auto_protection_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Field mask is used to specify the fields to be
                overwritten in the AutoProtectionPolicy resource by the
                update. The fields specified in the update_mask are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.AutoProtectionPolicy` An AutoprotectionPolicy is a policy resource designed to automate backup
                   management, moving from manual per-resource
                   protection to a bulk approach. The policy dynamically
                   discovers and applies a specified backup plan to all
                   eligible resources that match its defined scope and
                   criteria.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [auto_protection_policy, update_mask]
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
            request, autoprotectionpolicy.UpdateAutoProtectionPolicyRequest
        ):
            request = autoprotectionpolicy.UpdateAutoProtectionPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if auto_protection_policy is not None:
            request.auto_protection_policy = auto_protection_policy
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_auto_protection_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("auto_protection_policy.name", request.auto_protection_policy.name),)
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
            autoprotectionpolicy.AutoProtectionPolicy,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_auto_protection_policy(
        self,
        request: Optional[
            Union[autoprotectionpolicy.DeleteAutoProtectionPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single AutoProtectionPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_auto_protection_policy():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteAutoProtectionPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_auto_protection_policy(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteAutoProtectionPolicyRequest, dict]]):
                The request object. Request message for deleting an
                AutoProtectionPolicy.
            name (:class:`str`):
                Required. The name of the policy to delete. Format:
                projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}

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
        if not isinstance(
            request, autoprotectionpolicy.DeleteAutoProtectionPolicyRequest
        ):
            request = autoprotectionpolicy.DeleteAutoProtectionPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_auto_protection_policy
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_auto_protection_policy_binding(
        self,
        request: Optional[
            Union[
                autoprotectionpolicybinding.CreateAutoProtectionPolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        auto_protection_policy_binding: Optional[
            autoprotectionpolicybinding.AutoProtectionPolicyBinding
        ] = None,
        auto_protection_policy_binding_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new AutoProtectionPolicyBinding in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_auto_protection_policy_binding():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                auto_protection_policy_binding = backupdr_v1.AutoProtectionPolicyBinding()
                auto_protection_policy_binding.scope = "scope_value"

                request = backupdr_v1.CreateAutoProtectionPolicyBindingRequest(
                    parent="parent_value",
                    auto_protection_policy_binding_id="auto_protection_policy_binding_id_value",
                    auto_protection_policy_binding=auto_protection_policy_binding,
                )

                # Make the request
                operation = await client.create_auto_protection_policy_binding(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateAutoProtectionPolicyBindingRequest, dict]]):
                The request object. Request message for creating an
                AutoProtectionPolicyBinding.
            parent (:class:`str`):
                Required. The parent resource where this binding will be
                created. Format:
                projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            auto_protection_policy_binding (:class:`google.cloud.backupdr_v1.types.AutoProtectionPolicyBinding`):
                Required. The
                AutoProtectionPolicyBinding resource to
                create.

                This corresponds to the ``auto_protection_policy_binding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            auto_protection_policy_binding_id (:class:`str`):
                Required. The ID to use for the
                binding. This will become the final
                component of the binding's resource
                name.

                This value must start with a lowercase
                letter followed by up to 62 lowercase
                letters, numbers, or hyphens, and cannot
                end with a hyphen.

                This corresponds to the ``auto_protection_policy_binding_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.AutoProtectionPolicyBinding` An AutoProtectionPolicyBinding (APPA) acts as the bridge between an
                   AutoProtectionPolicy and the scope (Project) where
                   the policy should be applied.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            auto_protection_policy_binding,
            auto_protection_policy_binding_id,
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
        if not isinstance(
            request,
            autoprotectionpolicybinding.CreateAutoProtectionPolicyBindingRequest,
        ):
            request = (
                autoprotectionpolicybinding.CreateAutoProtectionPolicyBindingRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if auto_protection_policy_binding is not None:
            request.auto_protection_policy_binding = auto_protection_policy_binding
        if auto_protection_policy_binding_id is not None:
            request.auto_protection_policy_binding_id = (
                auto_protection_policy_binding_id
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_auto_protection_policy_binding
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
            autoprotectionpolicybinding.AutoProtectionPolicyBinding,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_auto_protection_policy_binding(
        self,
        request: Optional[
            Union[
                autoprotectionpolicybinding.GetAutoProtectionPolicyBindingRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> autoprotectionpolicybinding.AutoProtectionPolicyBinding:
        r"""Returns the auto protection policy binding read from
        the CCFE tables.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_auto_protection_policy_binding():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetAutoProtectionPolicyBindingRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_auto_protection_policy_binding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetAutoProtectionPolicyBindingRequest, dict]]):
                The request object. Request message for getting an
                AutoProtectionPolicyBinding.
            name (:class:`str`):
                Required. The name of the binding to retrieve. Format:
                projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}

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
            google.cloud.backupdr_v1.types.AutoProtectionPolicyBinding:
                An AutoProtectionPolicyBinding (APPA)
                acts as the bridge between an
                AutoProtectionPolicy and the scope
                (Project) where the policy should be
                applied.

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
            request, autoprotectionpolicybinding.GetAutoProtectionPolicyBindingRequest
        ):
            request = autoprotectionpolicybinding.GetAutoProtectionPolicyBindingRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_auto_protection_policy_binding
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

    async def list_auto_protection_policy_bindings(
        self,
        request: Optional[
            Union[
                autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAutoProtectionPolicyBindingsAsyncPager:
        r"""Returns the auto protection policy bindings read from
        the CCFE tables.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_auto_protection_policy_bindings():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListAutoProtectionPolicyBindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_auto_protection_policy_bindings(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsRequest, dict]]):
                The request object. Request message for
                ListAutoProtectionPolicyBindings.
            parent (:class:`str`):
                Required. The project and location
                for which to retrieve the list of
                policies. Format:
                projects/{project}/locations/{location}

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsAsyncPager:
                Response message for
                ListAutoProtectionPolicyBindings.
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
        if not isinstance(
            request, autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest
        ):
            request = (
                autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_auto_protection_policy_bindings
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
        response = pagers.ListAutoProtectionPolicyBindingsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_applied_auto_protection_policies(
        self,
        request: Optional[
            Union[
                appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAppliedAutoProtectionPoliciesAsyncPager:
        r"""Lists AppliedAutoProtectionPolicies in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_applied_auto_protection_policies():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListAppliedAutoProtectionPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_applied_auto_protection_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesRequest, dict]]):
                The request object. Request message for listing
                AppliedAutoProtectionPolicies.
            parent (:class:`str`):
                Required. The project and location
                for which to retrieve the list of
                applied policies. Format:
                projects/{project}/locations/{location}

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesAsyncPager:
                Response message for
                ListAppliedAutoProtectionPolicies.
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
        if not isinstance(
            request,
            appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
        ):
            request = (
                appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_applied_auto_protection_policies
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
        response = pagers.ListAppliedAutoProtectionPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def initiate_delete_auto_protection_policy_binding(
        self,
        request: Optional[
            Union[
                autoprotectionpolicybinding.InitiateDeleteAutoProtectionPolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""InitiateDeleteAutoProtectionPolicyBinding initiates
        delete for AutoProtectionPolicy Binding

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_initiate_delete_auto_protection_policy_binding():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.InitiateDeleteAutoProtectionPolicyBindingRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.initiate_delete_auto_protection_policy_binding(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.InitiateDeleteAutoProtectionPolicyBindingRequest, dict]]):
                The request object. Request message for initiating delete
                of an AutoProtectionPolicyBinding.
            name (:class:`str`):
                Required. The name of the binding to delete. Format:
                projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.AutoProtectionPolicyBinding` An AutoProtectionPolicyBinding (APPA) acts as the bridge between an
                   AutoProtectionPolicy and the scope (Project) where
                   the policy should be applied.

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
            request,
            autoprotectionpolicybinding.InitiateDeleteAutoProtectionPolicyBindingRequest,
        ):
            request = autoprotectionpolicybinding.InitiateDeleteAutoProtectionPolicyBindingRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.initiate_delete_auto_protection_policy_binding
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
            autoprotectionpolicybinding.AutoProtectionPolicyBinding,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_binding_matching_resources(
        self,
        request: Optional[
            Union[bindingmatchingresource.ListBindingMatchingResourcesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBindingMatchingResourcesAsyncPager:
        r"""Lists Binding Matching Resources for a given
        AutoProtectionPolicyBinding.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_binding_matching_resources():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListBindingMatchingResourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_binding_matching_resources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListBindingMatchingResourcesRequest, dict]]):
                The request object. Request message for List
                BindingMatchingResources.
            parent (:class:`str`):
                Required. The project, location, auto protection policy
                and binding for which to retrieve
                ``BindingMatchingResources`` information. Format:
                ``projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}``.
                In Google Cloud Backup and DR, locations map to Google
                Cloud regions, for example **us-central1**.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListBindingMatchingResourcesAsyncPager:
                The response message for getting a list of
                BindingMatchingResources.

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
            request, bindingmatchingresource.ListBindingMatchingResourcesRequest
        ):
            request = bindingmatchingresource.ListBindingMatchingResourcesRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_binding_matching_resources
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
        response = pagers.ListBindingMatchingResourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_restore_template(
        self,
        request: Optional[
            Union[gcb_restore_template.CreateRestoreTemplateRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        restore_template: Optional[gcb_restore_template.RestoreTemplate] = None,
        restore_template_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new RestoreTemplate in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_restore_template():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                restore_template = backupdr_v1.RestoreTemplate()
                restore_template.resource_type = "resource_type_value"
                restore_template.backup_selection_config.data_source = "data_source_value"

                request = backupdr_v1.CreateRestoreTemplateRequest(
                    parent="parent_value",
                    restore_template_id="restore_template_id_value",
                    restore_template=restore_template,
                )

                # Make the request
                operation = await client.create_restore_template(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateRestoreTemplateRequest, dict]]):
                The request object. Request message for creating a
                RestoreTemplate instance.
            parent (:class:`str`):
                Required. The restore template project and location in
                the format 'projects/{project_id}/locations/{location}'.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_template (:class:`google.cloud.backupdr_v1.types.RestoreTemplate`):
                Required. A RestoreTemplate resource.
                This corresponds to the ``restore_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_template_id (:class:`str`):
                Required. The ID of the restore
                template to create. The ID must be
                unique for the specified project and
                location.

                This corresponds to the ``restore_template_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.RestoreTemplate` A RestoreTemplate encapsulates DR readiness configurations for validating
                   backups.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, restore_template, restore_template_id]
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
        if not isinstance(request, gcb_restore_template.CreateRestoreTemplateRequest):
            request = gcb_restore_template.CreateRestoreTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if restore_template is not None:
            request.restore_template = restore_template
        if restore_template_id is not None:
            request.restore_template_id = restore_template_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_restore_template
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
            gcb_restore_template.RestoreTemplate,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_restore_template(
        self,
        request: Optional[
            Union[restore_template.GetRestoreTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> restore_template.RestoreTemplate:
        r"""Gets details of a RestoreTemplate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_restore_template():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetRestoreTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_restore_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetRestoreTemplateRequest, dict]]):
                The request object. Request message for getting a
                RestoreTemplate instance.
            name (:class:`str`):
                Required. The name of the restore template to retrieve.
                Format:
                'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}'

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
            google.cloud.backupdr_v1.types.RestoreTemplate:
                A RestoreTemplate encapsulates DR readiness configurations for validating
                   backups.

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
        if not isinstance(request, restore_template.GetRestoreTemplateRequest):
            request = restore_template.GetRestoreTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_restore_template
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

    async def list_restore_templates(
        self,
        request: Optional[
            Union[restore_template.ListRestoreTemplatesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRestoreTemplatesAsyncPager:
        r"""Lists RestoreTemplates in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_restore_templates():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListRestoreTemplatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_restore_templates(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListRestoreTemplatesRequest, dict]]):
                The request object. Request message for listing
                RestoreTemplates.
            parent (:class:`str`):
                Required. The project and location from which to list
                the restore templates. Format:
                ``projects/{project}/locations/{location}``.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListRestoreTemplatesAsyncPager:
                Response message for listing
                RestoreTemplates.
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
        if not isinstance(request, restore_template.ListRestoreTemplatesRequest):
            request = restore_template.ListRestoreTemplatesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_restore_templates
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
        response = pagers.ListRestoreTemplatesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_restore_template(
        self,
        request: Optional[
            Union[gcb_restore_template.UpdateRestoreTemplateRequest, dict]
        ] = None,
        *,
        restore_template: Optional[gcb_restore_template.RestoreTemplate] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the settings of a RestoreTemplate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_update_restore_template():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                restore_template = backupdr_v1.RestoreTemplate()
                restore_template.resource_type = "resource_type_value"
                restore_template.backup_selection_config.data_source = "data_source_value"

                request = backupdr_v1.UpdateRestoreTemplateRequest(
                    restore_template=restore_template,
                )

                # Make the request
                operation = await client.update_restore_template(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.UpdateRestoreTemplateRequest, dict]]):
                The request object. Request message for updating a
                RestoreTemplate instance.
            restore_template (:class:`google.cloud.backupdr_v1.types.RestoreTemplate`):
                Required. The restore template to
                update.

                This corresponds to the ``restore_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to update. Field mask is
                used to specify the fields to be overwritten in the
                RestoreTemplate resource by the update. The fields
                specified in the update_mask are relative to the
                resource, not the full request. A field will be
                overwritten if it is in the mask.

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.RestoreTemplate` A RestoreTemplate encapsulates DR readiness configurations for validating
                   backups.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [restore_template, update_mask]
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
        if not isinstance(request, gcb_restore_template.UpdateRestoreTemplateRequest):
            request = gcb_restore_template.UpdateRestoreTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if restore_template is not None:
            request.restore_template = restore_template
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_restore_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("restore_template.name", request.restore_template.name),)
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
            gcb_restore_template.RestoreTemplate,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_restore_template(
        self,
        request: Optional[
            Union[restore_template.DeleteRestoreTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a RestoreTemplate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_restore_template():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteRestoreTemplateRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_restore_template(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteRestoreTemplateRequest, dict]]):
                The request object. Request message for deleting a
                RestoreTemplate instance.
            name (:class:`str`):
                Required. The name of the restore template to delete.
                Format:
                'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}'

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
        if not isinstance(request, restore_template.DeleteRestoreTemplateRequest):
            request = restore_template.DeleteRestoreTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_restore_template
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def run_restore_template(
        self,
        request: Optional[
            Union[restore_template.RunRestoreTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Runs a RestoreTemplate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_run_restore_template():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.RunRestoreTemplateRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.run_restore_template(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.RunRestoreTemplateRequest, dict]]):
                The request object. Request message for running a
                RestoreTemplate.
            name (:class:`str`):
                Required. The name of the restore template to run.
                Format:
                'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}'

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

                The result type for the operation will be
                :class:`google.cloud.backupdr_v1.types.RunRestoreTemplateResponse`
                Response message for RunRestoreTemplate.

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
        if not isinstance(request, restore_template.RunRestoreTemplateRequest):
            request = restore_template.RunRestoreTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_restore_template
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
            restore_template.RunRestoreTemplateResponse,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_restore_template_execution(
        self,
        request: Optional[
            Union[restore_template_execution.GetRestoreTemplateExecutionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> restore_template_execution.RestoreTemplateExecution:
        r"""Gets details of a RestoreTemplateExecution.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_restore_template_execution():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetRestoreTemplateExecutionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_restore_template_execution(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetRestoreTemplateExecutionRequest, dict]]):
                The request object. Request message for getting a
                RestoreTemplateExecution instance.
            name (:class:`str`):
                Required. The name of the restore template execution to
                retrieve. Format:
                'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}/executions/{execution_id}'

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
            google.cloud.backupdr_v1.types.RestoreTemplateExecution:
                A RestoreTemplateExecution represents a single historical or active
                   execution run.

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
            request, restore_template_execution.GetRestoreTemplateExecutionRequest
        ):
            request = restore_template_execution.GetRestoreTemplateExecutionRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_restore_template_execution
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

    async def list_restore_template_executions(
        self,
        request: Optional[
            Union[restore_template_execution.ListRestoreTemplateExecutionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRestoreTemplateExecutionsAsyncPager:
        r"""Lists RestoreTemplateExecutions in a given project,
        location and restore template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_restore_template_executions():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListRestoreTemplateExecutionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_restore_template_executions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsRequest, dict]]):
                The request object. Request message for listing
                RestoreTemplateExecutions.
            parent (:class:`str`):
                Required. The project, location, and restore template
                for which to retrieve executions information. Format:
                ``projects/{project}/locations/{location}/restoreTemplates/{restore_template}``.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListRestoreTemplateExecutionsAsyncPager:
                Response message for listing
                RestoreTemplateExecutions.
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
        if not isinstance(
            request, restore_template_execution.ListRestoreTemplateExecutionsRequest
        ):
            request = restore_template_execution.ListRestoreTemplateExecutionsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_restore_template_executions
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
        response = pagers.ListRestoreTemplateExecutionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def trigger_restore_cleanup(
        self,
        request: Optional[
            Union[restore_template_execution.TriggerRestoreCleanupRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Triggers cleanup of restored resources created during
        execution.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_trigger_restore_cleanup():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.TriggerRestoreCleanupRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.trigger_restore_cleanup(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.TriggerRestoreCleanupRequest, dict]]):
                The request object. Request message for triggering a
                restore cleanup.
            name (:class:`str`):
                Required. Name of the restore template execution.
                Format:
                'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}/executions/{execution_id}'

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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.RestoreTemplateExecution` A RestoreTemplateExecution represents a single historical or active
                   execution run.

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
            request, restore_template_execution.TriggerRestoreCleanupRequest
        ):
            request = restore_template_execution.TriggerRestoreCleanupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.trigger_restore_cleanup
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
            restore_template_execution.RestoreTemplateExecution,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_restore_verification_plan(
        self,
        request: Optional[
            Union[
                gcb_restore_verification_plan.CreateRestoreVerificationPlanRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        restore_verification_plan: Optional[
            gcb_restore_verification_plan.RestoreVerificationPlan
        ] = None,
        restore_verification_plan_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new RestoreVerificationPlan in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_restore_verification_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                restore_verification_plan = backupdr_v1.RestoreVerificationPlan()
                restore_verification_plan.schedule = "schedule_value"

                request = backupdr_v1.CreateRestoreVerificationPlanRequest(
                    parent="parent_value",
                    restore_verification_plan_id="restore_verification_plan_id_value",
                    restore_verification_plan=restore_verification_plan,
                )

                # Make the request
                operation = await client.create_restore_verification_plan(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateRestoreVerificationPlanRequest, dict]]):
                The request object. The request message for creating a
                ``RestoreVerificationPlan``.
            parent (:class:`str`):
                Required. The ``RestoreVerificationPlan`` project and
                location in the format
                ``projects/{project}/locations/{location}``. In Google
                Cloud Backup and DR locations map to Google Cloud
                regions, for example **us-central1**.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_verification_plan (:class:`google.cloud.backupdr_v1.types.RestoreVerificationPlan`):
                Required. The ``RestoreVerificationPlan`` resource
                object to create.

                This corresponds to the ``restore_verification_plan`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_verification_plan_id (:class:`str`):
                Required. The name of the ``RestoreVerificationPlan`` to
                create. The name must be unique for the specified
                project and location. The name must start with a
                lowercase letter followed by up to 62 lowercase letters,
                numbers, or hyphens. Pattern,
                ``^[a-z]([-a-z0-9]*[a-z0-9])?$``.

                This corresponds to the ``restore_verification_plan_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.RestoreVerificationPlan` A RestoreVerificationPlan specifies the scheduling and clean-up template
                   for automated restore verification. It contains a
                   schedule to dictate when the verifications should
                   run, and a RestoreVerificationCleanupRule for
                   post-verification resource deletion.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            restore_verification_plan,
            restore_verification_plan_id,
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
        if not isinstance(
            request, gcb_restore_verification_plan.CreateRestoreVerificationPlanRequest
        ):
            request = (
                gcb_restore_verification_plan.CreateRestoreVerificationPlanRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if restore_verification_plan is not None:
            request.restore_verification_plan = restore_verification_plan
        if restore_verification_plan_id is not None:
            request.restore_verification_plan_id = restore_verification_plan_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_restore_verification_plan
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
            gcb_restore_verification_plan.RestoreVerificationPlan,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_restore_verification_plan_association(
        self,
        request: Optional[
            Union[
                gcb_restore_verification_plan_association.CreateRestoreVerificationPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        restore_verification_plan_association: Optional[
            gcb_restore_verification_plan_association.RestoreVerificationPlanAssociation
        ] = None,
        restore_verification_plan_association_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new RestoreVerificationPlanAssociation in a
        given RestoreVerificationPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_create_restore_verification_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                restore_verification_plan_association = backupdr_v1.RestoreVerificationPlanAssociation()
                restore_verification_plan_association.restore_template = "restore_template_value"
                restore_verification_plan_association.resource_type = "resource_type_value"

                request = backupdr_v1.CreateRestoreVerificationPlanAssociationRequest(
                    parent="parent_value",
                    restore_verification_plan_association_id="restore_verification_plan_association_id_value",
                    restore_verification_plan_association=restore_verification_plan_association,
                )

                # Make the request
                operation = await client.create_restore_verification_plan_association(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.CreateRestoreVerificationPlanAssociationRequest, dict]]):
                The request object. Request message for
                CreateRestoreVerificationPlanAssociation.
            parent (:class:`str`):
                Required. The parent resource where this association
                will be created. Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_verification_plan_association (:class:`google.cloud.backupdr_v1.types.RestoreVerificationPlanAssociation`):
                Required. The
                RestoreVerificationPlanAssociation
                resource to create.

                This corresponds to the ``restore_verification_plan_association`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_verification_plan_association_id (:class:`str`):
                Required. The ID to use for the association, which will
                become the final component of the association's resource
                name.

                This value should be 1-63 characters, and valid
                characters are /[a-z0-9\_-]/.

                This corresponds to the ``restore_verification_plan_association_id`` field
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

                The result type for the operation will be :class:`google.cloud.backupdr_v1.types.RestoreVerificationPlanAssociation` A RestoreVerificationPlanAssociation binds a specific workload to a
                   RestoreVerificationPlan.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            restore_verification_plan_association,
            restore_verification_plan_association_id,
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
        if not isinstance(
            request,
            gcb_restore_verification_plan_association.CreateRestoreVerificationPlanAssociationRequest,
        ):
            request = gcb_restore_verification_plan_association.CreateRestoreVerificationPlanAssociationRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if restore_verification_plan_association is not None:
            request.restore_verification_plan_association = (
                restore_verification_plan_association
            )
        if restore_verification_plan_association_id is not None:
            request.restore_verification_plan_association_id = (
                restore_verification_plan_association_id
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_restore_verification_plan_association
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
            gcb_restore_verification_plan_association.RestoreVerificationPlanAssociation,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_restore_verification_plan_association(
        self,
        request: Optional[
            Union[
                restore_verification_plan_association.GetRestoreVerificationPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> restore_verification_plan_association.RestoreVerificationPlanAssociation:
        r"""Gets details of a single
        RestoreVerificationPlanAssociation in a given
        RestoreVerificationPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_restore_verification_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetRestoreVerificationPlanAssociationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_restore_verification_plan_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetRestoreVerificationPlanAssociationRequest, dict]]):
                The request object. Request message for
                GetRestoreVerificationPlanAssociation.
            name (:class:`str`):
                Required. The resource name of the
                RestoreVerificationPlanAssociation to retrieve. Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``

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
            google.cloud.backupdr_v1.types.RestoreVerificationPlanAssociation:
                A RestoreVerificationPlanAssociation binds a specific workload to a
                   RestoreVerificationPlan.

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
            request,
            restore_verification_plan_association.GetRestoreVerificationPlanAssociationRequest,
        ):
            request = restore_verification_plan_association.GetRestoreVerificationPlanAssociationRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_restore_verification_plan_association
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

    async def list_restore_verification_plan_associations(
        self,
        request: Optional[
            Union[
                restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRestoreVerificationPlanAssociationsAsyncPager:
        r"""Lists RestoreVerificationPlanAssociations in a given
        RestoreVerificationPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_restore_verification_plan_associations():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListRestoreVerificationPlanAssociationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_restore_verification_plan_associations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsRequest, dict]]):
                The request object. Request message for
                ListRestoreVerificationPlanAssociations.
            parent (:class:`str`):
                Required. The parent RestoreVerificationPlan name.
                Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}``

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListRestoreVerificationPlanAssociationsAsyncPager:
                Response message for
                ListRestoreVerificationPlanAssociations.
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
        if not isinstance(
            request,
            restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest,
        ):
            request = restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_restore_verification_plan_associations
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
        response = pagers.ListRestoreVerificationPlanAssociationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_restore_verification_plan_association(
        self,
        request: Optional[
            Union[
                restore_verification_plan_association.DeleteRestoreVerificationPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single RestoreVerificationPlanAssociation
        in a given RestoreVerificationPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_restore_verification_plan_association():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteRestoreVerificationPlanAssociationRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_restore_verification_plan_association(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteRestoreVerificationPlanAssociationRequest, dict]]):
                The request object. Request message for
                DeleteRestoreVerificationPlanAssociation.
            name (:class:`str`):
                Required. The resource name of the
                RestoreVerificationPlanAssociation to delete. Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``

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
        if not isinstance(
            request,
            restore_verification_plan_association.DeleteRestoreVerificationPlanAssociationRequest,
        ):
            request = restore_verification_plan_association.DeleteRestoreVerificationPlanAssociationRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_restore_verification_plan_association
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
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def trigger_restore_verification(
        self,
        request: Optional[
            Union[
                restore_verification_plan_association.TriggerRestoreVerificationRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Triggers a new Restore Verification for the
        association in a given RestoreVerificationPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_trigger_restore_verification():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.TriggerRestoreVerificationRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.trigger_restore_verification(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.TriggerRestoreVerificationRequest, dict]]):
                The request object. Request message for
                TriggerRestoreVerification.
            name (:class:`str`):
                Required. The resource name of the
                RestoreVerificationPlanAssociation to trigger. Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``

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

                The result type for the operation will be
                :class:`google.cloud.backupdr_v1.types.TriggerRestoreVerificationResponse`
                Response message for TriggerRestoreVerification.

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
            request,
            restore_verification_plan_association.TriggerRestoreVerificationRequest,
        ):
            request = (
                restore_verification_plan_association.TriggerRestoreVerificationRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.trigger_restore_verification
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
            restore_verification_plan_association.TriggerRestoreVerificationResponse,
            metadata_type=backupdr.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_restore_verification_plan(
        self,
        request: Optional[
            Union[restore_verification_plan.GetRestoreVerificationPlanRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> restore_verification_plan.RestoreVerificationPlan:
        r"""Gets details of a single RestoreVerificationPlan.
        Returns the requested RestoreVerificationPlan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_get_restore_verification_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.GetRestoreVerificationPlanRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_restore_verification_plan(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.GetRestoreVerificationPlanRequest, dict]]):
                The request object. The request message for getting a
                ``RestoreVerificationPlan``.
            name (:class:`str`):
                Required. The resource name of the
                ``RestoreVerificationPlan`` to retrieve.

                Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restoreVerificationPlan}``

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
            google.cloud.backupdr_v1.types.RestoreVerificationPlan:
                A RestoreVerificationPlan specifies the scheduling and clean-up template
                   for automated restore verification. It contains a
                   schedule to dictate when the verifications should
                   run, and a RestoreVerificationCleanupRule for
                   post-verification resource deletion.

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
            request, restore_verification_plan.GetRestoreVerificationPlanRequest
        ):
            request = restore_verification_plan.GetRestoreVerificationPlanRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_restore_verification_plan
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

    async def list_restore_verification_plans(
        self,
        request: Optional[
            Union[restore_verification_plan.ListRestoreVerificationPlansRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRestoreVerificationPlansAsyncPager:
        r"""Lists RestoreVerificationPlans in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_list_restore_verification_plans():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.ListRestoreVerificationPlansRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_restore_verification_plans(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.ListRestoreVerificationPlansRequest, dict]]):
                The request object. The request message for getting a list of
                ``RestoreVerificationPlans``.
            parent (:class:`str`):
                Required. The project and location for which to retrieve
                ``RestoreVerificationPlans`` information. Format:
                ``projects/{project}/locations/{location}``. In Google
                Cloud Backup and DR, locations map to Google Cloud
                regions, for example **us-central1**. To retrieve
                restore verification plans for all locations, use "-"
                for the ``{location}`` value.

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
            google.cloud.backupdr_v1.services.backup_dr.pagers.ListRestoreVerificationPlansAsyncPager:
                The response message for getting a list of
                RestoreVerificationPlans.

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
            request, restore_verification_plan.ListRestoreVerificationPlansRequest
        ):
            request = restore_verification_plan.ListRestoreVerificationPlansRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_restore_verification_plans
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
        response = pagers.ListRestoreVerificationPlansAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_restore_verification_plan(
        self,
        request: Optional[
            Union[restore_verification_plan.DeleteRestoreVerificationPlanRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single RestoreVerificationPlan. If the ``force`` flag
        is set to ``true``, any RestoreVerificationPlanAssociations
        linked to this RestoreVerificationPlan will also be deleted.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import backupdr_v1

            async def sample_delete_restore_verification_plan():
                # Create a client
                client = backupdr_v1.BackupDRAsyncClient()

                # Initialize request argument(s)
                request = backupdr_v1.DeleteRestoreVerificationPlanRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_restore_verification_plan(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.backupdr_v1.types.DeleteRestoreVerificationPlanRequest, dict]]):
                The request object. The request message for deleting a
                ``RestoreVerificationPlan``.
            name (:class:`str`):
                Required. The resource name of the
                ``RestoreVerificationPlan`` to delete.

                Format:
                ``projects/{project}/locations/{location}/restoreVerificationPlans/{restoreVerificationPlan}``

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
        if not isinstance(
            request, restore_verification_plan.DeleteRestoreVerificationPlanRequest
        ):
            request = restore_verification_plan.DeleteRestoreVerificationPlanRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_restore_verification_plan
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
            metadata_type=backupdr.OperationMetadata,
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

    async def set_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.SetIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the IAM access control policy on the specified function.

        Replaces any existing policy.

        Args:
            request (:class:`~.iam_policy_pb2.SetIamPolicyRequest`):
                The request object. Request message for `SetIamPolicy`
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**

                ::

                    {
                      "bindings": [
                        {
                          "role": "roles/resourcemanager.organizationAdmin",
                          "members": [
                            "user:mike@example.com",
                            "group:admins@example.com",
                            "domain:google.com",
                            "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                          ]
                        },
                        {
                          "role": "roles/resourcemanager.organizationViewer",
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**

                ::

                    bindings:
                    - members:
                      - user:mike@example.com
                      - group:admins@example.com
                      - domain:google.com
                      - serviceAccount:my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin
                    - members:
                      - user:eve@example.com
                      role: roles/resourcemanager.organizationViewer
                      condition:
                        title: expirable access
                        description: Does not grant access after Sep 2020
                        expression: request.time < timestamp('2020-10-01T00:00:00.000Z')

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.SetIamPolicyRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.SetIamPolicyRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.set_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    async def get_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.GetIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the IAM access control policy for a function.

        Returns an empty policy if the function exists and does not have a
        policy set.

        Args:
            request (:class:`~.iam_policy_pb2.GetIamPolicyRequest`):
                The request object. Request message for `GetIamPolicy`
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if
                any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**

                ::

                    {
                      "bindings": [
                        {
                          "role": "roles/resourcemanager.organizationAdmin",
                          "members": [
                            "user:mike@example.com",
                            "group:admins@example.com",
                            "domain:google.com",
                            "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                          ]
                        },
                        {
                          "role": "roles/resourcemanager.organizationViewer",
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**

                ::

                    bindings:
                    - members:
                      - user:mike@example.com
                      - group:admins@example.com
                      - domain:google.com
                      - serviceAccount:my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin
                    - members:
                      - user:eve@example.com
                      role: roles/resourcemanager.organizationViewer
                      condition:
                        title: expirable access
                        description: Does not grant access after Sep 2020
                        expression: request.time < timestamp('2020-10-01T00:00:00.000Z')

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.GetIamPolicyRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.GetIamPolicyRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    async def test_iam_permissions(
        self,
        request: Optional[Union[iam_policy_pb2.TestIamPermissionsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Tests the specified IAM permissions against the IAM access control
            policy for a function.

        If the function does not exist, this will return an empty set
        of permissions, not a NOT_FOUND error.

        Args:
            request (:class:`~.iam_policy_pb2.TestIamPermissionsRequest`):
                The request object. Request message for
                `TestIamPermissions` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for ``TestIamPermissions`` method.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.TestIamPermissionsRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.TestIamPermissionsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[
            self._client._transport.test_iam_permissions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    async def __aenter__(self) -> "BackupDRAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("BackupDRAsyncClient",)
