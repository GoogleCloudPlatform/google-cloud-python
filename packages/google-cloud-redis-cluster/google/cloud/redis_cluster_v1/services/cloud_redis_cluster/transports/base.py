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
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.redis_cluster_v1 import gapic_version as package_version
from google.cloud.redis_cluster_v1.types import cloud_redis_cluster

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class CloudRedisClusterTransport(abc.ABC):
    """Abstract transport class for CloudRedisCluster."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "redis.googleapis.com"

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
                 The hostname to connect to (default: 'redis.googleapis.com').
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
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_acl_policies: gapic_v1.method.wrap_method(
                self.list_acl_policies,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_cluster: gapic_v1.method.wrap_method(
                self.get_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_acl_policy: gapic_v1.method.wrap_method(
                self.get_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_cluster: gapic_v1.method.wrap_method(
                self.update_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_acl_policy: gapic_v1.method.wrap_method(
                self.update_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_cluster: gapic_v1.method.wrap_method(
                self.delete_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_acl_policy: gapic_v1.method.wrap_method(
                self.delete_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_acl_policy_revision: gapic_v1.method.wrap_method(
                self.get_acl_policy_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_acl_policy_revisions: gapic_v1.method.wrap_method(
                self.list_acl_policy_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_cluster: gapic_v1.method.wrap_method(
                self.create_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.create_acl_policy: gapic_v1.method.wrap_method(
                self.create_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_cluster_certificate_authority: gapic_v1.method.wrap_method(
                self.get_cluster_certificate_authority,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_shared_regional_certificate_authority: gapic_v1.method.wrap_method(
                self.get_shared_regional_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reschedule_cluster_maintenance: gapic_v1.method.wrap_method(
                self.reschedule_cluster_maintenance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_backup_collections: gapic_v1.method.wrap_method(
                self.list_backup_collections,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_backup_collection: gapic_v1.method.wrap_method(
                self.get_backup_collection,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_backups: gapic_v1.method.wrap_method(
                self.list_backups,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_backup: gapic_v1.method.wrap_method(
                self.get_backup,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_backup: gapic_v1.method.wrap_method(
                self.delete_backup,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.export_backup: gapic_v1.method.wrap_method(
                self.export_backup,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.backup_cluster: gapic_v1.method.wrap_method(
                self.backup_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_token_auth_users: gapic_v1.method.wrap_method(
                self.list_token_auth_users,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_token_auth_user: gapic_v1.method.wrap_method(
                self.get_token_auth_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_auth_tokens: gapic_v1.method.wrap_method(
                self.list_auth_tokens,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_auth_token: gapic_v1.method.wrap_method(
                self.get_auth_token,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_token_auth_user: gapic_v1.method.wrap_method(
                self.add_token_auth_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_token_auth_user: gapic_v1.method.wrap_method(
                self.delete_token_auth_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_auth_token: gapic_v1.method.wrap_method(
                self.add_auth_token,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_auth_token: gapic_v1.method.wrap_method(
                self.delete_auth_token,
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
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
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
    def list_clusters(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListClustersRequest],
        Union[
            cloud_redis_cluster.ListClustersResponse,
            Awaitable[cloud_redis_cluster.ListClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_acl_policies(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListAclPoliciesRequest],
        Union[
            cloud_redis_cluster.ListAclPoliciesResponse,
            Awaitable[cloud_redis_cluster.ListAclPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetClusterRequest],
        Union[cloud_redis_cluster.Cluster, Awaitable[cloud_redis_cluster.Cluster]],
    ]:
        raise NotImplementedError()

    @property
    def get_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetAclPolicyRequest],
        Union[cloud_redis_cluster.AclPolicy, Awaitable[cloud_redis_cluster.AclPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.UpdateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.UpdateAclPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteAclPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_acl_policy_revision(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetAclPolicyRevisionRequest],
        Union[
            cloud_redis_cluster.AclPolicyRevision,
            Awaitable[cloud_redis_cluster.AclPolicyRevision],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_acl_policy_revisions(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListAclPolicyRevisionsRequest],
        Union[
            cloud_redis_cluster.ListAclPolicyRevisionsResponse,
            Awaitable[cloud_redis_cluster.ListAclPolicyRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.CreateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.CreateAclPolicyRequest],
        Union[cloud_redis_cluster.AclPolicy, Awaitable[cloud_redis_cluster.AclPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster_certificate_authority(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetClusterCertificateAuthorityRequest],
        Union[
            cloud_redis_cluster.CertificateAuthority,
            Awaitable[cloud_redis_cluster.CertificateAuthority],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_shared_regional_certificate_authority(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest],
        Union[
            cloud_redis_cluster.SharedRegionalCertificateAuthority,
            Awaitable[cloud_redis_cluster.SharedRegionalCertificateAuthority],
        ],
    ]:
        raise NotImplementedError()

    @property
    def reschedule_cluster_maintenance(
        self,
    ) -> Callable[
        [cloud_redis_cluster.RescheduleClusterMaintenanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_collections(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListBackupCollectionsRequest],
        Union[
            cloud_redis_cluster.ListBackupCollectionsResponse,
            Awaitable[cloud_redis_cluster.ListBackupCollectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_collection(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetBackupCollectionRequest],
        Union[
            cloud_redis_cluster.BackupCollection,
            Awaitable[cloud_redis_cluster.BackupCollection],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListBackupsRequest],
        Union[
            cloud_redis_cluster.ListBackupsResponse,
            Awaitable[cloud_redis_cluster.ListBackupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetBackupRequest],
        Union[cloud_redis_cluster.Backup, Awaitable[cloud_redis_cluster.Backup]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_backup(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ExportBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def backup_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.BackupClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_token_auth_users(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListTokenAuthUsersRequest],
        Union[
            cloud_redis_cluster.ListTokenAuthUsersResponse,
            Awaitable[cloud_redis_cluster.ListTokenAuthUsersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_token_auth_user(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetTokenAuthUserRequest],
        Union[
            cloud_redis_cluster.TokenAuthUser,
            Awaitable[cloud_redis_cluster.TokenAuthUser],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_auth_tokens(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListAuthTokensRequest],
        Union[
            cloud_redis_cluster.ListAuthTokensResponse,
            Awaitable[cloud_redis_cluster.ListAuthTokensResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_auth_token(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetAuthTokenRequest],
        Union[cloud_redis_cluster.AuthToken, Awaitable[cloud_redis_cluster.AuthToken]],
    ]:
        raise NotImplementedError()

    @property
    def add_token_auth_user(
        self,
    ) -> Callable[
        [cloud_redis_cluster.AddTokenAuthUserRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_token_auth_user(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteTokenAuthUserRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_auth_token(
        self,
    ) -> Callable[
        [cloud_redis_cluster.AddAuthTokenRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_auth_token(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteAuthTokenRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
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


__all__ = ("CloudRedisClusterTransport",)
