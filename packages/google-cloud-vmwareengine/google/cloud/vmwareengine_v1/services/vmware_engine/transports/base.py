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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.vmwareengine_v1 import gapic_version as package_version
from google.cloud.vmwareengine_v1.types import vmwareengine, vmwareengine_resources

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class VmwareEngineTransport(abc.ABC):
    """Abstract transport class for VmwareEngine."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "vmwareengine.googleapis.com"

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
                 The hostname to connect to (default: 'vmwareengine.googleapis.com').
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
            self.list_private_clouds: gapic_v1.method.wrap_method(
                self.list_private_clouds,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_private_cloud: gapic_v1.method.wrap_method(
                self.get_private_cloud,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_private_cloud: gapic_v1.method.wrap_method(
                self.create_private_cloud,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_private_cloud: gapic_v1.method.wrap_method(
                self.update_private_cloud,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_private_cloud: gapic_v1.method.wrap_method(
                self.delete_private_cloud,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undelete_private_cloud: gapic_v1.method.wrap_method(
                self.undelete_private_cloud,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_clusters: gapic_v1.method.wrap_method(
                self.list_clusters,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_cluster: gapic_v1.method.wrap_method(
                self.get_cluster,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_cluster: gapic_v1.method.wrap_method(
                self.create_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_cluster: gapic_v1.method.wrap_method(
                self.update_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_cluster: gapic_v1.method.wrap_method(
                self.delete_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_nodes: gapic_v1.method.wrap_method(
                self.list_nodes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_node: gapic_v1.method.wrap_method(
                self.get_node,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_external_addresses: gapic_v1.method.wrap_method(
                self.list_external_addresses,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.fetch_network_policy_external_addresses: gapic_v1.method.wrap_method(
                self.fetch_network_policy_external_addresses,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_external_address: gapic_v1.method.wrap_method(
                self.get_external_address,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_external_address: gapic_v1.method.wrap_method(
                self.create_external_address,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_external_address: gapic_v1.method.wrap_method(
                self.update_external_address,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_external_address: gapic_v1.method.wrap_method(
                self.delete_external_address,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subnets: gapic_v1.method.wrap_method(
                self.list_subnets,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_subnet: gapic_v1.method.wrap_method(
                self.get_subnet,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_subnet: gapic_v1.method.wrap_method(
                self.update_subnet,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_external_access_rules: gapic_v1.method.wrap_method(
                self.list_external_access_rules,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_external_access_rule: gapic_v1.method.wrap_method(
                self.get_external_access_rule,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_external_access_rule: gapic_v1.method.wrap_method(
                self.create_external_access_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_external_access_rule: gapic_v1.method.wrap_method(
                self.update_external_access_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_external_access_rule: gapic_v1.method.wrap_method(
                self.delete_external_access_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_logging_servers: gapic_v1.method.wrap_method(
                self.list_logging_servers,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_logging_server: gapic_v1.method.wrap_method(
                self.get_logging_server,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_logging_server: gapic_v1.method.wrap_method(
                self.create_logging_server,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_logging_server: gapic_v1.method.wrap_method(
                self.update_logging_server,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_logging_server: gapic_v1.method.wrap_method(
                self.delete_logging_server,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_node_types: gapic_v1.method.wrap_method(
                self.list_node_types,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_node_type: gapic_v1.method.wrap_method(
                self.get_node_type,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.show_nsx_credentials: gapic_v1.method.wrap_method(
                self.show_nsx_credentials,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.show_vcenter_credentials: gapic_v1.method.wrap_method(
                self.show_vcenter_credentials,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.reset_nsx_credentials: gapic_v1.method.wrap_method(
                self.reset_nsx_credentials,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_vcenter_credentials: gapic_v1.method.wrap_method(
                self.reset_vcenter_credentials,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_dns_forwarding: gapic_v1.method.wrap_method(
                self.get_dns_forwarding,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_dns_forwarding: gapic_v1.method.wrap_method(
                self.update_dns_forwarding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_network_peering: gapic_v1.method.wrap_method(
                self.get_network_peering,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_network_peerings: gapic_v1.method.wrap_method(
                self.list_network_peerings,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_network_peering: gapic_v1.method.wrap_method(
                self.create_network_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_network_peering: gapic_v1.method.wrap_method(
                self.delete_network_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_network_peering: gapic_v1.method.wrap_method(
                self.update_network_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_peering_routes: gapic_v1.method.wrap_method(
                self.list_peering_routes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_hcx_activation_key: gapic_v1.method.wrap_method(
                self.create_hcx_activation_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_hcx_activation_keys: gapic_v1.method.wrap_method(
                self.list_hcx_activation_keys,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_hcx_activation_key: gapic_v1.method.wrap_method(
                self.get_hcx_activation_key,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_network_policy: gapic_v1.method.wrap_method(
                self.get_network_policy,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_network_policies: gapic_v1.method.wrap_method(
                self.list_network_policies,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_network_policy: gapic_v1.method.wrap_method(
                self.create_network_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_network_policy: gapic_v1.method.wrap_method(
                self.update_network_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_network_policy: gapic_v1.method.wrap_method(
                self.delete_network_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_management_dns_zone_bindings: gapic_v1.method.wrap_method(
                self.list_management_dns_zone_bindings,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_management_dns_zone_binding: gapic_v1.method.wrap_method(
                self.get_management_dns_zone_binding,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_management_dns_zone_binding: gapic_v1.method.wrap_method(
                self.create_management_dns_zone_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_management_dns_zone_binding: gapic_v1.method.wrap_method(
                self.update_management_dns_zone_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_management_dns_zone_binding: gapic_v1.method.wrap_method(
                self.delete_management_dns_zone_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.repair_management_dns_zone_binding: gapic_v1.method.wrap_method(
                self.repair_management_dns_zone_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_vmware_engine_network: gapic_v1.method.wrap_method(
                self.create_vmware_engine_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_vmware_engine_network: gapic_v1.method.wrap_method(
                self.update_vmware_engine_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_vmware_engine_network: gapic_v1.method.wrap_method(
                self.delete_vmware_engine_network,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_vmware_engine_network: gapic_v1.method.wrap_method(
                self.get_vmware_engine_network,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_vmware_engine_networks: gapic_v1.method.wrap_method(
                self.list_vmware_engine_networks,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.create_private_connection: gapic_v1.method.wrap_method(
                self.create_private_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_private_connection: gapic_v1.method.wrap_method(
                self.get_private_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.list_private_connections: gapic_v1.method.wrap_method(
                self.list_private_connections,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_private_connection: gapic_v1.method.wrap_method(
                self.update_private_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_private_connection: gapic_v1.method.wrap_method(
                self.delete_private_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_private_connection_peering_routes: gapic_v1.method.wrap_method(
                self.list_private_connection_peering_routes,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.grant_dns_bind_permission: gapic_v1.method.wrap_method(
                self.grant_dns_bind_permission,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_dns_bind_permission: gapic_v1.method.wrap_method(
                self.get_dns_bind_permission,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.revoke_dns_bind_permission: gapic_v1.method.wrap_method(
                self.revoke_dns_bind_permission,
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
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
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
    def list_private_clouds(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateCloudsRequest],
        Union[
            vmwareengine.ListPrivateCloudsResponse,
            Awaitable[vmwareengine.ListPrivateCloudsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateCloudRequest],
        Union[
            vmwareengine_resources.PrivateCloud,
            Awaitable[vmwareengine_resources.PrivateCloud],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.CreatePrivateCloudRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.UpdatePrivateCloudRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.DeletePrivateCloudRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def undelete_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.UndeletePrivateCloudRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [vmwareengine.ListClustersRequest],
        Union[
            vmwareengine.ListClustersResponse,
            Awaitable[vmwareengine.ListClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [vmwareengine.GetClusterRequest],
        Union[
            vmwareengine_resources.Cluster, Awaitable[vmwareengine_resources.Cluster]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [vmwareengine.CreateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [vmwareengine.UpdateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [vmwareengine.DeleteClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_nodes(
        self,
    ) -> Callable[
        [vmwareengine.ListNodesRequest],
        Union[
            vmwareengine.ListNodesResponse, Awaitable[vmwareengine.ListNodesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_node(
        self,
    ) -> Callable[
        [vmwareengine.GetNodeRequest],
        Union[vmwareengine_resources.Node, Awaitable[vmwareengine_resources.Node]],
    ]:
        raise NotImplementedError()

    @property
    def list_external_addresses(
        self,
    ) -> Callable[
        [vmwareengine.ListExternalAddressesRequest],
        Union[
            vmwareengine.ListExternalAddressesResponse,
            Awaitable[vmwareengine.ListExternalAddressesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_network_policy_external_addresses(
        self,
    ) -> Callable[
        [vmwareengine.FetchNetworkPolicyExternalAddressesRequest],
        Union[
            vmwareengine.FetchNetworkPolicyExternalAddressesResponse,
            Awaitable[vmwareengine.FetchNetworkPolicyExternalAddressesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_external_address(
        self,
    ) -> Callable[
        [vmwareengine.GetExternalAddressRequest],
        Union[
            vmwareengine_resources.ExternalAddress,
            Awaitable[vmwareengine_resources.ExternalAddress],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_external_address(
        self,
    ) -> Callable[
        [vmwareengine.CreateExternalAddressRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_external_address(
        self,
    ) -> Callable[
        [vmwareengine.UpdateExternalAddressRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_external_address(
        self,
    ) -> Callable[
        [vmwareengine.DeleteExternalAddressRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_subnets(
        self,
    ) -> Callable[
        [vmwareengine.ListSubnetsRequest],
        Union[
            vmwareengine.ListSubnetsResponse,
            Awaitable[vmwareengine.ListSubnetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_subnet(
        self,
    ) -> Callable[
        [vmwareengine.GetSubnetRequest],
        Union[vmwareengine_resources.Subnet, Awaitable[vmwareengine_resources.Subnet]],
    ]:
        raise NotImplementedError()

    @property
    def update_subnet(
        self,
    ) -> Callable[
        [vmwareengine.UpdateSubnetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_external_access_rules(
        self,
    ) -> Callable[
        [vmwareengine.ListExternalAccessRulesRequest],
        Union[
            vmwareengine.ListExternalAccessRulesResponse,
            Awaitable[vmwareengine.ListExternalAccessRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.GetExternalAccessRuleRequest],
        Union[
            vmwareengine_resources.ExternalAccessRule,
            Awaitable[vmwareengine_resources.ExternalAccessRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.CreateExternalAccessRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.UpdateExternalAccessRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.DeleteExternalAccessRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_logging_servers(
        self,
    ) -> Callable[
        [vmwareengine.ListLoggingServersRequest],
        Union[
            vmwareengine.ListLoggingServersResponse,
            Awaitable[vmwareengine.ListLoggingServersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_logging_server(
        self,
    ) -> Callable[
        [vmwareengine.GetLoggingServerRequest],
        Union[
            vmwareengine_resources.LoggingServer,
            Awaitable[vmwareengine_resources.LoggingServer],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_logging_server(
        self,
    ) -> Callable[
        [vmwareengine.CreateLoggingServerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_logging_server(
        self,
    ) -> Callable[
        [vmwareengine.UpdateLoggingServerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_logging_server(
        self,
    ) -> Callable[
        [vmwareengine.DeleteLoggingServerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_node_types(
        self,
    ) -> Callable[
        [vmwareengine.ListNodeTypesRequest],
        Union[
            vmwareengine.ListNodeTypesResponse,
            Awaitable[vmwareengine.ListNodeTypesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_node_type(
        self,
    ) -> Callable[
        [vmwareengine.GetNodeTypeRequest],
        Union[
            vmwareengine_resources.NodeType, Awaitable[vmwareengine_resources.NodeType]
        ],
    ]:
        raise NotImplementedError()

    @property
    def show_nsx_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowNsxCredentialsRequest],
        Union[
            vmwareengine_resources.Credentials,
            Awaitable[vmwareengine_resources.Credentials],
        ],
    ]:
        raise NotImplementedError()

    @property
    def show_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowVcenterCredentialsRequest],
        Union[
            vmwareengine_resources.Credentials,
            Awaitable[vmwareengine_resources.Credentials],
        ],
    ]:
        raise NotImplementedError()

    @property
    def reset_nsx_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ResetNsxCredentialsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reset_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ResetVcenterCredentialsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_dns_forwarding(
        self,
    ) -> Callable[
        [vmwareengine.GetDnsForwardingRequest],
        Union[
            vmwareengine_resources.DnsForwarding,
            Awaitable[vmwareengine_resources.DnsForwarding],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_dns_forwarding(
        self,
    ) -> Callable[
        [vmwareengine.UpdateDnsForwardingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_network_peering(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPeeringRequest],
        Union[
            vmwareengine_resources.NetworkPeering,
            Awaitable[vmwareengine_resources.NetworkPeering],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_network_peerings(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPeeringsRequest],
        Union[
            vmwareengine.ListNetworkPeeringsResponse,
            Awaitable[vmwareengine.ListNetworkPeeringsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_network_peering(
        self,
    ) -> Callable[
        [vmwareengine.CreateNetworkPeeringRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_network_peering(
        self,
    ) -> Callable[
        [vmwareengine.DeleteNetworkPeeringRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_network_peering(
        self,
    ) -> Callable[
        [vmwareengine.UpdateNetworkPeeringRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_peering_routes(
        self,
    ) -> Callable[
        [vmwareengine.ListPeeringRoutesRequest],
        Union[
            vmwareengine.ListPeeringRoutesResponse,
            Awaitable[vmwareengine.ListPeeringRoutesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.CreateHcxActivationKeyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_hcx_activation_keys(
        self,
    ) -> Callable[
        [vmwareengine.ListHcxActivationKeysRequest],
        Union[
            vmwareengine.ListHcxActivationKeysResponse,
            Awaitable[vmwareengine.ListHcxActivationKeysResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.GetHcxActivationKeyRequest],
        Union[
            vmwareengine_resources.HcxActivationKey,
            Awaitable[vmwareengine_resources.HcxActivationKey],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPolicyRequest],
        Union[
            vmwareengine_resources.NetworkPolicy,
            Awaitable[vmwareengine_resources.NetworkPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_network_policies(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPoliciesRequest],
        Union[
            vmwareengine.ListNetworkPoliciesResponse,
            Awaitable[vmwareengine.ListNetworkPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.CreateNetworkPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.UpdateNetworkPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.DeleteNetworkPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_management_dns_zone_bindings(
        self,
    ) -> Callable[
        [vmwareengine.ListManagementDnsZoneBindingsRequest],
        Union[
            vmwareengine.ListManagementDnsZoneBindingsResponse,
            Awaitable[vmwareengine.ListManagementDnsZoneBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.GetManagementDnsZoneBindingRequest],
        Union[
            vmwareengine_resources.ManagementDnsZoneBinding,
            Awaitable[vmwareengine_resources.ManagementDnsZoneBinding],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.CreateManagementDnsZoneBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.UpdateManagementDnsZoneBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.DeleteManagementDnsZoneBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def repair_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.RepairManagementDnsZoneBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.CreateVmwareEngineNetworkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.UpdateVmwareEngineNetworkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.DeleteVmwareEngineNetworkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.GetVmwareEngineNetworkRequest],
        Union[
            vmwareengine_resources.VmwareEngineNetwork,
            Awaitable[vmwareengine_resources.VmwareEngineNetwork],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_vmware_engine_networks(
        self,
    ) -> Callable[
        [vmwareengine.ListVmwareEngineNetworksRequest],
        Union[
            vmwareengine.ListVmwareEngineNetworksResponse,
            Awaitable[vmwareengine.ListVmwareEngineNetworksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.CreatePrivateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateConnectionRequest],
        Union[
            vmwareengine_resources.PrivateConnection,
            Awaitable[vmwareengine_resources.PrivateConnection],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_private_connections(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateConnectionsRequest],
        Union[
            vmwareengine.ListPrivateConnectionsResponse,
            Awaitable[vmwareengine.ListPrivateConnectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.UpdatePrivateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.DeletePrivateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_private_connection_peering_routes(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateConnectionPeeringRoutesRequest],
        Union[
            vmwareengine.ListPrivateConnectionPeeringRoutesResponse,
            Awaitable[vmwareengine.ListPrivateConnectionPeeringRoutesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def grant_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.GrantDnsBindPermissionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.GetDnsBindPermissionRequest],
        Union[
            vmwareengine_resources.DnsBindPermission,
            Awaitable[vmwareengine_resources.DnsBindPermission],
        ],
    ]:
        raise NotImplementedError()

    @property
    def revoke_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.RevokeDnsBindPermissionRequest],
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
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
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


__all__ = ("VmwareEngineTransport",)
