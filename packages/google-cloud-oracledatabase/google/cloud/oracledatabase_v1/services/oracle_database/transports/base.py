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

from google.cloud.oracledatabase_v1 import gapic_version as package_version
from google.cloud.oracledatabase_v1.types import (
    autonomous_database,
    database,
    database_character_set,
    db_system,
    db_system_initial_storage_size,
    db_version,
    exadata_infra,
    exadb_vm_cluster,
    exascale_db_storage_vault,
    goldengate_connection,
    goldengate_connection_assignment,
    goldengate_connection_type,
    goldengate_deployment,
    goldengate_deployment_environment,
    goldengate_deployment_type,
    goldengate_deployment_version,
    minor_version,
    odb_dns_zone,
    odb_network,
    odb_subnet,
    oracledatabase,
    pluggable_database,
    vm_cluster,
)
from google.cloud.oracledatabase_v1.types import db_system as gco_db_system
from google.cloud.oracledatabase_v1.types import (
    exascale_db_storage_vault as gco_exascale_db_storage_vault,
)
from google.cloud.oracledatabase_v1.types import (
    goldengate_connection as gco_goldengate_connection,
)
from google.cloud.oracledatabase_v1.types import (
    goldengate_connection_assignment as gco_goldengate_connection_assignment,
)
from google.cloud.oracledatabase_v1.types import (
    goldengate_deployment as gco_goldengate_deployment,
)
from google.cloud.oracledatabase_v1.types import odb_dns_zone as gco_odb_dns_zone
from google.cloud.oracledatabase_v1.types import odb_network as gco_odb_network
from google.cloud.oracledatabase_v1.types import odb_subnet as gco_odb_subnet

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class OracleDatabaseTransport(abc.ABC):
    """Abstract transport class for OracleDatabase."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "oracledatabase.googleapis.com"

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
                 The hostname to connect to (default: 'oracledatabase.googleapis.com').
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
            self.list_cloud_exadata_infrastructures: gapic_v1.method.wrap_method(
                self.list_cloud_exadata_infrastructures,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_cloud_exadata_infrastructure: gapic_v1.method.wrap_method(
                self.get_cloud_exadata_infrastructure,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_cloud_exadata_infrastructure: gapic_v1.method.wrap_method(
                self.create_cloud_exadata_infrastructure,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_cloud_exadata_infrastructure: gapic_v1.method.wrap_method(
                self.delete_cloud_exadata_infrastructure,
                default_timeout=None,
                client_info=client_info,
            ),
            self.configure_exascale_cloud_exadata_infrastructure: gapic_v1.method.wrap_method(
                self.configure_exascale_cloud_exadata_infrastructure,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_cloud_vm_clusters: gapic_v1.method.wrap_method(
                self.list_cloud_vm_clusters,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_cloud_vm_cluster: gapic_v1.method.wrap_method(
                self.get_cloud_vm_cluster,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_cloud_vm_cluster: gapic_v1.method.wrap_method(
                self.create_cloud_vm_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_cloud_vm_cluster: gapic_v1.method.wrap_method(
                self.delete_cloud_vm_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entitlements: gapic_v1.method.wrap_method(
                self.list_entitlements,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_db_servers: gapic_v1.method.wrap_method(
                self.list_db_servers,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_db_nodes: gapic_v1.method.wrap_method(
                self.list_db_nodes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_gi_versions: gapic_v1.method.wrap_method(
                self.list_gi_versions,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_minor_versions: gapic_v1.method.wrap_method(
                self.list_minor_versions,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_db_system_shapes: gapic_v1.method.wrap_method(
                self.list_db_system_shapes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_autonomous_databases: gapic_v1.method.wrap_method(
                self.list_autonomous_databases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_autonomous_database: gapic_v1.method.wrap_method(
                self.get_autonomous_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_autonomous_database: gapic_v1.method.wrap_method(
                self.create_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_autonomous_database: gapic_v1.method.wrap_method(
                self.update_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_autonomous_database: gapic_v1.method.wrap_method(
                self.delete_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_autonomous_database: gapic_v1.method.wrap_method(
                self.restore_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_autonomous_database_wallet: gapic_v1.method.wrap_method(
                self.generate_autonomous_database_wallet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_autonomous_db_versions: gapic_v1.method.wrap_method(
                self.list_autonomous_db_versions,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_autonomous_database_character_sets: gapic_v1.method.wrap_method(
                self.list_autonomous_database_character_sets,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_autonomous_database_backups: gapic_v1.method.wrap_method(
                self.list_autonomous_database_backups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.stop_autonomous_database: gapic_v1.method.wrap_method(
                self.stop_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_autonomous_database: gapic_v1.method.wrap_method(
                self.start_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restart_autonomous_database: gapic_v1.method.wrap_method(
                self.restart_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.switchover_autonomous_database: gapic_v1.method.wrap_method(
                self.switchover_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.failover_autonomous_database: gapic_v1.method.wrap_method(
                self.failover_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.refresh_autonomous_database: gapic_v1.method.wrap_method(
                self.refresh_autonomous_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_autonomous_database_refreshable_clones: gapic_v1.method.wrap_method(
                self.get_autonomous_database_refreshable_clones,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_odb_networks: gapic_v1.method.wrap_method(
                self.list_odb_networks,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_odb_network: gapic_v1.method.wrap_method(
                self.get_odb_network,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_odb_network: gapic_v1.method.wrap_method(
                self.create_odb_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_odb_network: gapic_v1.method.wrap_method(
                self.delete_odb_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_odb_subnets: gapic_v1.method.wrap_method(
                self.list_odb_subnets,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_odb_subnet: gapic_v1.method.wrap_method(
                self.get_odb_subnet,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_odb_subnet: gapic_v1.method.wrap_method(
                self.create_odb_subnet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_odb_subnet: gapic_v1.method.wrap_method(
                self.delete_odb_subnet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_odb_dns_zones: gapic_v1.method.wrap_method(
                self.list_odb_dns_zones,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_odb_dns_zone: gapic_v1.method.wrap_method(
                self.get_odb_dns_zone,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_odb_dns_zone: gapic_v1.method.wrap_method(
                self.create_odb_dns_zone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_odb_dns_zone: gapic_v1.method.wrap_method(
                self.delete_odb_dns_zone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_exadb_vm_clusters: gapic_v1.method.wrap_method(
                self.list_exadb_vm_clusters,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_exadb_vm_cluster: gapic_v1.method.wrap_method(
                self.get_exadb_vm_cluster,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_exadb_vm_cluster: gapic_v1.method.wrap_method(
                self.create_exadb_vm_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_exadb_vm_cluster: gapic_v1.method.wrap_method(
                self.delete_exadb_vm_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_exadb_vm_cluster: gapic_v1.method.wrap_method(
                self.update_exadb_vm_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_virtual_machine_exadb_vm_cluster: gapic_v1.method.wrap_method(
                self.remove_virtual_machine_exadb_vm_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_exascale_db_storage_vaults: gapic_v1.method.wrap_method(
                self.list_exascale_db_storage_vaults,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_exascale_db_storage_vault: gapic_v1.method.wrap_method(
                self.get_exascale_db_storage_vault,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_exascale_db_storage_vault: gapic_v1.method.wrap_method(
                self.create_exascale_db_storage_vault,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_exascale_db_storage_vault: gapic_v1.method.wrap_method(
                self.delete_exascale_db_storage_vault,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_db_system_initial_storage_sizes: gapic_v1.method.wrap_method(
                self.list_db_system_initial_storage_sizes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_databases: gapic_v1.method.wrap_method(
                self.list_databases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_database: gapic_v1.method.wrap_method(
                self.get_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_pluggable_databases: gapic_v1.method.wrap_method(
                self.list_pluggable_databases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_pluggable_database: gapic_v1.method.wrap_method(
                self.get_pluggable_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_db_systems: gapic_v1.method.wrap_method(
                self.list_db_systems,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_db_system: gapic_v1.method.wrap_method(
                self.get_db_system,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_db_system: gapic_v1.method.wrap_method(
                self.create_db_system,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_db_system: gapic_v1.method.wrap_method(
                self.delete_db_system,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_goldengate_deployments: gapic_v1.method.wrap_method(
                self.list_goldengate_deployments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_goldengate_deployment: gapic_v1.method.wrap_method(
                self.get_goldengate_deployment,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_goldengate_deployment: gapic_v1.method.wrap_method(
                self.create_goldengate_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_goldengate_deployment: gapic_v1.method.wrap_method(
                self.delete_goldengate_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_goldengate_deployment: gapic_v1.method.wrap_method(
                self.stop_goldengate_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_goldengate_deployment: gapic_v1.method.wrap_method(
                self.start_goldengate_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_goldengate_connections: gapic_v1.method.wrap_method(
                self.list_goldengate_connections,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_goldengate_connection: gapic_v1.method.wrap_method(
                self.get_goldengate_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_goldengate_connection: gapic_v1.method.wrap_method(
                self.create_goldengate_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_goldengate_connection: gapic_v1.method.wrap_method(
                self.delete_goldengate_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_goldengate_deployment_versions: gapic_v1.method.wrap_method(
                self.list_goldengate_deployment_versions,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_goldengate_deployment_types: gapic_v1.method.wrap_method(
                self.list_goldengate_deployment_types,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_goldengate_deployment_environments: gapic_v1.method.wrap_method(
                self.list_goldengate_deployment_environments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_goldengate_connection_types: gapic_v1.method.wrap_method(
                self.list_goldengate_connection_types,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_db_versions: gapic_v1.method.wrap_method(
                self.list_db_versions,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_database_character_sets: gapic_v1.method.wrap_method(
                self.list_database_character_sets,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_goldengate_connection_assignments: gapic_v1.method.wrap_method(
                self.list_goldengate_connection_assignments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_goldengate_connection_assignment: gapic_v1.method.wrap_method(
                self.get_goldengate_connection_assignment,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_goldengate_connection_assignment: gapic_v1.method.wrap_method(
                self.create_goldengate_connection_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_goldengate_connection_assignment: gapic_v1.method.wrap_method(
                self.delete_goldengate_connection_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_goldengate_connection_assignment: gapic_v1.method.wrap_method(
                self.test_goldengate_connection_assignment,
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
    def list_cloud_exadata_infrastructures(
        self,
    ) -> Callable[
        [oracledatabase.ListCloudExadataInfrastructuresRequest],
        Union[
            oracledatabase.ListCloudExadataInfrastructuresResponse,
            Awaitable[oracledatabase.ListCloudExadataInfrastructuresResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [oracledatabase.GetCloudExadataInfrastructureRequest],
        Union[
            exadata_infra.CloudExadataInfrastructure,
            Awaitable[exadata_infra.CloudExadataInfrastructure],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [oracledatabase.CreateCloudExadataInfrastructureRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [oracledatabase.DeleteCloudExadataInfrastructureRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def configure_exascale_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [exadata_infra.ConfigureExascaleCloudExadataInfrastructureRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_cloud_vm_clusters(
        self,
    ) -> Callable[
        [oracledatabase.ListCloudVmClustersRequest],
        Union[
            oracledatabase.ListCloudVmClustersResponse,
            Awaitable[oracledatabase.ListCloudVmClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cloud_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.GetCloudVmClusterRequest],
        Union[vm_cluster.CloudVmCluster, Awaitable[vm_cluster.CloudVmCluster]],
    ]:
        raise NotImplementedError()

    @property
    def create_cloud_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.CreateCloudVmClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cloud_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.DeleteCloudVmClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_entitlements(
        self,
    ) -> Callable[
        [oracledatabase.ListEntitlementsRequest],
        Union[
            oracledatabase.ListEntitlementsResponse,
            Awaitable[oracledatabase.ListEntitlementsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_db_servers(
        self,
    ) -> Callable[
        [oracledatabase.ListDbServersRequest],
        Union[
            oracledatabase.ListDbServersResponse,
            Awaitable[oracledatabase.ListDbServersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_db_nodes(
        self,
    ) -> Callable[
        [oracledatabase.ListDbNodesRequest],
        Union[
            oracledatabase.ListDbNodesResponse,
            Awaitable[oracledatabase.ListDbNodesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_gi_versions(
        self,
    ) -> Callable[
        [oracledatabase.ListGiVersionsRequest],
        Union[
            oracledatabase.ListGiVersionsResponse,
            Awaitable[oracledatabase.ListGiVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_minor_versions(
        self,
    ) -> Callable[
        [minor_version.ListMinorVersionsRequest],
        Union[
            minor_version.ListMinorVersionsResponse,
            Awaitable[minor_version.ListMinorVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_db_system_shapes(
        self,
    ) -> Callable[
        [oracledatabase.ListDbSystemShapesRequest],
        Union[
            oracledatabase.ListDbSystemShapesResponse,
            Awaitable[oracledatabase.ListDbSystemShapesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_autonomous_databases(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDatabasesRequest],
        Union[
            oracledatabase.ListAutonomousDatabasesResponse,
            Awaitable[oracledatabase.ListAutonomousDatabasesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.GetAutonomousDatabaseRequest],
        Union[
            autonomous_database.AutonomousDatabase,
            Awaitable[autonomous_database.AutonomousDatabase],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.CreateAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.UpdateAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.DeleteAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restore_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.RestoreAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_autonomous_database_wallet(
        self,
    ) -> Callable[
        [oracledatabase.GenerateAutonomousDatabaseWalletRequest],
        Union[
            oracledatabase.GenerateAutonomousDatabaseWalletResponse,
            Awaitable[oracledatabase.GenerateAutonomousDatabaseWalletResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_autonomous_db_versions(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDbVersionsRequest],
        Union[
            oracledatabase.ListAutonomousDbVersionsResponse,
            Awaitable[oracledatabase.ListAutonomousDbVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_autonomous_database_character_sets(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDatabaseCharacterSetsRequest],
        Union[
            oracledatabase.ListAutonomousDatabaseCharacterSetsResponse,
            Awaitable[oracledatabase.ListAutonomousDatabaseCharacterSetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_autonomous_database_backups(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDatabaseBackupsRequest],
        Union[
            oracledatabase.ListAutonomousDatabaseBackupsResponse,
            Awaitable[oracledatabase.ListAutonomousDatabaseBackupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def stop_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.StopAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.StartAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restart_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.RestartAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def switchover_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.SwitchoverAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def failover_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.FailoverAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def refresh_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.RefreshAutonomousDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_autonomous_database_refreshable_clones(
        self,
    ) -> Callable[
        [oracledatabase.GetAutonomousDatabaseRefreshableClonesRequest],
        Union[
            oracledatabase.AutonomousDatabaseRefreshableClones,
            Awaitable[oracledatabase.AutonomousDatabaseRefreshableClones],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_odb_networks(
        self,
    ) -> Callable[
        [odb_network.ListOdbNetworksRequest],
        Union[
            odb_network.ListOdbNetworksResponse,
            Awaitable[odb_network.ListOdbNetworksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_odb_network(
        self,
    ) -> Callable[
        [odb_network.GetOdbNetworkRequest],
        Union[odb_network.OdbNetwork, Awaitable[odb_network.OdbNetwork]],
    ]:
        raise NotImplementedError()

    @property
    def create_odb_network(
        self,
    ) -> Callable[
        [gco_odb_network.CreateOdbNetworkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_odb_network(
        self,
    ) -> Callable[
        [odb_network.DeleteOdbNetworkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_odb_subnets(
        self,
    ) -> Callable[
        [odb_subnet.ListOdbSubnetsRequest],
        Union[
            odb_subnet.ListOdbSubnetsResponse,
            Awaitable[odb_subnet.ListOdbSubnetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_odb_subnet(
        self,
    ) -> Callable[
        [odb_subnet.GetOdbSubnetRequest],
        Union[odb_subnet.OdbSubnet, Awaitable[odb_subnet.OdbSubnet]],
    ]:
        raise NotImplementedError()

    @property
    def create_odb_subnet(
        self,
    ) -> Callable[
        [gco_odb_subnet.CreateOdbSubnetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_odb_subnet(
        self,
    ) -> Callable[
        [odb_subnet.DeleteOdbSubnetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_odb_dns_zones(
        self,
    ) -> Callable[
        [odb_dns_zone.ListOdbDnsZonesRequest],
        Union[
            odb_dns_zone.ListOdbDnsZonesResponse,
            Awaitable[odb_dns_zone.ListOdbDnsZonesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_odb_dns_zone(
        self,
    ) -> Callable[
        [odb_dns_zone.GetOdbDnsZoneRequest],
        Union[odb_dns_zone.OdbDnsZone, Awaitable[odb_dns_zone.OdbDnsZone]],
    ]:
        raise NotImplementedError()

    @property
    def create_odb_dns_zone(
        self,
    ) -> Callable[
        [gco_odb_dns_zone.CreateOdbDnsZoneRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_odb_dns_zone(
        self,
    ) -> Callable[
        [odb_dns_zone.DeleteOdbDnsZoneRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_exadb_vm_clusters(
        self,
    ) -> Callable[
        [oracledatabase.ListExadbVmClustersRequest],
        Union[
            oracledatabase.ListExadbVmClustersResponse,
            Awaitable[oracledatabase.ListExadbVmClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.GetExadbVmClusterRequest],
        Union[
            exadb_vm_cluster.ExadbVmCluster, Awaitable[exadb_vm_cluster.ExadbVmCluster]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.CreateExadbVmClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.DeleteExadbVmClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.UpdateExadbVmClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def remove_virtual_machine_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.RemoveVirtualMachineExadbVmClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_exascale_db_storage_vaults(
        self,
    ) -> Callable[
        [exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest],
        Union[
            exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse,
            Awaitable[exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_exascale_db_storage_vault(
        self,
    ) -> Callable[
        [exascale_db_storage_vault.GetExascaleDbStorageVaultRequest],
        Union[
            exascale_db_storage_vault.ExascaleDbStorageVault,
            Awaitable[exascale_db_storage_vault.ExascaleDbStorageVault],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_exascale_db_storage_vault(
        self,
    ) -> Callable[
        [gco_exascale_db_storage_vault.CreateExascaleDbStorageVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_exascale_db_storage_vault(
        self,
    ) -> Callable[
        [exascale_db_storage_vault.DeleteExascaleDbStorageVaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_db_system_initial_storage_sizes(
        self,
    ) -> Callable[
        [db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest],
        Union[
            db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse,
            Awaitable[
                db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_databases(
        self,
    ) -> Callable[
        [database.ListDatabasesRequest],
        Union[
            database.ListDatabasesResponse, Awaitable[database.ListDatabasesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_database(
        self,
    ) -> Callable[
        [database.GetDatabaseRequest],
        Union[database.Database, Awaitable[database.Database]],
    ]:
        raise NotImplementedError()

    @property
    def list_pluggable_databases(
        self,
    ) -> Callable[
        [pluggable_database.ListPluggableDatabasesRequest],
        Union[
            pluggable_database.ListPluggableDatabasesResponse,
            Awaitable[pluggable_database.ListPluggableDatabasesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_pluggable_database(
        self,
    ) -> Callable[
        [pluggable_database.GetPluggableDatabaseRequest],
        Union[
            pluggable_database.PluggableDatabase,
            Awaitable[pluggable_database.PluggableDatabase],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_db_systems(
        self,
    ) -> Callable[
        [db_system.ListDbSystemsRequest],
        Union[
            db_system.ListDbSystemsResponse, Awaitable[db_system.ListDbSystemsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_db_system(
        self,
    ) -> Callable[
        [db_system.GetDbSystemRequest],
        Union[db_system.DbSystem, Awaitable[db_system.DbSystem]],
    ]:
        raise NotImplementedError()

    @property
    def create_db_system(
        self,
    ) -> Callable[
        [gco_db_system.CreateDbSystemRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_db_system(
        self,
    ) -> Callable[
        [db_system.DeleteDbSystemRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_deployments(
        self,
    ) -> Callable[
        [goldengate_deployment.ListGoldengateDeploymentsRequest],
        Union[
            goldengate_deployment.ListGoldengateDeploymentsResponse,
            Awaitable[goldengate_deployment.ListGoldengateDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.GetGoldengateDeploymentRequest],
        Union[
            goldengate_deployment.GoldengateDeployment,
            Awaitable[goldengate_deployment.GoldengateDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_goldengate_deployment(
        self,
    ) -> Callable[
        [gco_goldengate_deployment.CreateGoldengateDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.DeleteGoldengateDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.StopGoldengateDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.StartGoldengateDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_connections(
        self,
    ) -> Callable[
        [goldengate_connection.ListGoldengateConnectionsRequest],
        Union[
            goldengate_connection.ListGoldengateConnectionsResponse,
            Awaitable[goldengate_connection.ListGoldengateConnectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_goldengate_connection(
        self,
    ) -> Callable[
        [goldengate_connection.GetGoldengateConnectionRequest],
        Union[
            goldengate_connection.GoldengateConnection,
            Awaitable[goldengate_connection.GoldengateConnection],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_goldengate_connection(
        self,
    ) -> Callable[
        [gco_goldengate_connection.CreateGoldengateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_goldengate_connection(
        self,
    ) -> Callable[
        [goldengate_connection.DeleteGoldengateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_deployment_versions(
        self,
    ) -> Callable[
        [goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest],
        Union[
            goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse,
            Awaitable[
                goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_deployment_types(
        self,
    ) -> Callable[
        [goldengate_deployment_type.ListGoldengateDeploymentTypesRequest],
        Union[
            goldengate_deployment_type.ListGoldengateDeploymentTypesResponse,
            Awaitable[goldengate_deployment_type.ListGoldengateDeploymentTypesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_deployment_environments(
        self,
    ) -> Callable[
        [goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest],
        Union[
            goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse,
            Awaitable[
                goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_connection_types(
        self,
    ) -> Callable[
        [goldengate_connection_type.ListGoldengateConnectionTypesRequest],
        Union[
            goldengate_connection_type.ListGoldengateConnectionTypesResponse,
            Awaitable[goldengate_connection_type.ListGoldengateConnectionTypesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_db_versions(
        self,
    ) -> Callable[
        [db_version.ListDbVersionsRequest],
        Union[
            db_version.ListDbVersionsResponse,
            Awaitable[db_version.ListDbVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_database_character_sets(
        self,
    ) -> Callable[
        [database_character_set.ListDatabaseCharacterSetsRequest],
        Union[
            database_character_set.ListDatabaseCharacterSetsResponse,
            Awaitable[database_character_set.ListDatabaseCharacterSetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_goldengate_connection_assignments(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest],
        Union[
            goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse,
            Awaitable[
                goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.GetGoldengateConnectionAssignmentRequest],
        Union[
            goldengate_connection_assignment.GoldengateConnectionAssignment,
            Awaitable[goldengate_connection_assignment.GoldengateConnectionAssignment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [
            gco_goldengate_connection_assignment.CreateGoldengateConnectionAssignmentRequest
        ],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.DeleteGoldengateConnectionAssignmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def test_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.TestGoldengateConnectionAssignmentRequest],
        Union[
            goldengate_connection_assignment.TestGoldengateConnectionAssignmentResponse,
            Awaitable[
                goldengate_connection_assignment.TestGoldengateConnectionAssignmentResponse
            ],
        ],
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


__all__ = ("OracleDatabaseTransport",)
