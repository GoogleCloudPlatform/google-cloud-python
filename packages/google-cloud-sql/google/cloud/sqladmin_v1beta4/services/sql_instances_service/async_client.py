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

from google.cloud.sqladmin_v1beta4 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.sqladmin_v1beta4.services.sql_instances_service import pagers
from google.cloud.sqladmin_v1beta4.types import cloud_sql, cloud_sql_resources

from .client import SqlInstancesServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, SqlInstancesServiceTransport
from .transports.grpc_asyncio import SqlInstancesServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SqlInstancesServiceAsyncClient:
    """"""

    _client: SqlInstancesServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SqlInstancesServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SqlInstancesServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SqlInstancesServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SqlInstancesServiceClient._DEFAULT_UNIVERSE

    backup_path = staticmethod(SqlInstancesServiceClient.backup_path)
    parse_backup_path = staticmethod(SqlInstancesServiceClient.parse_backup_path)
    backup_dr_backup_path = staticmethod(
        SqlInstancesServiceClient.backup_dr_backup_path
    )
    parse_backup_dr_backup_path = staticmethod(
        SqlInstancesServiceClient.parse_backup_dr_backup_path
    )
    crypto_key_path = staticmethod(SqlInstancesServiceClient.crypto_key_path)
    parse_crypto_key_path = staticmethod(
        SqlInstancesServiceClient.parse_crypto_key_path
    )
    crypto_key_version_path = staticmethod(
        SqlInstancesServiceClient.crypto_key_version_path
    )
    parse_crypto_key_version_path = staticmethod(
        SqlInstancesServiceClient.parse_crypto_key_version_path
    )
    network_path = staticmethod(SqlInstancesServiceClient.network_path)
    parse_network_path = staticmethod(SqlInstancesServiceClient.parse_network_path)
    network_attachment_path = staticmethod(
        SqlInstancesServiceClient.network_attachment_path
    )
    parse_network_attachment_path = staticmethod(
        SqlInstancesServiceClient.parse_network_attachment_path
    )
    secret_version_path = staticmethod(SqlInstancesServiceClient.secret_version_path)
    parse_secret_version_path = staticmethod(
        SqlInstancesServiceClient.parse_secret_version_path
    )
    service_connection_policy_path = staticmethod(
        SqlInstancesServiceClient.service_connection_policy_path
    )
    parse_service_connection_policy_path = staticmethod(
        SqlInstancesServiceClient.parse_service_connection_policy_path
    )
    common_billing_account_path = staticmethod(
        SqlInstancesServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SqlInstancesServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SqlInstancesServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        SqlInstancesServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        SqlInstancesServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        SqlInstancesServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(SqlInstancesServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        SqlInstancesServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(SqlInstancesServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        SqlInstancesServiceClient.parse_common_location_path
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
            SqlInstancesServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            SqlInstancesServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SqlInstancesServiceAsyncClient, info, *args, **kwargs)

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
            SqlInstancesServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            SqlInstancesServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(SqlInstancesServiceAsyncClient, filename, *args, **kwargs)

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
        return SqlInstancesServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> SqlInstancesServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            SqlInstancesServiceTransport: The transport used by the client instance.
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

    get_transport_class = SqlInstancesServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                SqlInstancesServiceTransport,
                Callable[..., SqlInstancesServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the sql instances service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SqlInstancesServiceTransport,Callable[..., SqlInstancesServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SqlInstancesServiceTransport constructor.
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
        self._client = SqlInstancesServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.sql_v1beta4.SqlInstancesServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
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
                    "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                    "credentialsType": None,
                },
            )

    async def add_server_ca(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesAddServerCaRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Add a new trusted Certificate Authority (CA) version
        for the specified instance. Required to prepare for a
        certificate rotation. If a CA version was previously
        added but never used in a certificate rotation, this
        operation replaces that version. There cannot be more
        than one CA version waiting to be rotated in. For
        instances that have enabled Certificate Authority
        Service (CAS) based server CA, use AddServerCertificate
        to add a new server certificate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_add_server_ca():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesAddServerCaRequest(
                )

                # Make the request
                response = await client.add_server_ca(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesAddServerCaRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesAddServerCaRequest):
            request = cloud_sql.SqlInstancesAddServerCaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_server_ca
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def add_server_certificate(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesAddServerCertificateRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Add a new trusted server certificate version for the
        specified instance using Certificate Authority Service
        (CAS) server CA. Required to prepare for a certificate
        rotation. If a server certificate version was previously
        added but never used in a certificate rotation, this
        operation replaces that version. There cannot be more
        than one certificate version waiting to be rotated in.
        For instances not using CAS server CA, use AddServerCa
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_add_server_certificate():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesAddServerCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.add_server_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesAddServerCertificateRequest, dict]]):
                The request object. Request for AddServerCertificate RPC.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesAddServerCertificateRequest):
            request = cloud_sql.SqlInstancesAddServerCertificateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_server_certificate
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def add_entra_id_certificate(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesAddEntraIdCertificateRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Adds a new Entra ID certificate for the specified
        instance. If an Entra ID certificate was previously
        added but never used in a certificate rotation, this
        operation replaces that version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_add_entra_id_certificate():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesAddEntraIdCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.add_entra_id_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesAddEntraIdCertificateRequest, dict]]):
                The request object. Request for AddEntraIdCertificate
                RPC.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesAddEntraIdCertificateRequest):
            request = cloud_sql.SqlInstancesAddEntraIdCertificateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_entra_id_certificate
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def clone(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesCloneRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Creates a Cloud SQL instance as a clone of the source
        instance. Using this operation might cause your instance
        to restart.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_clone():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesCloneRequest(
                )

                # Make the request
                response = await client.clone(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesCloneRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesCloneRequest):
            request = cloud_sql.SqlInstancesCloneRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.clone]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def delete(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesDeleteRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Deletes a Cloud SQL instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_delete():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesDeleteRequest(
                    final_backup_ttl_days=2210,
                )

                # Make the request
                response = await client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesDeleteRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesDeleteRequest):
            request = cloud_sql.SqlInstancesDeleteRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def demote_master(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesDemoteMasterRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Demotes the stand-alone instance to be a Cloud SQL
        read replica for an external database server.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_demote_master():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesDemoteMasterRequest(
                )

                # Make the request
                response = await client.demote_master(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesDemoteMasterRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesDemoteMasterRequest):
            request = cloud_sql.SqlInstancesDemoteMasterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.demote_master
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def demote(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesDemoteRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Demotes an existing standalone instance to be a Cloud
        SQL read replica for an external database server.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_demote():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesDemoteRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.demote(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesDemoteRequest, dict]]):
                The request object. Instance demote request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesDemoteRequest):
            request = cloud_sql.SqlInstancesDemoteRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.demote]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def export(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesExportRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Exports data from a Cloud SQL instance to a Cloud
        Storage bucket as a SQL dump or CSV file.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_export():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesExportRequest(
                )

                # Make the request
                response = await client.export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesExportRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesExportRequest):
            request = cloud_sql.SqlInstancesExportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.export]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def failover(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesFailoverRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Initiates a manual failover of a high availability (HA) primary
        instance to a standby instance, which becomes the primary
        instance. Users are then rerouted to the new primary. For more
        information, see the `Overview of high
        availability <https://cloud.google.com/sql/docs/mysql/high-availability>`__
        page in the Cloud SQL documentation. If using Legacy HA (MySQL
        only), this causes the instance to failover to its failover
        replica instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_failover():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesFailoverRequest(
                )

                # Make the request
                response = await client.failover(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesFailoverRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesFailoverRequest):
            request = cloud_sql.SqlInstancesFailoverRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.failover]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def reencrypt(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesReencryptRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Reencrypt CMEK instance with latest key version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_reencrypt():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesReencryptRequest(
                )

                # Make the request
                response = await client.reencrypt(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesReencryptRequest, dict]]):
                The request object. Instance reencrypt request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesReencryptRequest):
            request = cloud_sql.SqlInstancesReencryptRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reencrypt
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def get(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesGetRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.DatabaseInstance:
        r"""Retrieves a resource containing information about a
        Cloud SQL instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_get():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesGetRequest(
                )

                # Make the request
                response = await client.get(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesGetRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.DatabaseInstance:
                A Cloud SQL instance resource.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesGetRequest):
            request = cloud_sql.SqlInstancesGetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def import_(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesImportRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Imports data into a Cloud SQL instance from a SQL
        dump  or CSV file in Cloud Storage.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_import():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesImportRequest(
                )

                # Make the request
                response = await client.import_(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesImportRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesImportRequest):
            request = cloud_sql.SqlInstancesImportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.import_]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def insert(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesInsertRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Creates a new Cloud SQL instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_insert():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesInsertRequest(
                )

                # Make the request
                response = await client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesInsertRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesInsertRequest):
            request = cloud_sql.SqlInstancesInsertRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.insert]

        header_params: dict[str, str] = {}

        if request.project:
            header_params["project"] = request.project

        routing_param_regex = re.compile("^(?P<region>.*)$")
        regex_match = routing_param_regex.match(request.body.region)
        if regex_match and regex_match.group("region"):
            header_params["region"] = regex_match.group("region")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def list(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesListRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAsyncPager:
        r"""Lists instances under a given project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_list():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesListRequest(
                )

                # Make the request
                page_result = client.list(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesListRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.services.sql_instances_service.pagers.ListAsyncPager:
                Database instances list response.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesListRequest):
            request = cloud_sql.SqlInstancesListRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.list]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", request.project),)),
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
        response = pagers.ListAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_server_cas(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesListServerCasRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.InstancesListServerCasResponse:
        r"""Lists all of the trusted Certificate Authorities
        (CAs) for the specified instance. There can be up to
        three CAs listed: the CA that was used to sign the
        certificate that is currently in use, a CA that has been
        added but not yet used to sign a certificate, and a CA
        used to sign a certificate that has previously rotated
        out.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_list_server_cas():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesListServerCasRequest(
                )

                # Make the request
                response = await client.list_server_cas(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesListServerCasRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.InstancesListServerCasResponse:
                Instances ListServerCas response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesListServerCasRequest):
            request = cloud_sql.SqlInstancesListServerCasRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_server_cas
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def list_server_certificates(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesListServerCertificatesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.InstancesListServerCertificatesResponse:
        r"""Lists all versions of server certificates and
        certificate authorities (CAs) for the specified
        instance. There can be up to three sets of certs listed:

        the certificate that is currently in use, a future that
        has been added but not yet used to sign a certificate,
        and a certificate that has been rotated out. For
        instances not using Certificate Authority Service (CAS)
        server CA, use ListServerCas instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_list_server_certificates():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesListServerCertificatesRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.list_server_certificates(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesListServerCertificatesRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.InstancesListServerCertificatesResponse:
                Instances ListServerCertificatess
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesListServerCertificatesRequest):
            request = cloud_sql.SqlInstancesListServerCertificatesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_server_certificates
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def list_entra_id_certificates(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesListEntraIdCertificatesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.InstancesListEntraIdCertificatesResponse:
        r"""Lists all versions of EntraID certificates for the
        specified instance. There can be up to three sets of
        certificates listed: the certificate that is currently
        in use, a future that has been added but not yet used to
        sign a certificate, and a certificate that has been
        rotated out.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_list_entra_id_certificates():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesListEntraIdCertificatesRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.list_entra_id_certificates(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesListEntraIdCertificatesRequest, dict]]):
                The request object. Request message for
                SqlInstancesService.ListEntraIdCertificates.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.InstancesListEntraIdCertificatesResponse:
                Instances ListEntraIdCertificates
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql.SqlInstancesListEntraIdCertificatesRequest
        ):
            request = cloud_sql.SqlInstancesListEntraIdCertificatesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_entra_id_certificates
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def patch(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesPatchRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Partially updates settings of a Cloud SQL instance by
        merging the request with the current configuration. This
        method supports patch semantics.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_patch():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesPatchRequest(
                )

                # Make the request
                response = await client.patch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesPatchRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesPatchRequest):
            request = cloud_sql.SqlInstancesPatchRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.patch]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def promote_replica(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesPromoteReplicaRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Promotes the read replica instance to be an
        independent Cloud SQL primary instance.
        Using this operation might cause your instance to
        restart.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_promote_replica():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesPromoteReplicaRequest(
                )

                # Make the request
                response = await client.promote_replica(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesPromoteReplicaRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesPromoteReplicaRequest):
            request = cloud_sql.SqlInstancesPromoteReplicaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.promote_replica
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def switchover(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesSwitchoverRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Switches over from the primary instance to the DR
        replica instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_switchover():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesSwitchoverRequest(
                )

                # Make the request
                response = await client.switchover(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesSwitchoverRequest, dict]]):
                The request object. Instance switchover request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesSwitchoverRequest):
            request = cloud_sql.SqlInstancesSwitchoverRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.switchover
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def reset_ssl_config(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesResetSslConfigRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Deletes all client certificates and generates a new
        server SSL certificate for the instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_reset_ssl_config():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesResetSslConfigRequest(
                )

                # Make the request
                response = await client.reset_ssl_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesResetSslConfigRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesResetSslConfigRequest):
            request = cloud_sql.SqlInstancesResetSslConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reset_ssl_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def restart(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesRestartRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Restarts a Cloud SQL instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_restart():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesRestartRequest(
                )

                # Make the request
                response = await client.restart(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesRestartRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesRestartRequest):
            request = cloud_sql.SqlInstancesRestartRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.restart]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def restore_backup(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesRestoreBackupRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Restores a backup of a Cloud SQL instance. Using this
        operation might cause your instance to restart.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_restore_backup():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesRestoreBackupRequest(
                )

                # Make the request
                response = await client.restore_backup(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesRestoreBackupRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesRestoreBackupRequest):
            request = cloud_sql.SqlInstancesRestoreBackupRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.restore_backup
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def rotate_server_ca(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesRotateServerCaRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Rotates the server certificate to one signed by the
        Certificate Authority (CA) version previously added with
        the addServerCA method. For instances that have enabled
        Certificate Authority Service (CAS) based server CA, use
        RotateServerCertificate to rotate the server
        certificate.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_rotate_server_ca():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesRotateServerCaRequest(
                )

                # Make the request
                response = await client.rotate_server_ca(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesRotateServerCaRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesRotateServerCaRequest):
            request = cloud_sql.SqlInstancesRotateServerCaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.rotate_server_ca
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def rotate_server_certificate(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesRotateServerCertificateRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Rotates the server certificate version to one
        previously added with the addServerCertificate method.
        For instances not using Certificate Authority Service
        (CAS) server CA, use RotateServerCa instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_rotate_server_certificate():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesRotateServerCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.rotate_server_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesRotateServerCertificateRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql.SqlInstancesRotateServerCertificateRequest
        ):
            request = cloud_sql.SqlInstancesRotateServerCertificateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.rotate_server_certificate
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def rotate_entra_id_certificate(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesRotateEntraIdCertificateRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Rotates the Entra Id certificate version to one
        previously added with the addEntraIdCertificate method.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_rotate_entra_id_certificate():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesRotateEntraIdCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.rotate_entra_id_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesRotateEntraIdCertificateRequest, dict]]):
                The request object. Request message for
                SqlInstancesService.RotateEntraIdCertificate.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql.SqlInstancesRotateEntraIdCertificateRequest
        ):
            request = cloud_sql.SqlInstancesRotateEntraIdCertificateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.rotate_entra_id_certificate
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def start_replica(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesStartReplicaRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Starts the replication in the read replica instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_start_replica():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesStartReplicaRequest(
                )

                # Make the request
                response = await client.start_replica(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesStartReplicaRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesStartReplicaRequest):
            request = cloud_sql.SqlInstancesStartReplicaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.start_replica
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def stop_replica(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesStopReplicaRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Stops the replication in the read replica instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_stop_replica():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesStopReplicaRequest(
                )

                # Make the request
                response = await client.stop_replica(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesStopReplicaRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesStopReplicaRequest):
            request = cloud_sql.SqlInstancesStopReplicaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.stop_replica
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def truncate_log(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesTruncateLogRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Truncate MySQL general and slow query log tables
        MySQL only.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_truncate_log():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesTruncateLogRequest(
                )

                # Make the request
                response = await client.truncate_log(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesTruncateLogRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesTruncateLogRequest):
            request = cloud_sql.SqlInstancesTruncateLogRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.truncate_log
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def update(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesUpdateRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Updates settings of a Cloud SQL instance. Using this
        operation might cause your instance to restart.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_update():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesUpdateRequest(
                )

                # Make the request
                response = await client.update(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesUpdateRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesUpdateRequest):
            request = cloud_sql.SqlInstancesUpdateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.update]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def create_ephemeral(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesCreateEphemeralCertRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.SslCert:
        r"""Generates a short-lived X509 certificate containing
        the provided public key and signed by a private key
        specific to the target instance. Users may use the
        certificate to authenticate as themselves when
        connecting to the database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_create_ephemeral():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesCreateEphemeralCertRequest(
                )

                # Make the request
                response = await client.create_ephemeral(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesCreateEphemeralCertRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SslCert:
                SslCerts Resource
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesCreateEphemeralCertRequest):
            request = cloud_sql.SqlInstancesCreateEphemeralCertRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_ephemeral
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def reschedule_maintenance(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesRescheduleMaintenanceRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Reschedules the maintenance on the given instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_reschedule_maintenance():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesRescheduleMaintenanceRequest(
                )

                # Make the request
                response = await client.reschedule_maintenance(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesRescheduleMaintenanceRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesRescheduleMaintenanceRequest):
            request = cloud_sql.SqlInstancesRescheduleMaintenanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reschedule_maintenance
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def verify_external_sync_settings(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse:
        r"""Verify External primary instance external sync
        settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_verify_external_sync_settings():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesVerifyExternalSyncSettingsRequest(
                )

                # Make the request
                response = await client.verify_external_sync_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesVerifyExternalSyncSettingsRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SqlInstancesVerifyExternalSyncSettingsResponse:
                Instance verify external sync
                settings response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest
        ):
            request = cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.verify_external_sync_settings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def start_external_sync(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesStartExternalSyncRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Start External primary instance migration.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_start_external_sync():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesStartExternalSyncRequest(
                )

                # Make the request
                response = await client.start_external_sync(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesStartExternalSyncRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesStartExternalSyncRequest):
            request = cloud_sql.SqlInstancesStartExternalSyncRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.start_external_sync
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def perform_disk_shrink(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesPerformDiskShrinkRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Perform Disk Shrink on primary instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_perform_disk_shrink():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesPerformDiskShrinkRequest(
                )

                # Make the request
                response = await client.perform_disk_shrink(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesPerformDiskShrinkRequest, dict]]):
                The request object. Instance perform disk shrink request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesPerformDiskShrinkRequest):
            request = cloud_sql.SqlInstancesPerformDiskShrinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.perform_disk_shrink
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def get_disk_shrink_config(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesGetDiskShrinkConfigRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse:
        r"""Get Disk Shrink Config for a given instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_get_disk_shrink_config():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesGetDiskShrinkConfigRequest(
                )

                # Make the request
                response = await client.get_disk_shrink_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesGetDiskShrinkConfigRequest, dict]]):
                The request object. Instance get disk shrink config
                request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SqlInstancesGetDiskShrinkConfigResponse:
                Instance get disk shrink config
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesGetDiskShrinkConfigRequest):
            request = cloud_sql.SqlInstancesGetDiskShrinkConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_disk_shrink_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def reset_replica_size(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesResetReplicaSizeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Reset Replica Size to primary instance disk size.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_reset_replica_size():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesResetReplicaSizeRequest(
                )

                # Make the request
                response = await client.reset_replica_size(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesResetReplicaSizeRequest, dict]]):
                The request object. Instance reset replica size request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesResetReplicaSizeRequest):
            request = cloud_sql.SqlInstancesResetReplicaSizeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reset_replica_size
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def get_latest_recovery_time(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse:
        r"""Get Latest Recovery Time for a given instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_get_latest_recovery_time():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesGetLatestRecoveryTimeRequest(
                )

                # Make the request
                response = await client.get_latest_recovery_time(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesGetLatestRecoveryTimeRequest, dict]]):
                The request object. Instance get latest recovery time
                request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SqlInstancesGetLatestRecoveryTimeResponse:
                Instance get latest recovery time
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest):
            request = cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_latest_recovery_time
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def execute_sql(
        self,
        request: Optional[Union[cloud_sql.SqlInstancesExecuteSqlRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql.SqlInstancesExecuteSqlResponse:
        r"""Execute SQL statements.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_execute_sql():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesExecuteSqlRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.execute_sql(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesExecuteSqlRequest, dict]]):
                The request object. Execute SQL statements request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SqlInstancesExecuteSqlResponse:

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesExecuteSqlRequest):
            request = cloud_sql.SqlInstancesExecuteSqlRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.execute_sql
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def acquire_ssrs_lease(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesAcquireSsrsLeaseRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql.SqlInstancesAcquireSsrsLeaseResponse:
        r"""Acquire a lease for the setup of SQL Server Reporting
        Services (SSRS).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_acquire_ssrs_lease():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesAcquireSsrsLeaseRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.acquire_ssrs_lease(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesAcquireSsrsLeaseRequest, dict]]):
                The request object. Request to acquire a lease for SSRS.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SqlInstancesAcquireSsrsLeaseResponse:
                Acquire SSRS lease response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesAcquireSsrsLeaseRequest):
            request = cloud_sql.SqlInstancesAcquireSsrsLeaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.acquire_ssrs_lease
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def release_ssrs_lease(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesReleaseSsrsLeaseRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql.SqlInstancesReleaseSsrsLeaseResponse:
        r"""Release a lease for the setup of SQL Server Reporting
        Services (SSRS).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_release_ssrs_lease():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesReleaseSsrsLeaseRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = await client.release_ssrs_lease(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesReleaseSsrsLeaseRequest, dict]]):
                The request object. Request to release a lease for SSRS.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.SqlInstancesReleaseSsrsLeaseResponse:
                The response for the release of the
                SSRS lease.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesReleaseSsrsLeaseRequest):
            request = cloud_sql.SqlInstancesReleaseSsrsLeaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.release_ssrs_lease
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def pre_check_major_version_upgrade(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Execute MVU Pre-checks

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_pre_check_major_version_upgrade():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                body = sqladmin_v1beta4.InstancesPreCheckMajorVersionUpgradeRequest()
                body.pre_check_major_version_upgrade_context.target_database_version = "SQLSERVER_2025_EXPRESS"

                request = sqladmin_v1beta4.SqlInstancesPreCheckMajorVersionUpgradeRequest(
                    instance="instance_value",
                    project="project_value",
                    body=body,
                )

                # Make the request
                response = await client.pre_check_major_version_upgrade(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesPreCheckMajorVersionUpgradeRequest, dict]]):
                The request object. Request for Pre-checks for MVU
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest
        ):
            request = cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.pre_check_major_version_upgrade
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project", request.project),
                    ("instance", request.instance),
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

    async def point_in_time_restore(
        self,
        request: Optional[
            Union[cloud_sql.SqlInstancesPointInTimeRestoreRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Point in time restore for an instance managed by
        Google Cloud Backup and Disaster Recovery.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1beta4

            async def sample_point_in_time_restore():
                # Create a client
                client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

                # Initialize request argument(s)
                request = sqladmin_v1beta4.SqlInstancesPointInTimeRestoreRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.point_in_time_restore(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.sqladmin_v1beta4.types.SqlInstancesPointInTimeRestoreRequest, dict]]):
                The request object. Request to perform a point in time
                restore on a Google Cloud Backup and
                Disaster Recovery managed instance.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1beta4.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql.SqlInstancesPointInTimeRestoreRequest):
            request = cloud_sql.SqlInstancesPointInTimeRestoreRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.point_in_time_restore
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

    async def __aenter__(self) -> "SqlInstancesServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SqlInstancesServiceAsyncClient",)
