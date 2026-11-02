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
import json
import logging as std_logging
import os
import re
import warnings
from collections import OrderedDict
from http import HTTPStatus
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
    cast,
)

import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.oracledatabase_v1 import gapic_version as package_version
from google.cloud.oracledatabase_v1._compat import (
    get_api_endpoint,
    get_default_mtls_endpoint,
    get_universe_domain,
    read_environment_variables,
    should_use_client_cert,
)

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.oracledatabase_v1.services.oracle_database import pagers
from google.cloud.oracledatabase_v1.types import (
    autonomous_database,
    autonomous_database_character_set,
    autonomous_db_backup,
    autonomous_db_version,
    common,
    database,
    database_character_set,
    db_node,
    db_server,
    db_system,
    db_system_initial_storage_size,
    db_system_shape,
    db_version,
    entitlement,
    exadata_infra,
    exadb_vm_cluster,
    exascale_db_storage_vault,
    gi_version,
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
from google.cloud.oracledatabase_v1.types import (
    autonomous_database as gco_autonomous_database,
)
from google.cloud.oracledatabase_v1.types import db_system as gco_db_system
from google.cloud.oracledatabase_v1.types import (
    exadb_vm_cluster as gco_exadb_vm_cluster,
)
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

from .transports.base import DEFAULT_CLIENT_INFO, OracleDatabaseTransport
from .transports.grpc import OracleDatabaseGrpcTransport
from .transports.grpc_asyncio import OracleDatabaseGrpcAsyncIOTransport
from .transports.rest import OracleDatabaseRestTransport


class OracleDatabaseClientMeta(type):
    """Metaclass for the OracleDatabase client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[OracleDatabaseTransport]]
    _transport_registry["grpc"] = OracleDatabaseGrpcTransport
    _transport_registry["grpc_asyncio"] = OracleDatabaseGrpcAsyncIOTransport
    _transport_registry["rest"] = OracleDatabaseRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[OracleDatabaseTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class OracleDatabaseClient(metaclass=OracleDatabaseClientMeta):
    """Service describing handlers for resources"""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "oracledatabase.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "oracledatabase.{UNIVERSE_DOMAIN}"
    _DEFAULT_UNIVERSE = "googleapis.com"

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            OracleDatabaseClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

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
            OracleDatabaseClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> OracleDatabaseTransport:
        """Returns the transport used by the client instance.

        Returns:
            OracleDatabaseTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def autonomous_database_path(
        project: str,
        location: str,
        autonomous_database: str,
    ) -> str:
        """Returns a fully-qualified autonomous_database string."""
        return "projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}".format(
            project=project,
            location=location,
            autonomous_database=autonomous_database,
        )

    @staticmethod
    def parse_autonomous_database_path(path: str) -> Dict[str, str]:
        """Parses a autonomous_database path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/autonomousDatabases/(?P<autonomous_database>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def autonomous_database_backup_path(
        project: str,
        location: str,
        autonomous_database_backup: str,
    ) -> str:
        """Returns a fully-qualified autonomous_database_backup string."""
        return "projects/{project}/locations/{location}/autonomousDatabaseBackups/{autonomous_database_backup}".format(
            project=project,
            location=location,
            autonomous_database_backup=autonomous_database_backup,
        )

    @staticmethod
    def parse_autonomous_database_backup_path(path: str) -> Dict[str, str]:
        """Parses a autonomous_database_backup path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/autonomousDatabaseBackups/(?P<autonomous_database_backup>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def autonomous_database_character_set_path(
        project: str,
        location: str,
        autonomous_database_character_set: str,
    ) -> str:
        """Returns a fully-qualified autonomous_database_character_set string."""
        return "projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}".format(
            project=project,
            location=location,
            autonomous_database_character_set=autonomous_database_character_set,
        )

    @staticmethod
    def parse_autonomous_database_character_set_path(path: str) -> Dict[str, str]:
        """Parses a autonomous_database_character_set path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/autonomousDatabaseCharacterSets/(?P<autonomous_database_character_set>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def autonomous_db_version_path(
        project: str,
        location: str,
        autonomous_db_version: str,
    ) -> str:
        """Returns a fully-qualified autonomous_db_version string."""
        return "projects/{project}/locations/{location}/autonomousDbVersions/{autonomous_db_version}".format(
            project=project,
            location=location,
            autonomous_db_version=autonomous_db_version,
        )

    @staticmethod
    def parse_autonomous_db_version_path(path: str) -> Dict[str, str]:
        """Parses a autonomous_db_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/autonomousDbVersions/(?P<autonomous_db_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def cloud_exadata_infrastructure_path(
        project: str,
        location: str,
        cloud_exadata_infrastructure: str,
    ) -> str:
        """Returns a fully-qualified cloud_exadata_infrastructure string."""
        return "projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}".format(
            project=project,
            location=location,
            cloud_exadata_infrastructure=cloud_exadata_infrastructure,
        )

    @staticmethod
    def parse_cloud_exadata_infrastructure_path(path: str) -> Dict[str, str]:
        """Parses a cloud_exadata_infrastructure path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/cloudExadataInfrastructures/(?P<cloud_exadata_infrastructure>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def cloud_vm_cluster_path(
        project: str,
        location: str,
        cloud_vm_cluster: str,
    ) -> str:
        """Returns a fully-qualified cloud_vm_cluster string."""
        return "projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}".format(
            project=project,
            location=location,
            cloud_vm_cluster=cloud_vm_cluster,
        )

    @staticmethod
    def parse_cloud_vm_cluster_path(path: str) -> Dict[str, str]:
        """Parses a cloud_vm_cluster path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/cloudVmClusters/(?P<cloud_vm_cluster>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def crypto_key_path(
        project: str,
        location: str,
        key_ring: str,
        crypto_key: str,
    ) -> str:
        """Returns a fully-qualified crypto_key string."""
        return "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}".format(
            project=project,
            location=location,
            key_ring=key_ring,
            crypto_key=crypto_key,
        )

    @staticmethod
    def parse_crypto_key_path(path: str) -> Dict[str, str]:
        """Parses a crypto_key path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/keyRings/(?P<key_ring>.+?)/cryptoKeys/(?P<crypto_key>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def database_path(
        project: str,
        location: str,
        database: str,
    ) -> str:
        """Returns a fully-qualified database string."""
        return "projects/{project}/locations/{location}/databases/{database}".format(
            project=project,
            location=location,
            database=database,
        )

    @staticmethod
    def parse_database_path(path: str) -> Dict[str, str]:
        """Parses a database path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/databases/(?P<database>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def database_character_set_path(
        project: str,
        location: str,
        database_character_set: str,
    ) -> str:
        """Returns a fully-qualified database_character_set string."""
        return "projects/{project}/locations/{location}/databaseCharacterSets/{database_character_set}".format(
            project=project,
            location=location,
            database_character_set=database_character_set,
        )

    @staticmethod
    def parse_database_character_set_path(path: str) -> Dict[str, str]:
        """Parses a database_character_set path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/databaseCharacterSets/(?P<database_character_set>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def db_node_path(
        project: str,
        location: str,
        cloud_vm_cluster: str,
        db_node: str,
    ) -> str:
        """Returns a fully-qualified db_node string."""
        return "projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}".format(
            project=project,
            location=location,
            cloud_vm_cluster=cloud_vm_cluster,
            db_node=db_node,
        )

    @staticmethod
    def parse_db_node_path(path: str) -> Dict[str, str]:
        """Parses a db_node path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/cloudVmClusters/(?P<cloud_vm_cluster>.+?)/dbNodes/(?P<db_node>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def db_server_path(
        project: str,
        location: str,
        cloud_exadata_infrastructure: str,
        db_server: str,
    ) -> str:
        """Returns a fully-qualified db_server string."""
        return "projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}/dbServers/{db_server}".format(
            project=project,
            location=location,
            cloud_exadata_infrastructure=cloud_exadata_infrastructure,
            db_server=db_server,
        )

    @staticmethod
    def parse_db_server_path(path: str) -> Dict[str, str]:
        """Parses a db_server path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/cloudExadataInfrastructures/(?P<cloud_exadata_infrastructure>.+?)/dbServers/(?P<db_server>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def db_system_path(
        project: str,
        location: str,
        db_system: str,
    ) -> str:
        """Returns a fully-qualified db_system string."""
        return "projects/{project}/locations/{location}/dbSystems/{db_system}".format(
            project=project,
            location=location,
            db_system=db_system,
        )

    @staticmethod
    def parse_db_system_path(path: str) -> Dict[str, str]:
        """Parses a db_system path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/dbSystems/(?P<db_system>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def db_system_initial_storage_size_path(
        project: str,
        location: str,
        db_system_initial_storage_size: str,
    ) -> str:
        """Returns a fully-qualified db_system_initial_storage_size string."""
        return "projects/{project}/locations/{location}/dbSystemInitialStorageSizes/{db_system_initial_storage_size}".format(
            project=project,
            location=location,
            db_system_initial_storage_size=db_system_initial_storage_size,
        )

    @staticmethod
    def parse_db_system_initial_storage_size_path(path: str) -> Dict[str, str]:
        """Parses a db_system_initial_storage_size path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/dbSystemInitialStorageSizes/(?P<db_system_initial_storage_size>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def db_system_shape_path(
        project: str,
        location: str,
        db_system_shape: str,
    ) -> str:
        """Returns a fully-qualified db_system_shape string."""
        return "projects/{project}/locations/{location}/dbSystemShapes/{db_system_shape}".format(
            project=project,
            location=location,
            db_system_shape=db_system_shape,
        )

    @staticmethod
    def parse_db_system_shape_path(path: str) -> Dict[str, str]:
        """Parses a db_system_shape path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/dbSystemShapes/(?P<db_system_shape>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def db_version_path(
        project: str,
        location: str,
        db_version: str,
    ) -> str:
        """Returns a fully-qualified db_version string."""
        return "projects/{project}/locations/{location}/dbVersions/{db_version}".format(
            project=project,
            location=location,
            db_version=db_version,
        )

    @staticmethod
    def parse_db_version_path(path: str) -> Dict[str, str]:
        """Parses a db_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/dbVersions/(?P<db_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def entitlement_path(
        project: str,
        location: str,
        entitlement: str,
    ) -> str:
        """Returns a fully-qualified entitlement string."""
        return (
            "projects/{project}/locations/{location}/entitlements/{entitlement}".format(
                project=project,
                location=location,
                entitlement=entitlement,
            )
        )

    @staticmethod
    def parse_entitlement_path(path: str) -> Dict[str, str]:
        """Parses a entitlement path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/entitlements/(?P<entitlement>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def exadb_vm_cluster_path(
        project: str,
        location: str,
        exadb_vm_cluster: str,
    ) -> str:
        """Returns a fully-qualified exadb_vm_cluster string."""
        return "projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}".format(
            project=project,
            location=location,
            exadb_vm_cluster=exadb_vm_cluster,
        )

    @staticmethod
    def parse_exadb_vm_cluster_path(path: str) -> Dict[str, str]:
        """Parses a exadb_vm_cluster path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/exadbVmClusters/(?P<exadb_vm_cluster>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def exascale_db_storage_vault_path(
        project: str,
        location: str,
        exascale_db_storage_vault: str,
    ) -> str:
        """Returns a fully-qualified exascale_db_storage_vault string."""
        return "projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}".format(
            project=project,
            location=location,
            exascale_db_storage_vault=exascale_db_storage_vault,
        )

    @staticmethod
    def parse_exascale_db_storage_vault_path(path: str) -> Dict[str, str]:
        """Parses a exascale_db_storage_vault path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/exascaleDbStorageVaults/(?P<exascale_db_storage_vault>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def gi_version_path(
        project: str,
        location: str,
        gi_version: str,
    ) -> str:
        """Returns a fully-qualified gi_version string."""
        return "projects/{project}/locations/{location}/giVersions/{gi_version}".format(
            project=project,
            location=location,
            gi_version=gi_version,
        )

    @staticmethod
    def parse_gi_version_path(path: str) -> Dict[str, str]:
        """Parses a gi_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/giVersions/(?P<gi_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_connection_path(
        project: str,
        location: str,
        goldengate_connection: str,
    ) -> str:
        """Returns a fully-qualified goldengate_connection string."""
        return "projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}".format(
            project=project,
            location=location,
            goldengate_connection=goldengate_connection,
        )

    @staticmethod
    def parse_goldengate_connection_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_connection path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateConnections/(?P<goldengate_connection>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_connection_assignment_path(
        project: str,
        location: str,
        goldengate_connection_assignment: str,
    ) -> str:
        """Returns a fully-qualified goldengate_connection_assignment string."""
        return "projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}".format(
            project=project,
            location=location,
            goldengate_connection_assignment=goldengate_connection_assignment,
        )

    @staticmethod
    def parse_goldengate_connection_assignment_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_connection_assignment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateConnectionAssignments/(?P<goldengate_connection_assignment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_connection_type_path(
        project: str,
        location: str,
        goldengate_connection_type: str,
    ) -> str:
        """Returns a fully-qualified goldengate_connection_type string."""
        return "projects/{project}/locations/{location}/goldengateConnectionTypes/{goldengate_connection_type}".format(
            project=project,
            location=location,
            goldengate_connection_type=goldengate_connection_type,
        )

    @staticmethod
    def parse_goldengate_connection_type_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_connection_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateConnectionTypes/(?P<goldengate_connection_type>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_deployment_path(
        project: str,
        location: str,
        goldengate_deployment: str,
    ) -> str:
        """Returns a fully-qualified goldengate_deployment string."""
        return "projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}".format(
            project=project,
            location=location,
            goldengate_deployment=goldengate_deployment,
        )

    @staticmethod
    def parse_goldengate_deployment_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_deployment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateDeployments/(?P<goldengate_deployment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_deployment_environment_path(
        project: str,
        location: str,
        goldengate_deployment_environment: str,
    ) -> str:
        """Returns a fully-qualified goldengate_deployment_environment string."""
        return "projects/{project}/locations/{location}/goldengateDeploymentEnvironments/{goldengate_deployment_environment}".format(
            project=project,
            location=location,
            goldengate_deployment_environment=goldengate_deployment_environment,
        )

    @staticmethod
    def parse_goldengate_deployment_environment_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_deployment_environment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateDeploymentEnvironments/(?P<goldengate_deployment_environment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_deployment_type_path(
        project: str,
        location: str,
        goldengate_deployment_type: str,
    ) -> str:
        """Returns a fully-qualified goldengate_deployment_type string."""
        return "projects/{project}/locations/{location}/goldengateDeploymentTypes/{goldengate_deployment_type}".format(
            project=project,
            location=location,
            goldengate_deployment_type=goldengate_deployment_type,
        )

    @staticmethod
    def parse_goldengate_deployment_type_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_deployment_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateDeploymentTypes/(?P<goldengate_deployment_type>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def goldengate_deployment_version_path(
        project: str,
        location: str,
        goldengate_deployment_version: str,
    ) -> str:
        """Returns a fully-qualified goldengate_deployment_version string."""
        return "projects/{project}/locations/{location}/goldengateDeploymentVersions/{goldengate_deployment_version}".format(
            project=project,
            location=location,
            goldengate_deployment_version=goldengate_deployment_version,
        )

    @staticmethod
    def parse_goldengate_deployment_version_path(path: str) -> Dict[str, str]:
        """Parses a goldengate_deployment_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/goldengateDeploymentVersions/(?P<goldengate_deployment_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def minor_version_path(
        project: str,
        location: str,
        gi_version: str,
        minor_version: str,
    ) -> str:
        """Returns a fully-qualified minor_version string."""
        return "projects/{project}/locations/{location}/giVersions/{gi_version}/minorVersions/{minor_version}".format(
            project=project,
            location=location,
            gi_version=gi_version,
            minor_version=minor_version,
        )

    @staticmethod
    def parse_minor_version_path(path: str) -> Dict[str, str]:
        """Parses a minor_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/giVersions/(?P<gi_version>.+?)/minorVersions/(?P<minor_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def network_path(
        project: str,
        network: str,
    ) -> str:
        """Returns a fully-qualified network string."""
        return "projects/{project}/global/networks/{network}".format(
            project=project,
            network=network,
        )

    @staticmethod
    def parse_network_path(path: str) -> Dict[str, str]:
        """Parses a network path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/global/networks/(?P<network>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def odb_dns_zone_path(
        project: str,
        location: str,
        odb_network: str,
        odb_dns_zone: str,
    ) -> str:
        """Returns a fully-qualified odb_dns_zone string."""
        return "projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}".format(
            project=project,
            location=location,
            odb_network=odb_network,
            odb_dns_zone=odb_dns_zone,
        )

    @staticmethod
    def parse_odb_dns_zone_path(path: str) -> Dict[str, str]:
        """Parses a odb_dns_zone path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/odbNetworks/(?P<odb_network>.+?)/odbDnsZones/(?P<odb_dns_zone>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def odb_network_path(
        project: str,
        location: str,
        odb_network: str,
    ) -> str:
        """Returns a fully-qualified odb_network string."""
        return (
            "projects/{project}/locations/{location}/odbNetworks/{odb_network}".format(
                project=project,
                location=location,
                odb_network=odb_network,
            )
        )

    @staticmethod
    def parse_odb_network_path(path: str) -> Dict[str, str]:
        """Parses a odb_network path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/odbNetworks/(?P<odb_network>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def odb_subnet_path(
        project: str,
        location: str,
        odb_network: str,
        odb_subnet: str,
    ) -> str:
        """Returns a fully-qualified odb_subnet string."""
        return "projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}".format(
            project=project,
            location=location,
            odb_network=odb_network,
            odb_subnet=odb_subnet,
        )

    @staticmethod
    def parse_odb_subnet_path(path: str) -> Dict[str, str]:
        """Parses a odb_subnet path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/odbNetworks/(?P<odb_network>.+?)/odbSubnets/(?P<odb_subnet>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def pluggable_database_path(
        project: str,
        location: str,
        pluggable_database: str,
    ) -> str:
        """Returns a fully-qualified pluggable_database string."""
        return "projects/{project}/locations/{location}/pluggableDatabases/{pluggable_database}".format(
            project=project,
            location=location,
            pluggable_database=pluggable_database,
        )

    @staticmethod
    def parse_pluggable_database_path(path: str) -> Dict[str, str]:
        """Parses a pluggable_database path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/pluggableDatabases/(?P<pluggable_database>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def secret_version_path(
        project: str,
        secret: str,
        secret_version: str,
    ) -> str:
        """Returns a fully-qualified secret_version string."""
        return "projects/{project}/secrets/{secret}/versions/{secret_version}".format(
            project=project,
            secret=secret,
            secret_version=secret_version,
        )

    @staticmethod
    def parse_secret_version_path(path: str) -> Dict[str, str]:
        """Parses a secret_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/secrets/(?P<secret>.+?)/versions/(?P<secret_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Deprecated. Return the API endpoint and client cert source for mutual TLS.

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

        warnings.warn(
            "get_mtls_endpoint_and_cert_source is deprecated. Use the api_endpoint property instead.",
            DeprecationWarning,
        )
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = should_use_client_cert()
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert:
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT  # type: ignore
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    @staticmethod
    def _get_client_cert_source(provided_cert_source, use_cert_flag):
        """Return the client cert source to be used by the client.

        Args:
            provided_cert_source (bytes): The client certificate source provided.
            use_cert_flag (bool): A flag indicating whether to use the client certificate.

        Returns:
            bytes or None: The client cert source to be used by the client.
        """
        client_cert_source = None
        if use_cert_flag:
            if provided_cert_source:
                client_cert_source = provided_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()
        return client_cert_source

    def _validate_universe_domain(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            ValueError: If the configured universe domain is not valid.
        """

        # NOTE (b/349488459): universe validation is disabled until further notice.
        return True

    def _add_cred_info_for_auth_errors(
        self, error: core_exceptions.GoogleAPICallError
    ) -> None:
        """Adds credential info string to error details for 401/403/404 errors.

        Args:
            error (google.api_core.exceptions.GoogleAPICallError): The error to add the cred info.
        """
        if error.code not in [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
        ]:
            return

        cred = self._transport._credentials

        # get_cred_info is only available in google-auth>=2.35.0
        if not hasattr(cred, "get_cred_info"):
            return

        # ignore the type check since pypy test fails when get_cred_info
        # is not available
        cred_info = cred.get_cred_info()  # type: ignore
        if cred_info and hasattr(error._details, "append"):
            error._details.append(json.dumps(cred_info))

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used by the client instance.
        """
        return self._universe_domain

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, OracleDatabaseTransport, Callable[..., OracleDatabaseTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the oracle database client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,OracleDatabaseTransport,Callable[..., OracleDatabaseTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the OracleDatabaseTransport constructor.
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
                default "googleapis.com" universe. Note that the ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client_options = client_options
        if isinstance(self._client_options, dict):
            self._client_options = client_options_lib.from_dict(self._client_options)
        if self._client_options is None:
            self._client_options = client_options_lib.ClientOptions()
        self._client_options = cast(
            client_options_lib.ClientOptions, self._client_options
        )

        universe_domain_opt = getattr(self._client_options, "universe_domain", None)

        self._use_client_cert, self._use_mtls_endpoint, self._universe_domain_env = (
            read_environment_variables()
        )
        self._client_cert_source = OracleDatabaseClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=OracleDatabaseClient._DEFAULT_UNIVERSE,
        )
        self._api_endpoint: str = ""  # updated below, depending on `transport`

        # Initialize the universe domain validation.
        self._is_universe_domain_valid = False

        if CLIENT_LOGGING_SUPPORTED:  # pragma: NO COVER
            # Setup logging.
            client_logging.initialize_logging()

        api_key_value = getattr(self._client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        transport_provided = isinstance(transport, OracleDatabaseTransport)
        if transport_provided:
            # transport is a OracleDatabaseTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(OracleDatabaseTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=OracleDatabaseClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=OracleDatabaseClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=OracleDatabaseClient._DEFAULT_ENDPOINT_TEMPLATE,
            use_mtls=self._use_mtls_endpoint == "always"
            or (self._use_mtls_endpoint == "auto" and self._client_cert_source),
        )

        if not transport_provided:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            transport_init: Union[
                Type[OracleDatabaseTransport], Callable[..., OracleDatabaseTransport]
            ] = (
                OracleDatabaseClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., OracleDatabaseTransport], transport)
            )
            # initialize with the provided callable or the passed in class
            self._transport = transport_init(
                credentials=credentials,
                credentials_file=self._client_options.credentials_file,
                host=self._api_endpoint,
                scopes=self._client_options.scopes,
                client_cert_source_for_mtls=self._client_cert_source,
                quota_project_id=self._client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=self._client_options.api_audience,
            )

        if "async" not in str(self._transport):
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                std_logging.DEBUG
            ):  # pragma: NO COVER
                _LOGGER.debug(
                    "Created client `google.cloud.oracledatabase_v1.OracleDatabaseClient`.",
                    extra={
                        "serviceName": "google.cloud.oracledatabase.v1.OracleDatabase",
                        "universeDomain": getattr(
                            self._transport._credentials, "universe_domain", ""
                        ),
                        "credentialsType": f"{type(self._transport._credentials).__module__}.{type(self._transport._credentials).__qualname__}",
                        "credentialsInfo": getattr(
                            self.transport._credentials, "get_cred_info", lambda: None
                        )(),
                    }
                    if hasattr(self._transport, "_credentials")
                    else {
                        "serviceName": "google.cloud.oracledatabase.v1.OracleDatabase",
                        "credentialsType": None,
                    },
                )

    def list_cloud_exadata_infrastructures(
        self,
        request: Optional[
            Union[oracledatabase.ListCloudExadataInfrastructuresRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCloudExadataInfrastructuresPager:
        r"""Lists Exadata Infrastructures in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_cloud_exadata_infrastructures():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListCloudExadataInfrastructuresRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_cloud_exadata_infrastructures(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresRequest, dict]):
                The request object. The request for ``CloudExadataInfrastructures.List``.
            parent (str):
                Required. The parent value for
                CloudExadataInfrastructure in the
                following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListCloudExadataInfrastructuresPager:
                The response for CloudExadataInfrastructures.list.

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
            request, oracledatabase.ListCloudExadataInfrastructuresRequest
        ):
            request = oracledatabase.ListCloudExadataInfrastructuresRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_cloud_exadata_infrastructures
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCloudExadataInfrastructuresPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_cloud_exadata_infrastructure(
        self,
        request: Optional[
            Union[oracledatabase.GetCloudExadataInfrastructureRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> exadata_infra.CloudExadataInfrastructure:
        r"""Gets details of a single Exadata Infrastructure.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_cloud_exadata_infrastructure():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetCloudExadataInfrastructureRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_cloud_exadata_infrastructure(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetCloudExadataInfrastructureRequest, dict]):
                The request object. The request for ``CloudExadataInfrastructure.Get``.
            name (str):
                Required. The name of the Cloud Exadata Infrastructure
                in the following format:
                projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.CloudExadataInfrastructure:
                Represents CloudExadataInfrastructure
                resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudExadataInfrastructure/

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
        if not isinstance(request, oracledatabase.GetCloudExadataInfrastructureRequest):
            request = oracledatabase.GetCloudExadataInfrastructureRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_cloud_exadata_infrastructure
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_cloud_exadata_infrastructure(
        self,
        request: Optional[
            Union[oracledatabase.CreateCloudExadataInfrastructureRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        cloud_exadata_infrastructure: Optional[
            exadata_infra.CloudExadataInfrastructure
        ] = None,
        cloud_exadata_infrastructure_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new Exadata Infrastructure in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_cloud_exadata_infrastructure():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.CreateCloudExadataInfrastructureRequest(
                    parent="parent_value",
                    cloud_exadata_infrastructure_id="cloud_exadata_infrastructure_id_value",
                )

                # Make the request
                operation = client.create_cloud_exadata_infrastructure(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateCloudExadataInfrastructureRequest, dict]):
                The request object. The request for ``CloudExadataInfrastructure.Create``.
            parent (str):
                Required. The parent value for
                CloudExadataInfrastructure in the
                following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cloud_exadata_infrastructure (google.cloud.oracledatabase_v1.types.CloudExadataInfrastructure):
                Required. Details of the Exadata
                Infrastructure instance to create.

                This corresponds to the ``cloud_exadata_infrastructure`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cloud_exadata_infrastructure_id (str):
                Required. The ID of the Exadata Infrastructure to
                create. This value is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``cloud_exadata_infrastructure_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.CloudExadataInfrastructure` Represents CloudExadataInfrastructure resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudExadataInfrastructure/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            cloud_exadata_infrastructure,
            cloud_exadata_infrastructure_id,
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
            request, oracledatabase.CreateCloudExadataInfrastructureRequest
        ):
            request = oracledatabase.CreateCloudExadataInfrastructureRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if cloud_exadata_infrastructure is not None:
                request.cloud_exadata_infrastructure = cloud_exadata_infrastructure
            if cloud_exadata_infrastructure_id is not None:
                request.cloud_exadata_infrastructure_id = (
                    cloud_exadata_infrastructure_id
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_cloud_exadata_infrastructure
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            exadata_infra.CloudExadataInfrastructure,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_cloud_exadata_infrastructure(
        self,
        request: Optional[
            Union[oracledatabase.DeleteCloudExadataInfrastructureRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single Exadata Infrastructure.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_cloud_exadata_infrastructure():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteCloudExadataInfrastructureRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_cloud_exadata_infrastructure(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteCloudExadataInfrastructureRequest, dict]):
                The request object. The request for ``CloudExadataInfrastructure.Delete``.
            name (str):
                Required. The name of the Cloud Exadata Infrastructure
                in the following format:
                projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
            request, oracledatabase.DeleteCloudExadataInfrastructureRequest
        ):
            request = oracledatabase.DeleteCloudExadataInfrastructureRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_cloud_exadata_infrastructure
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def configure_exascale_cloud_exadata_infrastructure(
        self,
        request: Optional[
            Union[
                exadata_infra.ConfigureExascaleCloudExadataInfrastructureRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        total_storage_size_gb: Optional[int] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Configures Exascale for a single Exadata
        Infrastructure.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_configure_exascale_cloud_exadata_infrastructure():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ConfigureExascaleCloudExadataInfrastructureRequest(
                    name="name_value",
                    total_storage_size_gb=2234,
                )

                # Make the request
                operation = client.configure_exascale_cloud_exadata_infrastructure(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ConfigureExascaleCloudExadataInfrastructureRequest, dict]):
                The request object. The request for
                ``CloudExadataInfrastructure.ConfigureExascale``.
            name (str):
                Required. The name of the Cloud Exadata Infrastructure
                in the following format:
                projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            total_storage_size_gb (int):
                Required. The total storage to be
                allocated to Exascale in GBs.

                This corresponds to the ``total_storage_size_gb`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.CloudExadataInfrastructure` Represents CloudExadataInfrastructure resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudExadataInfrastructure/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, total_storage_size_gb]
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
            request, exadata_infra.ConfigureExascaleCloudExadataInfrastructureRequest
        ):
            request = exadata_infra.ConfigureExascaleCloudExadataInfrastructureRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if total_storage_size_gb is not None:
                request.total_storage_size_gb = total_storage_size_gb

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.configure_exascale_cloud_exadata_infrastructure
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            exadata_infra.CloudExadataInfrastructure,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_cloud_vm_clusters(
        self,
        request: Optional[
            Union[oracledatabase.ListCloudVmClustersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCloudVmClustersPager:
        r"""Lists the VM Clusters in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_cloud_vm_clusters():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListCloudVmClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_cloud_vm_clusters(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListCloudVmClustersRequest, dict]):
                The request object. The request for ``CloudVmCluster.List``.
            parent (str):
                Required. The name of the parent in
                the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListCloudVmClustersPager:
                The response for CloudVmCluster.List.

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
        if not isinstance(request, oracledatabase.ListCloudVmClustersRequest):
            request = oracledatabase.ListCloudVmClustersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_cloud_vm_clusters]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCloudVmClustersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_cloud_vm_cluster(
        self,
        request: Optional[Union[oracledatabase.GetCloudVmClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vm_cluster.CloudVmCluster:
        r"""Gets details of a single VM Cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_cloud_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetCloudVmClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_cloud_vm_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetCloudVmClusterRequest, dict]):
                The request object. The request for ``CloudVmCluster.Get``.
            name (str):
                Required. The name of the Cloud VM Cluster in the
                following format:
                projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.CloudVmCluster:
                Details of the Cloud VM Cluster
                resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudVmCluster/

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
        if not isinstance(request, oracledatabase.GetCloudVmClusterRequest):
            request = oracledatabase.GetCloudVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_cloud_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_cloud_vm_cluster(
        self,
        request: Optional[
            Union[oracledatabase.CreateCloudVmClusterRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        cloud_vm_cluster: Optional[vm_cluster.CloudVmCluster] = None,
        cloud_vm_cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new VM Cluster in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_cloud_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                cloud_vm_cluster = oracledatabase_v1.CloudVmCluster()
                cloud_vm_cluster.exadata_infrastructure = "exadata_infrastructure_value"

                request = oracledatabase_v1.CreateCloudVmClusterRequest(
                    parent="parent_value",
                    cloud_vm_cluster_id="cloud_vm_cluster_id_value",
                    cloud_vm_cluster=cloud_vm_cluster,
                )

                # Make the request
                operation = client.create_cloud_vm_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateCloudVmClusterRequest, dict]):
                The request object. The request for ``CloudVmCluster.Create``.
            parent (str):
                Required. The name of the parent in
                the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cloud_vm_cluster (google.cloud.oracledatabase_v1.types.CloudVmCluster):
                Required. The resource being created
                This corresponds to the ``cloud_vm_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cloud_vm_cluster_id (str):
                Required. The ID of the VM Cluster to create. This value
                is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``cloud_vm_cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.CloudVmCluster` Details of the Cloud VM Cluster resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudVmCluster/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, cloud_vm_cluster, cloud_vm_cluster_id]
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
        if not isinstance(request, oracledatabase.CreateCloudVmClusterRequest):
            request = oracledatabase.CreateCloudVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if cloud_vm_cluster is not None:
                request.cloud_vm_cluster = cloud_vm_cluster
            if cloud_vm_cluster_id is not None:
                request.cloud_vm_cluster_id = cloud_vm_cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_cloud_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            vm_cluster.CloudVmCluster,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_cloud_vm_cluster(
        self,
        request: Optional[
            Union[oracledatabase.DeleteCloudVmClusterRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single VM Cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_cloud_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteCloudVmClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_cloud_vm_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteCloudVmClusterRequest, dict]):
                The request object. The request for ``CloudVmCluster.Delete``.
            name (str):
                Required. The name of the Cloud VM Cluster in the
                following format:
                projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, oracledatabase.DeleteCloudVmClusterRequest):
            request = oracledatabase.DeleteCloudVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_cloud_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_entitlements(
        self,
        request: Optional[Union[oracledatabase.ListEntitlementsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEntitlementsPager:
        r"""Lists the entitlements in a given project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_entitlements():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListEntitlementsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entitlements(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListEntitlementsRequest, dict]):
                The request object. The request for ``Entitlement.List``.
            parent (str):
                Required. The parent value for the
                entitlement in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListEntitlementsPager:
                The response for Entitlement.List.

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
        if not isinstance(request, oracledatabase.ListEntitlementsRequest):
            request = oracledatabase.ListEntitlementsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_entitlements]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListEntitlementsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_db_servers(
        self,
        request: Optional[Union[oracledatabase.ListDbServersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDbServersPager:
        r"""Lists the database servers of an Exadata
        Infrastructure instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_db_servers():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDbServersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_db_servers(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDbServersRequest, dict]):
                The request object. The request for ``DbServer.List``.
            parent (str):
                Required. The parent value for
                database server in the following format:
                projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDbServersPager:
                The response for DbServer.List.

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
        if not isinstance(request, oracledatabase.ListDbServersRequest):
            request = oracledatabase.ListDbServersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_db_servers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDbServersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_db_nodes(
        self,
        request: Optional[Union[oracledatabase.ListDbNodesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDbNodesPager:
        r"""Lists the database nodes of a VM Cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_db_nodes():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDbNodesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_db_nodes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDbNodesRequest, dict]):
                The request object. The request for ``DbNode.List``.
            parent (str):
                Required. The parent value for
                database node in the following format:
                projects/{project}/locations/{location}/cloudVmClusters/{cloudVmCluster}.
                .

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDbNodesPager:
                The response for DbNode.List.

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
        if not isinstance(request, oracledatabase.ListDbNodesRequest):
            request = oracledatabase.ListDbNodesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_db_nodes]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDbNodesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_gi_versions(
        self,
        request: Optional[Union[oracledatabase.ListGiVersionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGiVersionsPager:
        r"""Lists all the valid Oracle Grid Infrastructure (GI)
        versions for the given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_gi_versions():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGiVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_gi_versions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGiVersionsRequest, dict]):
                The request object. The request for ``GiVersion.List``.
            parent (str):
                Required. The parent value for Grid
                Infrastructure Version in the following
                format: Format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGiVersionsPager:
                The response for GiVersion.List.

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
        if not isinstance(request, oracledatabase.ListGiVersionsRequest):
            request = oracledatabase.ListGiVersionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_gi_versions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGiVersionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_minor_versions(
        self,
        request: Optional[Union[minor_version.ListMinorVersionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMinorVersionsPager:
        r"""Lists all the valid minor versions for the given
        project, location, gi version and shape family.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_minor_versions():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListMinorVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_minor_versions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListMinorVersionsRequest, dict]):
                The request object. The request for ``MinorVersion.List``.
            parent (str):
                Required. The parent value for the MinorVersion resource
                with the format:
                projects/{project}/locations/{location}/giVersions/{gi_version}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListMinorVersionsPager:
                The response for MinorVersion.List.

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
        if not isinstance(request, minor_version.ListMinorVersionsRequest):
            request = minor_version.ListMinorVersionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_minor_versions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListMinorVersionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_db_system_shapes(
        self,
        request: Optional[Union[oracledatabase.ListDbSystemShapesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDbSystemShapesPager:
        r"""Lists the database system shapes available for the
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_db_system_shapes():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDbSystemShapesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_db_system_shapes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDbSystemShapesRequest, dict]):
                The request object. The request for ``DbSystemShape.List``.
            parent (str):
                Required. The parent value for
                Database System Shapes in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDbSystemShapesPager:
                The response for DbSystemShape.List.

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
        if not isinstance(request, oracledatabase.ListDbSystemShapesRequest):
            request = oracledatabase.ListDbSystemShapesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_db_system_shapes]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDbSystemShapesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_autonomous_databases(
        self,
        request: Optional[
            Union[oracledatabase.ListAutonomousDatabasesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAutonomousDatabasesPager:
        r"""Lists the Autonomous Databases in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_autonomous_databases():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListAutonomousDatabasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_autonomous_databases(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesRequest, dict]):
                The request object. The request for ``AutonomousDatabase.List``.
            parent (str):
                Required. The parent value for the
                Autonomous Database in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListAutonomousDatabasesPager:
                The response for AutonomousDatabase.List.

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
        if not isinstance(request, oracledatabase.ListAutonomousDatabasesRequest):
            request = oracledatabase.ListAutonomousDatabasesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_autonomous_databases
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAutonomousDatabasesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.GetAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> autonomous_database.AutonomousDatabase:
        r"""Gets the details of a single Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_autonomous_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Get``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.AutonomousDatabase:
                Details of the Autonomous Database
                resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

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
        if not isinstance(request, oracledatabase.GetAutonomousDatabaseRequest):
            request = oracledatabase.GetAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_autonomous_database]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.CreateAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        autonomous_database: Optional[
            gco_autonomous_database.AutonomousDatabase
        ] = None,
        autonomous_database_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new Autonomous Database in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.CreateAutonomousDatabaseRequest(
                    parent="parent_value",
                    autonomous_database_id="autonomous_database_id_value",
                )

                # Make the request
                operation = client.create_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Create``.
            parent (str):
                Required. The name of the parent in
                the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            autonomous_database (google.cloud.oracledatabase_v1.types.AutonomousDatabase):
                Required. The Autonomous Database
                being created.

                This corresponds to the ``autonomous_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            autonomous_database_id (str):
                Required. The ID of the Autonomous Database to create.
                This value is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``autonomous_database_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, autonomous_database, autonomous_database_id]
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
        if not isinstance(request, oracledatabase.CreateAutonomousDatabaseRequest):
            request = oracledatabase.CreateAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if autonomous_database is not None:
                request.autonomous_database = autonomous_database
            if autonomous_database_id is not None:
                request.autonomous_database_id = autonomous_database_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.UpdateAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        autonomous_database: Optional[
            gco_autonomous_database.AutonomousDatabase
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single Autonomous
        Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_update_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.UpdateAutonomousDatabaseRequest(
                )

                # Make the request
                operation = client.update_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.UpdateAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Update``.
            autonomous_database (google.cloud.oracledatabase_v1.types.AutonomousDatabase):
                Required. The resource being updated
                This corresponds to the ``autonomous_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the Exadata resource by the update. The
                fields specified in the update_mask are relative to the
                resource, not the full request. A field will be
                overwritten if it is in the mask. If the user does not
                provide a mask then all fields will be overwritten.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [autonomous_database, update_mask]
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
        if not isinstance(request, oracledatabase.UpdateAutonomousDatabaseRequest):
            request = oracledatabase.UpdateAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if autonomous_database is not None:
                request.autonomous_database = autonomous_database
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("autonomous_database.name", request.autonomous_database.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.DeleteAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Delete``.
            name (str):
                Required. The name of the resource in the following
                format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, oracledatabase.DeleteAutonomousDatabaseRequest):
            request = oracledatabase.DeleteAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def restore_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.RestoreAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        restore_time: Optional[timestamp_pb2.Timestamp] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Restores a single Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_restore_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.RestoreAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.restore_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.RestoreAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Restore``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            restore_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. The time and date to
                restore the database to.

                This corresponds to the ``restore_time`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, restore_time]
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
        if not isinstance(request, oracledatabase.RestoreAutonomousDatabaseRequest):
            request = oracledatabase.RestoreAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if restore_time is not None:
                request.restore_time = restore_time

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.restore_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def generate_autonomous_database_wallet(
        self,
        request: Optional[
            Union[oracledatabase.GenerateAutonomousDatabaseWalletRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        type_: Optional[autonomous_database.GenerateType] = None,
        is_regional: Optional[bool] = None,
        password: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> oracledatabase.GenerateAutonomousDatabaseWalletResponse:
        r"""Generates a wallet for an Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_generate_autonomous_database_wallet():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GenerateAutonomousDatabaseWalletRequest(
                    name="name_value",
                    password="password_value",
                )

                # Make the request
                response = client.generate_autonomous_database_wallet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GenerateAutonomousDatabaseWalletRequest, dict]):
                The request object. The request for ``AutonomousDatabase.GenerateWallet``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            type_ (google.cloud.oracledatabase_v1.types.GenerateType):
                Optional. The type of wallet
                generation for the Autonomous Database.
                The default value is SINGLE.

                This corresponds to the ``type_`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            is_regional (bool):
                Optional. True when requesting
                regional connection strings in PDB
                connect info, applicable to cross-region
                Data Guard only.

                This corresponds to the ``is_regional`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            password (str):
                Required. The password used to
                encrypt the keys inside the wallet. The
                password must be a minimum of 8
                characters.

                This corresponds to the ``password`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.GenerateAutonomousDatabaseWalletResponse:
                The response for AutonomousDatabase.GenerateWallet.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, type_, is_regional, password]
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
            request, oracledatabase.GenerateAutonomousDatabaseWalletRequest
        ):
            request = oracledatabase.GenerateAutonomousDatabaseWalletRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if type_ is not None:
                request.type_ = type_
            if is_regional is not None:
                request.is_regional = is_regional
            if password is not None:
                request.password = password

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_autonomous_database_wallet
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_autonomous_db_versions(
        self,
        request: Optional[
            Union[oracledatabase.ListAutonomousDbVersionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAutonomousDbVersionsPager:
        r"""Lists all the available Autonomous Database versions
        for a project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_autonomous_db_versions():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListAutonomousDbVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_autonomous_db_versions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsRequest, dict]):
                The request object. The request for ``AutonomousDbVersion.List``.
            parent (str):
                Required. The parent value for the
                Autonomous Database in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListAutonomousDbVersionsPager:
                The response for AutonomousDbVersion.List.

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
        if not isinstance(request, oracledatabase.ListAutonomousDbVersionsRequest):
            request = oracledatabase.ListAutonomousDbVersionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_autonomous_db_versions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAutonomousDbVersionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_autonomous_database_character_sets(
        self,
        request: Optional[
            Union[oracledatabase.ListAutonomousDatabaseCharacterSetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAutonomousDatabaseCharacterSetsPager:
        r"""Lists Autonomous Database Character Sets in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_autonomous_database_character_sets():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListAutonomousDatabaseCharacterSetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_autonomous_database_character_sets(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsRequest, dict]):
                The request object. The request for ``AutonomousDatabaseCharacterSet.List``.
            parent (str):
                Required. The parent value for the
                Autonomous Database in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListAutonomousDatabaseCharacterSetsPager:
                The response for AutonomousDatabaseCharacterSet.List.

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
            request, oracledatabase.ListAutonomousDatabaseCharacterSetsRequest
        ):
            request = oracledatabase.ListAutonomousDatabaseCharacterSetsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_autonomous_database_character_sets
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAutonomousDatabaseCharacterSetsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_autonomous_database_backups(
        self,
        request: Optional[
            Union[oracledatabase.ListAutonomousDatabaseBackupsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAutonomousDatabaseBackupsPager:
        r"""Lists the long-term and automatic backups of an
        Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_autonomous_database_backups():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListAutonomousDatabaseBackupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_autonomous_database_backups(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsRequest, dict]):
                The request object. The request for ``AutonomousDatabaseBackup.List``.
            parent (str):
                Required. The parent value for
                ListAutonomousDatabaseBackups in the
                following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListAutonomousDatabaseBackupsPager:
                The response for AutonomousDatabaseBackup.List.

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
        if not isinstance(request, oracledatabase.ListAutonomousDatabaseBackupsRequest):
            request = oracledatabase.ListAutonomousDatabaseBackupsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_autonomous_database_backups
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAutonomousDatabaseBackupsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def stop_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.StopAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Stops an Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_stop_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.StopAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.stop_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.StopAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Stop``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

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
        if not isinstance(request, oracledatabase.StopAutonomousDatabaseRequest):
            request = oracledatabase.StopAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.stop_autonomous_database]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def start_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.StartAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Starts an Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_start_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.StartAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.start_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.StartAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Start``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

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
        if not isinstance(request, oracledatabase.StartAutonomousDatabaseRequest):
            request = oracledatabase.StartAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.start_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def restart_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.RestartAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Restarts an Autonomous Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_restart_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.RestartAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.restart_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.RestartAutonomousDatabaseRequest, dict]):
                The request object. The request for ``AutonomousDatabase.Restart``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

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
        if not isinstance(request, oracledatabase.RestartAutonomousDatabaseRequest):
            request = oracledatabase.RestartAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.restart_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def switchover_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.SwitchoverAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        peer_autonomous_database: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Initiates a switchover of specified autonomous
        database to the associated peer database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_switchover_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.SwitchoverAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.switchover_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.SwitchoverAutonomousDatabaseRequest, dict]):
                The request object. The request for
                ``OracleDatabase.SwitchoverAutonomousDatabase``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            peer_autonomous_database (str):
                Optional. The peer database name to
                switch over to. Required for
                cross-region standby, and must be
                omitted for in-region Data Guard.

                This corresponds to the ``peer_autonomous_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, peer_autonomous_database]
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
        if not isinstance(request, oracledatabase.SwitchoverAutonomousDatabaseRequest):
            request = oracledatabase.SwitchoverAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if peer_autonomous_database is not None:
                request.peer_autonomous_database = peer_autonomous_database

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.switchover_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def failover_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.FailoverAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        peer_autonomous_database: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Initiates a failover to target autonomous database
        from the associated primary database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_failover_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.FailoverAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.failover_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.FailoverAutonomousDatabaseRequest, dict]):
                The request object. The request for
                ``OracleDatabase.FailoverAutonomousDatabase``.
            name (str):
                Required. The name of the Autonomous Database in the
                following format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            peer_autonomous_database (str):
                Optional. The peer database name to
                fail over to. Required for cross-region
                standby, and must be omitted for
                in-region Data Guard.

                This corresponds to the ``peer_autonomous_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, peer_autonomous_database]
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
        if not isinstance(request, oracledatabase.FailoverAutonomousDatabaseRequest):
            request = oracledatabase.FailoverAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if peer_autonomous_database is not None:
                request.peer_autonomous_database = peer_autonomous_database

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.failover_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def refresh_autonomous_database(
        self,
        request: Optional[
            Union[oracledatabase.RefreshAutonomousDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        refresh_cutoff_time: Optional[timestamp_pb2.Timestamp] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Refreshes the refreshable clone of an Autonomous
        Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_refresh_autonomous_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.RefreshAutonomousDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.refresh_autonomous_database(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.RefreshAutonomousDatabaseRequest, dict]):
                The request object. Request message for
                RefreshAutonomousDatabase method.
            name (str):
                Required. The name of the AutonomousDatabase resource.
                Format:
                projects/{project}/location/{location}/autonomousDatabases/{autonomous_database}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            refresh_cutoff_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. The timestamp to which the
                Autonomous Database refreshable clone
                will be refreshed. Changes made in the
                primary database after this timestamp
                are not part of the data refresh.

                This corresponds to the ``refresh_cutoff_time`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.AutonomousDatabase` Details of the Autonomous Database resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, refresh_cutoff_time]
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
        if not isinstance(request, oracledatabase.RefreshAutonomousDatabaseRequest):
            request = oracledatabase.RefreshAutonomousDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if refresh_cutoff_time is not None:
                request.refresh_cutoff_time = refresh_cutoff_time

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.refresh_autonomous_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            autonomous_database.AutonomousDatabase,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_autonomous_database_refreshable_clones(
        self,
        request: Optional[
            Union[oracledatabase.GetAutonomousDatabaseRefreshableClonesRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> oracledatabase.AutonomousDatabaseRefreshableClones:
        r"""Gets the refreshable clones for a given Autonomous
        Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_autonomous_database_refreshable_clones():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetAutonomousDatabaseRefreshableClonesRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_autonomous_database_refreshable_clones(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetAutonomousDatabaseRefreshableClonesRequest, dict]):
                The request object. Request message for getting
                refreshable clones for an Autonomous
                Database.
            name (str):
                Required. The Autonomous Database resource whose
                refreshable clones are to be listed. Format:
                projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.AutonomousDatabaseRefreshableClones:
                Response message for getting the
                Autonomous Database refreshable clones.

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
            request, oracledatabase.GetAutonomousDatabaseRefreshableClonesRequest
        ):
            request = oracledatabase.GetAutonomousDatabaseRefreshableClonesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_autonomous_database_refreshable_clones
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_odb_networks(
        self,
        request: Optional[Union[odb_network.ListOdbNetworksRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOdbNetworksPager:
        r"""Lists the ODB Networks in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_odb_networks():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListOdbNetworksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_odb_networks(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListOdbNetworksRequest, dict]):
                The request object. The request for ``OdbNetwork.List``.
            parent (str):
                Required. The parent value for the
                ODB Network in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListOdbNetworksPager:
                The response for OdbNetwork.List.

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
        if not isinstance(request, odb_network.ListOdbNetworksRequest):
            request = odb_network.ListOdbNetworksRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_odb_networks]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListOdbNetworksPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_odb_network(
        self,
        request: Optional[Union[odb_network.GetOdbNetworkRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> odb_network.OdbNetwork:
        r"""Gets details of a single ODB Network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_odb_network():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetOdbNetworkRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_odb_network(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetOdbNetworkRequest, dict]):
                The request object. The request for ``OdbNetwork.Get``.
            name (str):
                Required. The name of the OdbNetwork in the following
                format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.OdbNetwork:
                Represents OdbNetwork resource.
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
        if not isinstance(request, odb_network.GetOdbNetworkRequest):
            request = odb_network.GetOdbNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_odb_network]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_odb_network(
        self,
        request: Optional[Union[gco_odb_network.CreateOdbNetworkRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        odb_network: Optional[gco_odb_network.OdbNetwork] = None,
        odb_network_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ODB Network in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_odb_network():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                odb_network = oracledatabase_v1.OdbNetwork()
                odb_network.network = "network_value"

                request = oracledatabase_v1.CreateOdbNetworkRequest(
                    parent="parent_value",
                    odb_network_id="odb_network_id_value",
                    odb_network=odb_network,
                )

                # Make the request
                operation = client.create_odb_network(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateOdbNetworkRequest, dict]):
                The request object. The request for ``OdbNetwork.Create``.
            parent (str):
                Required. The parent value for the
                OdbNetwork in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            odb_network (google.cloud.oracledatabase_v1.types.OdbNetwork):
                Required. Details of the OdbNetwork
                instance to create.

                This corresponds to the ``odb_network`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            odb_network_id (str):
                Required. The ID of the OdbNetwork to create. This value
                is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``odb_network_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.OdbNetwork`
                Represents OdbNetwork resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, odb_network, odb_network_id]
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
        if not isinstance(request, gco_odb_network.CreateOdbNetworkRequest):
            request = gco_odb_network.CreateOdbNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if odb_network is not None:
                request.odb_network = odb_network
            if odb_network_id is not None:
                request.odb_network_id = odb_network_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_odb_network]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_odb_network.OdbNetwork,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_odb_network(
        self,
        request: Optional[Union[odb_network.DeleteOdbNetworkRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single ODB Network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_odb_network():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteOdbNetworkRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_odb_network(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteOdbNetworkRequest, dict]):
                The request object. The request for ``OdbNetwork.Delete``.
            name (str):
                Required. The name of the resource in the following
                format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, odb_network.DeleteOdbNetworkRequest):
            request = odb_network.DeleteOdbNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_odb_network]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_odb_subnets(
        self,
        request: Optional[Union[odb_subnet.ListOdbSubnetsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOdbSubnetsPager:
        r"""Lists all the ODB Subnets in a given ODB Network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_odb_subnets():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListOdbSubnetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_odb_subnets(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListOdbSubnetsRequest, dict]):
                The request object. The request for ``OdbSubnet.List``.
            parent (str):
                Required. The parent value for the OdbSubnet in the
                following format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListOdbSubnetsPager:
                The response for OdbSubnet.List.

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
        if not isinstance(request, odb_subnet.ListOdbSubnetsRequest):
            request = odb_subnet.ListOdbSubnetsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_odb_subnets]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListOdbSubnetsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_odb_subnet(
        self,
        request: Optional[Union[odb_subnet.GetOdbSubnetRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> odb_subnet.OdbSubnet:
        r"""Gets details of a single ODB Subnet.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_odb_subnet():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetOdbSubnetRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_odb_subnet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetOdbSubnetRequest, dict]):
                The request object. The request for ``OdbSubnet.Get``.
            name (str):
                Required. The name of the OdbSubnet in the following
                format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.OdbSubnet:
                Represents OdbSubnet resource.
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
        if not isinstance(request, odb_subnet.GetOdbSubnetRequest):
            request = odb_subnet.GetOdbSubnetRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_odb_subnet]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_odb_subnet(
        self,
        request: Optional[Union[gco_odb_subnet.CreateOdbSubnetRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        odb_subnet: Optional[gco_odb_subnet.OdbSubnet] = None,
        odb_subnet_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ODB Subnet in a given ODB Network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_odb_subnet():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                odb_subnet = oracledatabase_v1.OdbSubnet()
                odb_subnet.cidr_range = "cidr_range_value"
                odb_subnet.purpose = "BACKUP_SUBNET"

                request = oracledatabase_v1.CreateOdbSubnetRequest(
                    parent="parent_value",
                    odb_subnet_id="odb_subnet_id_value",
                    odb_subnet=odb_subnet,
                )

                # Make the request
                operation = client.create_odb_subnet(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateOdbSubnetRequest, dict]):
                The request object. The request for ``OdbSubnet.Create``.
            parent (str):
                Required. The parent value for the OdbSubnet in the
                following format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            odb_subnet (google.cloud.oracledatabase_v1.types.OdbSubnet):
                Required. Details of the OdbSubnet
                instance to create.

                This corresponds to the ``odb_subnet`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            odb_subnet_id (str):
                Required. The ID of the OdbSubnet to create. This value
                is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``odb_subnet_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.OdbSubnet`
                Represents OdbSubnet resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, odb_subnet, odb_subnet_id]
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
        if not isinstance(request, gco_odb_subnet.CreateOdbSubnetRequest):
            request = gco_odb_subnet.CreateOdbSubnetRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if odb_subnet is not None:
                request.odb_subnet = odb_subnet
            if odb_subnet_id is not None:
                request.odb_subnet_id = odb_subnet_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_odb_subnet]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_odb_subnet.OdbSubnet,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_odb_subnet(
        self,
        request: Optional[Union[odb_subnet.DeleteOdbSubnetRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single ODB Subnet.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_odb_subnet():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteOdbSubnetRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_odb_subnet(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteOdbSubnetRequest, dict]):
                The request object. The request for ``OdbSubnet.Delete``.
            name (str):
                Required. The name of the resource in the following
                format:
                projects/{project}/locations/{region}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, odb_subnet.DeleteOdbSubnetRequest):
            request = odb_subnet.DeleteOdbSubnetRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_odb_subnet]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_odb_dns_zones(
        self,
        request: Optional[Union[odb_dns_zone.ListOdbDnsZonesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOdbDnsZonesPager:
        r"""Lists all the ODB DNS Zones in a given ODB Network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_odb_dns_zones():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListOdbDnsZonesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_odb_dns_zones(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListOdbDnsZonesRequest, dict]):
                The request object. The request for ``OdbDnsZone.List``.
            parent (str):
                Required. The parent value for the OdbDnsZone in the
                following format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListOdbDnsZonesPager:
                The response for OdbDnsZone.List.

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
        if not isinstance(request, odb_dns_zone.ListOdbDnsZonesRequest):
            request = odb_dns_zone.ListOdbDnsZonesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_odb_dns_zones]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListOdbDnsZonesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_odb_dns_zone(
        self,
        request: Optional[Union[odb_dns_zone.GetOdbDnsZoneRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> odb_dns_zone.OdbDnsZone:
        r"""Gets details of a single ODB DNS Zone.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_odb_dns_zone():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetOdbDnsZoneRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_odb_dns_zone(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetOdbDnsZoneRequest, dict]):
                The request object. The request for ``OdbDnsZone.Get``.
            name (str):
                Required. The name of the OdbDnsZone in the following
                format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.OdbDnsZone:
                Represents OdbDnsZone resource.
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
        if not isinstance(request, odb_dns_zone.GetOdbDnsZoneRequest):
            request = odb_dns_zone.GetOdbDnsZoneRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_odb_dns_zone]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_odb_dns_zone(
        self,
        request: Optional[Union[gco_odb_dns_zone.CreateOdbDnsZoneRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        odb_dns_zone: Optional[gco_odb_dns_zone.OdbDnsZone] = None,
        odb_dns_zone_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ODB DNS Zone in a given ODB Network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_odb_dns_zone():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                odb_dns_zone = oracledatabase_v1.OdbDnsZone()
                odb_dns_zone.domain = "domain_value"

                request = oracledatabase_v1.CreateOdbDnsZoneRequest(
                    parent="parent_value",
                    odb_dns_zone_id="odb_dns_zone_id_value",
                    odb_dns_zone=odb_dns_zone,
                )

                # Make the request
                operation = client.create_odb_dns_zone(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateOdbDnsZoneRequest, dict]):
                The request object. The request for ``OdbDnsZone.Create``.
            parent (str):
                Required. The parent value for the OdbDnsZone in the
                following format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            odb_dns_zone (google.cloud.oracledatabase_v1.types.OdbDnsZone):
                Required. Details of the OdbDnsZone
                instance to create.

                This corresponds to the ``odb_dns_zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            odb_dns_zone_id (str):
                Required. The ID of the OdbDnsZone to create. This value
                is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``odb_dns_zone_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.OdbDnsZone`
                Represents OdbDnsZone resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, odb_dns_zone, odb_dns_zone_id]
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
        if not isinstance(request, gco_odb_dns_zone.CreateOdbDnsZoneRequest):
            request = gco_odb_dns_zone.CreateOdbDnsZoneRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if odb_dns_zone is not None:
                request.odb_dns_zone = odb_dns_zone
            if odb_dns_zone_id is not None:
                request.odb_dns_zone_id = odb_dns_zone_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_odb_dns_zone]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_odb_dns_zone.OdbDnsZone,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_odb_dns_zone(
        self,
        request: Optional[Union[odb_dns_zone.DeleteOdbDnsZoneRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single ODB DNS Zone.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_odb_dns_zone():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteOdbDnsZoneRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_odb_dns_zone(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteOdbDnsZoneRequest, dict]):
                The request object. The request for ``OdbDnsZone.Delete``.
            name (str):
                Required. The name of the resource in the following
                format:
                projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, odb_dns_zone.DeleteOdbDnsZoneRequest):
            request = odb_dns_zone.DeleteOdbDnsZoneRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_odb_dns_zone]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_exadb_vm_clusters(
        self,
        request: Optional[
            Union[oracledatabase.ListExadbVmClustersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListExadbVmClustersPager:
        r"""Lists all the Exadb (Exascale) VM Clusters for the
        given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_exadb_vm_clusters():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListExadbVmClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_exadb_vm_clusters(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListExadbVmClustersRequest, dict]):
                The request object. The request for ``ExadbVmCluster.List``.
            parent (str):
                Required. The parent value for
                ExadbVmClusters in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListExadbVmClustersPager:
                The response for ExadbVmCluster.List.

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
        if not isinstance(request, oracledatabase.ListExadbVmClustersRequest):
            request = oracledatabase.ListExadbVmClustersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_exadb_vm_clusters]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListExadbVmClustersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_exadb_vm_cluster(
        self,
        request: Optional[Union[oracledatabase.GetExadbVmClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> exadb_vm_cluster.ExadbVmCluster:
        r"""Gets details of a single Exadb (Exascale) VM Cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_exadb_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetExadbVmClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_exadb_vm_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetExadbVmClusterRequest, dict]):
                The request object. The request for ``ExadbVmCluster.Get``.
            name (str):
                Required. The name of the ExadbVmCluster in the
                following format:
                projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.ExadbVmCluster:
                ExadbVmCluster represents a cluster
                of VMs that are used to run Exadata
                workloads.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/

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
        if not isinstance(request, oracledatabase.GetExadbVmClusterRequest):
            request = oracledatabase.GetExadbVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_exadb_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_exadb_vm_cluster(
        self,
        request: Optional[
            Union[oracledatabase.CreateExadbVmClusterRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        exadb_vm_cluster: Optional[gco_exadb_vm_cluster.ExadbVmCluster] = None,
        exadb_vm_cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new Exadb (Exascale) VM Cluster resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_exadb_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                exadb_vm_cluster = oracledatabase_v1.ExadbVmCluster()
                exadb_vm_cluster.properties.grid_image_id = "grid_image_id_value"
                exadb_vm_cluster.properties.node_count = 1070
                exadb_vm_cluster.properties.enabled_ecpu_count_per_node = 2826
                exadb_vm_cluster.properties.vm_file_system_storage.size_in_gbs_per_node = 2103
                exadb_vm_cluster.properties.exascale_db_storage_vault = "exascale_db_storage_vault_value"
                exadb_vm_cluster.properties.hostname_prefix = "hostname_prefix_value"
                exadb_vm_cluster.properties.ssh_public_keys = ['ssh_public_keys_value1', 'ssh_public_keys_value2']
                exadb_vm_cluster.properties.shape_attribute = "BLOCK_STORAGE"
                exadb_vm_cluster.odb_subnet = "odb_subnet_value"
                exadb_vm_cluster.backup_odb_subnet = "backup_odb_subnet_value"
                exadb_vm_cluster.display_name = "display_name_value"

                request = oracledatabase_v1.CreateExadbVmClusterRequest(
                    parent="parent_value",
                    exadb_vm_cluster_id="exadb_vm_cluster_id_value",
                    exadb_vm_cluster=exadb_vm_cluster,
                )

                # Make the request
                operation = client.create_exadb_vm_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateExadbVmClusterRequest, dict]):
                The request object. The request for ``ExadbVmCluster.Create``.
            parent (str):
                Required. The value for parent of the
                ExadbVmCluster in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            exadb_vm_cluster (google.cloud.oracledatabase_v1.types.ExadbVmCluster):
                Required. The resource being created.
                This corresponds to the ``exadb_vm_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            exadb_vm_cluster_id (str):
                Required. The ID of the ExadbVmCluster to create. This
                value is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``exadb_vm_cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.ExadbVmCluster` ExadbVmCluster represents a cluster of VMs that are used to run Exadata
                   workloads.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, exadb_vm_cluster, exadb_vm_cluster_id]
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
        if not isinstance(request, oracledatabase.CreateExadbVmClusterRequest):
            request = oracledatabase.CreateExadbVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if exadb_vm_cluster is not None:
                request.exadb_vm_cluster = exadb_vm_cluster
            if exadb_vm_cluster_id is not None:
                request.exadb_vm_cluster_id = exadb_vm_cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_exadb_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_exadb_vm_cluster.ExadbVmCluster,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_exadb_vm_cluster(
        self,
        request: Optional[
            Union[oracledatabase.DeleteExadbVmClusterRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single Exadb (Exascale) VM Cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_exadb_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteExadbVmClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_exadb_vm_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteExadbVmClusterRequest, dict]):
                The request object. The request for ``ExadbVmCluster.Delete``.
            name (str):
                Required. The name of the ExadbVmCluster in the
                following format:
                projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, oracledatabase.DeleteExadbVmClusterRequest):
            request = oracledatabase.DeleteExadbVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_exadb_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_exadb_vm_cluster(
        self,
        request: Optional[
            Union[oracledatabase.UpdateExadbVmClusterRequest, dict]
        ] = None,
        *,
        exadb_vm_cluster: Optional[gco_exadb_vm_cluster.ExadbVmCluster] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates a single Exadb (Exascale) VM Cluster. To add
        virtual machines to existing exadb vm cluster, only pass
        the node count.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_update_exadb_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                exadb_vm_cluster = oracledatabase_v1.ExadbVmCluster()
                exadb_vm_cluster.properties.grid_image_id = "grid_image_id_value"
                exadb_vm_cluster.properties.node_count = 1070
                exadb_vm_cluster.properties.enabled_ecpu_count_per_node = 2826
                exadb_vm_cluster.properties.vm_file_system_storage.size_in_gbs_per_node = 2103
                exadb_vm_cluster.properties.exascale_db_storage_vault = "exascale_db_storage_vault_value"
                exadb_vm_cluster.properties.hostname_prefix = "hostname_prefix_value"
                exadb_vm_cluster.properties.ssh_public_keys = ['ssh_public_keys_value1', 'ssh_public_keys_value2']
                exadb_vm_cluster.properties.shape_attribute = "BLOCK_STORAGE"
                exadb_vm_cluster.odb_subnet = "odb_subnet_value"
                exadb_vm_cluster.backup_odb_subnet = "backup_odb_subnet_value"
                exadb_vm_cluster.display_name = "display_name_value"

                request = oracledatabase_v1.UpdateExadbVmClusterRequest(
                    exadb_vm_cluster=exadb_vm_cluster,
                )

                # Make the request
                operation = client.update_exadb_vm_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.UpdateExadbVmClusterRequest, dict]):
                The request object. The request for ``ExadbVmCluster.Update``. We only
                support adding the Virtual Machine to the
                ExadbVmCluster. Rest of the fields in ExadbVmCluster are
                immutable.
            exadb_vm_cluster (google.cloud.oracledatabase_v1.types.ExadbVmCluster):
                Required. The resource being updated.
                This corresponds to the ``exadb_vm_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. A mask specifying which
                fields in th VM Cluster should be
                updated. A field specified in the mask
                is overwritten. If a mask isn't provided
                then all the fields in the VM Cluster
                are overwritten.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.ExadbVmCluster` ExadbVmCluster represents a cluster of VMs that are used to run Exadata
                   workloads.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [exadb_vm_cluster, update_mask]
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
        if not isinstance(request, oracledatabase.UpdateExadbVmClusterRequest):
            request = oracledatabase.UpdateExadbVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if exadb_vm_cluster is not None:
                request.exadb_vm_cluster = exadb_vm_cluster
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_exadb_vm_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("exadb_vm_cluster.name", request.exadb_vm_cluster.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_exadb_vm_cluster.ExadbVmCluster,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def remove_virtual_machine_exadb_vm_cluster(
        self,
        request: Optional[
            Union[oracledatabase.RemoveVirtualMachineExadbVmClusterRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        hostnames: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Removes virtual machines from an existing exadb vm
        cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_remove_virtual_machine_exadb_vm_cluster():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.RemoveVirtualMachineExadbVmClusterRequest(
                    name="name_value",
                    hostnames=['hostnames_value1', 'hostnames_value2'],
                )

                # Make the request
                operation = client.remove_virtual_machine_exadb_vm_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.RemoveVirtualMachineExadbVmClusterRequest, dict]):
                The request object. The request for ``ExadbVmCluster.RemoveVirtualMachine``.
            name (str):
                Required. The name of the ExadbVmCluster in the
                following format:
                projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hostnames (MutableSequence[str]):
                Required. The list of host names of
                db nodes to be removed from the
                ExadbVmCluster.

                This corresponds to the ``hostnames`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.ExadbVmCluster` ExadbVmCluster represents a cluster of VMs that are used to run Exadata
                   workloads.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, hostnames]
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
            request, oracledatabase.RemoveVirtualMachineExadbVmClusterRequest
        ):
            request = oracledatabase.RemoveVirtualMachineExadbVmClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if hostnames is not None:
                request.hostnames = hostnames

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.remove_virtual_machine_exadb_vm_cluster
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            exadb_vm_cluster.ExadbVmCluster,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_exascale_db_storage_vaults(
        self,
        request: Optional[
            Union[exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListExascaleDbStorageVaultsPager:
        r"""Lists all the ExascaleDB Storage Vaults for the given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_exascale_db_storage_vaults():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListExascaleDbStorageVaultsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_exascale_db_storage_vaults(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsRequest, dict]):
                The request object. The request for ``ExascaleDbStorageVault.List``.
            parent (str):
                Required. The parent value for
                ExascaleDbStorageVault in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListExascaleDbStorageVaultsPager:
                The response for ExascaleDbStorageVault.List.

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
            request, exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest
        ):
            request = exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_exascale_db_storage_vaults
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListExascaleDbStorageVaultsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_exascale_db_storage_vault(
        self,
        request: Optional[
            Union[exascale_db_storage_vault.GetExascaleDbStorageVaultRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> exascale_db_storage_vault.ExascaleDbStorageVault:
        r"""Gets details of a single ExascaleDB Storage Vault.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_exascale_db_storage_vault():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetExascaleDbStorageVaultRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_exascale_db_storage_vault(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetExascaleDbStorageVaultRequest, dict]):
                The request object. The request for ``ExascaleDbStorageVault.Get``.
            name (str):
                Required. The name of the ExascaleDbStorageVault in the
                following format:
                projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.ExascaleDbStorageVault:
                ExascaleDbStorageVault represents a
                storage vault exadb vm cluster resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExascaleDbStorageVault/

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
            request, exascale_db_storage_vault.GetExascaleDbStorageVaultRequest
        ):
            request = exascale_db_storage_vault.GetExascaleDbStorageVaultRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_exascale_db_storage_vault
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_exascale_db_storage_vault(
        self,
        request: Optional[
            Union[
                gco_exascale_db_storage_vault.CreateExascaleDbStorageVaultRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        exascale_db_storage_vault: Optional[
            gco_exascale_db_storage_vault.ExascaleDbStorageVault
        ] = None,
        exascale_db_storage_vault_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ExascaleDB Storage Vault resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_exascale_db_storage_vault():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                exascale_db_storage_vault = oracledatabase_v1.ExascaleDbStorageVault()
                exascale_db_storage_vault.display_name = "display_name_value"
                exascale_db_storage_vault.properties.exascale_db_storage_details.total_size_gbs = 1497

                request = oracledatabase_v1.CreateExascaleDbStorageVaultRequest(
                    parent="parent_value",
                    exascale_db_storage_vault_id="exascale_db_storage_vault_id_value",
                    exascale_db_storage_vault=exascale_db_storage_vault,
                )

                # Make the request
                operation = client.create_exascale_db_storage_vault(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateExascaleDbStorageVaultRequest, dict]):
                The request object. The request for ``ExascaleDbStorageVault.Create``.
            parent (str):
                Required. The value for parent of the
                ExascaleDbStorageVault in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            exascale_db_storage_vault (google.cloud.oracledatabase_v1.types.ExascaleDbStorageVault):
                Required. The resource being created.
                This corresponds to the ``exascale_db_storage_vault`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            exascale_db_storage_vault_id (str):
                Required. The ID of the ExascaleDbStorageVault to
                create. This value is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``exascale_db_storage_vault_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.ExascaleDbStorageVault` ExascaleDbStorageVault represents a storage vault exadb vm cluster resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExascaleDbStorageVault/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            exascale_db_storage_vault,
            exascale_db_storage_vault_id,
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
            request, gco_exascale_db_storage_vault.CreateExascaleDbStorageVaultRequest
        ):
            request = gco_exascale_db_storage_vault.CreateExascaleDbStorageVaultRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if exascale_db_storage_vault is not None:
                request.exascale_db_storage_vault = exascale_db_storage_vault
            if exascale_db_storage_vault_id is not None:
                request.exascale_db_storage_vault_id = exascale_db_storage_vault_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_exascale_db_storage_vault
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_exascale_db_storage_vault.ExascaleDbStorageVault,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_exascale_db_storage_vault(
        self,
        request: Optional[
            Union[exascale_db_storage_vault.DeleteExascaleDbStorageVaultRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single ExascaleDB Storage Vault.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_exascale_db_storage_vault():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteExascaleDbStorageVaultRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_exascale_db_storage_vault(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteExascaleDbStorageVaultRequest, dict]):
                The request object. The request message for
                ``ExascaleDbStorageVault.Delete``.
            name (str):
                Required. The name of the ExascaleDbStorageVault in the
                following format:
                projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
            request, exascale_db_storage_vault.DeleteExascaleDbStorageVaultRequest
        ):
            request = exascale_db_storage_vault.DeleteExascaleDbStorageVaultRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_exascale_db_storage_vault
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_db_system_initial_storage_sizes(
        self,
        request: Optional[
            Union[
                db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDbSystemInitialStorageSizesPager:
        r"""Lists all the DbSystemInitialStorageSizes for the
        given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_db_system_initial_storage_sizes():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDbSystemInitialStorageSizesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_db_system_initial_storage_sizes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesRequest, dict]):
                The request object. The request for ``DbSystemInitialStorageSizes.List``.
            parent (str):
                Required. The parent value for the
                DbSystemInitialStorageSize resource with
                the format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDbSystemInitialStorageSizesPager:
                The response for DbSystemInitialStorageSizes.List.

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
            request,
            db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest,
        ):
            request = (
                db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_db_system_initial_storage_sizes
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDbSystemInitialStorageSizesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_databases(
        self,
        request: Optional[Union[database.ListDatabasesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDatabasesPager:
        r"""Lists all the Databases for the given project,
        location and DbSystem.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_databases():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDatabasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_databases(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDatabasesRequest, dict]):
                The request object. The request for ``Database.List``.
            parent (str):
                Required. The parent resource name in
                the following format:
                projects/{project}/locations/{region}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDatabasesPager:
                The response for Database.List.

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
        if not isinstance(request, database.ListDatabasesRequest):
            request = database.ListDatabasesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_databases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDatabasesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_database(
        self,
        request: Optional[Union[database.GetDatabaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> database.Database:
        r"""Gets details of a single Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetDatabaseRequest, dict]):
                The request object. The request for ``Database.Get``.
            name (str):
                Required. The name of the Database
                resource in the following format:
                projects/{project}/locations/{region}/databases/{database}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.Database:
                Details of the Database resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/Database/

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
        if not isinstance(request, database.GetDatabaseRequest):
            request = database.GetDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_database]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_pluggable_databases(
        self,
        request: Optional[
            Union[pluggable_database.ListPluggableDatabasesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPluggableDatabasesPager:
        r"""Lists all the PluggableDatabases for the given
        project, location and Container Database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_pluggable_databases():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListPluggableDatabasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_pluggable_databases(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListPluggableDatabasesRequest, dict]):
                The request object. The request for ``PluggableDatabase.List``.
            parent (str):
                Required. The parent, which owns this
                collection of PluggableDatabases.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListPluggableDatabasesPager:
                The response for PluggableDatabase.List.

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
        if not isinstance(request, pluggable_database.ListPluggableDatabasesRequest):
            request = pluggable_database.ListPluggableDatabasesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_pluggable_databases]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPluggableDatabasesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_pluggable_database(
        self,
        request: Optional[
            Union[pluggable_database.GetPluggableDatabaseRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pluggable_database.PluggableDatabase:
        r"""Gets details of a single PluggableDatabase.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_pluggable_database():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetPluggableDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_pluggable_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetPluggableDatabaseRequest, dict]):
                The request object. The request for ``PluggableDatabase.Get``.
            name (str):
                Required. The name of the PluggableDatabase resource in
                the following format:
                projects/{project}/locations/{region}/pluggableDatabases/{pluggable_database}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.PluggableDatabase:
                The PluggableDatabase resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/PluggableDatabase/

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
        if not isinstance(request, pluggable_database.GetPluggableDatabaseRequest):
            request = pluggable_database.GetPluggableDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_pluggable_database]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_db_systems(
        self,
        request: Optional[Union[db_system.ListDbSystemsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDbSystemsPager:
        r"""Lists all the DbSystems for the given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_db_systems():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDbSystemsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_db_systems(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDbSystemsRequest, dict]):
                The request object. The request for ``DbSystem.List``.
            parent (str):
                Required. The parent value for
                DbSystems in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDbSystemsPager:
                The response for DbSystem.List.

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
        if not isinstance(request, db_system.ListDbSystemsRequest):
            request = db_system.ListDbSystemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_db_systems]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDbSystemsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_db_system(
        self,
        request: Optional[Union[db_system.GetDbSystemRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> db_system.DbSystem:
        r"""Gets details of a single DbSystem.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_db_system():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetDbSystemRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_db_system(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetDbSystemRequest, dict]):
                The request object. The request for ``DbSystem.Get``.
            name (str):
                Required. The name of the DbSystem in the following
                format:
                projects/{project}/locations/{location}/dbSystems/{db_system}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.DbSystem:
                Details of the DbSystem (BaseDB)
                resource.
                https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystem/

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
        if not isinstance(request, db_system.GetDbSystemRequest):
            request = db_system.GetDbSystemRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_db_system]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_db_system(
        self,
        request: Optional[Union[gco_db_system.CreateDbSystemRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        db_system: Optional[gco_db_system.DbSystem] = None,
        db_system_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new DbSystem in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_db_system():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                db_system = oracledatabase_v1.DbSystem()
                db_system.odb_subnet = "odb_subnet_value"
                db_system.display_name = "display_name_value"

                request = oracledatabase_v1.CreateDbSystemRequest(
                    parent="parent_value",
                    db_system_id="db_system_id_value",
                    db_system=db_system,
                )

                # Make the request
                operation = client.create_db_system(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateDbSystemRequest, dict]):
                The request object. The request for ``DbSystem.Create``.
            parent (str):
                Required. The value for parent of the
                DbSystem in the following format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            db_system (google.cloud.oracledatabase_v1.types.DbSystem):
                Required. The resource being created.
                This corresponds to the ``db_system`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            db_system_id (str):
                Required. The ID of the DbSystem to create. This value
                is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``db_system_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.oracledatabase_v1.types.DbSystem` Details of the DbSystem (BaseDB) resource.
                   https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystem/

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, db_system, db_system_id]
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
        if not isinstance(request, gco_db_system.CreateDbSystemRequest):
            request = gco_db_system.CreateDbSystemRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if db_system is not None:
                request.db_system = db_system
            if db_system_id is not None:
                request.db_system_id = db_system_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_db_system]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_db_system.DbSystem,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_db_system(
        self,
        request: Optional[Union[db_system.DeleteDbSystemRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single DbSystem.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_db_system():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteDbSystemRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_db_system(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteDbSystemRequest, dict]):
                The request object. The request for ``DbSystem.Delete``.
            name (str):
                Required. The name of the DbSystem in the following
                format:
                projects/{project}/locations/{location}/dbSystems/{db_system}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
        if not isinstance(request, db_system.DeleteDbSystemRequest):
            request = db_system.DeleteDbSystemRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_db_system]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_deployments(
        self,
        request: Optional[
            Union[goldengate_deployment.ListGoldengateDeploymentsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateDeploymentsPager:
        r"""Lists all the GoldengateDeployments for the given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_deployments():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateDeploymentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_deployments(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsRequest, dict]):
                The request object. The request for ``GoldengateDeployment.List``.
            parent (str):
                Required. The parent value for
                GoldengateDeployments in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateDeploymentsPager:
                The response for GoldengateDeployment.List.

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
            request, goldengate_deployment.ListGoldengateDeploymentsRequest
        ):
            request = goldengate_deployment.ListGoldengateDeploymentsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_deployments
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateDeploymentsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_goldengate_deployment(
        self,
        request: Optional[
            Union[goldengate_deployment.GetGoldengateDeploymentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> goldengate_deployment.GoldengateDeployment:
        r"""Gets details of a single GoldengateDeployment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_goldengate_deployment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetGoldengateDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_goldengate_deployment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetGoldengateDeploymentRequest, dict]):
                The request object. The request for ``GoldengateDeployment.Get``.
            name (str):
                Required. The name of the GoldengateDeployment in the
                following format:
                projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.GoldengateDeployment:
                GoldengateDeployment Goldengate
                Deployment resource model.

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
            request, goldengate_deployment.GetGoldengateDeploymentRequest
        ):
            request = goldengate_deployment.GetGoldengateDeploymentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_goldengate_deployment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_goldengate_deployment(
        self,
        request: Optional[
            Union[gco_goldengate_deployment.CreateGoldengateDeploymentRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        goldengate_deployment: Optional[
            gco_goldengate_deployment.GoldengateDeployment
        ] = None,
        goldengate_deployment_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new GoldengateDeployment in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_goldengate_deployment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                goldengate_deployment = oracledatabase_v1.GoldengateDeployment()
                goldengate_deployment.properties.deployment_type = "deployment_type_value"
                goldengate_deployment.properties.ogg_data.admin_password = "admin_password_value"
                goldengate_deployment.properties.ogg_data.deployment = "deployment_value"
                goldengate_deployment.properties.ogg_data.admin_username = "admin_username_value"
                goldengate_deployment.odb_subnet = "odb_subnet_value"
                goldengate_deployment.display_name = "display_name_value"

                request = oracledatabase_v1.CreateGoldengateDeploymentRequest(
                    parent="parent_value",
                    goldengate_deployment_id="goldengate_deployment_id_value",
                    goldengate_deployment=goldengate_deployment,
                )

                # Make the request
                operation = client.create_goldengate_deployment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateGoldengateDeploymentRequest, dict]):
                The request object. The request for ``GoldengateDeployment.Create``.
            parent (str):
                Required. The value for parent of the
                GoldengateDeployment in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            goldengate_deployment (google.cloud.oracledatabase_v1.types.GoldengateDeployment):
                Required. The resource being created.
                This corresponds to the ``goldengate_deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            goldengate_deployment_id (str):
                Required. The ID of the GoldengateDeployment to create.
                This value is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``goldengate_deployment_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.GoldengateDeployment`
                GoldengateDeployment Goldengate Deployment resource
                model.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, goldengate_deployment, goldengate_deployment_id]
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
            request, gco_goldengate_deployment.CreateGoldengateDeploymentRequest
        ):
            request = gco_goldengate_deployment.CreateGoldengateDeploymentRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if goldengate_deployment is not None:
                request.goldengate_deployment = goldengate_deployment
            if goldengate_deployment_id is not None:
                request.goldengate_deployment_id = goldengate_deployment_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_goldengate_deployment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_goldengate_deployment.GoldengateDeployment,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_goldengate_deployment(
        self,
        request: Optional[
            Union[goldengate_deployment.DeleteGoldengateDeploymentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single GoldengateDeployment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_goldengate_deployment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteGoldengateDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_goldengate_deployment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteGoldengateDeploymentRequest, dict]):
                The request object. The request for ``GoldengateDeployment.Delete``.
            name (str):
                Required. The name of the GoldengateDeployment in the
                following format:
                projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
            request, goldengate_deployment.DeleteGoldengateDeploymentRequest
        ):
            request = goldengate_deployment.DeleteGoldengateDeploymentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_goldengate_deployment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def stop_goldengate_deployment(
        self,
        request: Optional[
            Union[goldengate_deployment.StopGoldengateDeploymentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Stops a single GoldengateDeployment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_stop_goldengate_deployment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.StopGoldengateDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.stop_goldengate_deployment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.StopGoldengateDeploymentRequest, dict]):
                The request object. The request for ``GoldengateDeployment.Stop``.
            name (str):
                Required. The name of the Goldengate Deployment in the
                following format:
                projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.GoldengateDeployment`
                GoldengateDeployment Goldengate Deployment resource
                model.

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
            request, goldengate_deployment.StopGoldengateDeploymentRequest
        ):
            request = goldengate_deployment.StopGoldengateDeploymentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.stop_goldengate_deployment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            goldengate_deployment.GoldengateDeployment,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def start_goldengate_deployment(
        self,
        request: Optional[
            Union[goldengate_deployment.StartGoldengateDeploymentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Starts a single GoldengateDeployment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_start_goldengate_deployment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.StartGoldengateDeploymentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.start_goldengate_deployment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.StartGoldengateDeploymentRequest, dict]):
                The request object. The request for ``GoldengateDeployment.Start``.
            name (str):
                Required. The name of the Goldengate Deployment in the
                following format:
                projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.GoldengateDeployment`
                GoldengateDeployment Goldengate Deployment resource
                model.

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
            request, goldengate_deployment.StartGoldengateDeploymentRequest
        ):
            request = goldengate_deployment.StartGoldengateDeploymentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.start_goldengate_deployment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            goldengate_deployment.GoldengateDeployment,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_connections(
        self,
        request: Optional[
            Union[goldengate_connection.ListGoldengateConnectionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateConnectionsPager:
        r"""Lists all the GoldengateConnections for the given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_connections():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateConnectionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_connections(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsRequest, dict]):
                The request object. The request for ``GoldengateConnection.List``.
            parent (str):
                Required. The parent value for
                GoldengateConnections in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateConnectionsPager:
                The response for GoldengateConnection.List.

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
            request, goldengate_connection.ListGoldengateConnectionsRequest
        ):
            request = goldengate_connection.ListGoldengateConnectionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_connections
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateConnectionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_goldengate_connection(
        self,
        request: Optional[
            Union[goldengate_connection.GetGoldengateConnectionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> goldengate_connection.GoldengateConnection:
        r"""Gets details of a single GoldengateConnection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_goldengate_connection():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetGoldengateConnectionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_goldengate_connection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetGoldengateConnectionRequest, dict]):
                The request object. The request for ``GoldengateConnection.Get``.
            name (str):
                Required. The name of the GoldengateConnection in the
                following format:
                projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.GoldengateConnection:
                Details of the GoldengateConnection
                resource.

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
            request, goldengate_connection.GetGoldengateConnectionRequest
        ):
            request = goldengate_connection.GetGoldengateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_goldengate_connection
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_goldengate_connection(
        self,
        request: Optional[
            Union[gco_goldengate_connection.CreateGoldengateConnectionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        goldengate_connection: Optional[
            gco_goldengate_connection.GoldengateConnection
        ] = None,
        goldengate_connection_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new GoldengateConnection in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_goldengate_connection():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                goldengate_connection = oracledatabase_v1.GoldengateConnection()
                goldengate_connection.properties.oracle_connection_properties.password = "password_value"
                goldengate_connection.properties.connection_type = "ICEBERG"
                goldengate_connection.properties.display_name = "display_name_value"

                request = oracledatabase_v1.CreateGoldengateConnectionRequest(
                    parent="parent_value",
                    goldengate_connection_id="goldengate_connection_id_value",
                    goldengate_connection=goldengate_connection,
                )

                # Make the request
                operation = client.create_goldengate_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateGoldengateConnectionRequest, dict]):
                The request object. The request for ``GoldengateConnection.Create``.
            parent (str):
                Required. The value for parent of the
                GoldengateConnection in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            goldengate_connection (google.cloud.oracledatabase_v1.types.GoldengateConnection):
                Required. The resource being created.
                This corresponds to the ``goldengate_connection`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            goldengate_connection_id (str):
                Required. The ID of the GoldengateConnection to create.
                This value is restricted to
                (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
                maximum of 63 characters in length. The value must start
                with a letter and end with a letter or a number.

                This corresponds to the ``goldengate_connection_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.GoldengateConnection`
                Details of the GoldengateConnection resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, goldengate_connection, goldengate_connection_id]
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
            request, gco_goldengate_connection.CreateGoldengateConnectionRequest
        ):
            request = gco_goldengate_connection.CreateGoldengateConnectionRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if goldengate_connection is not None:
                request.goldengate_connection = goldengate_connection
            if goldengate_connection_id is not None:
                request.goldengate_connection_id = goldengate_connection_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_goldengate_connection
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_goldengate_connection.GoldengateConnection,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_goldengate_connection(
        self,
        request: Optional[
            Union[goldengate_connection.DeleteGoldengateConnectionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single GoldengateConnection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_goldengate_connection():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteGoldengateConnectionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_goldengate_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteGoldengateConnectionRequest, dict]):
                The request object. The request for ``GoldengateConnection.Delete``.
            name (str):
                Required. The name of the GoldengateConnection in the
                following format:
                projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
            request, goldengate_connection.DeleteGoldengateConnectionRequest
        ):
            request = goldengate_connection.DeleteGoldengateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_goldengate_connection
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_deployment_versions(
        self,
        request: Optional[
            Union[
                goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateDeploymentVersionsPager:
        r"""Lists GoldengateDeploymentVersions in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_deployment_versions():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateDeploymentVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_deployment_versions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsRequest, dict]):
                The request object. Message for listing
                GoldengateDeploymentVersions.
            parent (str):
                Required. Parent value for
                ListGoldengateDeploymentVersionsRequest
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateDeploymentVersionsPager:
                Message for response to listing
                GoldengateDeploymentVersions
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
            goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest,
        ):
            request = (
                goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_deployment_versions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateDeploymentVersionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_deployment_types(
        self,
        request: Optional[
            Union[goldengate_deployment_type.ListGoldengateDeploymentTypesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateDeploymentTypesPager:
        r"""Lists GoldenGateDeploymentTypes in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_deployment_types():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateDeploymentTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_deployment_types(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesRequest, dict]):
                The request object. Message for listing
                GoldengateDeploymentTypes.
            parent (str):
                Required. The parent resource.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateDeploymentTypesPager:
                Message for response to listing
                GoldengateDeploymentTypes
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
            request, goldengate_deployment_type.ListGoldengateDeploymentTypesRequest
        ):
            request = goldengate_deployment_type.ListGoldengateDeploymentTypesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_deployment_types
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateDeploymentTypesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_deployment_environments(
        self,
        request: Optional[
            Union[
                goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateDeploymentEnvironmentsPager:
        r"""Lists GoldengateDeploymentEnvironments in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_deployment_environments():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateDeploymentEnvironmentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_deployment_environments(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsRequest, dict]):
                The request object. Message for listing
                GoldengateDeploymentEnvironments.
            parent (str):
                Required. The parent, which owns this
                collection of
                GoldengateDeploymentEnvironments.
                Format:

                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateDeploymentEnvironmentsPager:
                Message for response to listing
                GoldengateDeploymentEnvironments
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
            goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest,
        ):
            request = goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_deployment_environments
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateDeploymentEnvironmentsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_connection_types(
        self,
        request: Optional[
            Union[goldengate_connection_type.ListGoldengateConnectionTypesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateConnectionTypesPager:
        r"""Lists GoldengateConnectionTypes in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_connection_types():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateConnectionTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_connection_types(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesRequest, dict]):
                The request object. Message for listing
                GoldengateConnectionTypes.
            parent (str):
                Required. Parent value for
                ListGoldengateConnectionTypesRequest
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateConnectionTypesPager:
                Message for response to listing
                GoldengateConnectionTypes
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
            request, goldengate_connection_type.ListGoldengateConnectionTypesRequest
        ):
            request = goldengate_connection_type.ListGoldengateConnectionTypesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_connection_types
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateConnectionTypesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_db_versions(
        self,
        request: Optional[Union[db_version.ListDbVersionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDbVersionsPager:
        r"""List DbVersions for the given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_db_versions():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDbVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_db_versions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDbVersionsRequest, dict]):
                The request object. The request for ``DbVersions.List``.
            parent (str):
                Required. The parent value for the
                DbVersion resource with the format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDbVersionsPager:
                The response for DbVersions.List.

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
        if not isinstance(request, db_version.ListDbVersionsRequest):
            request = db_version.ListDbVersionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_db_versions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDbVersionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_database_character_sets(
        self,
        request: Optional[
            Union[database_character_set.ListDatabaseCharacterSetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDatabaseCharacterSetsPager:
        r"""List DatabaseCharacterSets for the given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_database_character_sets():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListDatabaseCharacterSetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_database_character_sets(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsRequest, dict]):
                The request object. The request for ``DatabaseCharacterSet.List``.
            parent (str):
                Required. The parent value for
                DatabaseCharacterSets in the following
                format:
                projects/{project}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListDatabaseCharacterSetsPager:
                The response for DatabaseCharacterSet.List.

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
            request, database_character_set.ListDatabaseCharacterSetsRequest
        ):
            request = database_character_set.ListDatabaseCharacterSetsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_database_character_sets
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDatabaseCharacterSetsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_goldengate_connection_assignments(
        self,
        request: Optional[
            Union[
                goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGoldengateConnectionAssignmentsPager:
        r"""Lists GoldengateConnectionAssignments in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_list_goldengate_connection_assignments():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.ListGoldengateConnectionAssignmentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_goldengate_connection_assignments(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsRequest, dict]):
                The request object. Request message for listing
                GoldengateConnectionAssignments.
            parent (str):
                Required. The parent value for the
                GoldengateConnectionAssignments. Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListGoldengateConnectionAssignmentsPager:
                Response message for listing
                GoldengateConnectionAssignments.
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
            goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest,
        ):
            request = goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_goldengate_connection_assignments
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGoldengateConnectionAssignmentsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_goldengate_connection_assignment(
        self,
        request: Optional[
            Union[
                goldengate_connection_assignment.GetGoldengateConnectionAssignmentRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> goldengate_connection_assignment.GoldengateConnectionAssignment:
        r"""Gets details of a single
        GoldengateConnectionAssignment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_get_goldengate_connection_assignment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.GetGoldengateConnectionAssignmentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_goldengate_connection_assignment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.GetGoldengateConnectionAssignmentRequest, dict]):
                The request object. Request message for getting a
                GoldengateConnectionAssignment.
            name (str):
                Required. The name of the GoldengateConnectionAssignment
                to retrieve. Format:
                projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignment:
                Represents the metadata of a
                Goldengate Connection Assignment.

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
            goldengate_connection_assignment.GetGoldengateConnectionAssignmentRequest,
        ):
            request = goldengate_connection_assignment.GetGoldengateConnectionAssignmentRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_goldengate_connection_assignment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_goldengate_connection_assignment(
        self,
        request: Optional[
            Union[
                gco_goldengate_connection_assignment.CreateGoldengateConnectionAssignmentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        goldengate_connection_assignment: Optional[
            gco_goldengate_connection_assignment.GoldengateConnectionAssignment
        ] = None,
        goldengate_connection_assignment_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new GoldengateConnectionAssignment in a
        given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_create_goldengate_connection_assignment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                goldengate_connection_assignment = oracledatabase_v1.GoldengateConnectionAssignment()
                goldengate_connection_assignment.properties.goldengate_connection = "goldengate_connection_value"
                goldengate_connection_assignment.properties.goldengate_deployment = "goldengate_deployment_value"

                request = oracledatabase_v1.CreateGoldengateConnectionAssignmentRequest(
                    parent="parent_value",
                    goldengate_connection_assignment_id="goldengate_connection_assignment_id_value",
                    goldengate_connection_assignment=goldengate_connection_assignment,
                )

                # Make the request
                operation = client.create_goldengate_connection_assignment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.CreateGoldengateConnectionAssignmentRequest, dict]):
                The request object. Request message for creating a
                GoldengateConnectionAssignment.
            parent (str):
                Required. The parent resource where
                this GoldengateConnectionAssignment will
                be created. Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            goldengate_connection_assignment (google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignment):
                Required. The
                GoldengateConnectionAssignment to
                create.

                This corresponds to the ``goldengate_connection_assignment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            goldengate_connection_assignment_id (str):
                Required. The ID of the
                GoldengateConnectionAssignment to
                create.

                This corresponds to the ``goldengate_connection_assignment_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.oracledatabase_v1.types.GoldengateConnectionAssignment`
                Represents the metadata of a Goldengate Connection
                Assignment.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            goldengate_connection_assignment,
            goldengate_connection_assignment_id,
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
            gco_goldengate_connection_assignment.CreateGoldengateConnectionAssignmentRequest,
        ):
            request = gco_goldengate_connection_assignment.CreateGoldengateConnectionAssignmentRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if goldengate_connection_assignment is not None:
                request.goldengate_connection_assignment = (
                    goldengate_connection_assignment
                )
            if goldengate_connection_assignment_id is not None:
                request.goldengate_connection_assignment_id = (
                    goldengate_connection_assignment_id
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_goldengate_connection_assignment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            gco_goldengate_connection_assignment.GoldengateConnectionAssignment,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_goldengate_connection_assignment(
        self,
        request: Optional[
            Union[
                goldengate_connection_assignment.DeleteGoldengateConnectionAssignmentRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single GoldengateConnectionAssignment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_delete_goldengate_connection_assignment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.DeleteGoldengateConnectionAssignmentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_goldengate_connection_assignment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.DeleteGoldengateConnectionAssignmentRequest, dict]):
                The request object. Request message for deleting a
                GoldengateConnectionAssignment.
            name (str):
                Required. The name of the GoldengateConnectionAssignment
                to delete. Format:
                projects/{project}/locations/{location}/goldengateConnectionAssignments/{goldengate_connection_assignment}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
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
            goldengate_connection_assignment.DeleteGoldengateConnectionAssignmentRequest,
        ):
            request = goldengate_connection_assignment.DeleteGoldengateConnectionAssignmentRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_goldengate_connection_assignment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=oracledatabase.OperationMetadata,
        )

        # Done; return the response.
        return response

    def test_goldengate_connection_assignment(
        self,
        request: Optional[
            Union[
                goldengate_connection_assignment.TestGoldengateConnectionAssignmentRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> goldengate_connection_assignment.TestGoldengateConnectionAssignmentResponse:
        r"""Tests a single GoldengateConnectionAssignment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import oracledatabase_v1

            def sample_test_goldengate_connection_assignment():
                # Create a client
                client = oracledatabase_v1.OracleDatabaseClient()

                # Initialize request argument(s)
                request = oracledatabase_v1.TestGoldengateConnectionAssignmentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.test_goldengate_connection_assignment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.oracledatabase_v1.types.TestGoldengateConnectionAssignmentRequest, dict]):
                The request object. Request message for
                TestGoldengateConnectionAssignment.
            name (str):
                Required. Name of the connection assignment for which to
                test connection.
                projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengate_connection_assignment}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.oracledatabase_v1.types.TestGoldengateConnectionAssignmentResponse:
                The result of the connectivity test
                performed between the Goldengate
                deployment and the associated database /
                service.

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
            goldengate_connection_assignment.TestGoldengateConnectionAssignmentRequest,
        ):
            request = goldengate_connection_assignment.TestGoldengateConnectionAssignmentRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.test_goldengate_connection_assignment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "OracleDatabaseClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()

    def list_operations(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.list_operations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e

    def get_operation(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e

    def delete_operation(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.delete_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def cancel_operation(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def get_location(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.get_location]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e

    def list_locations(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.list_locations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

__all__ = ("OracleDatabaseClient",)
