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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.container_v1beta1 import gapic_version as package_version
from google.cloud.container_v1beta1.types import cluster_service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ClusterManagerTransport(abc.ABC):
    """Abstract transport class for ClusterManager."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/container",
        "https://www.googleapis.com/auth/container.read-only",
    )

    DEFAULT_HOST: str = "container.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'container.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_clusters: gapic_v1.method.wrap_method(
                self.list_clusters,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.get_cluster: gapic_v1.method.wrap_method(
                self.get_cluster,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.create_cluster: gapic_v1.method.wrap_method(
                self.create_cluster,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.update_cluster: gapic_v1.method.wrap_method(
                self.update_cluster,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.update_node_pool: gapic_v1.method.wrap_method(
                self.update_node_pool,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_node_pool_autoscaling: gapic_v1.method.wrap_method(
                self.set_node_pool_autoscaling,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_logging_service: gapic_v1.method.wrap_method(
                self.set_logging_service,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_monitoring_service: gapic_v1.method.wrap_method(
                self.set_monitoring_service,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_addons_config: gapic_v1.method.wrap_method(
                self.set_addons_config,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_locations: gapic_v1.method.wrap_method(
                self.set_locations,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.update_master: gapic_v1.method.wrap_method(
                self.update_master,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_master_auth: gapic_v1.method.wrap_method(
                self.set_master_auth,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.delete_cluster: gapic_v1.method.wrap_method(
                self.delete_cluster,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.get_server_config: gapic_v1.method.wrap_method(
                self.get_server_config,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.get_json_web_keys: gapic_v1.method.wrap_method(
                self.get_json_web_keys,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_node_pools: gapic_v1.method.wrap_method(
                self.list_node_pools,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.get_node_pool: gapic_v1.method.wrap_method(
                self.get_node_pool,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.create_node_pool: gapic_v1.method.wrap_method(
                self.create_node_pool,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.delete_node_pool: gapic_v1.method.wrap_method(
                self.delete_node_pool,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.complete_node_pool_upgrade: gapic_v1.method.wrap_method(
                self.complete_node_pool_upgrade,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rollback_node_pool_upgrade: gapic_v1.method.wrap_method(
                self.rollback_node_pool_upgrade,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_node_pool_management: gapic_v1.method.wrap_method(
                self.set_node_pool_management,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_labels: gapic_v1.method.wrap_method(
                self.set_labels,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_legacy_abac: gapic_v1.method.wrap_method(
                self.set_legacy_abac,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.start_ip_rotation: gapic_v1.method.wrap_method(
                self.start_ip_rotation,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.complete_ip_rotation: gapic_v1.method.wrap_method(
                self.complete_ip_rotation,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_node_pool_size: gapic_v1.method.wrap_method(
                self.set_node_pool_size,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_network_policy: gapic_v1.method.wrap_method(
                self.set_network_policy,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.set_maintenance_policy: gapic_v1.method.wrap_method(
                self.set_maintenance_policy,
                default_timeout=45.0,
                client_info=client_info,
            ),
            self.list_usable_subnetworks: gapic_v1.method.wrap_method(
                self.list_usable_subnetworks,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.check_autopilot_compatibility: gapic_v1.method.wrap_method(
                self.check_autopilot_compatibility,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.fetch_cluster_upgrade_info: gapic_v1.method.wrap_method(
                self.fetch_cluster_upgrade_info,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_node_pool_upgrade_info: gapic_v1.method.wrap_method(
                self.fetch_node_pool_upgrade_info,
                default_timeout=None,
                client_info=client_info,
            ),
            self.complete_control_plane_upgrade: gapic_v1.method.wrap_method(
                self.complete_control_plane_upgrade,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [cluster_service.ListClustersRequest],
        Union[
            cluster_service.ListClustersResponse,
            Awaitable[cluster_service.ListClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [cluster_service.GetClusterRequest],
        Union[cluster_service.Cluster, Awaitable[cluster_service.Cluster]],
    ]:
        raise NotImplementedError()

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [cluster_service.CreateClusterRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [cluster_service.UpdateClusterRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_node_pool(
        self,
    ) -> Callable[
        [cluster_service.UpdateNodePoolRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_node_pool_autoscaling(
        self,
    ) -> Callable[
        [cluster_service.SetNodePoolAutoscalingRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_logging_service(
        self,
    ) -> Callable[
        [cluster_service.SetLoggingServiceRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_monitoring_service(
        self,
    ) -> Callable[
        [cluster_service.SetMonitoringServiceRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_addons_config(
        self,
    ) -> Callable[
        [cluster_service.SetAddonsConfigRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_locations(
        self,
    ) -> Callable[
        [cluster_service.SetLocationsRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_master(
        self,
    ) -> Callable[
        [cluster_service.UpdateMasterRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_master_auth(
        self,
    ) -> Callable[
        [cluster_service.SetMasterAuthRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [cluster_service.DeleteClusterRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [cluster_service.ListOperationsRequest],
        Union[
            cluster_service.ListOperationsResponse,
            Awaitable[cluster_service.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [cluster_service.GetOperationRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [cluster_service.CancelOperationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_server_config(
        self,
    ) -> Callable[
        [cluster_service.GetServerConfigRequest],
        Union[cluster_service.ServerConfig, Awaitable[cluster_service.ServerConfig]],
    ]:
        raise NotImplementedError()

    @property
    def get_json_web_keys(
        self,
    ) -> Callable[
        [cluster_service.GetJSONWebKeysRequest],
        Union[
            cluster_service.GetJSONWebKeysResponse,
            Awaitable[cluster_service.GetJSONWebKeysResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_node_pools(
        self,
    ) -> Callable[
        [cluster_service.ListNodePoolsRequest],
        Union[
            cluster_service.ListNodePoolsResponse,
            Awaitable[cluster_service.ListNodePoolsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_node_pool(
        self,
    ) -> Callable[
        [cluster_service.GetNodePoolRequest],
        Union[cluster_service.NodePool, Awaitable[cluster_service.NodePool]],
    ]:
        raise NotImplementedError()

    @property
    def create_node_pool(
        self,
    ) -> Callable[
        [cluster_service.CreateNodePoolRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_node_pool(
        self,
    ) -> Callable[
        [cluster_service.DeleteNodePoolRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def complete_node_pool_upgrade(
        self,
    ) -> Callable[
        [cluster_service.CompleteNodePoolUpgradeRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def rollback_node_pool_upgrade(
        self,
    ) -> Callable[
        [cluster_service.RollbackNodePoolUpgradeRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_node_pool_management(
        self,
    ) -> Callable[
        [cluster_service.SetNodePoolManagementRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_labels(
        self,
    ) -> Callable[
        [cluster_service.SetLabelsRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_legacy_abac(
        self,
    ) -> Callable[
        [cluster_service.SetLegacyAbacRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_ip_rotation(
        self,
    ) -> Callable[
        [cluster_service.StartIPRotationRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def complete_ip_rotation(
        self,
    ) -> Callable[
        [cluster_service.CompleteIPRotationRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_node_pool_size(
        self,
    ) -> Callable[
        [cluster_service.SetNodePoolSizeRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_network_policy(
        self,
    ) -> Callable[
        [cluster_service.SetNetworkPolicyRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_maintenance_policy(
        self,
    ) -> Callable[
        [cluster_service.SetMaintenancePolicyRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_usable_subnetworks(
        self,
    ) -> Callable[
        [cluster_service.ListUsableSubnetworksRequest],
        Union[
            cluster_service.ListUsableSubnetworksResponse,
            Awaitable[cluster_service.ListUsableSubnetworksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def check_autopilot_compatibility(
        self,
    ) -> Callable[
        [cluster_service.CheckAutopilotCompatibilityRequest],
        Union[
            cluster_service.CheckAutopilotCompatibilityResponse,
            Awaitable[cluster_service.CheckAutopilotCompatibilityResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [cluster_service.ListLocationsRequest],
        Union[
            cluster_service.ListLocationsResponse,
            Awaitable[cluster_service.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_cluster_upgrade_info(
        self,
    ) -> Callable[
        [cluster_service.FetchClusterUpgradeInfoRequest],
        Union[
            cluster_service.ClusterUpgradeInfo,
            Awaitable[cluster_service.ClusterUpgradeInfo],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_node_pool_upgrade_info(
        self,
    ) -> Callable[
        [cluster_service.FetchNodePoolUpgradeInfoRequest],
        Union[
            cluster_service.NodePoolUpgradeInfo,
            Awaitable[cluster_service.NodePoolUpgradeInfo],
        ],
    ]:
        raise NotImplementedError()

    @property
    def complete_control_plane_upgrade(
        self,
    ) -> Callable[
        [cluster_service.CompleteControlPlaneUpgradeRequest],
        Union[cluster_service.Operation, Awaitable[cluster_service.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ClusterManagerTransport",)
