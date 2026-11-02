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

from google.cloud.vmwareengine_v1 import gapic_version as package_version
from google.cloud.vmwareengine_v1._compat import (
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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.vmwareengine_v1.services.vmware_engine import pagers
from google.cloud.vmwareengine_v1.types import vmwareengine, vmwareengine_resources

from .transports.base import DEFAULT_CLIENT_INFO, VmwareEngineTransport
from .transports.grpc import VmwareEngineGrpcTransport
from .transports.grpc_asyncio import VmwareEngineGrpcAsyncIOTransport
from .transports.rest import VmwareEngineRestTransport


class VmwareEngineClientMeta(type):
    """Metaclass for the VmwareEngine client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[VmwareEngineTransport]]
    _transport_registry["grpc"] = VmwareEngineGrpcTransport
    _transport_registry["grpc_asyncio"] = VmwareEngineGrpcAsyncIOTransport
    _transport_registry["rest"] = VmwareEngineRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[VmwareEngineTransport]:
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


class VmwareEngineClient(metaclass=VmwareEngineClientMeta):
    """VMwareEngine manages VMware's private clusters in the Cloud."""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "vmwareengine.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "vmwareengine.{UNIVERSE_DOMAIN}"
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
            VmwareEngineClient: The constructed client.
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
            VmwareEngineClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> VmwareEngineTransport:
        """Returns the transport used by the client instance.

        Returns:
            VmwareEngineTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def cluster_path(
        project: str,
        location: str,
        private_cloud: str,
        cluster: str,
    ) -> str:
        """Returns a fully-qualified cluster string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/clusters/{cluster}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            cluster=cluster,
        )

    @staticmethod
    def parse_cluster_path(path: str) -> Dict[str, str]:
        """Parses a cluster path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/clusters/(?P<cluster>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def dns_bind_permission_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified dns_bind_permission string."""
        return "projects/{project}/locations/{location}/dnsBindPermission".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_dns_bind_permission_path(path: str) -> Dict[str, str]:
        """Parses a dns_bind_permission path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/dnsBindPermission$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def dns_forwarding_path(
        project: str,
        location: str,
        private_cloud: str,
    ) -> str:
        """Returns a fully-qualified dns_forwarding string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/dnsForwarding".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
        )

    @staticmethod
    def parse_dns_forwarding_path(path: str) -> Dict[str, str]:
        """Parses a dns_forwarding path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/dnsForwarding$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def external_access_rule_path(
        project: str,
        location: str,
        network_policy: str,
        external_access_rule: str,
    ) -> str:
        """Returns a fully-qualified external_access_rule string."""
        return "projects/{project}/locations/{location}/networkPolicies/{network_policy}/externalAccessRules/{external_access_rule}".format(
            project=project,
            location=location,
            network_policy=network_policy,
            external_access_rule=external_access_rule,
        )

    @staticmethod
    def parse_external_access_rule_path(path: str) -> Dict[str, str]:
        """Parses a external_access_rule path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/networkPolicies/(?P<network_policy>.+?)/externalAccessRules/(?P<external_access_rule>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def external_address_path(
        project: str,
        location: str,
        private_cloud: str,
        external_address: str,
    ) -> str:
        """Returns a fully-qualified external_address string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            external_address=external_address,
        )

    @staticmethod
    def parse_external_address_path(path: str) -> Dict[str, str]:
        """Parses a external_address path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/externalAddresses/(?P<external_address>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def hcx_activation_key_path(
        project: str,
        location: str,
        private_cloud: str,
        hcx_activation_key: str,
    ) -> str:
        """Returns a fully-qualified hcx_activation_key string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/hcxActivationKeys/{hcx_activation_key}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            hcx_activation_key=hcx_activation_key,
        )

    @staticmethod
    def parse_hcx_activation_key_path(path: str) -> Dict[str, str]:
        """Parses a hcx_activation_key path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/hcxActivationKeys/(?P<hcx_activation_key>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def logging_server_path(
        project: str,
        location: str,
        private_cloud: str,
        logging_server: str,
    ) -> str:
        """Returns a fully-qualified logging_server string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/loggingServers/{logging_server}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            logging_server=logging_server,
        )

    @staticmethod
    def parse_logging_server_path(path: str) -> Dict[str, str]:
        """Parses a logging_server path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/loggingServers/(?P<logging_server>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def management_dns_zone_binding_path(
        project: str,
        location: str,
        private_cloud: str,
        management_dns_zone_binding: str,
    ) -> str:
        """Returns a fully-qualified management_dns_zone_binding string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/managementDnsZoneBindings/{management_dns_zone_binding}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            management_dns_zone_binding=management_dns_zone_binding,
        )

    @staticmethod
    def parse_management_dns_zone_binding_path(path: str) -> Dict[str, str]:
        """Parses a management_dns_zone_binding path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/managementDnsZoneBindings/(?P<management_dns_zone_binding>.+?)$",
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
    def network_peering_path(
        project: str,
        location: str,
        network_peering: str,
    ) -> str:
        """Returns a fully-qualified network_peering string."""
        return "projects/{project}/locations/{location}/networkPeerings/{network_peering}".format(
            project=project,
            location=location,
            network_peering=network_peering,
        )

    @staticmethod
    def parse_network_peering_path(path: str) -> Dict[str, str]:
        """Parses a network_peering path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/networkPeerings/(?P<network_peering>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def network_policy_path(
        project: str,
        location: str,
        network_policy: str,
    ) -> str:
        """Returns a fully-qualified network_policy string."""
        return "projects/{project}/locations/{location}/networkPolicies/{network_policy}".format(
            project=project,
            location=location,
            network_policy=network_policy,
        )

    @staticmethod
    def parse_network_policy_path(path: str) -> Dict[str, str]:
        """Parses a network_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/networkPolicies/(?P<network_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def node_path(
        project: str,
        location: str,
        private_cloud: str,
        cluster: str,
        node: str,
    ) -> str:
        """Returns a fully-qualified node string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/clusters/{cluster}/nodes/{node}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            cluster=cluster,
            node=node,
        )

    @staticmethod
    def parse_node_path(path: str) -> Dict[str, str]:
        """Parses a node path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/clusters/(?P<cluster>.+?)/nodes/(?P<node>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def node_type_path(
        project: str,
        location: str,
        node_type: str,
    ) -> str:
        """Returns a fully-qualified node_type string."""
        return "projects/{project}/locations/{location}/nodeTypes/{node_type}".format(
            project=project,
            location=location,
            node_type=node_type,
        )

    @staticmethod
    def parse_node_type_path(path: str) -> Dict[str, str]:
        """Parses a node_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/nodeTypes/(?P<node_type>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def private_cloud_path(
        project: str,
        location: str,
        private_cloud: str,
    ) -> str:
        """Returns a fully-qualified private_cloud string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
        )

    @staticmethod
    def parse_private_cloud_path(path: str) -> Dict[str, str]:
        """Parses a private_cloud path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def private_connection_path(
        project: str,
        location: str,
        private_connection: str,
    ) -> str:
        """Returns a fully-qualified private_connection string."""
        return "projects/{project}/locations/{location}/privateConnections/{private_connection}".format(
            project=project,
            location=location,
            private_connection=private_connection,
        )

    @staticmethod
    def parse_private_connection_path(path: str) -> Dict[str, str]:
        """Parses a private_connection path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateConnections/(?P<private_connection>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def subnet_path(
        project: str,
        location: str,
        private_cloud: str,
        subnet: str,
    ) -> str:
        """Returns a fully-qualified subnet string."""
        return "projects/{project}/locations/{location}/privateClouds/{private_cloud}/subnets/{subnet}".format(
            project=project,
            location=location,
            private_cloud=private_cloud,
            subnet=subnet,
        )

    @staticmethod
    def parse_subnet_path(path: str) -> Dict[str, str]:
        """Parses a subnet path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/privateClouds/(?P<private_cloud>.+?)/subnets/(?P<subnet>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def vmware_engine_network_path(
        project: str,
        location: str,
        vmware_engine_network: str,
    ) -> str:
        """Returns a fully-qualified vmware_engine_network string."""
        return "projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network}".format(
            project=project,
            location=location,
            vmware_engine_network=vmware_engine_network,
        )

    @staticmethod
    def parse_vmware_engine_network_path(path: str) -> Dict[str, str]:
        """Parses a vmware_engine_network path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/vmwareEngineNetworks/(?P<vmware_engine_network>.+?)$",
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
            Union[str, VmwareEngineTransport, Callable[..., VmwareEngineTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the vmware engine client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,VmwareEngineTransport,Callable[..., VmwareEngineTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the VmwareEngineTransport constructor.
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
        self._client_cert_source = VmwareEngineClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=VmwareEngineClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, VmwareEngineTransport)
        if transport_provided:
            # transport is a VmwareEngineTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(VmwareEngineTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=VmwareEngineClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=VmwareEngineClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=VmwareEngineClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[VmwareEngineTransport], Callable[..., VmwareEngineTransport]
            ] = (
                VmwareEngineClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., VmwareEngineTransport], transport)
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
                    "Created client `google.cloud.vmwareengine_v1.VmwareEngineClient`.",
                    extra={
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
                        "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                        "credentialsType": None,
                    },
                )

    def list_private_clouds(
        self,
        request: Optional[Union[vmwareengine.ListPrivateCloudsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPrivateCloudsPager:
        r"""Lists ``PrivateCloud`` resources in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_private_clouds():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListPrivateCloudsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_private_clouds(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListPrivateCloudsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListPrivateClouds][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds]
            parent (str):
                Required. The resource name of the private cloud to be
                queried for clusters. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1-a``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListPrivateCloudsPager:
                Response message for
                   [VmwareEngine.ListPrivateClouds][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds]

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
        if not isinstance(request, vmwareengine.ListPrivateCloudsRequest):
            request = vmwareengine.ListPrivateCloudsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_private_clouds]

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
        response = pagers.ListPrivateCloudsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_private_cloud(
        self,
        request: Optional[Union[vmwareengine.GetPrivateCloudRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.PrivateCloud:
        r"""Retrieves a ``PrivateCloud`` resource by its resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_private_cloud():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetPrivateCloudRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_private_cloud(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetPrivateCloudRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetPrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateCloud]
            name (str):
                Required. The resource name of the private cloud to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.types.PrivateCloud:
                Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

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
        if not isinstance(request, vmwareengine.GetPrivateCloudRequest):
            request = vmwareengine.GetPrivateCloudRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_private_cloud]

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

    def create_private_cloud(
        self,
        request: Optional[Union[vmwareengine.CreatePrivateCloudRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        private_cloud: Optional[vmwareengine_resources.PrivateCloud] = None,
        private_cloud_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ``PrivateCloud`` resource in a given project and
        location. Private clouds of type ``STANDARD`` and
        ``TIME_LIMITED`` are zonal resources, ``STRETCHED`` private
        clouds are regional. Creating a private cloud also creates a
        `management
        cluster <https://cloud.google.com/vmware-engine/docs/concepts-vmware-components>`__
        for that private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_private_cloud():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                private_cloud = vmwareengine_v1.PrivateCloud()
                private_cloud.network_config.management_cidr = "management_cidr_value"
                private_cloud.management_cluster.cluster_id = "cluster_id_value"

                request = vmwareengine_v1.CreatePrivateCloudRequest(
                    parent="parent_value",
                    private_cloud_id="private_cloud_id_value",
                    private_cloud=private_cloud,
                )

                # Make the request
                operation = client.create_private_cloud(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreatePrivateCloudRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreatePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateCloud]
            parent (str):
                Required. The resource name of the location to create
                the new private cloud in. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1-a``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            private_cloud (google.cloud.vmwareengine_v1.types.PrivateCloud):
                Required. The initial description of
                the new private cloud.

                This corresponds to the ``private_cloud`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            private_cloud_id (str):
                Required. The user-provided identifier of the private
                cloud to be created. This identifier must be unique
                among each ``PrivateCloud`` within the parent and
                becomes the final token in the name URI. The identifier
                must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``private_cloud_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateCloud` Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, private_cloud, private_cloud_id]
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
        if not isinstance(request, vmwareengine.CreatePrivateCloudRequest):
            request = vmwareengine.CreatePrivateCloudRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if private_cloud is not None:
                request.private_cloud = private_cloud
            if private_cloud_id is not None:
                request.private_cloud_id = private_cloud_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_private_cloud]

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
            vmwareengine_resources.PrivateCloud,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_private_cloud(
        self,
        request: Optional[Union[vmwareengine.UpdatePrivateCloudRequest, dict]] = None,
        *,
        private_cloud: Optional[vmwareengine_resources.PrivateCloud] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Modifies a ``PrivateCloud`` resource. Only the following fields
        can be updated: ``description``. Only fields specified in
        ``updateMask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_private_cloud():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                private_cloud = vmwareengine_v1.PrivateCloud()
                private_cloud.network_config.management_cidr = "management_cidr_value"
                private_cloud.management_cluster.cluster_id = "cluster_id_value"

                request = vmwareengine_v1.UpdatePrivateCloudRequest(
                    private_cloud=private_cloud,
                )

                # Make the request
                operation = client.update_private_cloud(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdatePrivateCloudRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdatePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateCloud]
            private_cloud (google.cloud.vmwareengine_v1.types.PrivateCloud):
                Required. Private cloud description.
                This corresponds to the ``private_cloud`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``PrivateCloud`` resource by the
                update. The fields specified in ``updateMask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateCloud` Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [private_cloud, update_mask]
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
        if not isinstance(request, vmwareengine.UpdatePrivateCloudRequest):
            request = vmwareengine.UpdatePrivateCloudRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if private_cloud is not None:
                request.private_cloud = private_cloud
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_private_cloud]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("private_cloud.name", request.private_cloud.name),)
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
            vmwareengine_resources.PrivateCloud,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_private_cloud(
        self,
        request: Optional[Union[vmwareengine.DeletePrivateCloudRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Schedules a ``PrivateCloud`` resource for deletion.

        A ``PrivateCloud`` resource scheduled for deletion has
        ``PrivateCloud.state`` set to ``DELETED`` and ``expireTime`` set
        to the time when deletion is final and can no longer be
        reversed. The delete operation is marked as done as soon as the
        ``PrivateCloud`` is successfully scheduled for deletion (this
        also applies when ``delayHours`` is set to zero), and the
        operation is not kept in pending state until ``PrivateCloud`` is
        purged. ``PrivateCloud`` can be restored using
        ``UndeletePrivateCloud`` method before the ``expireTime``
        elapses. When ``expireTime`` is reached, deletion is final and
        all private cloud resources are irreversibly removed and billing
        stops. During the final removal process, ``PrivateCloud.state``
        is set to ``PURGING``. ``PrivateCloud`` can be polled using
        standard ``GET`` method for the whole period of deletion and
        purging. It will not be returned only when it is completely
        purged.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_private_cloud():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeletePrivateCloudRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_private_cloud(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeletePrivateCloudRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateCloud]
            name (str):
                Required. The resource name of the private cloud to
                delete. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateCloud` Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

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
        if not isinstance(request, vmwareengine.DeletePrivateCloudRequest):
            request = vmwareengine.DeletePrivateCloudRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_private_cloud]

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
            vmwareengine_resources.PrivateCloud,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def undelete_private_cloud(
        self,
        request: Optional[Union[vmwareengine.UndeletePrivateCloudRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Restores a private cloud that was previously scheduled for
        deletion by ``DeletePrivateCloud``. A ``PrivateCloud`` resource
        scheduled for deletion has ``PrivateCloud.state`` set to
        ``DELETED`` and ``PrivateCloud.expireTime`` set to the time when
        deletion can no longer be reversed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_undelete_private_cloud():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.UndeletePrivateCloudRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.undelete_private_cloud(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UndeletePrivateCloudRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UndeletePrivateCloud][google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud]
            name (str):
                Required. The resource name of the private cloud
                scheduled for deletion. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateCloud` Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

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
        if not isinstance(request, vmwareengine.UndeletePrivateCloudRequest):
            request = vmwareengine.UndeletePrivateCloudRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.undelete_private_cloud]

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
            vmwareengine_resources.PrivateCloud,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_clusters(
        self,
        request: Optional[Union[vmwareengine.ListClustersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListClustersPager:
        r"""Lists ``Cluster`` resources in a given private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_clusters():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_clusters(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListClustersRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListClusters][google.cloud.vmwareengine.v1.VmwareEngine.ListClusters]
            parent (str):
                Required. The resource name of the private cloud to
                query for clusters. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListClustersPager:
                Response message for
                   [VmwareEngine.ListClusters][google.cloud.vmwareengine.v1.VmwareEngine.ListClusters]

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
        if not isinstance(request, vmwareengine.ListClustersRequest):
            request = vmwareengine.ListClustersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_clusters]

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
        response = pagers.ListClustersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_cluster(
        self,
        request: Optional[Union[vmwareengine.GetClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.Cluster:
        r"""Retrieves a ``Cluster`` resource by its resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_cluster():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetClusterRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetCluster][google.cloud.vmwareengine.v1.VmwareEngine.GetCluster]
            name (str):
                Required. The cluster resource name to retrieve.
                Resource names are schemeless URIs that follow the
                conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``

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
            google.cloud.vmwareengine_v1.types.Cluster:
                A cluster in a private cloud.
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
        if not isinstance(request, vmwareengine.GetClusterRequest):
            request = vmwareengine.GetClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_cluster]

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

    def create_cluster(
        self,
        request: Optional[Union[vmwareengine.CreateClusterRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        cluster: Optional[vmwareengine_resources.Cluster] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new cluster in a given private cloud. Creating a new
        cluster provides additional nodes for use in the parent private
        cloud and requires sufficient `node
        quota <https://cloud.google.com/vmware-engine/quotas>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_cluster():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.CreateClusterRequest(
                    parent="parent_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                operation = client.create_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateClusterRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateCluster][google.cloud.vmwareengine.v1.VmwareEngine.CreateCluster]
            parent (str):
                Required. The resource name of the private cloud to
                create a new cluster in. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster (google.cloud.vmwareengine_v1.types.Cluster):
                Required. The initial description of
                the new cluster.

                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (str):
                Required. The user-provided identifier of the new
                ``Cluster``. This identifier must be unique among
                clusters within the parent and becomes the final token
                in the name URI. The identifier must meet the following
                requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``cluster_id`` field
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
                :class:`google.cloud.vmwareengine_v1.types.Cluster` A
                cluster in a private cloud.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, cluster, cluster_id]
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
        if not isinstance(request, vmwareengine.CreateClusterRequest):
            request = vmwareengine.CreateClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if cluster is not None:
                request.cluster = cluster
            if cluster_id is not None:
                request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_cluster]

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
            vmwareengine_resources.Cluster,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_cluster(
        self,
        request: Optional[Union[vmwareengine.UpdateClusterRequest, dict]] = None,
        *,
        cluster: Optional[vmwareengine_resources.Cluster] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Modifies a ``Cluster`` resource. Only fields specified in
        ``updateMask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_cluster():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.UpdateClusterRequest(
                )

                # Make the request
                operation = client.update_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateClusterRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateCluster][google.cloud.vmwareengine.v1.VmwareEngine.UpdateCluster]
            cluster (google.cloud.vmwareengine_v1.types.Cluster):
                Required. The description of the
                cluster.

                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``Cluster`` resource by the update.
                The fields specified in the ``updateMask`` are relative
                to the resource, not the full request. A field will be
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

                The result type for the operation will be
                :class:`google.cloud.vmwareengine_v1.types.Cluster` A
                cluster in a private cloud.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [cluster, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateClusterRequest):
            request = vmwareengine.UpdateClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if cluster is not None:
                request.cluster = cluster
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("cluster.name", request.cluster.name),)
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
            vmwareengine_resources.Cluster,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_cluster(
        self,
        request: Optional[Union[vmwareengine.DeleteClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``Cluster`` resource. To avoid unintended data loss,
        migrate or gracefully shut down any workloads running on the
        cluster before deletion. You cannot delete the management
        cluster of a private cloud using this method.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_cluster():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteClusterRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteCluster][google.cloud.vmwareengine.v1.VmwareEngine.DeleteCluster]
            name (str):
                Required. The resource name of the cluster to delete.
                Resource names are schemeless URIs that follow the
                conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``

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
        if not isinstance(request, vmwareengine.DeleteClusterRequest):
            request = vmwareengine.DeleteClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_cluster]

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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_nodes(
        self,
        request: Optional[Union[vmwareengine.ListNodesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNodesPager:
        r"""Lists nodes in a given cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_nodes():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListNodesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_nodes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListNodesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListNodes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodes]
            parent (str):
                Required. The resource name of the cluster to be queried
                for nodes. Resource names are schemeless URIs that
                follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListNodesPager:
                Response message for
                   [VmwareEngine.ListNodes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodes]

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
        if not isinstance(request, vmwareengine.ListNodesRequest):
            request = vmwareengine.ListNodesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_nodes]

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
        response = pagers.ListNodesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_node(
        self,
        request: Optional[Union[vmwareengine.GetNodeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.Node:
        r"""Gets details of a single node.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_node():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetNodeRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_node(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetNodeRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetNode][google.cloud.vmwareengine.v1.VmwareEngine.GetNode]
            name (str):
                Required. The resource name of the node to retrieve. For
                example:
                ``projects/{project}/locations/{location}/privateClouds/{private_cloud}/clusters/{cluster}/nodes/{node}``

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
            google.cloud.vmwareengine_v1.types.Node:
                Node in a cluster.
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
        if not isinstance(request, vmwareengine.GetNodeRequest):
            request = vmwareengine.GetNodeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_node]

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

    def list_external_addresses(
        self,
        request: Optional[
            Union[vmwareengine.ListExternalAddressesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListExternalAddressesPager:
        r"""Lists external IP addresses assigned to VMware
        workload VMs in a given private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_external_addresses():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListExternalAddressesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_external_addresses(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListExternalAddressesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses]
            parent (str):
                Required. The resource name of the private cloud to be
                queried for external IP addresses. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListExternalAddressesPager:
                Response message for
                   [VmwareEngine.ListExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses]

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
        if not isinstance(request, vmwareengine.ListExternalAddressesRequest):
            request = vmwareengine.ListExternalAddressesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_external_addresses]

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
        response = pagers.ListExternalAddressesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def fetch_network_policy_external_addresses(
        self,
        request: Optional[
            Union[vmwareengine.FetchNetworkPolicyExternalAddressesRequest, dict]
        ] = None,
        *,
        network_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchNetworkPolicyExternalAddressesPager:
        r"""Lists external IP addresses assigned to VMware
        workload VMs within the scope of the given network
        policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_fetch_network_policy_external_addresses():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.FetchNetworkPolicyExternalAddressesRequest(
                    network_policy="network_policy_value",
                )

                # Make the request
                page_result = client.fetch_network_policy_external_addresses(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.FetchNetworkPolicyExternalAddressesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.FetchNetworkPolicyExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses]
            network_policy (str):
                Required. The resource name of the network policy to
                query for assigned external IP addresses. Resource names
                are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-policy``

                This corresponds to the ``network_policy`` field
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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.FetchNetworkPolicyExternalAddressesPager:
                Response message for
                   [VmwareEngine.FetchNetworkPolicyExternalAddresses][google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses]

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [network_policy]
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
            request, vmwareengine.FetchNetworkPolicyExternalAddressesRequest
        ):
            request = vmwareengine.FetchNetworkPolicyExternalAddressesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if network_policy is not None:
                request.network_policy = network_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.fetch_network_policy_external_addresses
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("network_policy", request.network_policy),)
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.FetchNetworkPolicyExternalAddressesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_external_address(
        self,
        request: Optional[Union[vmwareengine.GetExternalAddressRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.ExternalAddress:
        r"""Gets details of a single external IP address.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_external_address():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetExternalAddressRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_external_address(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetExternalAddressRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAddress]
            name (str):
                Required. The resource name of the external IP address
                to retrieve. Resource names are schemeless URIs that
                follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip``

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
            google.cloud.vmwareengine_v1.types.ExternalAddress:
                Represents an allocated external IP
                address and its corresponding internal
                IP address in a private cloud.

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
        if not isinstance(request, vmwareengine.GetExternalAddressRequest):
            request = vmwareengine.GetExternalAddressRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_external_address]

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

    def create_external_address(
        self,
        request: Optional[
            Union[vmwareengine.CreateExternalAddressRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        external_address: Optional[vmwareengine_resources.ExternalAddress] = None,
        external_address_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ``ExternalAddress`` resource in a given private
        cloud. The network policy that corresponds to the private cloud
        must have the external IP address network service enabled
        (``NetworkPolicy.external_ip``).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_external_address():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.CreateExternalAddressRequest(
                    parent="parent_value",
                    external_address_id="external_address_id_value",
                )

                # Make the request
                operation = client.create_external_address(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateExternalAddressRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAddress]
            parent (str):
                Required. The resource name of the private cloud to
                create a new external IP address in. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            external_address (google.cloud.vmwareengine_v1.types.ExternalAddress):
                Required. The initial description of
                a new external IP address.

                This corresponds to the ``external_address`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            external_address_id (str):
                Required. The user-provided identifier of the
                ``ExternalAddress`` to be created. This identifier must
                be unique among ``ExternalAddress`` resources within the
                parent and becomes the final token in the name URI. The
                identifier must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``external_address_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ExternalAddress` Represents an allocated external IP address and its corresponding internal IP
                   address in a private cloud.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, external_address, external_address_id]
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
        if not isinstance(request, vmwareengine.CreateExternalAddressRequest):
            request = vmwareengine.CreateExternalAddressRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if external_address is not None:
                request.external_address = external_address
            if external_address_id is not None:
                request.external_address_id = external_address_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_external_address]

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
            vmwareengine_resources.ExternalAddress,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_external_address(
        self,
        request: Optional[
            Union[vmwareengine.UpdateExternalAddressRequest, dict]
        ] = None,
        *,
        external_address: Optional[vmwareengine_resources.ExternalAddress] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single external IP address. Only
        fields specified in ``update_mask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_external_address():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.UpdateExternalAddressRequest(
                )

                # Make the request
                operation = client.update_external_address(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateExternalAddressRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAddress]
            external_address (google.cloud.vmwareengine_v1.types.ExternalAddress):
                Required. External IP address
                description.

                This corresponds to the ``external_address`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``ExternalAddress`` resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ExternalAddress` Represents an allocated external IP address and its corresponding internal IP
                   address in a private cloud.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [external_address, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateExternalAddressRequest):
            request = vmwareengine.UpdateExternalAddressRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if external_address is not None:
                request.external_address = external_address
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_external_address]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("external_address.name", request.external_address.name),)
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
            vmwareengine_resources.ExternalAddress,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_external_address(
        self,
        request: Optional[
            Union[vmwareengine.DeleteExternalAddressRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single external IP address. When you delete
        an external IP address, connectivity between the
        external IP address and the corresponding internal IP
        address is lost.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_external_address():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteExternalAddressRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_external_address(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteExternalAddressRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteExternalAddress][google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAddress]
            name (str):
                Required. The resource name of the external IP address
                to delete. Resource names are schemeless URIs that
                follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip``

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
        if not isinstance(request, vmwareengine.DeleteExternalAddressRequest):
            request = vmwareengine.DeleteExternalAddressRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_external_address]

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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_subnets(
        self,
        request: Optional[Union[vmwareengine.ListSubnetsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSubnetsPager:
        r"""Lists subnets in a given private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_subnets():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListSubnetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_subnets(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListSubnetsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListSubnets][google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets]
            parent (str):
                Required. The resource name of the private cloud to be
                queried for subnets. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListSubnetsPager:
                Response message for
                   [VmwareEngine.ListSubnets][google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets]

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
        if not isinstance(request, vmwareengine.ListSubnetsRequest):
            request = vmwareengine.ListSubnetsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_subnets]

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
        response = pagers.ListSubnetsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_subnet(
        self,
        request: Optional[Union[vmwareengine.GetSubnetRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.Subnet:
        r"""Gets details of a single subnet.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_subnet():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetSubnetRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_subnet(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetSubnetRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetSubnet][google.cloud.vmwareengine.v1.VmwareEngine.GetSubnet]
            name (str):
                Required. The resource name of the subnet to retrieve.
                Resource names are schemeless URIs that follow the
                conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet``

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
            google.cloud.vmwareengine_v1.types.Subnet:
                Subnet in a private cloud. Either management subnets (such as vMotion) that
                   are read-only, or userDefined, which can also be
                   updated.

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
        if not isinstance(request, vmwareengine.GetSubnetRequest):
            request = vmwareengine.GetSubnetRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_subnet]

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

    def update_subnet(
        self,
        request: Optional[Union[vmwareengine.UpdateSubnetRequest, dict]] = None,
        *,
        subnet: Optional[vmwareengine_resources.Subnet] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single subnet. Only fields specified
        in ``update_mask`` are applied.

        *Note*: This API is synchronous and always returns a successful
        ``google.longrunning.Operation`` (LRO). The returned LRO will
        only have ``done`` and ``response`` fields.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_subnet():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.UpdateSubnetRequest(
                )

                # Make the request
                operation = client.update_subnet(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateSubnetRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateSubnet][google.cloud.vmwareengine.v1.VmwareEngine.UpdateSubnet]
            subnet (google.cloud.vmwareengine_v1.types.Subnet):
                Required. Subnet description.
                This corresponds to the ``subnet`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``Subnet`` resource by the update.
                The fields specified in the ``update_mask`` are relative
                to the resource, not the full request. A field will be
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.Subnet` Subnet in a private cloud. Either management subnets (such as vMotion) that
                   are read-only, or userDefined, which can also be
                   updated.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [subnet, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateSubnetRequest):
            request = vmwareengine.UpdateSubnetRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if subnet is not None:
                request.subnet = subnet
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_subnet]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("subnet.name", request.subnet.name),)
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
            vmwareengine_resources.Subnet,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_external_access_rules(
        self,
        request: Optional[
            Union[vmwareengine.ListExternalAccessRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListExternalAccessRulesPager:
        r"""Lists ``ExternalAccessRule`` resources in the specified network
        policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_external_access_rules():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListExternalAccessRulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_external_access_rules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListExternalAccessRulesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListExternalAccessRules][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules]
            parent (str):
                Required. The resource name of the network policy to
                query for external access firewall rules. Resource names
                are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-policy``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListExternalAccessRulesPager:
                Response message for
                   [VmwareEngine.ListExternalAccessRules][google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules]

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
        if not isinstance(request, vmwareengine.ListExternalAccessRulesRequest):
            request = vmwareengine.ListExternalAccessRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_external_access_rules
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
        response = pagers.ListExternalAccessRulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_external_access_rule(
        self,
        request: Optional[
            Union[vmwareengine.GetExternalAccessRuleRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.ExternalAccessRule:
        r"""Gets details of a single external access rule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_external_access_rule():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetExternalAccessRuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_external_access_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetExternalAccessRuleRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAccessRule]
            name (str):
                Required. The resource name of the external access
                firewall rule to retrieve. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule``

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
            google.cloud.vmwareengine_v1.types.ExternalAccessRule:
                External access firewall rules for filtering incoming traffic destined to
                   ExternalAddress resources.

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
        if not isinstance(request, vmwareengine.GetExternalAccessRuleRequest):
            request = vmwareengine.GetExternalAccessRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_external_access_rule]

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

    def create_external_access_rule(
        self,
        request: Optional[
            Union[vmwareengine.CreateExternalAccessRuleRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        external_access_rule: Optional[
            vmwareengine_resources.ExternalAccessRule
        ] = None,
        external_access_rule_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new external access rule in a given network
        policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_external_access_rule():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.CreateExternalAccessRuleRequest(
                    parent="parent_value",
                    external_access_rule_id="external_access_rule_id_value",
                )

                # Make the request
                operation = client.create_external_access_rule(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateExternalAccessRuleRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAccessRule]
            parent (str):
                Required. The resource name of the network policy to
                create a new external access firewall rule in. Resource
                names are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-policy``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            external_access_rule (google.cloud.vmwareengine_v1.types.ExternalAccessRule):
                Required. The initial description of
                a new external access rule.

                This corresponds to the ``external_access_rule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            external_access_rule_id (str):
                Required. The user-provided identifier of the
                ``ExternalAccessRule`` to be created. This identifier
                must be unique among ``ExternalAccessRule`` resources
                within the parent and becomes the final token in the
                name URI. The identifier must meet the following
                requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``external_access_rule_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ExternalAccessRule` External access firewall rules for filtering incoming traffic destined to
                   ExternalAddress resources.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, external_access_rule, external_access_rule_id]
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
        if not isinstance(request, vmwareengine.CreateExternalAccessRuleRequest):
            request = vmwareengine.CreateExternalAccessRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if external_access_rule is not None:
                request.external_access_rule = external_access_rule
            if external_access_rule_id is not None:
                request.external_access_rule_id = external_access_rule_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_external_access_rule
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
            vmwareengine_resources.ExternalAccessRule,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_external_access_rule(
        self,
        request: Optional[
            Union[vmwareengine.UpdateExternalAccessRuleRequest, dict]
        ] = None,
        *,
        external_access_rule: Optional[
            vmwareengine_resources.ExternalAccessRule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single external access rule. Only
        fields specified in ``update_mask`` are applied.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_external_access_rule():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.UpdateExternalAccessRuleRequest(
                )

                # Make the request
                operation = client.update_external_access_rule(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateExternalAccessRuleRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAccessRule]
            external_access_rule (google.cloud.vmwareengine_v1.types.ExternalAccessRule):
                Required. Description of the external
                access rule.

                This corresponds to the ``external_access_rule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``ExternalAccessRule`` resource by
                the update. The fields specified in the ``update_mask``
                are relative to the resource, not the full request. A
                field will be overwritten if it is in the mask. If the
                user does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ExternalAccessRule` External access firewall rules for filtering incoming traffic destined to
                   ExternalAddress resources.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [external_access_rule, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateExternalAccessRuleRequest):
            request = vmwareengine.UpdateExternalAccessRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if external_access_rule is not None:
                request.external_access_rule = external_access_rule
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_external_access_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("external_access_rule.name", request.external_access_rule.name),)
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
            vmwareengine_resources.ExternalAccessRule,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_external_access_rule(
        self,
        request: Optional[
            Union[vmwareengine.DeleteExternalAccessRuleRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single external access rule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_external_access_rule():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteExternalAccessRuleRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_external_access_rule(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteExternalAccessRuleRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteExternalAccessRule][google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAccessRule]
            name (str):
                Required. The resource name of the external access
                firewall rule to delete. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule``

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
        if not isinstance(request, vmwareengine.DeleteExternalAccessRuleRequest):
            request = vmwareengine.DeleteExternalAccessRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_external_access_rule
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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_logging_servers(
        self,
        request: Optional[Union[vmwareengine.ListLoggingServersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListLoggingServersPager:
        r"""Lists logging servers configured for a given private
        cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_logging_servers():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListLoggingServersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_logging_servers(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListLoggingServersRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]
            parent (str):
                Required. The resource name of the private cloud to be
                queried for logging servers. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListLoggingServersPager:
                Response message for
                   [VmwareEngine.ListLoggingServers][google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers]

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
        if not isinstance(request, vmwareengine.ListLoggingServersRequest):
            request = vmwareengine.ListLoggingServersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_logging_servers]

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
        response = pagers.ListLoggingServersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_logging_server(
        self,
        request: Optional[Union[vmwareengine.GetLoggingServerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.LoggingServer:
        r"""Gets details of a logging server.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_logging_server():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetLoggingServerRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_logging_server(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetLoggingServerRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.GetLoggingServer]
            name (str):
                Required. The resource name of the Logging Server to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server``

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
            google.cloud.vmwareengine_v1.types.LoggingServer:
                Logging server to receive vCenter or
                ESXi logs.

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
        if not isinstance(request, vmwareengine.GetLoggingServerRequest):
            request = vmwareengine.GetLoggingServerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_logging_server]

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

    def create_logging_server(
        self,
        request: Optional[Union[vmwareengine.CreateLoggingServerRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        logging_server: Optional[vmwareengine_resources.LoggingServer] = None,
        logging_server_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Create a new logging server for a given private
        cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_logging_server():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                logging_server = vmwareengine_v1.LoggingServer()
                logging_server.hostname = "hostname_value"
                logging_server.port = 453
                logging_server.protocol = "RELP"
                logging_server.source_type = "VCSA"

                request = vmwareengine_v1.CreateLoggingServerRequest(
                    parent="parent_value",
                    logging_server=logging_server,
                    logging_server_id="logging_server_id_value",
                )

                # Make the request
                operation = client.create_logging_server(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateLoggingServerRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.CreateLoggingServer]
            parent (str):
                Required. The resource name of the private cloud to
                create a new Logging Server in. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            logging_server (google.cloud.vmwareengine_v1.types.LoggingServer):
                Required. The initial description of
                a new logging server.

                This corresponds to the ``logging_server`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            logging_server_id (str):
                Required. The user-provided identifier of the
                ``LoggingServer`` to be created. This identifier must be
                unique among ``LoggingServer`` resources within the
                parent and becomes the final token in the name URI. The
                identifier must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``logging_server_id`` field
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
                :class:`google.cloud.vmwareengine_v1.types.LoggingServer`
                Logging server to receive vCenter or ESXi logs.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, logging_server, logging_server_id]
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
        if not isinstance(request, vmwareengine.CreateLoggingServerRequest):
            request = vmwareengine.CreateLoggingServerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if logging_server is not None:
                request.logging_server = logging_server
            if logging_server_id is not None:
                request.logging_server_id = logging_server_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_logging_server]

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
            vmwareengine_resources.LoggingServer,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_logging_server(
        self,
        request: Optional[Union[vmwareengine.UpdateLoggingServerRequest, dict]] = None,
        *,
        logging_server: Optional[vmwareengine_resources.LoggingServer] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single logging server. Only fields
        specified in ``update_mask`` are applied.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_logging_server():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                logging_server = vmwareengine_v1.LoggingServer()
                logging_server.hostname = "hostname_value"
                logging_server.port = 453
                logging_server.protocol = "RELP"
                logging_server.source_type = "VCSA"

                request = vmwareengine_v1.UpdateLoggingServerRequest(
                    logging_server=logging_server,
                )

                # Make the request
                operation = client.update_logging_server(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateLoggingServerRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.UpdateLoggingServer]
            logging_server (google.cloud.vmwareengine_v1.types.LoggingServer):
                Required. Logging server description.
                This corresponds to the ``logging_server`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``LoggingServer`` resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be
                :class:`google.cloud.vmwareengine_v1.types.LoggingServer`
                Logging server to receive vCenter or ESXi logs.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [logging_server, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateLoggingServerRequest):
            request = vmwareengine.UpdateLoggingServerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if logging_server is not None:
                request.logging_server = logging_server
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_logging_server]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("logging_server.name", request.logging_server.name),)
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
            vmwareengine_resources.LoggingServer,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_logging_server(
        self,
        request: Optional[Union[vmwareengine.DeleteLoggingServerRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single logging server.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_logging_server():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteLoggingServerRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_logging_server(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteLoggingServerRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteLoggingServer][google.cloud.vmwareengine.v1.VmwareEngine.DeleteLoggingServer]
            name (str):
                Required. The resource name of the logging server to
                delete. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server``

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
        if not isinstance(request, vmwareengine.DeleteLoggingServerRequest):
            request = vmwareengine.DeleteLoggingServerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_logging_server]

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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_node_types(
        self,
        request: Optional[Union[vmwareengine.ListNodeTypesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNodeTypesPager:
        r"""Lists node types

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_node_types():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListNodeTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_node_types(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListNodeTypesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListNodeTypes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes]
            parent (str):
                Required. The resource name of the location to be
                queried for node types. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1-a``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListNodeTypesPager:
                Response message for
                   [VmwareEngine.ListNodeTypes][google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes]

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
        if not isinstance(request, vmwareengine.ListNodeTypesRequest):
            request = vmwareengine.ListNodeTypesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_node_types]

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
        response = pagers.ListNodeTypesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_node_type(
        self,
        request: Optional[Union[vmwareengine.GetNodeTypeRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.NodeType:
        r"""Gets details of a single ``NodeType``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_node_type():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetNodeTypeRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_node_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetNodeTypeRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetNodeType][google.cloud.vmwareengine.v1.VmwareEngine.GetNodeType]
            name (str):
                Required. The resource name of the node type to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-proj/locations/us-central1-a/nodeTypes/standard-72``

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
            google.cloud.vmwareengine_v1.types.NodeType:
                Describes node type.
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
        if not isinstance(request, vmwareengine.GetNodeTypeRequest):
            request = vmwareengine.GetNodeTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_node_type]

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

    def show_nsx_credentials(
        self,
        request: Optional[Union[vmwareengine.ShowNsxCredentialsRequest, dict]] = None,
        *,
        private_cloud: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.Credentials:
        r"""Gets details of credentials for NSX appliance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_show_nsx_credentials():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ShowNsxCredentialsRequest(
                    private_cloud="private_cloud_value",
                )

                # Make the request
                response = client.show_nsx_credentials(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ShowNsxCredentialsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ShowNsxCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ShowNsxCredentials]
            private_cloud (str):
                Required. The resource name of the private cloud to be
                queried for credentials. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``private_cloud`` field
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
            google.cloud.vmwareengine_v1.types.Credentials:
                Credentials for a private cloud.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [private_cloud]
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
        if not isinstance(request, vmwareengine.ShowNsxCredentialsRequest):
            request = vmwareengine.ShowNsxCredentialsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if private_cloud is not None:
                request.private_cloud = private_cloud

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.show_nsx_credentials]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("private_cloud", request.private_cloud),)
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

        # Done; return the response.
        return response

    def show_vcenter_credentials(
        self,
        request: Optional[
            Union[vmwareengine.ShowVcenterCredentialsRequest, dict]
        ] = None,
        *,
        private_cloud: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.Credentials:
        r"""Gets details of credentials for Vcenter appliance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_show_vcenter_credentials():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ShowVcenterCredentialsRequest(
                    private_cloud="private_cloud_value",
                )

                # Make the request
                response = client.show_vcenter_credentials(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ShowVcenterCredentialsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ShowVcenterCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ShowVcenterCredentials]
            private_cloud (str):
                Required. The resource name of the private cloud to be
                queried for credentials. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``private_cloud`` field
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
            google.cloud.vmwareengine_v1.types.Credentials:
                Credentials for a private cloud.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [private_cloud]
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
        if not isinstance(request, vmwareengine.ShowVcenterCredentialsRequest):
            request = vmwareengine.ShowVcenterCredentialsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if private_cloud is not None:
                request.private_cloud = private_cloud

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.show_vcenter_credentials]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("private_cloud", request.private_cloud),)
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

        # Done; return the response.
        return response

    def reset_nsx_credentials(
        self,
        request: Optional[Union[vmwareengine.ResetNsxCredentialsRequest, dict]] = None,
        *,
        private_cloud: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Resets credentials of the NSX appliance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_reset_nsx_credentials():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ResetNsxCredentialsRequest(
                    private_cloud="private_cloud_value",
                )

                # Make the request
                operation = client.reset_nsx_credentials(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ResetNsxCredentialsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ResetNsxCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ResetNsxCredentials]
            private_cloud (str):
                Required. The resource name of the private cloud to
                reset credentials for. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``private_cloud`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateCloud` Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [private_cloud]
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
        if not isinstance(request, vmwareengine.ResetNsxCredentialsRequest):
            request = vmwareengine.ResetNsxCredentialsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if private_cloud is not None:
                request.private_cloud = private_cloud

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reset_nsx_credentials]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("private_cloud", request.private_cloud),)
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
            vmwareengine_resources.PrivateCloud,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def reset_vcenter_credentials(
        self,
        request: Optional[
            Union[vmwareengine.ResetVcenterCredentialsRequest, dict]
        ] = None,
        *,
        private_cloud: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Resets credentials of the Vcenter appliance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_reset_vcenter_credentials():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ResetVcenterCredentialsRequest(
                    private_cloud="private_cloud_value",
                )

                # Make the request
                operation = client.reset_vcenter_credentials(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ResetVcenterCredentialsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ResetVcenterCredentials][google.cloud.vmwareengine.v1.VmwareEngine.ResetVcenterCredentials]
            private_cloud (str):
                Required. The resource name of the private cloud to
                reset credentials for. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``private_cloud`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateCloud` Represents a private cloud resource. Private clouds of type STANDARD and
                   TIME_LIMITED are zonal resources, STRETCHED private
                   clouds are regional.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [private_cloud]
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
        if not isinstance(request, vmwareengine.ResetVcenterCredentialsRequest):
            request = vmwareengine.ResetVcenterCredentialsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if private_cloud is not None:
                request.private_cloud = private_cloud

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.reset_vcenter_credentials
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("private_cloud", request.private_cloud),)
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
            vmwareengine_resources.PrivateCloud,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_dns_forwarding(
        self,
        request: Optional[Union[vmwareengine.GetDnsForwardingRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.DnsForwarding:
        r"""Gets details of the ``DnsForwarding`` config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_dns_forwarding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetDnsForwardingRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_dns_forwarding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetDnsForwardingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetDnsForwarding][google.cloud.vmwareengine.v1.VmwareEngine.GetDnsForwarding]
            name (str):
                Required. The resource name of a ``DnsForwarding`` to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding``

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
            google.cloud.vmwareengine_v1.types.DnsForwarding:
                DNS forwarding config.
                This config defines a list of domain to
                name server mappings, and is attached to
                the private cloud for custom domain
                resolution.

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
        if not isinstance(request, vmwareengine.GetDnsForwardingRequest):
            request = vmwareengine.GetDnsForwardingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_dns_forwarding]

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

    def update_dns_forwarding(
        self,
        request: Optional[Union[vmwareengine.UpdateDnsForwardingRequest, dict]] = None,
        *,
        dns_forwarding: Optional[vmwareengine_resources.DnsForwarding] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of the ``DnsForwarding`` config, like
        associated domains. Only fields specified in ``update_mask`` are
        applied.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_dns_forwarding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                dns_forwarding = vmwareengine_v1.DnsForwarding()
                dns_forwarding.forwarding_rules.domain = "domain_value"
                dns_forwarding.forwarding_rules.name_servers = ['name_servers_value1', 'name_servers_value2']

                request = vmwareengine_v1.UpdateDnsForwardingRequest(
                    dns_forwarding=dns_forwarding,
                )

                # Make the request
                operation = client.update_dns_forwarding(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateDnsForwardingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateDnsForwarding][google.cloud.vmwareengine.v1.VmwareEngine.UpdateDnsForwarding]
            dns_forwarding (google.cloud.vmwareengine_v1.types.DnsForwarding):
                Required. DnsForwarding config
                details.

                This corresponds to the ``dns_forwarding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``DnsForwarding`` resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.DnsForwarding` DNS forwarding config.
                   This config defines a list of domain to name server
                   mappings, and is attached to the private cloud for
                   custom domain resolution.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [dns_forwarding, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateDnsForwardingRequest):
            request = vmwareengine.UpdateDnsForwardingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if dns_forwarding is not None:
                request.dns_forwarding = dns_forwarding
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_dns_forwarding]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("dns_forwarding.name", request.dns_forwarding.name),)
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
            vmwareengine_resources.DnsForwarding,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_network_peering(
        self,
        request: Optional[Union[vmwareengine.GetNetworkPeeringRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.NetworkPeering:
        r"""Retrieves a ``NetworkPeering`` resource by its resource name.
        The resource contains details of the network peering, such as
        peered networks, import and export custom route configurations,
        and peering state. NetworkPeering is a global resource and
        location can only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_network_peering():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetNetworkPeeringRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_network_peering(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetNetworkPeeringRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPeering]
            name (str):
                Required. The resource name of the network peering to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/networkPeerings/my-peering``

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
            google.cloud.vmwareengine_v1.types.NetworkPeering:
                Details of a network peering.
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
        if not isinstance(request, vmwareengine.GetNetworkPeeringRequest):
            request = vmwareengine.GetNetworkPeeringRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_network_peering]

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

    def list_network_peerings(
        self,
        request: Optional[Union[vmwareengine.ListNetworkPeeringsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNetworkPeeringsPager:
        r"""Lists ``NetworkPeering`` resources in a given project.
        NetworkPeering is a global resource and location can only be
        global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_network_peerings():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListNetworkPeeringsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_network_peerings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListNetworkPeeringsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListNetworkPeerings][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings]
            parent (str):
                Required. The resource name of the location (global) to
                query for network peerings. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/global``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListNetworkPeeringsPager:
                Response message for
                   [VmwareEngine.ListNetworkPeerings][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings]

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
        if not isinstance(request, vmwareengine.ListNetworkPeeringsRequest):
            request = vmwareengine.ListNetworkPeeringsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_network_peerings]

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
        response = pagers.ListNetworkPeeringsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_network_peering(
        self,
        request: Optional[Union[vmwareengine.CreateNetworkPeeringRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        network_peering: Optional[vmwareengine_resources.NetworkPeering] = None,
        network_peering_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new network peering between the peer network and
        VMware Engine network provided in a ``NetworkPeering`` resource.
        NetworkPeering is a global resource and location can only be
        global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_network_peering():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                network_peering = vmwareengine_v1.NetworkPeering()
                network_peering.peer_network = "peer_network_value"
                network_peering.peer_network_type = "GOOGLE_CLOUD_NETAPP_VOLUMES"
                network_peering.vmware_engine_network = "vmware_engine_network_value"

                request = vmwareengine_v1.CreateNetworkPeeringRequest(
                    parent="parent_value",
                    network_peering_id="network_peering_id_value",
                    network_peering=network_peering,
                )

                # Make the request
                operation = client.create_network_peering(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateNetworkPeeringRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPeering]
            parent (str):
                Required. The resource name of the location to create
                the new network peering in. This value is always
                ``global``, because ``NetworkPeering`` is a global
                resource. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/global``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            network_peering (google.cloud.vmwareengine_v1.types.NetworkPeering):
                Required. The initial description of
                the new network peering.

                This corresponds to the ``network_peering`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            network_peering_id (str):
                Required. The user-provided identifier of the new
                ``NetworkPeering``. This identifier must be unique among
                ``NetworkPeering`` resources within the parent and
                becomes the final token in the name URI. The identifier
                must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``network_peering_id`` field
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
                :class:`google.cloud.vmwareengine_v1.types.NetworkPeering`
                Details of a network peering.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, network_peering, network_peering_id]
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
        if not isinstance(request, vmwareengine.CreateNetworkPeeringRequest):
            request = vmwareengine.CreateNetworkPeeringRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if network_peering is not None:
                request.network_peering = network_peering
            if network_peering_id is not None:
                request.network_peering_id = network_peering_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_network_peering]

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
            vmwareengine_resources.NetworkPeering,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_network_peering(
        self,
        request: Optional[Union[vmwareengine.DeleteNetworkPeeringRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``NetworkPeering`` resource. When a network peering is
        deleted for a VMware Engine network, the peer network becomes
        inaccessible to that VMware Engine network. NetworkPeering is a
        global resource and location can only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_network_peering():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteNetworkPeeringRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_network_peering(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteNetworkPeeringRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPeering]
            name (str):
                Required. The resource name of the network peering to be
                deleted. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/networkPeerings/my-peering``

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
        if not isinstance(request, vmwareengine.DeleteNetworkPeeringRequest):
            request = vmwareengine.DeleteNetworkPeeringRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_network_peering]

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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_network_peering(
        self,
        request: Optional[Union[vmwareengine.UpdateNetworkPeeringRequest, dict]] = None,
        *,
        network_peering: Optional[vmwareengine_resources.NetworkPeering] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Modifies a ``NetworkPeering`` resource. Only the ``description``
        field can be updated. Only fields specified in ``updateMask``
        are applied. NetworkPeering is a global resource and location
        can only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_network_peering():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                network_peering = vmwareengine_v1.NetworkPeering()
                network_peering.peer_network = "peer_network_value"
                network_peering.peer_network_type = "GOOGLE_CLOUD_NETAPP_VOLUMES"
                network_peering.vmware_engine_network = "vmware_engine_network_value"

                request = vmwareengine_v1.UpdateNetworkPeeringRequest(
                    network_peering=network_peering,
                )

                # Make the request
                operation = client.update_network_peering(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateNetworkPeeringRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateNetworkPeering][google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPeering]
            network_peering (google.cloud.vmwareengine_v1.types.NetworkPeering):
                Required. Network peering
                description.

                This corresponds to the ``network_peering`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``NetworkPeering`` resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be
                :class:`google.cloud.vmwareengine_v1.types.NetworkPeering`
                Details of a network peering.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [network_peering, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateNetworkPeeringRequest):
            request = vmwareengine.UpdateNetworkPeeringRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if network_peering is not None:
                request.network_peering = network_peering
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_network_peering]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("network_peering.name", request.network_peering.name),)
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
            vmwareengine_resources.NetworkPeering,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_peering_routes(
        self,
        request: Optional[Union[vmwareengine.ListPeeringRoutesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPeeringRoutesPager:
        r"""Lists the network peering routes exchanged over a
        peering connection. NetworkPeering is a global resource
        and location can only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_peering_routes():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListPeeringRoutesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_peering_routes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListPeeringRoutesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes]
            parent (str):
                Required. The resource name of the network peering to
                retrieve peering routes from. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/networkPeerings/my-peering``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListPeeringRoutesPager:
                Response message for
                   [VmwareEngine.ListPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes]

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
        if not isinstance(request, vmwareengine.ListPeeringRoutesRequest):
            request = vmwareengine.ListPeeringRoutesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_peering_routes]

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
        response = pagers.ListPeeringRoutesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_hcx_activation_key(
        self,
        request: Optional[
            Union[vmwareengine.CreateHcxActivationKeyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        hcx_activation_key: Optional[vmwareengine_resources.HcxActivationKey] = None,
        hcx_activation_key_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new HCX activation key in a given private
        cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_hcx_activation_key():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.CreateHcxActivationKeyRequest(
                    parent="parent_value",
                    hcx_activation_key_id="hcx_activation_key_id_value",
                )

                # Make the request
                operation = client.create_hcx_activation_key(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateHcxActivationKeyRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]
            parent (str):
                Required. The resource name of the private cloud to
                create the key for. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/privateClouds/my-cloud``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hcx_activation_key (google.cloud.vmwareengine_v1.types.HcxActivationKey):
                Required. The initial description of
                a new HCX activation key. When creating
                a new key, this field must be an empty
                object.

                This corresponds to the ``hcx_activation_key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hcx_activation_key_id (str):
                Required. The user-provided identifier of the
                ``HcxActivationKey`` to be created. This identifier must
                be unique among ``HcxActivationKey`` resources within
                the parent and becomes the final token in the name URI.
                The identifier must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``hcx_activation_key_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.HcxActivationKey` HCX activation key. A default key is created during
                   private cloud provisioning, but this behavior is
                   subject to change and you should always verify active
                   keys. Use
                   [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]
                   to retrieve existing keys and
                   [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]
                   to create new ones.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hcx_activation_key, hcx_activation_key_id]
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
        if not isinstance(request, vmwareengine.CreateHcxActivationKeyRequest):
            request = vmwareengine.CreateHcxActivationKeyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if hcx_activation_key is not None:
                request.hcx_activation_key = hcx_activation_key
            if hcx_activation_key_id is not None:
                request.hcx_activation_key_id = hcx_activation_key_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_hcx_activation_key
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
            vmwareengine_resources.HcxActivationKey,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_hcx_activation_keys(
        self,
        request: Optional[
            Union[vmwareengine.ListHcxActivationKeysRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHcxActivationKeysPager:
        r"""Lists ``HcxActivationKey`` resources in a given private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_hcx_activation_keys():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListHcxActivationKeysRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hcx_activation_keys(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListHcxActivationKeysRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]
            parent (str):
                Required. The resource name of the private cloud to be
                queried for HCX activation keys. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListHcxActivationKeysPager:
                Response message for
                   [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]

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
        if not isinstance(request, vmwareengine.ListHcxActivationKeysRequest):
            request = vmwareengine.ListHcxActivationKeysRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_hcx_activation_keys]

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
        response = pagers.ListHcxActivationKeysPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_hcx_activation_key(
        self,
        request: Optional[Union[vmwareengine.GetHcxActivationKeyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.HcxActivationKey:
        r"""Retrieves a ``HcxActivationKey`` resource by its resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_hcx_activation_key():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetHcxActivationKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_hcx_activation_key(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetHcxActivationKeyRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetHcxActivationKeys][]
            name (str):
                Required. The resource name of the HCX activation key to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key``

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
            google.cloud.vmwareengine_v1.types.HcxActivationKey:
                HCX activation key. A default key is created during
                   private cloud provisioning, but this behavior is
                   subject to change and you should always verify active
                   keys. Use
                   [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]
                   to retrieve existing keys and
                   [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]
                   to create new ones.

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
        if not isinstance(request, vmwareengine.GetHcxActivationKeyRequest):
            request = vmwareengine.GetHcxActivationKeyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_hcx_activation_key]

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

    def get_network_policy(
        self,
        request: Optional[Union[vmwareengine.GetNetworkPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.NetworkPolicy:
        r"""Retrieves a ``NetworkPolicy`` resource by its resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_network_policy():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetNetworkPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_network_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetNetworkPolicyRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPolicy]
            name (str):
                Required. The resource name of the network policy to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-network-policy``

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
            google.cloud.vmwareengine_v1.types.NetworkPolicy:
                Represents a network policy resource.
                Network policies are regional resources.
                You can use a network policy to enable
                or disable internet access and external
                IP access. Network policies are
                associated with a VMware Engine network,
                which might span across regions. For a
                given region, a network policy applies
                to all private clouds in the VMware
                Engine network associated with the
                policy.

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
        if not isinstance(request, vmwareengine.GetNetworkPolicyRequest):
            request = vmwareengine.GetNetworkPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_network_policy]

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

    def list_network_policies(
        self,
        request: Optional[Union[vmwareengine.ListNetworkPoliciesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNetworkPoliciesPager:
        r"""Lists ``NetworkPolicy`` resources in a specified project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_network_policies():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListNetworkPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_network_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListNetworkPoliciesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListNetworkPolicies][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies]
            parent (str):
                Required. The resource name of the location (region) to
                query for network policies. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListNetworkPoliciesPager:
                Response message for
                   [VmwareEngine.ListNetworkPolicies][google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies]

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
        if not isinstance(request, vmwareengine.ListNetworkPoliciesRequest):
            request = vmwareengine.ListNetworkPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_network_policies]

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
        response = pagers.ListNetworkPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_network_policy(
        self,
        request: Optional[Union[vmwareengine.CreateNetworkPolicyRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        network_policy: Optional[vmwareengine_resources.NetworkPolicy] = None,
        network_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new network policy in a given VMware Engine
        network of a project and location (region). A new
        network policy cannot be created if another network
        policy already exists in the same scope.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_network_policy():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                network_policy = vmwareengine_v1.NetworkPolicy()
                network_policy.edge_services_cidr = "edge_services_cidr_value"

                request = vmwareengine_v1.CreateNetworkPolicyRequest(
                    parent="parent_value",
                    network_policy_id="network_policy_id_value",
                    network_policy=network_policy,
                )

                # Make the request
                operation = client.create_network_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateNetworkPolicyRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPolicy]
            parent (str):
                Required. The resource name of the location (region) to
                create the new network policy in. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            network_policy (google.cloud.vmwareengine_v1.types.NetworkPolicy):
                Required. The network policy
                configuration to use in the request.

                This corresponds to the ``network_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            network_policy_id (str):
                Required. The user-provided identifier of the network
                policy to be created. This identifier must be unique
                within parent
                ``projects/{my-project}/locations/{us-central1}/networkPolicies``
                and becomes the final token in the name URI. The
                identifier must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``network_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.NetworkPolicy` Represents a network policy resource. Network policies are regional
                   resources. You can use a network policy to enable or
                   disable internet access and external IP access.
                   Network policies are associated with a VMware Engine
                   network, which might span across regions. For a given
                   region, a network policy applies to all private
                   clouds in the VMware Engine network associated with
                   the policy.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, network_policy, network_policy_id]
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
        if not isinstance(request, vmwareengine.CreateNetworkPolicyRequest):
            request = vmwareengine.CreateNetworkPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if network_policy is not None:
                request.network_policy = network_policy
            if network_policy_id is not None:
                request.network_policy_id = network_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_network_policy]

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
            vmwareengine_resources.NetworkPolicy,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_network_policy(
        self,
        request: Optional[Union[vmwareengine.UpdateNetworkPolicyRequest, dict]] = None,
        *,
        network_policy: Optional[vmwareengine_resources.NetworkPolicy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Modifies a ``NetworkPolicy`` resource. Only the following fields
        can be updated: ``internet_access``, ``external_ip``,
        ``edge_services_cidr``. Only fields specified in ``updateMask``
        are applied. When updating a network policy, the external IP
        network service can only be disabled if there are no external IP
        addresses present in the scope of the policy. Also, a
        ``NetworkService`` cannot be updated when
        ``NetworkService.state`` is set to ``RECONCILING``.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_network_policy():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                network_policy = vmwareengine_v1.NetworkPolicy()
                network_policy.edge_services_cidr = "edge_services_cidr_value"

                request = vmwareengine_v1.UpdateNetworkPolicyRequest(
                    network_policy=network_policy,
                )

                # Make the request
                operation = client.update_network_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateNetworkPolicyRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPolicy]
            network_policy (google.cloud.vmwareengine_v1.types.NetworkPolicy):
                Required. Network policy description.
                This corresponds to the ``network_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``NetworkPolicy`` resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.NetworkPolicy` Represents a network policy resource. Network policies are regional
                   resources. You can use a network policy to enable or
                   disable internet access and external IP access.
                   Network policies are associated with a VMware Engine
                   network, which might span across regions. For a given
                   region, a network policy applies to all private
                   clouds in the VMware Engine network associated with
                   the policy.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [network_policy, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateNetworkPolicyRequest):
            request = vmwareengine.UpdateNetworkPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if network_policy is not None:
                request.network_policy = network_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_network_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("network_policy.name", request.network_policy.name),)
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
            vmwareengine_resources.NetworkPolicy,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_network_policy(
        self,
        request: Optional[Union[vmwareengine.DeleteNetworkPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``NetworkPolicy`` resource. A network policy cannot be
        deleted when ``NetworkService.state`` is set to ``RECONCILING``
        for either its external IP or internet access service.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_network_policy():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteNetworkPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_network_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteNetworkPolicyRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteNetworkPolicy][google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPolicy]
            name (str):
                Required. The resource name of the network policy to
                delete. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/networkPolicies/my-network-policy``

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
        if not isinstance(request, vmwareengine.DeleteNetworkPolicyRequest):
            request = vmwareengine.DeleteNetworkPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_network_policy]

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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_management_dns_zone_bindings(
        self,
        request: Optional[
            Union[vmwareengine.ListManagementDnsZoneBindingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListManagementDnsZoneBindingsPager:
        r"""Lists Consumer VPCs bound to Management DNS Zone of a
        given private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_management_dns_zone_bindings():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListManagementDnsZoneBindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_management_dns_zone_bindings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListManagementDnsZoneBindingsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListManagementDnsZoneBindings][google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings]
            parent (str):
                Required. The resource name of the private cloud to be
                queried for management DNS zone bindings. Resource names
                are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListManagementDnsZoneBindingsPager:
                Response message for
                   [VmwareEngine.ListManagementDnsZoneBindings][google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings]

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
        if not isinstance(request, vmwareengine.ListManagementDnsZoneBindingsRequest):
            request = vmwareengine.ListManagementDnsZoneBindingsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_management_dns_zone_bindings
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
        response = pagers.ListManagementDnsZoneBindingsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_management_dns_zone_binding(
        self,
        request: Optional[
            Union[vmwareengine.GetManagementDnsZoneBindingRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.ManagementDnsZoneBinding:
        r"""Retrieves a 'ManagementDnsZoneBinding' resource by
        its resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_management_dns_zone_binding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetManagementDnsZoneBindingRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_management_dns_zone_binding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetManagementDnsZoneBindingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.GetManagementDnsZoneBinding]
            name (str):
                Required. The resource name of the management DNS zone
                binding to retrieve. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``

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
            google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding:
                Represents a binding between a
                network and the management DNS zone. A
                management DNS zone is the Cloud DNS
                cross-project binding zone that VMware
                Engine creates for each private cloud.
                It contains FQDNs and corresponding IP
                addresses for the private cloud's ESXi
                hosts and management VM appliances like
                vCenter and NSX Manager.

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
        if not isinstance(request, vmwareengine.GetManagementDnsZoneBindingRequest):
            request = vmwareengine.GetManagementDnsZoneBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_management_dns_zone_binding
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

    def create_management_dns_zone_binding(
        self,
        request: Optional[
            Union[vmwareengine.CreateManagementDnsZoneBindingRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        management_dns_zone_binding: Optional[
            vmwareengine_resources.ManagementDnsZoneBinding
        ] = None,
        management_dns_zone_binding_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ``ManagementDnsZoneBinding`` resource in a private
        cloud. This RPC creates the DNS binding and the resource that
        represents the DNS binding of the consumer VPC network to the
        management DNS zone. A management DNS zone is the Cloud DNS
        cross-project binding zone that VMware Engine creates for each
        private cloud. It contains FQDNs and corresponding IP addresses
        for the private cloud's ESXi hosts and management VM appliances
        like vCenter and NSX Manager.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_management_dns_zone_binding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                management_dns_zone_binding = vmwareengine_v1.ManagementDnsZoneBinding()
                management_dns_zone_binding.vpc_network = "vpc_network_value"

                request = vmwareengine_v1.CreateManagementDnsZoneBindingRequest(
                    parent="parent_value",
                    management_dns_zone_binding=management_dns_zone_binding,
                    management_dns_zone_binding_id="management_dns_zone_binding_id_value",
                )

                # Make the request
                operation = client.create_management_dns_zone_binding(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateManagementDnsZoneBindingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateManagementDnsZoneBindings][]
            parent (str):
                Required. The resource name of the private cloud to
                create a new management DNS zone binding for. Resource
                names are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            management_dns_zone_binding (google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding):
                Required. The initial values for a
                new management DNS zone binding.

                This corresponds to the ``management_dns_zone_binding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            management_dns_zone_binding_id (str):
                Required. The user-provided identifier of the
                ``ManagementDnsZoneBinding`` resource to be created.
                This identifier must be unique among
                ``ManagementDnsZoneBinding`` resources within the parent
                and becomes the final token in the name URI. The
                identifier must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``management_dns_zone_binding_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding` Represents a binding between a network and the management DNS zone.
                   A management DNS zone is the Cloud DNS cross-project
                   binding zone that VMware Engine creates for each
                   private cloud. It contains FQDNs and corresponding IP
                   addresses for the private cloud's ESXi hosts and
                   management VM appliances like vCenter and NSX
                   Manager.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            management_dns_zone_binding,
            management_dns_zone_binding_id,
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
        if not isinstance(request, vmwareengine.CreateManagementDnsZoneBindingRequest):
            request = vmwareengine.CreateManagementDnsZoneBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if management_dns_zone_binding is not None:
                request.management_dns_zone_binding = management_dns_zone_binding
            if management_dns_zone_binding_id is not None:
                request.management_dns_zone_binding_id = management_dns_zone_binding_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_management_dns_zone_binding
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
            vmwareengine_resources.ManagementDnsZoneBinding,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_management_dns_zone_binding(
        self,
        request: Optional[
            Union[vmwareengine.UpdateManagementDnsZoneBindingRequest, dict]
        ] = None,
        *,
        management_dns_zone_binding: Optional[
            vmwareengine_resources.ManagementDnsZoneBinding
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates a ``ManagementDnsZoneBinding`` resource. Only fields
        specified in ``update_mask`` are applied.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_management_dns_zone_binding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                management_dns_zone_binding = vmwareengine_v1.ManagementDnsZoneBinding()
                management_dns_zone_binding.vpc_network = "vpc_network_value"

                request = vmwareengine_v1.UpdateManagementDnsZoneBindingRequest(
                    management_dns_zone_binding=management_dns_zone_binding,
                )

                # Make the request
                operation = client.update_management_dns_zone_binding(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateManagementDnsZoneBindingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.UpdateManagementDnsZoneBinding]
            management_dns_zone_binding (google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding):
                Required. New values to update the
                management DNS zone binding with.

                This corresponds to the ``management_dns_zone_binding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``ManagementDnsZoneBinding`` resource
                by the update. The fields specified in the
                ``update_mask`` are relative to the resource, not the
                full request. A field will be overwritten if it is in
                the mask. If the user does not provide a mask then all
                fields will be overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding` Represents a binding between a network and the management DNS zone.
                   A management DNS zone is the Cloud DNS cross-project
                   binding zone that VMware Engine creates for each
                   private cloud. It contains FQDNs and corresponding IP
                   addresses for the private cloud's ESXi hosts and
                   management VM appliances like vCenter and NSX
                   Manager.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [management_dns_zone_binding, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateManagementDnsZoneBindingRequest):
            request = vmwareengine.UpdateManagementDnsZoneBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if management_dns_zone_binding is not None:
                request.management_dns_zone_binding = management_dns_zone_binding
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_management_dns_zone_binding
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "management_dns_zone_binding.name",
                        request.management_dns_zone_binding.name,
                    ),
                )
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
            vmwareengine_resources.ManagementDnsZoneBinding,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_management_dns_zone_binding(
        self,
        request: Optional[
            Union[vmwareengine.DeleteManagementDnsZoneBindingRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``ManagementDnsZoneBinding`` resource. When a
        management DNS zone binding is deleted, the corresponding
        consumer VPC network is no longer bound to the management DNS
        zone.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_management_dns_zone_binding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteManagementDnsZoneBindingRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_management_dns_zone_binding(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteManagementDnsZoneBindingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteManagementDnsZoneBinding][google.cloud.vmwareengine.v1.VmwareEngine.DeleteManagementDnsZoneBinding]
            name (str):
                Required. The resource name of the management DNS zone
                binding to delete. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``

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
        if not isinstance(request, vmwareengine.DeleteManagementDnsZoneBindingRequest):
            request = vmwareengine.DeleteManagementDnsZoneBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_management_dns_zone_binding
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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def repair_management_dns_zone_binding(
        self,
        request: Optional[
            Union[vmwareengine.RepairManagementDnsZoneBindingRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Retries to create a ``ManagementDnsZoneBinding`` resource that
        is in failed state.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_repair_management_dns_zone_binding():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.RepairManagementDnsZoneBindingRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.repair_management_dns_zone_binding(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.RepairManagementDnsZoneBindingRequest, dict]):
                The request object. Request message for
                [VmwareEngine.RepairManagementDnsZoneBindings][]
            name (str):
                Required. The resource name of the management DNS zone
                binding to repair. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding` Represents a binding between a network and the management DNS zone.
                   A management DNS zone is the Cloud DNS cross-project
                   binding zone that VMware Engine creates for each
                   private cloud. It contains FQDNs and corresponding IP
                   addresses for the private cloud's ESXi hosts and
                   management VM appliances like vCenter and NSX
                   Manager.

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
        if not isinstance(request, vmwareengine.RepairManagementDnsZoneBindingRequest):
            request = vmwareengine.RepairManagementDnsZoneBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.repair_management_dns_zone_binding
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
            vmwareengine_resources.ManagementDnsZoneBinding,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_vmware_engine_network(
        self,
        request: Optional[
            Union[vmwareengine.CreateVmwareEngineNetworkRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        vmware_engine_network: Optional[
            vmwareengine_resources.VmwareEngineNetwork
        ] = None,
        vmware_engine_network_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new VMware Engine network that can be used
        by a private cloud.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_vmware_engine_network():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                vmware_engine_network = vmwareengine_v1.VmwareEngineNetwork()
                vmware_engine_network.type_ = "STANDARD"

                request = vmwareengine_v1.CreateVmwareEngineNetworkRequest(
                    parent="parent_value",
                    vmware_engine_network_id="vmware_engine_network_id_value",
                    vmware_engine_network=vmware_engine_network,
                )

                # Make the request
                operation = client.create_vmware_engine_network(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreateVmwareEngineNetworkRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreateVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.CreateVmwareEngineNetwork]
            parent (str):
                Required. The resource name of the location to create
                the new VMware Engine network in. A VMware Engine
                network of type ``LEGACY`` is a regional resource, and a
                VMware Engine network of type ``STANDARD`` is a global
                resource. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/global``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            vmware_engine_network (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork):
                Required. The initial description of
                the new VMware Engine network.

                This corresponds to the ``vmware_engine_network`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            vmware_engine_network_id (str):
                Required. The user-provided identifier of the new VMware
                Engine network. This identifier must be unique among
                VMware Engine network resources within the parent and
                becomes the final token in the name URI. The identifier
                must meet the following requirements:

                - For networks of type LEGACY, adheres to the format:
                  ``{region-id}-default``. Replace ``{region-id}`` with
                  the region where you want to create the VMware Engine
                  network. For example, "us-central1-default".
                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``vmware_engine_network_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.VmwareEngineNetwork` VMware Engine network resource that provides connectivity for VMware Engine
                   private clouds.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, vmware_engine_network, vmware_engine_network_id]
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
        if not isinstance(request, vmwareengine.CreateVmwareEngineNetworkRequest):
            request = vmwareengine.CreateVmwareEngineNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if vmware_engine_network is not None:
                request.vmware_engine_network = vmware_engine_network
            if vmware_engine_network_id is not None:
                request.vmware_engine_network_id = vmware_engine_network_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_vmware_engine_network
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
            vmwareengine_resources.VmwareEngineNetwork,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_vmware_engine_network(
        self,
        request: Optional[
            Union[vmwareengine.UpdateVmwareEngineNetworkRequest, dict]
        ] = None,
        *,
        vmware_engine_network: Optional[
            vmwareengine_resources.VmwareEngineNetwork
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Modifies a VMware Engine network resource. Only the following
        fields can be updated: ``description``. Only fields specified in
        ``updateMask`` are applied.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_vmware_engine_network():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                vmware_engine_network = vmwareengine_v1.VmwareEngineNetwork()
                vmware_engine_network.type_ = "STANDARD"

                request = vmwareengine_v1.UpdateVmwareEngineNetworkRequest(
                    vmware_engine_network=vmware_engine_network,
                )

                # Make the request
                operation = client.update_vmware_engine_network(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdateVmwareEngineNetworkRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdateVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.UpdateVmwareEngineNetwork]
            vmware_engine_network (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork):
                Required. VMware Engine network
                description.

                This corresponds to the ``vmware_engine_network`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the VMware Engine network resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten. Only the following fields can be updated:
                ``description``.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.VmwareEngineNetwork` VMware Engine network resource that provides connectivity for VMware Engine
                   private clouds.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [vmware_engine_network, update_mask]
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
        if not isinstance(request, vmwareengine.UpdateVmwareEngineNetworkRequest):
            request = vmwareengine.UpdateVmwareEngineNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if vmware_engine_network is not None:
                request.vmware_engine_network = vmware_engine_network
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_vmware_engine_network
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("vmware_engine_network.name", request.vmware_engine_network.name),)
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
            vmwareengine_resources.VmwareEngineNetwork,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_vmware_engine_network(
        self,
        request: Optional[
            Union[vmwareengine.DeleteVmwareEngineNetworkRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``VmwareEngineNetwork`` resource. You can only delete
        a VMware Engine network after all resources that refer to it are
        deleted. For example, a private cloud, a network peering, and a
        network policy can all refer to the same VMware Engine network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_vmware_engine_network():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeleteVmwareEngineNetworkRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_vmware_engine_network(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeleteVmwareEngineNetworkRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeleteVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.DeleteVmwareEngineNetwork]
            name (str):
                Required. The resource name of the VMware Engine network
                to be deleted. Resource names are schemeless URIs that
                follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/vmwareEngineNetworks/my-network``

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
        if not isinstance(request, vmwareengine.DeleteVmwareEngineNetworkRequest):
            request = vmwareengine.DeleteVmwareEngineNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_vmware_engine_network
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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_vmware_engine_network(
        self,
        request: Optional[
            Union[vmwareengine.GetVmwareEngineNetworkRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.VmwareEngineNetwork:
        r"""Retrieves a ``VmwareEngineNetwork`` resource by its resource
        name. The resource contains details of the VMware Engine
        network, such as its VMware Engine network type, peered networks
        in a service project, and state (for example, ``CREATING``,
        ``ACTIVE``, ``DELETING``).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_vmware_engine_network():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetVmwareEngineNetworkRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_vmware_engine_network(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetVmwareEngineNetworkRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetVmwareEngineNetwork][google.cloud.vmwareengine.v1.VmwareEngine.GetVmwareEngineNetwork]
            name (str):
                Required. The resource name of the VMware Engine network
                to retrieve. Resource names are schemeless URIs that
                follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/vmwareEngineNetworks/my-network``

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
            google.cloud.vmwareengine_v1.types.VmwareEngineNetwork:
                VMware Engine network resource that
                provides connectivity for VMware Engine
                private clouds.

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
        if not isinstance(request, vmwareengine.GetVmwareEngineNetworkRequest):
            request = vmwareengine.GetVmwareEngineNetworkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_vmware_engine_network
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

    def list_vmware_engine_networks(
        self,
        request: Optional[
            Union[vmwareengine.ListVmwareEngineNetworksRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListVmwareEngineNetworksPager:
        r"""Lists ``VmwareEngineNetwork`` resources in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_vmware_engine_networks():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListVmwareEngineNetworksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_vmware_engine_networks(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListVmwareEngineNetworksRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListVmwareEngineNetworks][google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks]
            parent (str):
                Required. The resource name of the location to query for
                VMware Engine networks. Resource names are schemeless
                URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/global``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListVmwareEngineNetworksPager:
                Response message for
                   [VmwareEngine.ListVmwareEngineNetworks][google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks]

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
        if not isinstance(request, vmwareengine.ListVmwareEngineNetworksRequest):
            request = vmwareengine.ListVmwareEngineNetworksRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_vmware_engine_networks
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
        response = pagers.ListVmwareEngineNetworksPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_private_connection(
        self,
        request: Optional[
            Union[vmwareengine.CreatePrivateConnectionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        private_connection: Optional[vmwareengine_resources.PrivateConnection] = None,
        private_connection_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new private connection that can be used for
        accessing private Clouds.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_create_private_connection():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                private_connection = vmwareengine_v1.PrivateConnection()
                private_connection.vmware_engine_network = "vmware_engine_network_value"
                private_connection.type_ = "THIRD_PARTY_SERVICE"
                private_connection.service_network = "service_network_value"

                request = vmwareengine_v1.CreatePrivateConnectionRequest(
                    parent="parent_value",
                    private_connection_id="private_connection_id_value",
                    private_connection=private_connection,
                )

                # Make the request
                operation = client.create_private_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.CreatePrivateConnectionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.CreatePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateConnection]
            parent (str):
                Required. The resource name of the location to create
                the new private connection in. Private connection is a
                regional resource. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            private_connection (google.cloud.vmwareengine_v1.types.PrivateConnection):
                Required. The initial description of
                the new private connection.

                This corresponds to the ``private_connection`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            private_connection_id (str):
                Required. The user-provided identifier of the new
                private connection. This identifier must be unique among
                private connection resources within the parent and
                becomes the final token in the name URI. The identifier
                must meet the following requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)

                This corresponds to the ``private_connection_id`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateConnection` Private connection resource that provides connectivity for VMware Engine
                   private clouds.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, private_connection, private_connection_id]
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
        if not isinstance(request, vmwareengine.CreatePrivateConnectionRequest):
            request = vmwareengine.CreatePrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if private_connection is not None:
                request.private_connection = private_connection
            if private_connection_id is not None:
                request.private_connection_id = private_connection_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_private_connection
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
            vmwareengine_resources.PrivateConnection,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_private_connection(
        self,
        request: Optional[Union[vmwareengine.GetPrivateConnectionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.PrivateConnection:
        r"""Retrieves a ``PrivateConnection`` resource by its resource name.
        The resource contains details of the private connection, such as
        connected network, routing mode and state.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_private_connection():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetPrivateConnectionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_private_connection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetPrivateConnectionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetPrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateConnection]
            name (str):
                Required. The resource name of the private connection to
                retrieve. Resource names are schemeless URIs that follow
                the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/privateConnections/my-connection``

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
            google.cloud.vmwareengine_v1.types.PrivateConnection:
                Private connection resource that
                provides connectivity for VMware Engine
                private clouds.

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
        if not isinstance(request, vmwareengine.GetPrivateConnectionRequest):
            request = vmwareengine.GetPrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_private_connection]

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

    def list_private_connections(
        self,
        request: Optional[
            Union[vmwareengine.ListPrivateConnectionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPrivateConnectionsPager:
        r"""Lists ``PrivateConnection`` resources in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_private_connections():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListPrivateConnectionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_private_connections(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListPrivateConnectionsRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListPrivateConnections][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections]
            parent (str):
                Required. The resource name of the location to query for
                private connections. Resource names are schemeless URIs
                that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example: ``projects/my-project/locations/us-central1``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListPrivateConnectionsPager:
                Response message for
                   [VmwareEngine.ListPrivateConnections][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections]

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
        if not isinstance(request, vmwareengine.ListPrivateConnectionsRequest):
            request = vmwareengine.ListPrivateConnectionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_private_connections]

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
        response = pagers.ListPrivateConnectionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_private_connection(
        self,
        request: Optional[
            Union[vmwareengine.UpdatePrivateConnectionRequest, dict]
        ] = None,
        *,
        private_connection: Optional[vmwareengine_resources.PrivateConnection] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Modifies a ``PrivateConnection`` resource. Only ``description``
        and ``routing_mode`` fields can be updated. Only fields
        specified in ``updateMask`` are applied.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_update_private_connection():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                private_connection = vmwareengine_v1.PrivateConnection()
                private_connection.vmware_engine_network = "vmware_engine_network_value"
                private_connection.type_ = "THIRD_PARTY_SERVICE"
                private_connection.service_network = "service_network_value"

                request = vmwareengine_v1.UpdatePrivateConnectionRequest(
                    private_connection=private_connection,
                )

                # Make the request
                operation = client.update_private_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.UpdatePrivateConnectionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.UpdatePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateConnection]
            private_connection (google.cloud.vmwareengine_v1.types.PrivateConnection):
                Required. Private connection
                description.

                This corresponds to the ``private_connection`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Field mask is used to specify the fields to be
                overwritten in the ``PrivateConnection`` resource by the
                update. The fields specified in the ``update_mask`` are
                relative to the resource, not the full request. A field
                will be overwritten if it is in the mask. If the user
                does not provide a mask then all fields will be
                overwritten.

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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.PrivateConnection` Private connection resource that provides connectivity for VMware Engine
                   private clouds.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [private_connection, update_mask]
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
        if not isinstance(request, vmwareengine.UpdatePrivateConnectionRequest):
            request = vmwareengine.UpdatePrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if private_connection is not None:
                request.private_connection = private_connection
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_private_connection
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("private_connection.name", request.private_connection.name),)
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
            vmwareengine_resources.PrivateConnection,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_private_connection(
        self,
        request: Optional[
            Union[vmwareengine.DeletePrivateConnectionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``PrivateConnection`` resource. When a private
        connection is deleted for a VMware Engine network, the connected
        network becomes inaccessible to that VMware Engine network.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_delete_private_connection():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.DeletePrivateConnectionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_private_connection(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.DeletePrivateConnectionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.DeletePrivateConnection][google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateConnection]
            name (str):
                Required. The resource name of the private connection to
                be deleted. Resource names are schemeless URIs that
                follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-central1/privateConnections/my-connection``

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
        if not isinstance(request, vmwareengine.DeletePrivateConnectionRequest):
            request = vmwareengine.DeletePrivateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_private_connection
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
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_private_connection_peering_routes(
        self,
        request: Optional[
            Union[vmwareengine.ListPrivateConnectionPeeringRoutesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPrivateConnectionPeeringRoutesPager:
        r"""Lists the private connection routes exchanged over a
        peering connection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_list_private_connection_peering_routes():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.ListPrivateConnectionPeeringRoutesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_private_connection_peering_routes(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.ListPrivateConnectionPeeringRoutesRequest, dict]):
                The request object. Request message for
                [VmwareEngine.ListPrivateConnectionPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes]
            parent (str):
                Required. The resource name of the private connection to
                retrieve peering routes from. Resource names are
                schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/us-west1/privateConnections/my-connection``

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
            google.cloud.vmwareengine_v1.services.vmware_engine.pagers.ListPrivateConnectionPeeringRoutesPager:
                Response message for
                   [VmwareEngine.ListPrivateConnectionPeeringRoutes][google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes]

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
            request, vmwareengine.ListPrivateConnectionPeeringRoutesRequest
        ):
            request = vmwareengine.ListPrivateConnectionPeeringRoutesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_private_connection_peering_routes
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
        response = pagers.ListPrivateConnectionPeeringRoutesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def grant_dns_bind_permission(
        self,
        request: Optional[
            Union[vmwareengine.GrantDnsBindPermissionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        principal: Optional[vmwareengine_resources.Principal] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Grants the bind permission to the customer provided
        principal(user / service account) to bind their DNS zone
        with the intranet VPC associated with the project.
        DnsBindPermission is a global resource and location can
        only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_grant_dns_bind_permission():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                principal = vmwareengine_v1.Principal()
                principal.user = "user_value"

                request = vmwareengine_v1.GrantDnsBindPermissionRequest(
                    name="name_value",
                    principal=principal,
                )

                # Make the request
                operation = client.grant_dns_bind_permission(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GrantDnsBindPermissionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GrantDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.GrantDnsBindPermission]
            name (str):
                Required. The name of the resource which stores the
                users/service accounts having the permission to bind to
                the corresponding intranet VPC of the consumer project.
                DnsBindPermission is a global resource. Resource names
                are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/dnsBindPermission``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            principal (google.cloud.vmwareengine_v1.types.Principal):
                Required. The consumer provided
                user/service account which needs to be
                granted permission to bind with the
                intranet VPC corresponding to the
                consumer project.

                This corresponds to the ``principal`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.DnsBindPermission` DnsBindPermission resource that contains the accounts having the consumer DNS
                   bind permission on the corresponding intranet VPC of
                   the consumer project.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, principal]
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
        if not isinstance(request, vmwareengine.GrantDnsBindPermissionRequest):
            request = vmwareengine.GrantDnsBindPermissionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if principal is not None:
                request.principal = principal

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.grant_dns_bind_permission
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
            vmwareengine_resources.DnsBindPermission,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_dns_bind_permission(
        self,
        request: Optional[Union[vmwareengine.GetDnsBindPermissionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vmwareengine_resources.DnsBindPermission:
        r"""Gets all the principals having bind permission on the
        intranet VPC associated with the consumer project
        granted by the Grant API. DnsBindPermission is a global
        resource and location can only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_get_dns_bind_permission():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                request = vmwareengine_v1.GetDnsBindPermissionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_dns_bind_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.GetDnsBindPermissionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.GetDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.GetDnsBindPermission]
            name (str):
                Required. The name of the resource which stores the
                users/service accounts having the permission to bind to
                the corresponding intranet VPC of the consumer project.
                DnsBindPermission is a global resource. Resource names
                are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/dnsBindPermission``

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
            google.cloud.vmwareengine_v1.types.DnsBindPermission:
                DnsBindPermission resource that
                contains the accounts having the
                consumer DNS bind permission on the
                corresponding intranet VPC of the
                consumer project.

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
        if not isinstance(request, vmwareengine.GetDnsBindPermissionRequest):
            request = vmwareengine.GetDnsBindPermissionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_dns_bind_permission]

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

    def revoke_dns_bind_permission(
        self,
        request: Optional[
            Union[vmwareengine.RevokeDnsBindPermissionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        principal: Optional[vmwareengine_resources.Principal] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Revokes the bind permission from the customer
        provided principal(user / service account) on the
        intranet VPC associated with the consumer project.
        DnsBindPermission is a global resource and location can
        only be global.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import vmwareengine_v1

            def sample_revoke_dns_bind_permission():
                # Create a client
                client = vmwareengine_v1.VmwareEngineClient()

                # Initialize request argument(s)
                principal = vmwareengine_v1.Principal()
                principal.user = "user_value"

                request = vmwareengine_v1.RevokeDnsBindPermissionRequest(
                    name="name_value",
                    principal=principal,
                )

                # Make the request
                operation = client.revoke_dns_bind_permission(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.vmwareengine_v1.types.RevokeDnsBindPermissionRequest, dict]):
                The request object. Request message for
                [VmwareEngine.RevokeDnsBindPermission][google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission]
            name (str):
                Required. The name of the resource which stores the
                users/service accounts having the permission to bind to
                the corresponding intranet VPC of the consumer project.
                DnsBindPermission is a global resource. Resource names
                are schemeless URIs that follow the conventions in
                https://cloud.google.com/apis/design/resource_names. For
                example:
                ``projects/my-project/locations/global/dnsBindPermission``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            principal (google.cloud.vmwareengine_v1.types.Principal):
                Required. The consumer provided
                user/service account which needs to be
                granted permission to bind with the
                intranet VPC corresponding to the
                consumer project.

                This corresponds to the ``principal`` field
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

                The result type for the operation will be :class:`google.cloud.vmwareengine_v1.types.DnsBindPermission` DnsBindPermission resource that contains the accounts having the consumer DNS
                   bind permission on the corresponding intranet VPC of
                   the consumer project.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, principal]
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
        if not isinstance(request, vmwareengine.RevokeDnsBindPermissionRequest):
            request = vmwareengine.RevokeDnsBindPermissionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if principal is not None:
                request.principal = principal

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.revoke_dns_bind_permission
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
            vmwareengine_resources.DnsBindPermission,
            metadata_type=vmwareengine.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "VmwareEngineClient":
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

    def set_iam_policy(
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
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
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
        rpc = self._transport._wrapped_methods[self._transport.set_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    def get_iam_policy(
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
            retry (google.api_core.retry.Retry): Designation of what errors, if
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
        rpc = self._transport._wrapped_methods[self._transport.get_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    def test_iam_permissions(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.test_iam_permissions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

__all__ = ("VmwareEngineClient",)
