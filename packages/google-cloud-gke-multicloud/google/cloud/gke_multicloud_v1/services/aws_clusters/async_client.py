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
import warnings
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

from google.cloud.gke_multicloud_v1 import gapic_version as package_version

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

from google.cloud.gke_multicloud_v1.services.aws_clusters import pagers
from google.cloud.gke_multicloud_v1.types import (
    aws_resources,
    aws_service,
    common_resources,
)

from .client import AwsClustersClient
from .transports.base import DEFAULT_CLIENT_INFO, AwsClustersTransport
from .transports.grpc_asyncio import AwsClustersGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AwsClustersAsyncClient:
    """The AwsClusters API provides a single centrally managed
    service to create and manage Anthos clusters that run on AWS
    infrastructure.
    """

    _client: AwsClustersClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AwsClustersClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AwsClustersClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AwsClustersClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AwsClustersClient._DEFAULT_UNIVERSE

    aws_cluster_path = staticmethod(AwsClustersClient.aws_cluster_path)
    parse_aws_cluster_path = staticmethod(AwsClustersClient.parse_aws_cluster_path)
    aws_node_pool_path = staticmethod(AwsClustersClient.aws_node_pool_path)
    parse_aws_node_pool_path = staticmethod(AwsClustersClient.parse_aws_node_pool_path)
    aws_server_config_path = staticmethod(AwsClustersClient.aws_server_config_path)
    parse_aws_server_config_path = staticmethod(
        AwsClustersClient.parse_aws_server_config_path
    )
    common_billing_account_path = staticmethod(
        AwsClustersClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AwsClustersClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AwsClustersClient.common_folder_path)
    parse_common_folder_path = staticmethod(AwsClustersClient.parse_common_folder_path)
    common_organization_path = staticmethod(AwsClustersClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        AwsClustersClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AwsClustersClient.common_project_path)
    parse_common_project_path = staticmethod(
        AwsClustersClient.parse_common_project_path
    )
    common_location_path = staticmethod(AwsClustersClient.common_location_path)
    parse_common_location_path = staticmethod(
        AwsClustersClient.parse_common_location_path
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
            AwsClustersAsyncClient: The constructed client.
        """
        sa_info_func = (
            AwsClustersClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AwsClustersAsyncClient, info, *args, **kwargs)

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
            AwsClustersAsyncClient: The constructed client.
        """
        sa_file_func = (
            AwsClustersClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AwsClustersAsyncClient, filename, *args, **kwargs)

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
        return AwsClustersClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AwsClustersTransport:
        """Returns the transport used by the client instance.

        Returns:
            AwsClustersTransport: The transport used by the client instance.
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

    get_transport_class = AwsClustersClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, AwsClustersTransport, Callable[..., AwsClustersTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the aws clusters async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AwsClustersTransport,Callable[..., AwsClustersTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AwsClustersTransport constructor.
                If set to None, a transport is chosen automatically.
                NOTE: "rest" transport functionality is currently in a
                beta state (preview). We welcome your feedback via an
                issue in this library's source repository.
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
        self._client = AwsClustersClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.gkemulticloud_v1.AwsClustersAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
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
                    "serviceName": "google.cloud.gkemulticloud.v1.AwsClusters",
                    "credentialsType": None,
                },
            )

    async def create_aws_cluster(
        self,
        request: Optional[Union[aws_service.CreateAwsClusterRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        aws_cluster: Optional[aws_resources.AwsCluster] = None,
        aws_cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster] resource
        on a given Google Cloud Platform project and region.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_create_aws_cluster():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                aws_cluster = gke_multicloud_v1.AwsCluster()
                aws_cluster.networking.vpc_id = "vpc_id_value"
                aws_cluster.networking.pod_address_cidr_blocks = ['pod_address_cidr_blocks_value1', 'pod_address_cidr_blocks_value2']
                aws_cluster.networking.service_address_cidr_blocks = ['service_address_cidr_blocks_value1', 'service_address_cidr_blocks_value2']
                aws_cluster.aws_region = "aws_region_value"
                aws_cluster.control_plane.version = "version_value"
                aws_cluster.control_plane.subnet_ids = ['subnet_ids_value1', 'subnet_ids_value2']
                aws_cluster.control_plane.iam_instance_profile = "iam_instance_profile_value"
                aws_cluster.control_plane.database_encryption.kms_key_arn = "kms_key_arn_value"
                aws_cluster.control_plane.aws_services_authentication.role_arn = "role_arn_value"
                aws_cluster.control_plane.config_encryption.kms_key_arn = "kms_key_arn_value"
                aws_cluster.fleet.project = "project_value"

                request = gke_multicloud_v1.CreateAwsClusterRequest(
                    parent="parent_value",
                    aws_cluster=aws_cluster,
                    aws_cluster_id="aws_cluster_id_value",
                )

                # Make the request
                operation = await client.create_aws_cluster(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.CreateAwsClusterRequest, dict]]):
                The request object. Request message for ``AwsClusters.CreateAwsCluster``
                method.
            parent (:class:`str`):
                Required. The parent location where this
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                resource will be created.

                Location names are formatted as
                ``projects/<project-id>/locations/<region>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            aws_cluster (:class:`google.cloud.gke_multicloud_v1.types.AwsCluster`):
                Required. The specification of the
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                to create.

                This corresponds to the ``aws_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            aws_cluster_id (:class:`str`):
                Required. A client provided ID the resource. Must be
                unique within the parent resource.

                The provided ID will be part of the
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                resource name formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>``.

                Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
                than 63 characters.

                This corresponds to the ``aws_cluster_id`` field
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
                :class:`google.cloud.gke_multicloud_v1.types.AwsCluster`
                An Anthos cluster running on AWS.

        """
        warnings.warn(
            "AwsClustersAsyncClient.create_aws_cluster is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, aws_cluster, aws_cluster_id]
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
        if not isinstance(request, aws_service.CreateAwsClusterRequest):
            request = aws_service.CreateAwsClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if aws_cluster is not None:
            request.aws_cluster = aws_cluster
        if aws_cluster_id is not None:
            request.aws_cluster_id = aws_cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_aws_cluster
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
            aws_resources.AwsCluster,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_aws_cluster(
        self,
        request: Optional[Union[aws_service.UpdateAwsClusterRequest, dict]] = None,
        *,
        aws_cluster: Optional[aws_resources.AwsCluster] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates an
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_update_aws_cluster():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                aws_cluster = gke_multicloud_v1.AwsCluster()
                aws_cluster.networking.vpc_id = "vpc_id_value"
                aws_cluster.networking.pod_address_cidr_blocks = ['pod_address_cidr_blocks_value1', 'pod_address_cidr_blocks_value2']
                aws_cluster.networking.service_address_cidr_blocks = ['service_address_cidr_blocks_value1', 'service_address_cidr_blocks_value2']
                aws_cluster.aws_region = "aws_region_value"
                aws_cluster.control_plane.version = "version_value"
                aws_cluster.control_plane.subnet_ids = ['subnet_ids_value1', 'subnet_ids_value2']
                aws_cluster.control_plane.iam_instance_profile = "iam_instance_profile_value"
                aws_cluster.control_plane.database_encryption.kms_key_arn = "kms_key_arn_value"
                aws_cluster.control_plane.aws_services_authentication.role_arn = "role_arn_value"
                aws_cluster.control_plane.config_encryption.kms_key_arn = "kms_key_arn_value"
                aws_cluster.fleet.project = "project_value"

                request = gke_multicloud_v1.UpdateAwsClusterRequest(
                    aws_cluster=aws_cluster,
                )

                # Make the request
                operation = await client.update_aws_cluster(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.UpdateAwsClusterRequest, dict]]):
                The request object. Request message for ``AwsClusters.UpdateAwsCluster``
                method.
            aws_cluster (:class:`google.cloud.gke_multicloud_v1.types.AwsCluster`):
                Required. The
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                resource to update.

                This corresponds to the ``aws_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. The elements of the
                repeated paths field can only include these fields from
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]:

                - ``description``.
                - ``annotations``.
                - ``control_plane.version``.
                - ``authorization.admin_users``.
                - ``authorization.admin_groups``.
                - ``binary_authorization.evaluation_mode``.
                - ``control_plane.aws_services_authentication.role_arn``.
                - ``control_plane.aws_services_authentication.role_session_name``.
                - ``control_plane.config_encryption.kms_key_arn``.
                - ``control_plane.instance_type``.
                - ``control_plane.security_group_ids``.
                - ``control_plane.proxy_config``.
                - ``control_plane.proxy_config.secret_arn``.
                - ``control_plane.proxy_config.secret_version``.
                - ``control_plane.root_volume.size_gib``.
                - ``control_plane.root_volume.volume_type``.
                - ``control_plane.root_volume.iops``.
                - ``control_plane.root_volume.throughput``.
                - ``control_plane.root_volume.kms_key_arn``.
                - ``control_plane.ssh_config``.
                - ``control_plane.ssh_config.ec2_key_pair``.
                - ``control_plane.instance_placement.tenancy``.
                - ``control_plane.iam_instance_profile``.
                - ``logging_config.component_config.enable_components``.
                - ``control_plane.tags``.
                - ``monitoring_config.managed_prometheus_config.enabled``.
                - ``networking.per_node_pool_sg_rules_disabled``.

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
                :class:`google.cloud.gke_multicloud_v1.types.AwsCluster`
                An Anthos cluster running on AWS.

        """
        warnings.warn(
            "AwsClustersAsyncClient.update_aws_cluster is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [aws_cluster, update_mask]
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
        if not isinstance(request, aws_service.UpdateAwsClusterRequest):
            request = aws_service.UpdateAwsClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if aws_cluster is not None:
            request.aws_cluster = aws_cluster
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_aws_cluster
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("aws_cluster.name", request.aws_cluster.name),)
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
            aws_resources.AwsCluster,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_aws_cluster(
        self,
        request: Optional[Union[aws_service.GetAwsClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_resources.AwsCluster:
        r"""Describes a specific
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster] resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_aws_cluster():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAwsClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_aws_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAwsClusterRequest, dict]]):
                The request object. Request message for ``AwsClusters.GetAwsCluster``
                method.
            name (:class:`str`):
                Required. The name of the
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                resource to describe.

                ``AwsCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
            google.cloud.gke_multicloud_v1.types.AwsCluster:
                An Anthos cluster running on AWS.
        """
        warnings.warn(
            "AwsClustersAsyncClient.get_aws_cluster is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, aws_service.GetAwsClusterRequest):
            request = aws_service.GetAwsClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_aws_cluster
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

    async def list_aws_clusters(
        self,
        request: Optional[Union[aws_service.ListAwsClustersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAwsClustersAsyncPager:
        r"""Lists all [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
        resources on a given Google Cloud project and region.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_list_aws_clusters():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.ListAwsClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_aws_clusters(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.ListAwsClustersRequest, dict]]):
                The request object. Request message for ``AwsClusters.ListAwsClusters``
                method.
            parent (:class:`str`):
                Required. The parent location which owns this collection
                of
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                resources.

                Location names are formatted as
                ``projects/<project-id>/locations/<region>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
            google.cloud.gke_multicloud_v1.services.aws_clusters.pagers.ListAwsClustersAsyncPager:
                Response message for AwsClusters.ListAwsClusters method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "AwsClustersAsyncClient.list_aws_clusters is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, aws_service.ListAwsClustersRequest):
            request = aws_service.ListAwsClustersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_aws_clusters
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
        response = pagers.ListAwsClustersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_aws_cluster(
        self,
        request: Optional[Union[aws_service.DeleteAwsClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a specific
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster] resource.

        Fails if the cluster has one or more associated
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
        resources.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_delete_aws_cluster():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.DeleteAwsClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_aws_cluster(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.DeleteAwsClusterRequest, dict]]):
                The request object. Request message for ``AwsClusters.DeleteAwsCluster``
                method.
            name (:class:`str`):
                Required. The resource name the
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                to delete.

                ``AwsCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
        warnings.warn(
            "AwsClustersAsyncClient.delete_aws_cluster is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, aws_service.DeleteAwsClusterRequest):
            request = aws_service.DeleteAwsClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_aws_cluster
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
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def generate_aws_cluster_agent_token(
        self,
        request: Optional[
            Union[aws_service.GenerateAwsClusterAgentTokenRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_service.GenerateAwsClusterAgentTokenResponse:
        r"""Generates an access token for a cluster agent.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_generate_aws_cluster_agent_token():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GenerateAwsClusterAgentTokenRequest(
                    aws_cluster="aws_cluster_value",
                    subject_token="subject_token_value",
                    subject_token_type="subject_token_type_value",
                    version="version_value",
                )

                # Make the request
                response = await client.generate_aws_cluster_agent_token(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GenerateAwsClusterAgentTokenRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gke_multicloud_v1.types.GenerateAwsClusterAgentTokenResponse:

        """
        warnings.warn(
            "AwsClustersAsyncClient.generate_aws_cluster_agent_token is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, aws_service.GenerateAwsClusterAgentTokenRequest):
            request = aws_service.GenerateAwsClusterAgentTokenRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_aws_cluster_agent_token
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("aws_cluster", request.aws_cluster),)
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

    async def generate_aws_access_token(
        self,
        request: Optional[
            Union[aws_service.GenerateAwsAccessTokenRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_service.GenerateAwsAccessTokenResponse:
        r"""Generates a short-lived access token to authenticate to a given
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster] resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_generate_aws_access_token():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GenerateAwsAccessTokenRequest(
                    aws_cluster="aws_cluster_value",
                )

                # Make the request
                response = await client.generate_aws_access_token(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GenerateAwsAccessTokenRequest, dict]]):
                The request object. Request message for
                ``AwsClusters.GenerateAwsAccessToken`` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gke_multicloud_v1.types.GenerateAwsAccessTokenResponse:
                Response message for AwsClusters.GenerateAwsAccessToken
                method.

        """
        warnings.warn(
            "AwsClustersAsyncClient.generate_aws_access_token is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, aws_service.GenerateAwsAccessTokenRequest):
            request = aws_service.GenerateAwsAccessTokenRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_aws_access_token
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("aws_cluster", request.aws_cluster),)
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

    async def create_aws_node_pool(
        self,
        request: Optional[Union[aws_service.CreateAwsNodePoolRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        aws_node_pool: Optional[aws_resources.AwsNodePool] = None,
        aws_node_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool],
        attached to a given
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster].

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_create_aws_node_pool():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                aws_node_pool = gke_multicloud_v1.AwsNodePool()
                aws_node_pool.version = "version_value"
                aws_node_pool.config.iam_instance_profile = "iam_instance_profile_value"
                aws_node_pool.config.config_encryption.kms_key_arn = "kms_key_arn_value"
                aws_node_pool.autoscaling.min_node_count = 1489
                aws_node_pool.autoscaling.max_node_count = 1491
                aws_node_pool.subnet_id = "subnet_id_value"
                aws_node_pool.max_pods_constraint.max_pods_per_node = 1798

                request = gke_multicloud_v1.CreateAwsNodePoolRequest(
                    parent="parent_value",
                    aws_node_pool=aws_node_pool,
                    aws_node_pool_id="aws_node_pool_id_value",
                )

                # Make the request
                operation = await client.create_aws_node_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.CreateAwsNodePoolRequest, dict]]):
                The request object. Response message for ``AwsClusters.CreateAwsNodePool``
                method.
            parent (:class:`str`):
                Required. The
                [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster]
                resource where this node pool will be created.

                ``AwsCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            aws_node_pool (:class:`google.cloud.gke_multicloud_v1.types.AwsNodePool`):
                Required. The specification of the
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                to create.

                This corresponds to the ``aws_node_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            aws_node_pool_id (:class:`str`):
                Required. A client provided ID the resource. Must be
                unique within the parent resource.

                The provided ID will be part of the
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                resource name formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>/awsNodePools/<node-pool-id>``.

                Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
                than 63 characters.

                This corresponds to the ``aws_node_pool_id`` field
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
                :class:`google.cloud.gke_multicloud_v1.types.AwsNodePool`
                An Anthos node pool running on AWS.

        """
        warnings.warn(
            "AwsClustersAsyncClient.create_aws_node_pool is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, aws_node_pool, aws_node_pool_id]
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
        if not isinstance(request, aws_service.CreateAwsNodePoolRequest):
            request = aws_service.CreateAwsNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if aws_node_pool is not None:
            request.aws_node_pool = aws_node_pool
        if aws_node_pool_id is not None:
            request.aws_node_pool_id = aws_node_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_aws_node_pool
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
            aws_resources.AwsNodePool,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_aws_node_pool(
        self,
        request: Optional[Union[aws_service.UpdateAwsNodePoolRequest, dict]] = None,
        *,
        aws_node_pool: Optional[aws_resources.AwsNodePool] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates an
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_update_aws_node_pool():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                aws_node_pool = gke_multicloud_v1.AwsNodePool()
                aws_node_pool.version = "version_value"
                aws_node_pool.config.iam_instance_profile = "iam_instance_profile_value"
                aws_node_pool.config.config_encryption.kms_key_arn = "kms_key_arn_value"
                aws_node_pool.autoscaling.min_node_count = 1489
                aws_node_pool.autoscaling.max_node_count = 1491
                aws_node_pool.subnet_id = "subnet_id_value"
                aws_node_pool.max_pods_constraint.max_pods_per_node = 1798

                request = gke_multicloud_v1.UpdateAwsNodePoolRequest(
                    aws_node_pool=aws_node_pool,
                )

                # Make the request
                operation = await client.update_aws_node_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.UpdateAwsNodePoolRequest, dict]]):
                The request object. Request message for ``AwsClusters.UpdateAwsNodePool``
                method.
            aws_node_pool (:class:`google.cloud.gke_multicloud_v1.types.AwsNodePool`):
                Required. The
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                resource to update.

                This corresponds to the ``aws_node_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. The elements of the
                repeated paths field can only include these fields from
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]:

                - ``annotations``.
                - ``version``.
                - ``autoscaling.min_node_count``.
                - ``autoscaling.max_node_count``.
                - ``config.config_encryption.kms_key_arn``.
                - ``config.security_group_ids``.
                - ``config.root_volume.iops``.
                - ``config.root_volume.throughput``.
                - ``config.root_volume.kms_key_arn``.
                - ``config.root_volume.volume_type``.
                - ``config.root_volume.size_gib``.
                - ``config.proxy_config``.
                - ``config.proxy_config.secret_arn``.
                - ``config.proxy_config.secret_version``.
                - ``config.ssh_config``.
                - ``config.ssh_config.ec2_key_pair``.
                - ``config.instance_placement.tenancy``.
                - ``config.iam_instance_profile``.
                - ``config.labels``.
                - ``config.tags``.
                - ``config.autoscaling_metrics_collection``.
                - ``config.autoscaling_metrics_collection.granularity``.
                - ``config.autoscaling_metrics_collection.metrics``.
                - ``config.instance_type``.
                - ``management.auto_repair``.
                - ``management``.
                - ``update_settings``.
                - ``update_settings.surge_settings``.
                - ``update_settings.surge_settings.max_surge``.
                - ``update_settings.surge_settings.max_unavailable``.

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
                :class:`google.cloud.gke_multicloud_v1.types.AwsNodePool`
                An Anthos node pool running on AWS.

        """
        warnings.warn(
            "AwsClustersAsyncClient.update_aws_node_pool is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [aws_node_pool, update_mask]
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
        if not isinstance(request, aws_service.UpdateAwsNodePoolRequest):
            request = aws_service.UpdateAwsNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if aws_node_pool is not None:
            request.aws_node_pool = aws_node_pool
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_aws_node_pool
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("aws_node_pool.name", request.aws_node_pool.name),)
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
            aws_resources.AwsNodePool,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def rollback_aws_node_pool_update(
        self,
        request: Optional[
            Union[aws_service.RollbackAwsNodePoolUpdateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Rolls back a previously aborted or failed
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool] update
        request. Makes no changes if the last update request
        successfully finished. If an update request is in progress, you
        cannot rollback the update. You must first cancel or let it
        finish unsuccessfully before you can rollback.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_rollback_aws_node_pool_update():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.RollbackAwsNodePoolUpdateRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.rollback_aws_node_pool_update(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.RollbackAwsNodePoolUpdateRequest, dict]]):
                The request object. Request message for
                ``AwsClusters.RollbackAwsNodePoolUpdate`` method.
            name (:class:`str`):
                Required. The name of the
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                resource to rollback.

                ``AwsNodePool`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>/awsNodePools/<node-pool-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
                :class:`google.cloud.gke_multicloud_v1.types.AwsNodePool`
                An Anthos node pool running on AWS.

        """
        warnings.warn(
            "AwsClustersAsyncClient.rollback_aws_node_pool_update is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, aws_service.RollbackAwsNodePoolUpdateRequest):
            request = aws_service.RollbackAwsNodePoolUpdateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.rollback_aws_node_pool_update
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
            aws_resources.AwsNodePool,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_aws_node_pool(
        self,
        request: Optional[Union[aws_service.GetAwsNodePoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_resources.AwsNodePool:
        r"""Describes a specific
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_aws_node_pool():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAwsNodePoolRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_aws_node_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAwsNodePoolRequest, dict]]):
                The request object. Request message for ``AwsClusters.GetAwsNodePool``
                method.
            name (:class:`str`):
                Required. The name of the
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                resource to describe.

                ``AwsNodePool`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>/awsNodePools/<node-pool-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.types.AwsNodePool:
                An Anthos node pool running on AWS.
        """
        warnings.warn(
            "AwsClustersAsyncClient.get_aws_node_pool is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, aws_service.GetAwsNodePoolRequest):
            request = aws_service.GetAwsNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_aws_node_pool
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

    async def list_aws_node_pools(
        self,
        request: Optional[Union[aws_service.ListAwsNodePoolsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAwsNodePoolsAsyncPager:
        r"""Lists all
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
        resources on a given
        [AwsCluster][google.cloud.gkemulticloud.v1.AwsCluster].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_list_aws_node_pools():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.ListAwsNodePoolsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_aws_node_pools(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsRequest, dict]]):
                The request object. Request message for ``AwsClusters.ListAwsNodePools``
                method.
            parent (:class:`str`):
                Required. The parent ``AwsCluster`` which owns this
                collection of
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                resources.

                ``AwsCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.services.aws_clusters.pagers.ListAwsNodePoolsAsyncPager:
                Response message for AwsClusters.ListAwsNodePools
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "AwsClustersAsyncClient.list_aws_node_pools is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, aws_service.ListAwsNodePoolsRequest):
            request = aws_service.ListAwsNodePoolsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_aws_node_pools
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
        response = pagers.ListAwsNodePoolsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_aws_node_pool(
        self,
        request: Optional[Union[aws_service.DeleteAwsNodePoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a specific
        [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
        resource.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_delete_aws_node_pool():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.DeleteAwsNodePoolRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_aws_node_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.DeleteAwsNodePoolRequest, dict]]):
                The request object. Request message for ``AwsClusters.DeleteAwsNodePool``
                method.
            name (:class:`str`):
                Required. The resource name the
                [AwsNodePool][google.cloud.gkemulticloud.v1.AwsNodePool]
                to delete.

                ``AwsNodePool`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsClusters/<cluster-id>/awsNodePools/<node-pool-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
        warnings.warn(
            "AwsClustersAsyncClient.delete_aws_node_pool is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, aws_service.DeleteAwsNodePoolRequest):
            request = aws_service.DeleteAwsNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_aws_node_pool
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
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_aws_open_id_config(
        self,
        request: Optional[Union[aws_service.GetAwsOpenIdConfigRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_resources.AwsOpenIdConfig:
        r"""Gets the OIDC discovery document for the cluster. See the
        `OpenID Connect Discovery 1.0
        specification <https://openid.net/specs/openid-connect-discovery-1_0.html>`__
        for details.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_aws_open_id_config():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAwsOpenIdConfigRequest(
                    aws_cluster="aws_cluster_value",
                )

                # Make the request
                response = await client.get_aws_open_id_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAwsOpenIdConfigRequest, dict]]):
                The request object. GetAwsOpenIdConfigRequest gets the
                OIDC discovery document for the cluster.
                See the OpenID Connect Discovery 1.0
                specification for details.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gke_multicloud_v1.types.AwsOpenIdConfig:
                AwsOpenIdConfig is an OIDC discovery
                document for the cluster. See the OpenID
                Connect Discovery 1.0 specification for
                details.

        """
        warnings.warn(
            "AwsClustersAsyncClient.get_aws_open_id_config is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, aws_service.GetAwsOpenIdConfigRequest):
            request = aws_service.GetAwsOpenIdConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_aws_open_id_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("aws_cluster", request.aws_cluster),)
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

    async def get_aws_json_web_keys(
        self,
        request: Optional[Union[aws_service.GetAwsJsonWebKeysRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_resources.AwsJsonWebKeys:
        r"""Gets the public component of the cluster signing keys
        in JSON Web Key format.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_aws_json_web_keys():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAwsJsonWebKeysRequest(
                    aws_cluster="aws_cluster_value",
                )

                # Make the request
                response = await client.get_aws_json_web_keys(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAwsJsonWebKeysRequest, dict]]):
                The request object. GetAwsJsonWebKeysRequest gets the public component of
                the keys used by the cluster to sign token requests.
                This will be the jwks_uri for the discover document
                returned by getOpenIDConfig. See the OpenID Connect
                Discovery 1.0 specification for details.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gke_multicloud_v1.types.AwsJsonWebKeys:
                AwsJsonWebKeys is a valid JSON Web
                Key Set as specififed in RFC 7517.

        """
        warnings.warn(
            "AwsClustersAsyncClient.get_aws_json_web_keys is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, aws_service.GetAwsJsonWebKeysRequest):
            request = aws_service.GetAwsJsonWebKeysRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_aws_json_web_keys
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("aws_cluster", request.aws_cluster),)
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

    async def get_aws_server_config(
        self,
        request: Optional[Union[aws_service.GetAwsServerConfigRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> aws_resources.AwsServerConfig:
        r"""Returns information, such as supported AWS regions
        and Kubernetes versions, on a given Google Cloud
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_aws_server_config():
                # Create a client
                client = gke_multicloud_v1.AwsClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAwsServerConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_aws_server_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAwsServerConfigRequest, dict]]):
                The request object. GetAwsServerConfigRequest gets the
                server config of GKE cluster on AWS.
            name (:class:`str`):
                Required. The name of the
                [AwsServerConfig][google.cloud.gkemulticloud.v1.AwsServerConfig]
                resource to describe.

                ``AwsServerConfig`` names are formatted as
                ``projects/<project-id>/locations/<region>/awsServerConfig``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.types.AwsServerConfig:
                AwsServerConfig is the configuration
                of GKE cluster on AWS.

        """
        warnings.warn(
            "AwsClustersAsyncClient.get_aws_server_config is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, aws_service.GetAwsServerConfigRequest):
            request = aws_service.GetAwsServerConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_aws_server_config
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

    async def __aenter__(self) -> "AwsClustersAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AwsClustersAsyncClient",)
