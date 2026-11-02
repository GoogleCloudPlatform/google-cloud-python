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
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.bare_metal_solution_v2 import gapic_version as package_version
from google.cloud.bare_metal_solution_v2.types import (
    instance,
    lun,
    network,
    nfs_share,
    osimage,
    provisioning,
    ssh_key,
    volume,
    volume_snapshot,
)
from google.cloud.bare_metal_solution_v2.types import instance as gcb_instance
from google.cloud.bare_metal_solution_v2.types import network as gcb_network
from google.cloud.bare_metal_solution_v2.types import nfs_share as gcb_nfs_share
from google.cloud.bare_metal_solution_v2.types import ssh_key as gcb_ssh_key
from google.cloud.bare_metal_solution_v2.types import volume as gcb_volume
from google.cloud.bare_metal_solution_v2.types import (
    volume_snapshot as gcb_volume_snapshot,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class BareMetalSolutionTransport(abc.ABC):
    """Abstract transport class for BareMetalSolution."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "baremetalsolution.googleapis.com"

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
                 The hostname to connect to (default: 'baremetalsolution.googleapis.com').
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
            self.list_instances: gapic_v1.method.wrap_method(
                self.list_instances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_instance: gapic_v1.method.wrap_method(
                self.get_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_instance: gapic_v1.method.wrap_method(
                self.update_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_instance: gapic_v1.method.wrap_method(
                self.rename_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_instance: gapic_v1.method.wrap_method(
                self.reset_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_instance: gapic_v1.method.wrap_method(
                self.start_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_instance: gapic_v1.method.wrap_method(
                self.stop_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_interactive_serial_console: gapic_v1.method.wrap_method(
                self.enable_interactive_serial_console,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_interactive_serial_console: gapic_v1.method.wrap_method(
                self.disable_interactive_serial_console,
                default_timeout=None,
                client_info=client_info,
            ),
            self.detach_lun: gapic_v1.method.wrap_method(
                self.detach_lun,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_ssh_keys: gapic_v1.method.wrap_method(
                self.list_ssh_keys,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ssh_key: gapic_v1.method.wrap_method(
                self.create_ssh_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_ssh_key: gapic_v1.method.wrap_method(
                self.delete_ssh_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_volumes: gapic_v1.method.wrap_method(
                self.list_volumes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_volume: gapic_v1.method.wrap_method(
                self.get_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_volume: gapic_v1.method.wrap_method(
                self.update_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_volume: gapic_v1.method.wrap_method(
                self.rename_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.evict_volume: gapic_v1.method.wrap_method(
                self.evict_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.resize_volume: gapic_v1.method.wrap_method(
                self.resize_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_networks: gapic_v1.method.wrap_method(
                self.list_networks,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_network_usage: gapic_v1.method.wrap_method(
                self.list_network_usage,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_network: gapic_v1.method.wrap_method(
                self.get_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_network: gapic_v1.method.wrap_method(
                self.update_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_volume_snapshot: gapic_v1.method.wrap_method(
                self.create_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_volume_snapshot: gapic_v1.method.wrap_method(
                self.restore_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_volume_snapshot: gapic_v1.method.wrap_method(
                self.delete_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_volume_snapshot: gapic_v1.method.wrap_method(
                self.get_volume_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_volume_snapshots: gapic_v1.method.wrap_method(
                self.list_volume_snapshots,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lun: gapic_v1.method.wrap_method(
                self.get_lun,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_luns: gapic_v1.method.wrap_method(
                self.list_luns,
                default_timeout=None,
                client_info=client_info,
            ),
            self.evict_lun: gapic_v1.method.wrap_method(
                self.evict_lun,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_nfs_share: gapic_v1.method.wrap_method(
                self.get_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_nfs_shares: gapic_v1.method.wrap_method(
                self.list_nfs_shares,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_nfs_share: gapic_v1.method.wrap_method(
                self.update_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_nfs_share: gapic_v1.method.wrap_method(
                self.create_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_nfs_share: gapic_v1.method.wrap_method(
                self.rename_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_nfs_share: gapic_v1.method.wrap_method(
                self.delete_nfs_share,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_provisioning_quotas: gapic_v1.method.wrap_method(
                self.list_provisioning_quotas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.submit_provisioning_config: gapic_v1.method.wrap_method(
                self.submit_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_provisioning_config: gapic_v1.method.wrap_method(
                self.get_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_provisioning_config: gapic_v1.method.wrap_method(
                self.create_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_provisioning_config: gapic_v1.method.wrap_method(
                self.update_provisioning_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_network: gapic_v1.method.wrap_method(
                self.rename_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_os_images: gapic_v1.method.wrap_method(
                self.list_os_images,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
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
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_instances(
        self,
    ) -> Callable[
        [instance.ListInstancesRequest],
        Union[
            instance.ListInstancesResponse, Awaitable[instance.ListInstancesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_instance(
        self,
    ) -> Callable[
        [instance.GetInstanceRequest],
        Union[instance.Instance, Awaitable[instance.Instance]],
    ]:
        raise NotImplementedError()

    @property
    def update_instance(
        self,
    ) -> Callable[
        [gcb_instance.UpdateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rename_instance(
        self,
    ) -> Callable[
        [instance.RenameInstanceRequest],
        Union[instance.Instance, Awaitable[instance.Instance]],
    ]:
        raise NotImplementedError()

    @property
    def reset_instance(
        self,
    ) -> Callable[
        [instance.ResetInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_instance(
        self,
    ) -> Callable[
        [instance.StartInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_instance(
        self,
    ) -> Callable[
        [instance.StopInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def enable_interactive_serial_console(
        self,
    ) -> Callable[
        [instance.EnableInteractiveSerialConsoleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def disable_interactive_serial_console(
        self,
    ) -> Callable[
        [instance.DisableInteractiveSerialConsoleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def detach_lun(
        self,
    ) -> Callable[
        [gcb_instance.DetachLunRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_ssh_keys(
        self,
    ) -> Callable[
        [ssh_key.ListSSHKeysRequest],
        Union[ssh_key.ListSSHKeysResponse, Awaitable[ssh_key.ListSSHKeysResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_ssh_key(
        self,
    ) -> Callable[
        [gcb_ssh_key.CreateSSHKeyRequest],
        Union[gcb_ssh_key.SSHKey, Awaitable[gcb_ssh_key.SSHKey]],
    ]:
        raise NotImplementedError()

    @property
    def delete_ssh_key(
        self,
    ) -> Callable[
        [ssh_key.DeleteSSHKeyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_volumes(
        self,
    ) -> Callable[
        [volume.ListVolumesRequest],
        Union[volume.ListVolumesResponse, Awaitable[volume.ListVolumesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_volume(
        self,
    ) -> Callable[
        [volume.GetVolumeRequest], Union[volume.Volume, Awaitable[volume.Volume]]
    ]:
        raise NotImplementedError()

    @property
    def update_volume(
        self,
    ) -> Callable[
        [gcb_volume.UpdateVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rename_volume(
        self,
    ) -> Callable[
        [volume.RenameVolumeRequest], Union[volume.Volume, Awaitable[volume.Volume]]
    ]:
        raise NotImplementedError()

    @property
    def evict_volume(
        self,
    ) -> Callable[
        [volume.EvictVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def resize_volume(
        self,
    ) -> Callable[
        [gcb_volume.ResizeVolumeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_networks(
        self,
    ) -> Callable[
        [network.ListNetworksRequest],
        Union[network.ListNetworksResponse, Awaitable[network.ListNetworksResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_network_usage(
        self,
    ) -> Callable[
        [network.ListNetworkUsageRequest],
        Union[
            network.ListNetworkUsageResponse,
            Awaitable[network.ListNetworkUsageResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_network(
        self,
    ) -> Callable[
        [network.GetNetworkRequest], Union[network.Network, Awaitable[network.Network]]
    ]:
        raise NotImplementedError()

    @property
    def update_network(
        self,
    ) -> Callable[
        [gcb_network.UpdateNetworkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_volume_snapshot(
        self,
    ) -> Callable[
        [gcb_volume_snapshot.CreateVolumeSnapshotRequest],
        Union[
            gcb_volume_snapshot.VolumeSnapshot,
            Awaitable[gcb_volume_snapshot.VolumeSnapshot],
        ],
    ]:
        raise NotImplementedError()

    @property
    def restore_volume_snapshot(
        self,
    ) -> Callable[
        [gcb_volume_snapshot.RestoreVolumeSnapshotRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_volume_snapshot(
        self,
    ) -> Callable[
        [volume_snapshot.DeleteVolumeSnapshotRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_volume_snapshot(
        self,
    ) -> Callable[
        [volume_snapshot.GetVolumeSnapshotRequest],
        Union[
            volume_snapshot.VolumeSnapshot, Awaitable[volume_snapshot.VolumeSnapshot]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_volume_snapshots(
        self,
    ) -> Callable[
        [volume_snapshot.ListVolumeSnapshotsRequest],
        Union[
            volume_snapshot.ListVolumeSnapshotsResponse,
            Awaitable[volume_snapshot.ListVolumeSnapshotsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_lun(
        self,
    ) -> Callable[[lun.GetLunRequest], Union[lun.Lun, Awaitable[lun.Lun]]]:
        raise NotImplementedError()

    @property
    def list_luns(
        self,
    ) -> Callable[
        [lun.ListLunsRequest],
        Union[lun.ListLunsResponse, Awaitable[lun.ListLunsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def evict_lun(
        self,
    ) -> Callable[
        [lun.EvictLunRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_nfs_share(
        self,
    ) -> Callable[
        [nfs_share.GetNfsShareRequest],
        Union[nfs_share.NfsShare, Awaitable[nfs_share.NfsShare]],
    ]:
        raise NotImplementedError()

    @property
    def list_nfs_shares(
        self,
    ) -> Callable[
        [nfs_share.ListNfsSharesRequest],
        Union[
            nfs_share.ListNfsSharesResponse, Awaitable[nfs_share.ListNfsSharesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_nfs_share(
        self,
    ) -> Callable[
        [gcb_nfs_share.UpdateNfsShareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_nfs_share(
        self,
    ) -> Callable[
        [gcb_nfs_share.CreateNfsShareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rename_nfs_share(
        self,
    ) -> Callable[
        [nfs_share.RenameNfsShareRequest],
        Union[nfs_share.NfsShare, Awaitable[nfs_share.NfsShare]],
    ]:
        raise NotImplementedError()

    @property
    def delete_nfs_share(
        self,
    ) -> Callable[
        [nfs_share.DeleteNfsShareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_provisioning_quotas(
        self,
    ) -> Callable[
        [provisioning.ListProvisioningQuotasRequest],
        Union[
            provisioning.ListProvisioningQuotasResponse,
            Awaitable[provisioning.ListProvisioningQuotasResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def submit_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.SubmitProvisioningConfigRequest],
        Union[
            provisioning.SubmitProvisioningConfigResponse,
            Awaitable[provisioning.SubmitProvisioningConfigResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.GetProvisioningConfigRequest],
        Union[
            provisioning.ProvisioningConfig, Awaitable[provisioning.ProvisioningConfig]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.CreateProvisioningConfigRequest],
        Union[
            provisioning.ProvisioningConfig, Awaitable[provisioning.ProvisioningConfig]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_provisioning_config(
        self,
    ) -> Callable[
        [provisioning.UpdateProvisioningConfigRequest],
        Union[
            provisioning.ProvisioningConfig, Awaitable[provisioning.ProvisioningConfig]
        ],
    ]:
        raise NotImplementedError()

    @property
    def rename_network(
        self,
    ) -> Callable[
        [network.RenameNetworkRequest],
        Union[network.Network, Awaitable[network.Network]],
    ]:
        raise NotImplementedError()

    @property
    def list_os_images(
        self,
    ) -> Callable[
        [osimage.ListOSImagesRequest],
        Union[osimage.ListOSImagesResponse, Awaitable[osimage.ListOSImagesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("BareMetalSolutionTransport",)
