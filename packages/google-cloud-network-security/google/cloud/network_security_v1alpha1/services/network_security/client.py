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

from google.cloud.network_security_v1alpha1 import gapic_version as package_version
from google.cloud.network_security_v1alpha1._compat import (
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

from google.cloud.network_security_v1alpha1.services.network_security import pagers
from google.cloud.network_security_v1alpha1.types import (
    authorization_policy,
    authz_policy,
    backend_authentication_config,
    client_tls_policy,
    common,
    gateway_security_policy,
    gateway_security_policy_rule,
    server_tls_policy,
    tls,
    tls_inspection_policy,
    url_list,
)
from google.cloud.network_security_v1alpha1.types import (
    authorization_policy as gcn_authorization_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    authz_policy as gcn_authz_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    backend_authentication_config as gcn_backend_authentication_config,
)
from google.cloud.network_security_v1alpha1.types import (
    client_tls_policy as gcn_client_tls_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    gateway_security_policy as gcn_gateway_security_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    gateway_security_policy_rule as gcn_gateway_security_policy_rule,
)
from google.cloud.network_security_v1alpha1.types import (
    server_tls_policy as gcn_server_tls_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    tls_inspection_policy as gcn_tls_inspection_policy,
)
from google.cloud.network_security_v1alpha1.types import url_list as gcn_url_list

from .transports.base import DEFAULT_CLIENT_INFO, NetworkSecurityTransport
from .transports.grpc import NetworkSecurityGrpcTransport
from .transports.grpc_asyncio import NetworkSecurityGrpcAsyncIOTransport
from .transports.rest import NetworkSecurityRestTransport


class NetworkSecurityClientMeta(type):
    """Metaclass for the NetworkSecurity client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[NetworkSecurityTransport]]
    _transport_registry["grpc"] = NetworkSecurityGrpcTransport
    _transport_registry["grpc_asyncio"] = NetworkSecurityGrpcAsyncIOTransport
    _transport_registry["rest"] = NetworkSecurityRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[NetworkSecurityTransport]:
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


class NetworkSecurityClient(metaclass=NetworkSecurityClientMeta):
    """Network Security API provides resources to configure
    authentication and authorization policies. Refer to per API
    resource documentation for more information.
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "networksecurity.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "networksecurity.{UNIVERSE_DOMAIN}"
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
            NetworkSecurityClient: The constructed client.
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
            NetworkSecurityClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> NetworkSecurityTransport:
        """Returns the transport used by the client instance.

        Returns:
            NetworkSecurityTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def authorization_policy_path(
        project: str,
        location: str,
        authorization_policy: str,
    ) -> str:
        """Returns a fully-qualified authorization_policy string."""
        return "projects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}".format(
            project=project,
            location=location,
            authorization_policy=authorization_policy,
        )

    @staticmethod
    def parse_authorization_policy_path(path: str) -> Dict[str, str]:
        """Parses a authorization_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/authorizationPolicies/(?P<authorization_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def authz_policy_path(
        project: str,
        location: str,
        authz_policy: str,
    ) -> str:
        """Returns a fully-qualified authz_policy string."""
        return "projects/{project}/locations/{location}/authzPolicies/{authz_policy}".format(
            project=project,
            location=location,
            authz_policy=authz_policy,
        )

    @staticmethod
    def parse_authz_policy_path(path: str) -> Dict[str, str]:
        """Parses a authz_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/authzPolicies/(?P<authz_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def backend_authentication_config_path(
        project: str,
        location: str,
        backend_authentication_config: str,
    ) -> str:
        """Returns a fully-qualified backend_authentication_config string."""
        return "projects/{project}/locations/{location}/backendAuthenticationConfigs/{backend_authentication_config}".format(
            project=project,
            location=location,
            backend_authentication_config=backend_authentication_config,
        )

    @staticmethod
    def parse_backend_authentication_config_path(path: str) -> Dict[str, str]:
        """Parses a backend_authentication_config path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/backendAuthenticationConfigs/(?P<backend_authentication_config>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ca_pool_path(
        project: str,
        location: str,
        ca_pool: str,
    ) -> str:
        """Returns a fully-qualified ca_pool string."""
        return "projects/{project}/locations/{location}/caPools/{ca_pool}".format(
            project=project,
            location=location,
            ca_pool=ca_pool,
        )

    @staticmethod
    def parse_ca_pool_path(path: str) -> Dict[str, str]:
        """Parses a ca_pool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/caPools/(?P<ca_pool>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def certificate_path(
        project: str,
        location: str,
        certificate: str,
    ) -> str:
        """Returns a fully-qualified certificate string."""
        return (
            "projects/{project}/locations/{location}/certificates/{certificate}".format(
                project=project,
                location=location,
                certificate=certificate,
            )
        )

    @staticmethod
    def parse_certificate_path(path: str) -> Dict[str, str]:
        """Parses a certificate path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/certificates/(?P<certificate>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def client_tls_policy_path(
        project: str,
        location: str,
        client_tls_policy: str,
    ) -> str:
        """Returns a fully-qualified client_tls_policy string."""
        return "projects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}".format(
            project=project,
            location=location,
            client_tls_policy=client_tls_policy,
        )

    @staticmethod
    def parse_client_tls_policy_path(path: str) -> Dict[str, str]:
        """Parses a client_tls_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/clientTlsPolicies/(?P<client_tls_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def gateway_security_policy_path(
        project: str,
        location: str,
        gateway_security_policy: str,
    ) -> str:
        """Returns a fully-qualified gateway_security_policy string."""
        return "projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}".format(
            project=project,
            location=location,
            gateway_security_policy=gateway_security_policy,
        )

    @staticmethod
    def parse_gateway_security_policy_path(path: str) -> Dict[str, str]:
        """Parses a gateway_security_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/gatewaySecurityPolicies/(?P<gateway_security_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def gateway_security_policy_rule_path(
        project: str,
        location: str,
        gateway_security_policy: str,
        rule: str,
    ) -> str:
        """Returns a fully-qualified gateway_security_policy_rule string."""
        return "projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}/rules/{rule}".format(
            project=project,
            location=location,
            gateway_security_policy=gateway_security_policy,
            rule=rule,
        )

    @staticmethod
    def parse_gateway_security_policy_rule_path(path: str) -> Dict[str, str]:
        """Parses a gateway_security_policy_rule path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/gatewaySecurityPolicies/(?P<gateway_security_policy>.+?)/rules/(?P<rule>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def server_tls_policy_path(
        project: str,
        location: str,
        server_tls_policy: str,
    ) -> str:
        """Returns a fully-qualified server_tls_policy string."""
        return "projects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}".format(
            project=project,
            location=location,
            server_tls_policy=server_tls_policy,
        )

    @staticmethod
    def parse_server_tls_policy_path(path: str) -> Dict[str, str]:
        """Parses a server_tls_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/serverTlsPolicies/(?P<server_tls_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def tls_inspection_policy_path(
        project: str,
        location: str,
        tls_inspection_policy: str,
    ) -> str:
        """Returns a fully-qualified tls_inspection_policy string."""
        return "projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}".format(
            project=project,
            location=location,
            tls_inspection_policy=tls_inspection_policy,
        )

    @staticmethod
    def parse_tls_inspection_policy_path(path: str) -> Dict[str, str]:
        """Parses a tls_inspection_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/tlsInspectionPolicies/(?P<tls_inspection_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def trust_config_path(
        project: str,
        location: str,
        trust_config: str,
    ) -> str:
        """Returns a fully-qualified trust_config string."""
        return "projects/{project}/locations/{location}/trustConfigs/{trust_config}".format(
            project=project,
            location=location,
            trust_config=trust_config,
        )

    @staticmethod
    def parse_trust_config_path(path: str) -> Dict[str, str]:
        """Parses a trust_config path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/trustConfigs/(?P<trust_config>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def url_list_path(
        project: str,
        location: str,
        url_list: str,
    ) -> str:
        """Returns a fully-qualified url_list string."""
        return "projects/{project}/locations/{location}/urlLists/{url_list}".format(
            project=project,
            location=location,
            url_list=url_list,
        )

    @staticmethod
    def parse_url_list_path(path: str) -> Dict[str, str]:
        """Parses a url_list path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/urlLists/(?P<url_list>.+?)$",
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
            Union[
                str, NetworkSecurityTransport, Callable[..., NetworkSecurityTransport]
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the network security client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,NetworkSecurityTransport,Callable[..., NetworkSecurityTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the NetworkSecurityTransport constructor.
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
        self._client_cert_source = NetworkSecurityClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=NetworkSecurityClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, NetworkSecurityTransport)
        if transport_provided:
            # transport is a NetworkSecurityTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(NetworkSecurityTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=NetworkSecurityClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=NetworkSecurityClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=NetworkSecurityClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[NetworkSecurityTransport], Callable[..., NetworkSecurityTransport]
            ] = (
                NetworkSecurityClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., NetworkSecurityTransport], transport)
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
                    "Created client `google.cloud.networksecurity_v1alpha1.NetworkSecurityClient`.",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.NetworkSecurity",
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
                        "serviceName": "google.cloud.networksecurity.v1alpha1.NetworkSecurity",
                        "credentialsType": None,
                    },
                )

    def list_authorization_policies(
        self,
        request: Optional[
            Union[authorization_policy.ListAuthorizationPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuthorizationPoliciesPager:
        r"""Lists AuthorizationPolicies in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_authorization_policies():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListAuthorizationPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_authorization_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListAuthorizationPoliciesRequest, dict]):
                The request object. Request used with the
                ListAuthorizationPolicies method.
            parent (str):
                Required. The project and location from which the
                AuthorizationPolicies should be listed, specified in the
                format ``projects/{project}/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListAuthorizationPoliciesPager:
                Response returned by the
                ListAuthorizationPolicies method.
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
            request, authorization_policy.ListAuthorizationPoliciesRequest
        ):
            request = authorization_policy.ListAuthorizationPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_authorization_policies
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
        response = pagers.ListAuthorizationPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_authorization_policy(
        self,
        request: Optional[
            Union[authorization_policy.GetAuthorizationPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authorization_policy.AuthorizationPolicy:
        r"""Gets details of a single AuthorizationPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_authorization_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetAuthorizationPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_authorization_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetAuthorizationPolicyRequest, dict]):
                The request object. Request used by the
                GetAuthorizationPolicy method.
            name (str):
                Required. A name of the AuthorizationPolicy to get. Must
                be in the format
                ``projects/{project}/locations/{location}/authorizationPolicies/*``.

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
            google.cloud.network_security_v1alpha1.types.AuthorizationPolicy:
                AuthorizationPolicy is a resource
                that specifies how a server should
                authorize incoming connections. This
                resource in itself does not change the
                configuration unless it's attached to a
                target https proxy or endpoint config
                selector resource.

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
        if not isinstance(request, authorization_policy.GetAuthorizationPolicyRequest):
            request = authorization_policy.GetAuthorizationPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_authorization_policy]

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

    def create_authorization_policy(
        self,
        request: Optional[
            Union[gcn_authorization_policy.CreateAuthorizationPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        authorization_policy: Optional[
            gcn_authorization_policy.AuthorizationPolicy
        ] = None,
        authorization_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new AuthorizationPolicy in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_authorization_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                authorization_policy = network_security_v1alpha1.AuthorizationPolicy()
                authorization_policy.name = "name_value"
                authorization_policy.action = "DENY"

                request = network_security_v1alpha1.CreateAuthorizationPolicyRequest(
                    parent="parent_value",
                    authorization_policy_id="authorization_policy_id_value",
                    authorization_policy=authorization_policy,
                )

                # Make the request
                operation = client.create_authorization_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateAuthorizationPolicyRequest, dict]):
                The request object. Request used by the
                CreateAuthorizationPolicy method.
            parent (str):
                Required. The parent resource of the
                AuthorizationPolicy. Must be in the format
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            authorization_policy (google.cloud.network_security_v1alpha1.types.AuthorizationPolicy):
                Required. AuthorizationPolicy
                resource to be created.

                This corresponds to the ``authorization_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            authorization_policy_id (str):
                Required. Short name of the AuthorizationPolicy resource
                to be created. This value should be 1-63 characters
                long, containing only letters, numbers, hyphens, and
                underscores, and should not start with a number. E.g.
                "authz_policy".

                This corresponds to the ``authorization_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.AuthorizationPolicy` AuthorizationPolicy is a resource that specifies how a server
                   should authorize incoming connections. This resource
                   in itself does not change the configuration unless
                   it's attached to a target https proxy or endpoint
                   config selector resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, authorization_policy, authorization_policy_id]
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
            request, gcn_authorization_policy.CreateAuthorizationPolicyRequest
        ):
            request = gcn_authorization_policy.CreateAuthorizationPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if authorization_policy is not None:
                request.authorization_policy = authorization_policy
            if authorization_policy_id is not None:
                request.authorization_policy_id = authorization_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_authorization_policy
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
            gcn_authorization_policy.AuthorizationPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_authorization_policy(
        self,
        request: Optional[
            Union[gcn_authorization_policy.UpdateAuthorizationPolicyRequest, dict]
        ] = None,
        *,
        authorization_policy: Optional[
            gcn_authorization_policy.AuthorizationPolicy
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single
        AuthorizationPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_authorization_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                authorization_policy = network_security_v1alpha1.AuthorizationPolicy()
                authorization_policy.name = "name_value"
                authorization_policy.action = "DENY"

                request = network_security_v1alpha1.UpdateAuthorizationPolicyRequest(
                    authorization_policy=authorization_policy,
                )

                # Make the request
                operation = client.update_authorization_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateAuthorizationPolicyRequest, dict]):
                The request object. Request used by the
                UpdateAuthorizationPolicy method.
            authorization_policy (google.cloud.network_security_v1alpha1.types.AuthorizationPolicy):
                Required. Updated AuthorizationPolicy
                resource.

                This corresponds to the ``authorization_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the AuthorizationPolicy resource by the
                update. The fields specified in the update_mask are
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.AuthorizationPolicy` AuthorizationPolicy is a resource that specifies how a server
                   should authorize incoming connections. This resource
                   in itself does not change the configuration unless
                   it's attached to a target https proxy or endpoint
                   config selector resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [authorization_policy, update_mask]
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
            request, gcn_authorization_policy.UpdateAuthorizationPolicyRequest
        ):
            request = gcn_authorization_policy.UpdateAuthorizationPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if authorization_policy is not None:
                request.authorization_policy = authorization_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_authorization_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("authorization_policy.name", request.authorization_policy.name),)
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
            gcn_authorization_policy.AuthorizationPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_authorization_policy(
        self,
        request: Optional[
            Union[authorization_policy.DeleteAuthorizationPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single AuthorizationPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_authorization_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteAuthorizationPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_authorization_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteAuthorizationPolicyRequest, dict]):
                The request object. Request used by the
                DeleteAuthorizationPolicy method.
            name (str):
                Required. A name of the AuthorizationPolicy to delete.
                Must be in the format
                ``projects/{project}/locations/{location}/authorizationPolicies/*``.

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
            request, authorization_policy.DeleteAuthorizationPolicyRequest
        ):
            request = authorization_policy.DeleteAuthorizationPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_authorization_policy
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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_backend_authentication_configs(
        self,
        request: Optional[
            Union[
                backend_authentication_config.ListBackendAuthenticationConfigsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackendAuthenticationConfigsPager:
        r"""Lists BackendAuthenticationConfigs in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_backend_authentication_configs():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListBackendAuthenticationConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backend_authentication_configs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListBackendAuthenticationConfigsRequest, dict]):
                The request object. Request used by the
                ListBackendAuthenticationConfigs method.
            parent (str):
                Required. The project and location from which the
                BackendAuthenticationConfigs should be listed, specified
                in the format ``projects/*/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListBackendAuthenticationConfigsPager:
                Response returned by the
                ListBackendAuthenticationConfigs method.
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
            backend_authentication_config.ListBackendAuthenticationConfigsRequest,
        ):
            request = (
                backend_authentication_config.ListBackendAuthenticationConfigsRequest(
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
            self._transport.list_backend_authentication_configs
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
        response = pagers.ListBackendAuthenticationConfigsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_backend_authentication_config(
        self,
        request: Optional[
            Union[
                backend_authentication_config.GetBackendAuthenticationConfigRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> backend_authentication_config.BackendAuthenticationConfig:
        r"""Gets details of a single BackendAuthenticationConfig
        to BackendAuthenticationConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_backend_authentication_config():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetBackendAuthenticationConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_backend_authentication_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetBackendAuthenticationConfigRequest, dict]):
                The request object. Request used by the
                GetBackendAuthenticationConfig method.
            name (str):
                Required. A name of the BackendAuthenticationConfig to
                get. Must be in the format
                ``projects/*/locations/{location}/backendAuthenticationConfigs/*``.

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
            google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig:
                BackendAuthenticationConfig message groups the TrustConfig together with
                   other settings that control how the load balancer
                   authenticates, and expresses its identity to, the
                   backend:

                   - trustConfig is the attached TrustConfig.

                   \* wellKnownRoots indicates whether the load balance
                   should trust backend server certificates that are
                   issued by public certificate authorities, in addition
                   to certificates trusted by the TrustConfig.

                   \* clientCertificate is a client certificate that the
                   load balancer uses to express its identity to the
                   backend, if the connection to the backend uses mTLS.

                   You can attach the BackendAuthenticationConfig to the
                   load balancer's BackendService directly determining
                   how that BackendService negotiates TLS.

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
            request, backend_authentication_config.GetBackendAuthenticationConfigRequest
        ):
            request = (
                backend_authentication_config.GetBackendAuthenticationConfigRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_backend_authentication_config
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

    def create_backend_authentication_config(
        self,
        request: Optional[
            Union[
                gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        backend_authentication_config: Optional[
            gcn_backend_authentication_config.BackendAuthenticationConfig
        ] = None,
        backend_authentication_config_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new BackendAuthenticationConfig in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_backend_authentication_config():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                backend_authentication_config = network_security_v1alpha1.BackendAuthenticationConfig()
                backend_authentication_config.name = "name_value"

                request = network_security_v1alpha1.CreateBackendAuthenticationConfigRequest(
                    parent="parent_value",
                    backend_authentication_config_id="backend_authentication_config_id_value",
                    backend_authentication_config=backend_authentication_config,
                )

                # Make the request
                operation = client.create_backend_authentication_config(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateBackendAuthenticationConfigRequest, dict]):
                The request object. Request used by the
                CreateBackendAuthenticationConfig
                method.
            parent (str):
                Required. The parent resource of the
                BackendAuthenticationConfig. Must be in the format
                ``projects/*/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backend_authentication_config (google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig):
                Required. BackendAuthenticationConfig
                resource to be created.

                This corresponds to the ``backend_authentication_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            backend_authentication_config_id (str):
                Required. Short name of the
                BackendAuthenticationConfig resource to
                be created. This value should be 1-63
                characters long, containing only
                letters, numbers, hyphens, and
                underscores, and should not start with a
                number. E.g. "backend-auth-config".

                This corresponds to the ``backend_authentication_config_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig` BackendAuthenticationConfig message groups the TrustConfig together with
                   other settings that control how the load balancer
                   authenticates, and expresses its identity to, the
                   backend:

                   - trustConfig is the attached TrustConfig.

                   \* wellKnownRoots indicates whether the load balance
                   should trust backend server certificates that are
                   issued by public certificate authorities, in addition
                   to certificates trusted by the TrustConfig.

                   \* clientCertificate is a client certificate that the
                   load balancer uses to express its identity to the
                   backend, if the connection to the backend uses mTLS.

                   You can attach the BackendAuthenticationConfig to the
                   load balancer's BackendService directly determining
                   how that BackendService negotiates TLS.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            backend_authentication_config,
            backend_authentication_config_id,
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
            gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest,
        ):
            request = gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if backend_authentication_config is not None:
                request.backend_authentication_config = backend_authentication_config
            if backend_authentication_config_id is not None:
                request.backend_authentication_config_id = (
                    backend_authentication_config_id
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_backend_authentication_config
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
            gcn_backend_authentication_config.BackendAuthenticationConfig,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_backend_authentication_config(
        self,
        request: Optional[
            Union[
                gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest,
                dict,
            ]
        ] = None,
        *,
        backend_authentication_config: Optional[
            gcn_backend_authentication_config.BackendAuthenticationConfig
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single
        BackendAuthenticationConfig to
        BackendAuthenticationConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_backend_authentication_config():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                backend_authentication_config = network_security_v1alpha1.BackendAuthenticationConfig()
                backend_authentication_config.name = "name_value"

                request = network_security_v1alpha1.UpdateBackendAuthenticationConfigRequest(
                    backend_authentication_config=backend_authentication_config,
                )

                # Make the request
                operation = client.update_backend_authentication_config(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateBackendAuthenticationConfigRequest, dict]):
                The request object. Request used by
                UpdateBackendAuthenticationConfig
                method.
            backend_authentication_config (google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig):
                Required. Updated
                BackendAuthenticationConfig resource.

                This corresponds to the ``backend_authentication_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the BackendAuthenticationConfig resource
                by the update. The fields specified in the update_mask
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig` BackendAuthenticationConfig message groups the TrustConfig together with
                   other settings that control how the load balancer
                   authenticates, and expresses its identity to, the
                   backend:

                   - trustConfig is the attached TrustConfig.

                   \* wellKnownRoots indicates whether the load balance
                   should trust backend server certificates that are
                   issued by public certificate authorities, in addition
                   to certificates trusted by the TrustConfig.

                   \* clientCertificate is a client certificate that the
                   load balancer uses to express its identity to the
                   backend, if the connection to the backend uses mTLS.

                   You can attach the BackendAuthenticationConfig to the
                   load balancer's BackendService directly determining
                   how that BackendService negotiates TLS.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [backend_authentication_config, update_mask]
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
            gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest,
        ):
            request = gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if backend_authentication_config is not None:
                request.backend_authentication_config = backend_authentication_config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_backend_authentication_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "backend_authentication_config.name",
                        request.backend_authentication_config.name,
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
            gcn_backend_authentication_config.BackendAuthenticationConfig,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_backend_authentication_config(
        self,
        request: Optional[
            Union[
                backend_authentication_config.DeleteBackendAuthenticationConfigRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single BackendAuthenticationConfig to
        BackendAuthenticationConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_backend_authentication_config():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteBackendAuthenticationConfigRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_backend_authentication_config(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteBackendAuthenticationConfigRequest, dict]):
                The request object. Request used by the
                DeleteBackendAuthenticationConfig
                method.
            name (str):
                Required. A name of the BackendAuthenticationConfig to
                delete. Must be in the format
                ``projects/*/locations/{location}/backendAuthenticationConfigs/*``.

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
            backend_authentication_config.DeleteBackendAuthenticationConfigRequest,
        ):
            request = (
                backend_authentication_config.DeleteBackendAuthenticationConfigRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_backend_authentication_config
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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_server_tls_policies(
        self,
        request: Optional[
            Union[server_tls_policy.ListServerTlsPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListServerTlsPoliciesPager:
        r"""Lists ServerTlsPolicies in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_server_tls_policies():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListServerTlsPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_server_tls_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListServerTlsPoliciesRequest, dict]):
                The request object. Request used by the
                ListServerTlsPolicies method.
            parent (str):
                Required. The project and location from which the
                ServerTlsPolicies should be listed, specified in the
                format ``projects/*/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListServerTlsPoliciesPager:
                Response returned by the
                ListServerTlsPolicies method.
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
        if not isinstance(request, server_tls_policy.ListServerTlsPoliciesRequest):
            request = server_tls_policy.ListServerTlsPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_server_tls_policies]

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
        response = pagers.ListServerTlsPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_server_tls_policy(
        self,
        request: Optional[
            Union[server_tls_policy.GetServerTlsPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> server_tls_policy.ServerTlsPolicy:
        r"""Gets details of a single ServerTlsPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_server_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetServerTlsPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_server_tls_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetServerTlsPolicyRequest, dict]):
                The request object. Request used by the
                GetServerTlsPolicy method.
            name (str):
                Required. A name of the ServerTlsPolicy to get. Must be
                in the format
                ``projects/*/locations/{location}/serverTlsPolicies/*``.

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
            google.cloud.network_security_v1alpha1.types.ServerTlsPolicy:
                ServerTlsPolicy is a resource that specifies how a server should authenticate
                   incoming requests. This resource itself does not
                   affect configuration unless it is attached to a
                   target HTTPS proxy or endpoint config selector
                   resource.

                   ServerTlsPolicy in the form accepted by Application
                   Load Balancers can be attached only to
                   TargetHttpsProxy with an EXTERNAL, EXTERNAL_MANAGED
                   or INTERNAL_MANAGED load balancing scheme. Traffic
                   Director compatible ServerTlsPolicies can be attached
                   to EndpointPolicy and TargetHttpsProxy with Traffic
                   Director INTERNAL_SELF_MANAGED load balancing scheme.

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
        if not isinstance(request, server_tls_policy.GetServerTlsPolicyRequest):
            request = server_tls_policy.GetServerTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_server_tls_policy]

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

    def create_server_tls_policy(
        self,
        request: Optional[
            Union[gcn_server_tls_policy.CreateServerTlsPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        server_tls_policy: Optional[gcn_server_tls_policy.ServerTlsPolicy] = None,
        server_tls_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ServerTlsPolicy in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_server_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                server_tls_policy = network_security_v1alpha1.ServerTlsPolicy()
                server_tls_policy.name = "name_value"

                request = network_security_v1alpha1.CreateServerTlsPolicyRequest(
                    parent="parent_value",
                    server_tls_policy_id="server_tls_policy_id_value",
                    server_tls_policy=server_tls_policy,
                )

                # Make the request
                operation = client.create_server_tls_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateServerTlsPolicyRequest, dict]):
                The request object. Request used by the
                CreateServerTlsPolicy method.
            parent (str):
                Required. The parent resource of the ServerTlsPolicy.
                Must be in the format
                ``projects/*/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            server_tls_policy (google.cloud.network_security_v1alpha1.types.ServerTlsPolicy):
                Required. ServerTlsPolicy resource to
                be created.

                This corresponds to the ``server_tls_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            server_tls_policy_id (str):
                Required. Short name of the ServerTlsPolicy resource to
                be created. This value should be 1-63 characters long,
                containing only letters, numbers, hyphens, and
                underscores, and should not start with a number. E.g.
                "server_mtls_policy".

                This corresponds to the ``server_tls_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.ServerTlsPolicy` ServerTlsPolicy is a resource that specifies how a server should authenticate
                   incoming requests. This resource itself does not
                   affect configuration unless it is attached to a
                   target HTTPS proxy or endpoint config selector
                   resource.

                   ServerTlsPolicy in the form accepted by Application
                   Load Balancers can be attached only to
                   TargetHttpsProxy with an EXTERNAL, EXTERNAL_MANAGED
                   or INTERNAL_MANAGED load balancing scheme. Traffic
                   Director compatible ServerTlsPolicies can be attached
                   to EndpointPolicy and TargetHttpsProxy with Traffic
                   Director INTERNAL_SELF_MANAGED load balancing scheme.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, server_tls_policy, server_tls_policy_id]
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
        if not isinstance(request, gcn_server_tls_policy.CreateServerTlsPolicyRequest):
            request = gcn_server_tls_policy.CreateServerTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if server_tls_policy is not None:
                request.server_tls_policy = server_tls_policy
            if server_tls_policy_id is not None:
                request.server_tls_policy_id = server_tls_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_server_tls_policy]

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
            gcn_server_tls_policy.ServerTlsPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_server_tls_policy(
        self,
        request: Optional[
            Union[gcn_server_tls_policy.UpdateServerTlsPolicyRequest, dict]
        ] = None,
        *,
        server_tls_policy: Optional[gcn_server_tls_policy.ServerTlsPolicy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single ServerTlsPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_server_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                server_tls_policy = network_security_v1alpha1.ServerTlsPolicy()
                server_tls_policy.name = "name_value"

                request = network_security_v1alpha1.UpdateServerTlsPolicyRequest(
                    server_tls_policy=server_tls_policy,
                )

                # Make the request
                operation = client.update_server_tls_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateServerTlsPolicyRequest, dict]):
                The request object. Request used by UpdateServerTlsPolicy
                method.
            server_tls_policy (google.cloud.network_security_v1alpha1.types.ServerTlsPolicy):
                Required. Updated ServerTlsPolicy
                resource.

                This corresponds to the ``server_tls_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the ServerTlsPolicy resource by the
                update. The fields specified in the update_mask are
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.ServerTlsPolicy` ServerTlsPolicy is a resource that specifies how a server should authenticate
                   incoming requests. This resource itself does not
                   affect configuration unless it is attached to a
                   target HTTPS proxy or endpoint config selector
                   resource.

                   ServerTlsPolicy in the form accepted by Application
                   Load Balancers can be attached only to
                   TargetHttpsProxy with an EXTERNAL, EXTERNAL_MANAGED
                   or INTERNAL_MANAGED load balancing scheme. Traffic
                   Director compatible ServerTlsPolicies can be attached
                   to EndpointPolicy and TargetHttpsProxy with Traffic
                   Director INTERNAL_SELF_MANAGED load balancing scheme.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [server_tls_policy, update_mask]
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
        if not isinstance(request, gcn_server_tls_policy.UpdateServerTlsPolicyRequest):
            request = gcn_server_tls_policy.UpdateServerTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if server_tls_policy is not None:
                request.server_tls_policy = server_tls_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_server_tls_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("server_tls_policy.name", request.server_tls_policy.name),)
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
            gcn_server_tls_policy.ServerTlsPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_server_tls_policy(
        self,
        request: Optional[
            Union[server_tls_policy.DeleteServerTlsPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single ServerTlsPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_server_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteServerTlsPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_server_tls_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteServerTlsPolicyRequest, dict]):
                The request object. Request used by the
                DeleteServerTlsPolicy method.
            name (str):
                Required. A name of the ServerTlsPolicy to delete. Must
                be in the format
                ``projects/*/locations/{location}/serverTlsPolicies/*``.

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
        if not isinstance(request, server_tls_policy.DeleteServerTlsPolicyRequest):
            request = server_tls_policy.DeleteServerTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_server_tls_policy]

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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_client_tls_policies(
        self,
        request: Optional[
            Union[client_tls_policy.ListClientTlsPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListClientTlsPoliciesPager:
        r"""Lists ClientTlsPolicies in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_client_tls_policies():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListClientTlsPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_client_tls_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListClientTlsPoliciesRequest, dict]):
                The request object. Request used by the
                ListClientTlsPolicies method.
            parent (str):
                Required. The project and location from which the
                ClientTlsPolicies should be listed, specified in the
                format ``projects/*/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListClientTlsPoliciesPager:
                Response returned by the
                ListClientTlsPolicies method.
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
        if not isinstance(request, client_tls_policy.ListClientTlsPoliciesRequest):
            request = client_tls_policy.ListClientTlsPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_client_tls_policies]

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
        response = pagers.ListClientTlsPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_client_tls_policy(
        self,
        request: Optional[
            Union[client_tls_policy.GetClientTlsPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> client_tls_policy.ClientTlsPolicy:
        r"""Gets details of a single ClientTlsPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_client_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetClientTlsPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_client_tls_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetClientTlsPolicyRequest, dict]):
                The request object. Request used by the
                GetClientTlsPolicy method.
            name (str):
                Required. A name of the ClientTlsPolicy to get. Must be
                in the format
                ``projects/*/locations/{location}/clientTlsPolicies/*``.

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
            google.cloud.network_security_v1alpha1.types.ClientTlsPolicy:
                ClientTlsPolicy is a resource that
                specifies how a client should
                authenticate connections to backends of
                a service. This resource itself does not
                affect configuration unless it is
                attached to a backend service resource.

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
        if not isinstance(request, client_tls_policy.GetClientTlsPolicyRequest):
            request = client_tls_policy.GetClientTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_client_tls_policy]

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

    def create_client_tls_policy(
        self,
        request: Optional[
            Union[gcn_client_tls_policy.CreateClientTlsPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        client_tls_policy: Optional[gcn_client_tls_policy.ClientTlsPolicy] = None,
        client_tls_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new ClientTlsPolicy in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_client_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                client_tls_policy = network_security_v1alpha1.ClientTlsPolicy()
                client_tls_policy.name = "name_value"

                request = network_security_v1alpha1.CreateClientTlsPolicyRequest(
                    parent="parent_value",
                    client_tls_policy_id="client_tls_policy_id_value",
                    client_tls_policy=client_tls_policy,
                )

                # Make the request
                operation = client.create_client_tls_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateClientTlsPolicyRequest, dict]):
                The request object. Request used by the
                CreateClientTlsPolicy method.
            parent (str):
                Required. The parent resource of the ClientTlsPolicy.
                Must be in the format
                ``projects/*/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_tls_policy (google.cloud.network_security_v1alpha1.types.ClientTlsPolicy):
                Required. ClientTlsPolicy resource to
                be created.

                This corresponds to the ``client_tls_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            client_tls_policy_id (str):
                Required. Short name of the ClientTlsPolicy resource to
                be created. This value should be 1-63 characters long,
                containing only letters, numbers, hyphens, and
                underscores, and should not start with a number. E.g.
                "client_mtls_policy".

                This corresponds to the ``client_tls_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.ClientTlsPolicy` ClientTlsPolicy is a resource that specifies how a client should authenticate
                   connections to backends of a service. This resource
                   itself does not affect configuration unless it is
                   attached to a backend service resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, client_tls_policy, client_tls_policy_id]
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
        if not isinstance(request, gcn_client_tls_policy.CreateClientTlsPolicyRequest):
            request = gcn_client_tls_policy.CreateClientTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if client_tls_policy is not None:
                request.client_tls_policy = client_tls_policy
            if client_tls_policy_id is not None:
                request.client_tls_policy_id = client_tls_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_client_tls_policy]

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
            gcn_client_tls_policy.ClientTlsPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_client_tls_policy(
        self,
        request: Optional[
            Union[gcn_client_tls_policy.UpdateClientTlsPolicyRequest, dict]
        ] = None,
        *,
        client_tls_policy: Optional[gcn_client_tls_policy.ClientTlsPolicy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single ClientTlsPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_client_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                client_tls_policy = network_security_v1alpha1.ClientTlsPolicy()
                client_tls_policy.name = "name_value"

                request = network_security_v1alpha1.UpdateClientTlsPolicyRequest(
                    client_tls_policy=client_tls_policy,
                )

                # Make the request
                operation = client.update_client_tls_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateClientTlsPolicyRequest, dict]):
                The request object. Request used by UpdateClientTlsPolicy
                method.
            client_tls_policy (google.cloud.network_security_v1alpha1.types.ClientTlsPolicy):
                Required. Updated ClientTlsPolicy
                resource.

                This corresponds to the ``client_tls_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the ClientTlsPolicy resource by the
                update. The fields specified in the update_mask are
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.ClientTlsPolicy` ClientTlsPolicy is a resource that specifies how a client should authenticate
                   connections to backends of a service. This resource
                   itself does not affect configuration unless it is
                   attached to a backend service resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [client_tls_policy, update_mask]
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
        if not isinstance(request, gcn_client_tls_policy.UpdateClientTlsPolicyRequest):
            request = gcn_client_tls_policy.UpdateClientTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if client_tls_policy is not None:
                request.client_tls_policy = client_tls_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_client_tls_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("client_tls_policy.name", request.client_tls_policy.name),)
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
            gcn_client_tls_policy.ClientTlsPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_client_tls_policy(
        self,
        request: Optional[
            Union[client_tls_policy.DeleteClientTlsPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single ClientTlsPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_client_tls_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteClientTlsPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_client_tls_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteClientTlsPolicyRequest, dict]):
                The request object. Request used by the
                DeleteClientTlsPolicy method.
            name (str):
                Required. A name of the ClientTlsPolicy to delete. Must
                be in the format
                ``projects/*/locations/{location}/clientTlsPolicies/*``.

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
        if not isinstance(request, client_tls_policy.DeleteClientTlsPolicyRequest):
            request = client_tls_policy.DeleteClientTlsPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_client_tls_policy]

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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_gateway_security_policies(
        self,
        request: Optional[
            Union[gateway_security_policy.ListGatewaySecurityPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGatewaySecurityPoliciesPager:
        r"""Lists GatewaySecurityPolicies in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_gateway_security_policies():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListGatewaySecurityPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_gateway_security_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPoliciesRequest, dict]):
                The request object. Request used with the
                ListGatewaySecurityPolicies method.
            parent (str):
                Required. The project and location from which the
                GatewaySecurityPolicies should be listed, specified in
                the format ``projects/{project}/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListGatewaySecurityPoliciesPager:
                Response returned by the
                ListGatewaySecurityPolicies method.
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
            request, gateway_security_policy.ListGatewaySecurityPoliciesRequest
        ):
            request = gateway_security_policy.ListGatewaySecurityPoliciesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_gateway_security_policies
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
        response = pagers.ListGatewaySecurityPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_gateway_security_policy(
        self,
        request: Optional[
            Union[gateway_security_policy.GetGatewaySecurityPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gateway_security_policy.GatewaySecurityPolicy:
        r"""Gets details of a single GatewaySecurityPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_gateway_security_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetGatewaySecurityPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_gateway_security_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetGatewaySecurityPolicyRequest, dict]):
                The request object. Request used by the
                GetGatewaySecurityPolicy method.
            name (str):
                Required. A name of the GatewaySecurityPolicy to get.
                Must be in the format
                ``projects/{project}/locations/{location}/gatewaySecurityPolicies/*``.

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
            google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy:
                The GatewaySecurityPolicy resource
                contains a collection of
                GatewaySecurityPolicyRules and
                associated metadata.

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
            request, gateway_security_policy.GetGatewaySecurityPolicyRequest
        ):
            request = gateway_security_policy.GetGatewaySecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_gateway_security_policy
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

    def create_gateway_security_policy(
        self,
        request: Optional[
            Union[gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        gateway_security_policy: Optional[
            gcn_gateway_security_policy.GatewaySecurityPolicy
        ] = None,
        gateway_security_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new GatewaySecurityPolicy in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_gateway_security_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                gateway_security_policy = network_security_v1alpha1.GatewaySecurityPolicy()
                gateway_security_policy.name = "name_value"

                request = network_security_v1alpha1.CreateGatewaySecurityPolicyRequest(
                    parent="parent_value",
                    gateway_security_policy_id="gateway_security_policy_id_value",
                    gateway_security_policy=gateway_security_policy,
                )

                # Make the request
                operation = client.create_gateway_security_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateGatewaySecurityPolicyRequest, dict]):
                The request object. Request used by the
                CreateGatewaySecurityPolicy method.
            parent (str):
                Required. The parent resource of the
                GatewaySecurityPolicy. Must be in the format
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gateway_security_policy (google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy):
                Required. GatewaySecurityPolicy
                resource to be created.

                This corresponds to the ``gateway_security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gateway_security_policy_id (str):
                Required. Short name of the GatewaySecurityPolicy
                resource to be created. This value should be 1-63
                characters long, containing only letters, numbers,
                hyphens, and underscores, and should not start with a
                number. E.g. "gateway_security_policy1".

                This corresponds to the ``gateway_security_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy` The GatewaySecurityPolicy resource contains a collection of
                   GatewaySecurityPolicyRules and associated metadata.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, gateway_security_policy, gateway_security_policy_id]
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
            request, gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest
        ):
            request = gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if gateway_security_policy is not None:
                request.gateway_security_policy = gateway_security_policy
            if gateway_security_policy_id is not None:
                request.gateway_security_policy_id = gateway_security_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_gateway_security_policy
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
            gcn_gateway_security_policy.GatewaySecurityPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_gateway_security_policy(
        self,
        request: Optional[
            Union[gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest, dict]
        ] = None,
        *,
        gateway_security_policy: Optional[
            gcn_gateway_security_policy.GatewaySecurityPolicy
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single
        GatewaySecurityPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_gateway_security_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                gateway_security_policy = network_security_v1alpha1.GatewaySecurityPolicy()
                gateway_security_policy.name = "name_value"

                request = network_security_v1alpha1.UpdateGatewaySecurityPolicyRequest(
                    gateway_security_policy=gateway_security_policy,
                )

                # Make the request
                operation = client.update_gateway_security_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateGatewaySecurityPolicyRequest, dict]):
                The request object. Request used by the
                UpdateGatewaySecurityPolicy method.
            gateway_security_policy (google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy):
                Required. Updated
                GatewaySecurityPolicy resource.

                This corresponds to the ``gateway_security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the GatewaySecurityPolicy resource by the
                update. The fields specified in the update_mask are
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy` The GatewaySecurityPolicy resource contains a collection of
                   GatewaySecurityPolicyRules and associated metadata.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [gateway_security_policy, update_mask]
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
            request, gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest
        ):
            request = gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if gateway_security_policy is not None:
                request.gateway_security_policy = gateway_security_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_gateway_security_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "gateway_security_policy.name",
                        request.gateway_security_policy.name,
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
            gcn_gateway_security_policy.GatewaySecurityPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_gateway_security_policy(
        self,
        request: Optional[
            Union[gateway_security_policy.DeleteGatewaySecurityPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single GatewaySecurityPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_gateway_security_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteGatewaySecurityPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_gateway_security_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteGatewaySecurityPolicyRequest, dict]):
                The request object. Request used by the
                DeleteGatewaySecurityPolicy method.
            name (str):
                Required. A name of the GatewaySecurityPolicy to delete.
                Must be in the format
                ``projects/{project}/locations/{location}/gatewaySecurityPolicies/*``.

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
            request, gateway_security_policy.DeleteGatewaySecurityPolicyRequest
        ):
            request = gateway_security_policy.DeleteGatewaySecurityPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_gateway_security_policy
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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_gateway_security_policy_rules(
        self,
        request: Optional[
            Union[
                gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGatewaySecurityPolicyRulesPager:
        r"""Lists GatewaySecurityPolicyRules in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_gateway_security_policy_rules():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListGatewaySecurityPolicyRulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_gateway_security_policy_rules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListGatewaySecurityPolicyRulesRequest, dict]):
                The request object. Request used with the
                ListGatewaySecurityPolicyRules method.
            parent (str):
                Required. The project, location and
                GatewaySecurityPolicy from which the
                GatewaySecurityPolicyRules should be listed, specified
                in the format
                ``projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListGatewaySecurityPolicyRulesPager:
                Response returned by the
                ListGatewaySecurityPolicyRules method.
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
            request, gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest
        ):
            request = (
                gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest(
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
            self._transport.list_gateway_security_policy_rules
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
        response = pagers.ListGatewaySecurityPolicyRulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_gateway_security_policy_rule(
        self,
        request: Optional[
            Union[
                gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gateway_security_policy_rule.GatewaySecurityPolicyRule:
        r"""Gets details of a single GatewaySecurityPolicyRule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_gateway_security_policy_rule():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetGatewaySecurityPolicyRuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_gateway_security_policy_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetGatewaySecurityPolicyRuleRequest, dict]):
                The request object. Request used by the
                GetGatewaySecurityPolicyRule method.
            name (str):
                Required. The name of the GatewaySecurityPolicyRule to
                retrieve. Format:
                projects/{project}/location/{location}/gatewaySecurityPolicies/*/rules/*

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
            google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicyRule:
                The GatewaySecurityPolicyRule
                resource is in a nested collection
                within a GatewaySecurityPolicy and
                represents a traffic matching condition
                and associated action to perform.

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
            request, gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest
        ):
            request = gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_gateway_security_policy_rule
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

    def create_gateway_security_policy_rule(
        self,
        request: Optional[
            Union[
                gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        gateway_security_policy_rule: Optional[
            gcn_gateway_security_policy_rule.GatewaySecurityPolicyRule
        ] = None,
        gateway_security_policy_rule_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new GatewaySecurityPolicy in a given
        project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_gateway_security_policy_rule():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                gateway_security_policy_rule = network_security_v1alpha1.GatewaySecurityPolicyRule()
                gateway_security_policy_rule.basic_profile = "DENY"
                gateway_security_policy_rule.name = "name_value"
                gateway_security_policy_rule.enabled = True
                gateway_security_policy_rule.priority = 898
                gateway_security_policy_rule.session_matcher = "session_matcher_value"

                request = network_security_v1alpha1.CreateGatewaySecurityPolicyRuleRequest(
                    parent="parent_value",
                    gateway_security_policy_rule=gateway_security_policy_rule,
                )

                # Make the request
                operation = client.create_gateway_security_policy_rule(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateGatewaySecurityPolicyRuleRequest, dict]):
                The request object. Methods for GatewaySecurityPolicy
                RULES/GatewaySecurityPolicyRules.
                Request used by the
                CreateGatewaySecurityPolicyRule method.
            parent (str):
                Required. The parent where this rule will be created.
                Format :
                projects/{project}/location/{location}/gatewaySecurityPolicies/\*

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gateway_security_policy_rule (google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicyRule):
                Required. The rule to be created.
                This corresponds to the ``gateway_security_policy_rule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gateway_security_policy_rule_id (str):
                The ID to use for the rule, which will become the final
                component of the rule's resource name. This value should
                be 4-63 characters, and valid characters are
                /[a-z][0-9]-/.

                This corresponds to the ``gateway_security_policy_rule_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicyRule` The GatewaySecurityPolicyRule resource is in a nested collection within a
                   GatewaySecurityPolicy and represents a traffic
                   matching condition and associated action to perform.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            gateway_security_policy_rule,
            gateway_security_policy_rule_id,
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
            gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest,
        ):
            request = (
                gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if gateway_security_policy_rule is not None:
                request.gateway_security_policy_rule = gateway_security_policy_rule
            if gateway_security_policy_rule_id is not None:
                request.gateway_security_policy_rule_id = (
                    gateway_security_policy_rule_id
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_gateway_security_policy_rule
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
            gcn_gateway_security_policy_rule.GatewaySecurityPolicyRule,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_gateway_security_policy_rule(
        self,
        request: Optional[
            Union[
                gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest,
                dict,
            ]
        ] = None,
        *,
        gateway_security_policy_rule: Optional[
            gcn_gateway_security_policy_rule.GatewaySecurityPolicyRule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single
        GatewaySecurityPolicyRule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_gateway_security_policy_rule():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                gateway_security_policy_rule = network_security_v1alpha1.GatewaySecurityPolicyRule()
                gateway_security_policy_rule.basic_profile = "DENY"
                gateway_security_policy_rule.name = "name_value"
                gateway_security_policy_rule.enabled = True
                gateway_security_policy_rule.priority = 898
                gateway_security_policy_rule.session_matcher = "session_matcher_value"

                request = network_security_v1alpha1.UpdateGatewaySecurityPolicyRuleRequest(
                    gateway_security_policy_rule=gateway_security_policy_rule,
                )

                # Make the request
                operation = client.update_gateway_security_policy_rule(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateGatewaySecurityPolicyRuleRequest, dict]):
                The request object. Request used by the
                UpdateGatewaySecurityPolicyRule method.
            gateway_security_policy_rule (google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicyRule):
                Required. Updated
                GatewaySecurityPolicyRule resource.

                This corresponds to the ``gateway_security_policy_rule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the GatewaySecurityPolicy resource by the
                update. The fields specified in the update_mask are
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicyRule` The GatewaySecurityPolicyRule resource is in a nested collection within a
                   GatewaySecurityPolicy and represents a traffic
                   matching condition and associated action to perform.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [gateway_security_policy_rule, update_mask]
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
            gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest,
        ):
            request = (
                gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if gateway_security_policy_rule is not None:
                request.gateway_security_policy_rule = gateway_security_policy_rule
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_gateway_security_policy_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "gateway_security_policy_rule.name",
                        request.gateway_security_policy_rule.name,
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
            gcn_gateway_security_policy_rule.GatewaySecurityPolicyRule,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_gateway_security_policy_rule(
        self,
        request: Optional[
            Union[
                gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single GatewaySecurityPolicyRule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_gateway_security_policy_rule():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteGatewaySecurityPolicyRuleRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_gateway_security_policy_rule(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteGatewaySecurityPolicyRuleRequest, dict]):
                The request object. Request used by the
                DeleteGatewaySecurityPolicyRule method.
            name (str):
                Required. A name of the GatewaySecurityPolicyRule to
                delete. Must be in the format
                ``projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}/rules/*``.

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
            request, gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest
        ):
            request = (
                gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_gateway_security_policy_rule
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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_url_lists(
        self,
        request: Optional[Union[url_list.ListUrlListsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUrlListsPager:
        r"""Lists UrlLists in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_url_lists():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListUrlListsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_url_lists(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListUrlListsRequest, dict]):
                The request object. Request used by the ListUrlList
                method.
            parent (str):
                Required. The project and location from which the
                UrlLists should be listed, specified in the format
                ``projects/{project}/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListUrlListsPager:
                Response returned by the ListUrlLists
                method.
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
        if not isinstance(request, url_list.ListUrlListsRequest):
            request = url_list.ListUrlListsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_url_lists]

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
        response = pagers.ListUrlListsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_url_list(
        self,
        request: Optional[Union[url_list.GetUrlListRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> url_list.UrlList:
        r"""Gets details of a single UrlList.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_url_list():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetUrlListRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_url_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetUrlListRequest, dict]):
                The request object. Request used by the GetUrlList
                method.
            name (str):
                Required. A name of the UrlList to get. Must be in the
                format ``projects/*/locations/{location}/urlLists/*``.

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
            google.cloud.network_security_v1alpha1.types.UrlList:
                UrlList proto helps users to set
                reusable, independently manageable lists
                of hosts, host patterns, URLs, URL
                patterns.

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
        if not isinstance(request, url_list.GetUrlListRequest):
            request = url_list.GetUrlListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_url_list]

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

    def create_url_list(
        self,
        request: Optional[Union[gcn_url_list.CreateUrlListRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        url_list: Optional[gcn_url_list.UrlList] = None,
        url_list_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new UrlList in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_url_list():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                url_list = network_security_v1alpha1.UrlList()
                url_list.name = "name_value"
                url_list.values = ['values_value1', 'values_value2']

                request = network_security_v1alpha1.CreateUrlListRequest(
                    parent="parent_value",
                    url_list_id="url_list_id_value",
                    url_list=url_list,
                )

                # Make the request
                operation = client.create_url_list(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateUrlListRequest, dict]):
                The request object. Request used by the CreateUrlList
                method.
            parent (str):
                Required. The parent resource of the UrlList. Must be in
                the format ``projects/*/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            url_list (google.cloud.network_security_v1alpha1.types.UrlList):
                Required. UrlList resource to be
                created.

                This corresponds to the ``url_list`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            url_list_id (str):
                Required. Short name of the UrlList resource to be
                created. This value should be 1-63 characters long,
                containing only letters, numbers, hyphens, and
                underscores, and should not start with a number. E.g.
                "url_list".

                This corresponds to the ``url_list_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.UrlList` UrlList proto helps users to set reusable, independently manageable lists
                   of hosts, host patterns, URLs, URL patterns.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, url_list, url_list_id]
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
        if not isinstance(request, gcn_url_list.CreateUrlListRequest):
            request = gcn_url_list.CreateUrlListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if url_list is not None:
                request.url_list = url_list
            if url_list_id is not None:
                request.url_list_id = url_list_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_url_list]

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
            gcn_url_list.UrlList,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_url_list(
        self,
        request: Optional[Union[gcn_url_list.UpdateUrlListRequest, dict]] = None,
        *,
        url_list: Optional[gcn_url_list.UrlList] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single UrlList.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_url_list():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                url_list = network_security_v1alpha1.UrlList()
                url_list.name = "name_value"
                url_list.values = ['values_value1', 'values_value2']

                request = network_security_v1alpha1.UpdateUrlListRequest(
                    url_list=url_list,
                )

                # Make the request
                operation = client.update_url_list(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateUrlListRequest, dict]):
                The request object. Request used by UpdateUrlList method.
            url_list (google.cloud.network_security_v1alpha1.types.UrlList):
                Required. Updated UrlList resource.
                This corresponds to the ``url_list`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the UrlList resource by the update. The
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.UrlList` UrlList proto helps users to set reusable, independently manageable lists
                   of hosts, host patterns, URLs, URL patterns.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [url_list, update_mask]
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
        if not isinstance(request, gcn_url_list.UpdateUrlListRequest):
            request = gcn_url_list.UpdateUrlListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if url_list is not None:
                request.url_list = url_list
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_url_list]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("url_list.name", request.url_list.name),)
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
            gcn_url_list.UrlList,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_url_list(
        self,
        request: Optional[Union[url_list.DeleteUrlListRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single UrlList.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_url_list():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteUrlListRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_url_list(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteUrlListRequest, dict]):
                The request object. Request used by the DeleteUrlList
                method.
            name (str):
                Required. A name of the UrlList to delete. Must be in
                the format
                ``projects/*/locations/{location}/urlLists/*``.

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
        if not isinstance(request, url_list.DeleteUrlListRequest):
            request = url_list.DeleteUrlListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_url_list]

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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_tls_inspection_policies(
        self,
        request: Optional[
            Union[tls_inspection_policy.ListTlsInspectionPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTlsInspectionPoliciesPager:
        r"""Lists TlsInspectionPolicies in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_tls_inspection_policies():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListTlsInspectionPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_tls_inspection_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListTlsInspectionPoliciesRequest, dict]):
                The request object. Request used with the
                ListTlsInspectionPolicies method.
            parent (str):
                Required. The project and location from which the
                TlsInspectionPolicies should be listed, specified in the
                format ``projects/{project}/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListTlsInspectionPoliciesPager:
                Response returned by the
                ListTlsInspectionPolicies method.
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
            request, tls_inspection_policy.ListTlsInspectionPoliciesRequest
        ):
            request = tls_inspection_policy.ListTlsInspectionPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_tls_inspection_policies
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
        response = pagers.ListTlsInspectionPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_tls_inspection_policy(
        self,
        request: Optional[
            Union[tls_inspection_policy.GetTlsInspectionPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tls_inspection_policy.TlsInspectionPolicy:
        r"""Gets details of a single TlsInspectionPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_tls_inspection_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetTlsInspectionPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_tls_inspection_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetTlsInspectionPolicyRequest, dict]):
                The request object. Request used by the
                GetTlsInspectionPolicy method.
            name (str):
                Required. A name of the TlsInspectionPolicy to get. Must
                be in the format
                ``projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}``.

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
            google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy:
                The TlsInspectionPolicy resource
                contains references to CA pools in
                Certificate Authority Service and
                associated metadata.

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
        if not isinstance(request, tls_inspection_policy.GetTlsInspectionPolicyRequest):
            request = tls_inspection_policy.GetTlsInspectionPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_tls_inspection_policy
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

    def create_tls_inspection_policy(
        self,
        request: Optional[
            Union[gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        tls_inspection_policy: Optional[
            gcn_tls_inspection_policy.TlsInspectionPolicy
        ] = None,
        tls_inspection_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new TlsInspectionPolicy in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_tls_inspection_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                tls_inspection_policy = network_security_v1alpha1.TlsInspectionPolicy()
                tls_inspection_policy.name = "name_value"
                tls_inspection_policy.ca_pool = "ca_pool_value"

                request = network_security_v1alpha1.CreateTlsInspectionPolicyRequest(
                    parent="parent_value",
                    tls_inspection_policy_id="tls_inspection_policy_id_value",
                    tls_inspection_policy=tls_inspection_policy,
                )

                # Make the request
                operation = client.create_tls_inspection_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateTlsInspectionPolicyRequest, dict]):
                The request object. Request used by the
                CreateTlsInspectionPolicy method.
            parent (str):
                Required. The parent resource of the
                TlsInspectionPolicy. Must be in the format
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tls_inspection_policy (google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy):
                Required. TlsInspectionPolicy
                resource to be created.

                This corresponds to the ``tls_inspection_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tls_inspection_policy_id (str):
                Required. Short name of the TlsInspectionPolicy resource
                to be created. This value should be 1-63 characters
                long, containing only letters, numbers, hyphens, and
                underscores, and should not start with a number. E.g.
                "tls_inspection_policy1".

                This corresponds to the ``tls_inspection_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy` The TlsInspectionPolicy resource contains references to CA pools in
                   Certificate Authority Service and associated
                   metadata.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, tls_inspection_policy, tls_inspection_policy_id]
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
            request, gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest
        ):
            request = gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if tls_inspection_policy is not None:
                request.tls_inspection_policy = tls_inspection_policy
            if tls_inspection_policy_id is not None:
                request.tls_inspection_policy_id = tls_inspection_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_tls_inspection_policy
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
            gcn_tls_inspection_policy.TlsInspectionPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_tls_inspection_policy(
        self,
        request: Optional[
            Union[gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest, dict]
        ] = None,
        *,
        tls_inspection_policy: Optional[
            gcn_tls_inspection_policy.TlsInspectionPolicy
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single
        TlsInspectionPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_tls_inspection_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                tls_inspection_policy = network_security_v1alpha1.TlsInspectionPolicy()
                tls_inspection_policy.name = "name_value"
                tls_inspection_policy.ca_pool = "ca_pool_value"

                request = network_security_v1alpha1.UpdateTlsInspectionPolicyRequest(
                    tls_inspection_policy=tls_inspection_policy,
                )

                # Make the request
                operation = client.update_tls_inspection_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateTlsInspectionPolicyRequest, dict]):
                The request object. Request used by the
                UpdateTlsInspectionPolicy method.
            tls_inspection_policy (google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy):
                Required. Updated TlsInspectionPolicy
                resource.

                This corresponds to the ``tls_inspection_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask is used to specify the fields to be
                overwritten in the TlsInspectionPolicy resource by the
                update. The fields specified in the update_mask are
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy` The TlsInspectionPolicy resource contains references to CA pools in
                   Certificate Authority Service and associated
                   metadata.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [tls_inspection_policy, update_mask]
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
            request, gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest
        ):
            request = gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if tls_inspection_policy is not None:
                request.tls_inspection_policy = tls_inspection_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_tls_inspection_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("tls_inspection_policy.name", request.tls_inspection_policy.name),)
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
            gcn_tls_inspection_policy.TlsInspectionPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_tls_inspection_policy(
        self,
        request: Optional[
            Union[tls_inspection_policy.DeleteTlsInspectionPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single TlsInspectionPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_tls_inspection_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteTlsInspectionPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_tls_inspection_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteTlsInspectionPolicyRequest, dict]):
                The request object. Request used by the
                DeleteTlsInspectionPolicy method.
            name (str):
                Required. A name of the TlsInspectionPolicy to delete.
                Must be in the format
                ``projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}``.

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
            request, tls_inspection_policy.DeleteTlsInspectionPolicyRequest
        ):
            request = tls_inspection_policy.DeleteTlsInspectionPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_tls_inspection_policy
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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_authz_policies(
        self,
        request: Optional[Union[authz_policy.ListAuthzPoliciesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuthzPoliciesPager:
        r"""Lists AuthzPolicies in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_list_authz_policies():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.ListAuthzPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_authz_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.ListAuthzPoliciesRequest, dict]):
                The request object. Message for requesting list of ``AuthzPolicy``
                resources.
            parent (str):
                Required. The project and location from which the
                ``AuthzPolicy`` resources are listed, specified in the
                following format:
                ``projects/{project}/locations/{location}``.

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
            google.cloud.network_security_v1alpha1.services.network_security.pagers.ListAuthzPoliciesPager:
                Message for response to listing AuthzPolicy resources.

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
        if not isinstance(request, authz_policy.ListAuthzPoliciesRequest):
            request = authz_policy.ListAuthzPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_authz_policies]

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
        response = pagers.ListAuthzPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_authz_policy(
        self,
        request: Optional[Union[authz_policy.GetAuthzPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authz_policy.AuthzPolicy:
        r"""Gets details of a single AuthzPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_get_authz_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.GetAuthzPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_authz_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.GetAuthzPolicyRequest, dict]):
                The request object. Message for getting a ``AuthzPolicy`` resource.
            name (str):
                Required. A name of the ``AuthzPolicy`` resource to get.
                Must be in the format
                ``projects/{project}/locations/{location}/authzPolicies/{authz_policy}``.

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
            google.cloud.network_security_v1alpha1.types.AuthzPolicy:
                AuthzPolicy is a resource that allows to forward traffic to a
                   callout backend designed to scan the traffic for
                   security purposes.

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
        if not isinstance(request, authz_policy.GetAuthzPolicyRequest):
            request = authz_policy.GetAuthzPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_authz_policy]

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

    def create_authz_policy(
        self,
        request: Optional[
            Union[gcn_authz_policy.CreateAuthzPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        authz_policy: Optional[gcn_authz_policy.AuthzPolicy] = None,
        authz_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new AuthzPolicy in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_create_authz_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                authz_policy = network_security_v1alpha1.AuthzPolicy()
                authz_policy.name = "name_value"
                authz_policy.target.load_balancing_scheme = "INTERNAL_SELF_MANAGED"
                authz_policy.target.resources = ['resources_value1', 'resources_value2']
                authz_policy.action = "CUSTOM"

                request = network_security_v1alpha1.CreateAuthzPolicyRequest(
                    parent="parent_value",
                    authz_policy_id="authz_policy_id_value",
                    authz_policy=authz_policy,
                )

                # Make the request
                operation = client.create_authz_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.CreateAuthzPolicyRequest, dict]):
                The request object. Message for creating an ``AuthzPolicy`` resource.
            parent (str):
                Required. The parent resource of the ``AuthzPolicy``
                resource. Must be in the format
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            authz_policy (google.cloud.network_security_v1alpha1.types.AuthzPolicy):
                Required. ``AuthzPolicy`` resource to be created.
                This corresponds to the ``authz_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            authz_policy_id (str):
                Required. User-provided ID of the ``AuthzPolicy``
                resource to be created.

                This corresponds to the ``authz_policy_id`` field
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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.AuthzPolicy` AuthzPolicy is a resource that allows to forward traffic to a
                   callout backend designed to scan the traffic for
                   security purposes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, authz_policy, authz_policy_id]
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
        if not isinstance(request, gcn_authz_policy.CreateAuthzPolicyRequest):
            request = gcn_authz_policy.CreateAuthzPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if authz_policy is not None:
                request.authz_policy = authz_policy
            if authz_policy_id is not None:
                request.authz_policy_id = authz_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_authz_policy]

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
            gcn_authz_policy.AuthzPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_authz_policy(
        self,
        request: Optional[
            Union[gcn_authz_policy.UpdateAuthzPolicyRequest, dict]
        ] = None,
        *,
        authz_policy: Optional[gcn_authz_policy.AuthzPolicy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the parameters of a single AuthzPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_update_authz_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                authz_policy = network_security_v1alpha1.AuthzPolicy()
                authz_policy.name = "name_value"
                authz_policy.target.load_balancing_scheme = "INTERNAL_SELF_MANAGED"
                authz_policy.target.resources = ['resources_value1', 'resources_value2']
                authz_policy.action = "CUSTOM"

                request = network_security_v1alpha1.UpdateAuthzPolicyRequest(
                    authz_policy=authz_policy,
                )

                # Make the request
                operation = client.update_authz_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.UpdateAuthzPolicyRequest, dict]):
                The request object. Message for updating an ``AuthzPolicy`` resource.
            authz_policy (google.cloud.network_security_v1alpha1.types.AuthzPolicy):
                Required. ``AuthzPolicy`` resource being updated.
                This corresponds to the ``authz_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Used to specify the fields to be overwritten
                in the ``AuthzPolicy`` resource by the update. The
                fields specified in the ``update_mask`` are relative to
                the resource, not the full request. A field is
                overwritten if it is in the mask. If the user does not
                specify a mask, then all fields are overwritten.

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

                The result type for the operation will be :class:`google.cloud.network_security_v1alpha1.types.AuthzPolicy` AuthzPolicy is a resource that allows to forward traffic to a
                   callout backend designed to scan the traffic for
                   security purposes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [authz_policy, update_mask]
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
        if not isinstance(request, gcn_authz_policy.UpdateAuthzPolicyRequest):
            request = gcn_authz_policy.UpdateAuthzPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if authz_policy is not None:
                request.authz_policy = authz_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_authz_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("authz_policy.name", request.authz_policy.name),)
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
            gcn_authz_policy.AuthzPolicy,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_authz_policy(
        self,
        request: Optional[Union[authz_policy.DeleteAuthzPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a single AuthzPolicy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import network_security_v1alpha1

            def sample_delete_authz_policy():
                # Create a client
                client = network_security_v1alpha1.NetworkSecurityClient()

                # Initialize request argument(s)
                request = network_security_v1alpha1.DeleteAuthzPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_authz_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.network_security_v1alpha1.types.DeleteAuthzPolicyRequest, dict]):
                The request object. Message for deleting an ``AuthzPolicy`` resource.
            name (str):
                Required. The name of the ``AuthzPolicy`` resource to
                delete. Must be in the format
                ``projects/{project}/locations/{location}/authzPolicies/{authz_policy}``.

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
        if not isinstance(request, authz_policy.DeleteAuthzPolicyRequest):
            request = authz_policy.DeleteAuthzPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_authz_policy]

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
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "NetworkSecurityClient":
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

__all__ = ("NetworkSecurityClient",)
