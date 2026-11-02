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

from google.cloud.sqladmin_v1 import gapic_version as package_version
from google.cloud.sqladmin_v1._compat import (
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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.sqladmin_v1.services.sql_instances_service import pagers
from google.cloud.sqladmin_v1.types import cloud_sql_instances, cloud_sql_resources

from .transports.base import DEFAULT_CLIENT_INFO, SqlInstancesServiceTransport
from .transports.grpc import SqlInstancesServiceGrpcTransport
from .transports.grpc_asyncio import SqlInstancesServiceGrpcAsyncIOTransport


class SqlInstancesServiceClientMeta(type):
    """Metaclass for the SqlInstancesService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[SqlInstancesServiceTransport]]
    _transport_registry["grpc"] = SqlInstancesServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = SqlInstancesServiceGrpcAsyncIOTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[SqlInstancesServiceTransport]:
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


class SqlInstancesServiceClient(metaclass=SqlInstancesServiceClientMeta):
    """"""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "sqladmin.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "sqladmin.{UNIVERSE_DOMAIN}"
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
            SqlInstancesServiceClient: The constructed client.
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
            SqlInstancesServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> SqlInstancesServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            SqlInstancesServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def backup_path(
        project: str,
        backup: str,
    ) -> str:
        """Returns a fully-qualified backup string."""
        return "projects/{project}/backups/{backup}".format(
            project=project,
            backup=backup,
        )

    @staticmethod
    def parse_backup_path(path: str) -> Dict[str, str]:
        """Parses a backup path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/backups/(?P<backup>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def backup_dr_backup_path(
        project: str,
        location: str,
        backupvault: str,
        datasource: str,
        backup: str,
    ) -> str:
        """Returns a fully-qualified backup_dr_backup string."""
        return "projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup}".format(
            project=project,
            location=location,
            backupvault=backupvault,
            datasource=datasource,
            backup=backup,
        )

    @staticmethod
    def parse_backup_dr_backup_path(path: str) -> Dict[str, str]:
        """Parses a backup_dr_backup path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/backupVaults/(?P<backupvault>.+?)/dataSources/(?P<datasource>.+?)/backups/(?P<backup>.+?)$",
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
    def crypto_key_version_path(
        project: str,
        location: str,
        key_ring: str,
        crypto_key: str,
        crypto_key_version: str,
    ) -> str:
        """Returns a fully-qualified crypto_key_version string."""
        return "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}".format(
            project=project,
            location=location,
            key_ring=key_ring,
            crypto_key=crypto_key,
            crypto_key_version=crypto_key_version,
        )

    @staticmethod
    def parse_crypto_key_version_path(path: str) -> Dict[str, str]:
        """Parses a crypto_key_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/keyRings/(?P<key_ring>.+?)/cryptoKeys/(?P<crypto_key>.+?)/cryptoKeyVersions/(?P<crypto_key_version>.+?)$",
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
    def network_attachment_path(
        project: str,
        region: str,
        network_attachment: str,
    ) -> str:
        """Returns a fully-qualified network_attachment string."""
        return "projects/{project}/regions/{region}/networkAttachments/{network_attachment}".format(
            project=project,
            region=region,
            network_attachment=network_attachment,
        )

    @staticmethod
    def parse_network_attachment_path(path: str) -> Dict[str, str]:
        """Parses a network_attachment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/regions/(?P<region>.+?)/networkAttachments/(?P<network_attachment>.+?)$",
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
    def service_connection_policy_path(
        project: str,
        region: str,
        service_connection_policy: str,
    ) -> str:
        """Returns a fully-qualified service_connection_policy string."""
        return "projects/{project}/regions/{region}/serviceConnectionPolicies/{service_connection_policy}".format(
            project=project,
            region=region,
            service_connection_policy=service_connection_policy,
        )

    @staticmethod
    def parse_service_connection_policy_path(path: str) -> Dict[str, str]:
        """Parses a service_connection_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/regions/(?P<region>.+?)/serviceConnectionPolicies/(?P<service_connection_policy>.+?)$",
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
                str,
                SqlInstancesServiceTransport,
                Callable[..., SqlInstancesServiceTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the sql instances service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SqlInstancesServiceTransport,Callable[..., SqlInstancesServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
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
        self._client_cert_source = SqlInstancesServiceClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=SqlInstancesServiceClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, SqlInstancesServiceTransport)
        if transport_provided:
            # transport is a SqlInstancesServiceTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(SqlInstancesServiceTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=SqlInstancesServiceClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=SqlInstancesServiceClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=SqlInstancesServiceClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[SqlInstancesServiceTransport],
                Callable[..., SqlInstancesServiceTransport],
            ] = (
                SqlInstancesServiceClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., SqlInstancesServiceTransport], transport)
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
                    "Created client `google.cloud.sql_v1.SqlInstancesServiceClient`.",
                    extra={
                        "serviceName": "google.cloud.sql.v1.SqlInstancesService",
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
                        "serviceName": "google.cloud.sql.v1.SqlInstancesService",
                        "credentialsType": None,
                    },
                )

    def add_server_ca(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesAddServerCaRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Adds a new trusted Certificate Authority (CA) version
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
            from google.cloud import sqladmin_v1

            def sample_add_server_ca():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesAddServerCaRequest(
                )

                # Make the request
                response = client.add_server_ca(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesAddServerCaRequest, dict]):
                The request object. Instance add server CA request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesAddServerCaRequest):
            request = cloud_sql_instances.SqlInstancesAddServerCaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_server_ca]

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

    def add_server_certificate(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesAddServerCertificateRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_add_server_certificate():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesAddServerCertificateRequest(
                )

                # Make the request
                response = client.add_server_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesAddServerCertificateRequest, dict]):
                The request object. Instance add server certificate
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesAddServerCertificateRequest
        ):
            request = cloud_sql_instances.SqlInstancesAddServerCertificateRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_server_certificate]

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

    def add_entra_id_certificate(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_add_entra_id_certificate():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesAddEntraIdCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.add_entra_id_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesAddEntraIdCertificateRequest, dict]):
                The request object. Instance add Entra ID certificate
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest
        ):
            request = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_entra_id_certificate]

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

    def clone(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesCloneRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_clone():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                body = sqladmin_v1.InstancesCloneRequest()
                body.clone_context.destination_instance_name = "destination_instance_name_value"

                request = sqladmin_v1.SqlInstancesCloneRequest(
                    instance="instance_value",
                    project="project_value",
                    body=body,
                )

                # Make the request
                response = client.clone(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesCloneRequest, dict]):
                The request object. Instance clone request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesCloneRequest):
            request = cloud_sql_instances.SqlInstancesCloneRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.clone]

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

    def delete(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesDeleteRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_delete():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesDeleteRequest(
                    final_backup_ttl_days=2210,
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesDeleteRequest, dict]):
                The request object. Instance delete request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesDeleteRequest):
            request = cloud_sql_instances.SqlInstancesDeleteRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

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

    def demote_master(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesDemoteMasterRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_demote_master():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesDemoteMasterRequest(
                )

                # Make the request
                response = client.demote_master(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesDemoteMasterRequest, dict]):
                The request object. Instance demote master request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesDemoteMasterRequest):
            request = cloud_sql_instances.SqlInstancesDemoteMasterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.demote_master]

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

    def demote(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesDemoteRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_demote():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                body = sqladmin_v1.InstancesDemoteRequest()
                body.demote_context.source_representative_instance_name = "source_representative_instance_name_value"

                request = sqladmin_v1.SqlInstancesDemoteRequest(
                    instance="instance_value",
                    project="project_value",
                    body=body,
                )

                # Make the request
                response = client.demote(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesDemoteRequest, dict]):
                The request object. Instance demote request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesDemoteRequest):
            request = cloud_sql_instances.SqlInstancesDemoteRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.demote]

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

    def export(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesExportRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_export():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesExportRequest(
                )

                # Make the request
                response = client.export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesExportRequest, dict]):
                The request object. Instance export request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesExportRequest):
            request = cloud_sql_instances.SqlInstancesExportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.export]

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

    def failover(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesFailoverRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_failover():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesFailoverRequest(
                )

                # Make the request
                response = client.failover(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesFailoverRequest, dict]):
                The request object. Instance failover request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesFailoverRequest):
            request = cloud_sql_instances.SqlInstancesFailoverRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.failover]

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

    def reencrypt(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesReencryptRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_reencrypt():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesReencryptRequest(
                )

                # Make the request
                response = client.reencrypt(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesReencryptRequest, dict]):
                The request object. Instance reencrypt request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesReencryptRequest):
            request = cloud_sql_instances.SqlInstancesReencryptRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reencrypt]

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

    def get(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesGetRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.DatabaseInstance:
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
            from google.cloud import sqladmin_v1

            def sample_get():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesGetRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.get(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesGetRequest, dict]):
                The request object. Instance get request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.DatabaseInstance:
                A Cloud SQL instance resource.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesGetRequest):
            request = cloud_sql_instances.SqlInstancesGetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get]

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

    def import_(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesImportRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_import():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesImportRequest(
                )

                # Make the request
                response = client.import_(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesImportRequest, dict]):
                The request object. Instance import request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesImportRequest):
            request = cloud_sql_instances.SqlInstancesImportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.import_]

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

    def insert(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesInsertRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_insert():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesInsertRequest(
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesInsertRequest, dict]):
                The request object. Instance insert request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesInsertRequest):
            request = cloud_sql_instances.SqlInstancesInsertRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

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

    def list(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesListRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPager:
        r"""Lists instances under a given project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1

            def sample_list():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesListRequest(
                )

                # Make the request
                page_result = client.list(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesListRequest, dict]):
                The request object. Instance list request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.services.sql_instances_service.pagers.ListPager:
                Database instances list response.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesListRequest):
            request = cloud_sql_instances.SqlInstancesListRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", request.project),)),
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
        response = pagers.ListPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_server_cas(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesListServerCasRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.InstancesListServerCasResponse:
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
            from google.cloud import sqladmin_v1

            def sample_list_server_cas():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesListServerCasRequest(
                )

                # Make the request
                response = client.list_server_cas(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesListServerCasRequest, dict]):
                The request object. Instance list server CAs request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.InstancesListServerCasResponse:
                Instances ListServerCas response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesListServerCasRequest
        ):
            request = cloud_sql_instances.SqlInstancesListServerCasRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_server_cas]

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

    def list_server_certificates(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesListServerCertificatesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.InstancesListServerCertificatesResponse:
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
            from google.cloud import sqladmin_v1

            def sample_list_server_certificates():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesListServerCertificatesRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.list_server_certificates(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesListServerCertificatesRequest, dict]):
                The request object. Instance list server certificates
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.InstancesListServerCertificatesResponse:
                Instances ListServerCertificates
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesListServerCertificatesRequest
        ):
            request = cloud_sql_instances.SqlInstancesListServerCertificatesRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_server_certificates]

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

    def list_entra_id_certificates(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.InstancesListEntraIdCertificatesResponse:
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
            from google.cloud import sqladmin_v1

            def sample_list_entra_id_certificates():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesListEntraIdCertificatesRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.list_entra_id_certificates(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesListEntraIdCertificatesRequest, dict]):
                The request object. Instance list Entra ID certificates
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.InstancesListEntraIdCertificatesResponse:
                Instances ListEntraIdCertificates
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest
        ):
            request = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_entra_id_certificates
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

    def patch(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesPatchRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_patch():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesPatchRequest(
                )

                # Make the request
                response = client.patch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesPatchRequest, dict]):
                The request object. Instance patch request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesPatchRequest):
            request = cloud_sql_instances.SqlInstancesPatchRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch]

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

    def promote_replica(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesPromoteReplicaRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_promote_replica():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesPromoteReplicaRequest(
                )

                # Make the request
                response = client.promote_replica(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesPromoteReplicaRequest, dict]):
                The request object. Instance promote replica request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesPromoteReplicaRequest
        ):
            request = cloud_sql_instances.SqlInstancesPromoteReplicaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.promote_replica]

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

    def switchover(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesSwitchoverRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_switchover():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesSwitchoverRequest(
                )

                # Make the request
                response = client.switchover(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesSwitchoverRequest, dict]):
                The request object. Instance switchover request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesSwitchoverRequest):
            request = cloud_sql_instances.SqlInstancesSwitchoverRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.switchover]

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

    def reset_ssl_config(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesResetSslConfigRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_reset_ssl_config():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesResetSslConfigRequest(
                )

                # Make the request
                response = client.reset_ssl_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesResetSslConfigRequest, dict]):
                The request object. Instance reset SSL config request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesResetSslConfigRequest
        ):
            request = cloud_sql_instances.SqlInstancesResetSslConfigRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reset_ssl_config]

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

    def restart(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesRestartRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_restart():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesRestartRequest(
                )

                # Make the request
                response = client.restart(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesRestartRequest, dict]):
                The request object. Instance restart request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesRestartRequest):
            request = cloud_sql_instances.SqlInstancesRestartRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.restart]

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

    def restore_backup(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesRestoreBackupRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_restore_backup():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesRestoreBackupRequest(
                )

                # Make the request
                response = client.restore_backup(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesRestoreBackupRequest, dict]):
                The request object. Instance restore backup request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesRestoreBackupRequest
        ):
            request = cloud_sql_instances.SqlInstancesRestoreBackupRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.restore_backup]

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

    def rotate_server_ca(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesRotateServerCaRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_rotate_server_ca():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesRotateServerCaRequest(
                )

                # Make the request
                response = client.rotate_server_ca(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesRotateServerCaRequest, dict]):
                The request object. Instance rotate server CA request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesRotateServerCaRequest
        ):
            request = cloud_sql_instances.SqlInstancesRotateServerCaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.rotate_server_ca]

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

    def rotate_server_certificate(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesRotateServerCertificateRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_rotate_server_certificate():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesRotateServerCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.rotate_server_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesRotateServerCertificateRequest, dict]):
                The request object. Instance rotate server certificate
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesRotateServerCertificateRequest
        ):
            request = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.rotate_server_certificate
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

    def rotate_entra_id_certificate(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_resources.Operation:
        r"""Rotates the server certificate version to one
        previously added with the addEntraIdCertificate method.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1

            def sample_rotate_entra_id_certificate():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesRotateEntraIdCertificateRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.rotate_entra_id_certificate(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesRotateEntraIdCertificateRequest, dict]):
                The request object. Instance rotate server certificate
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest
        ):
            request = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.rotate_entra_id_certificate
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

    def start_replica(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesStartReplicaRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_start_replica():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesStartReplicaRequest(
                )

                # Make the request
                response = client.start_replica(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesStartReplicaRequest, dict]):
                The request object. Instance start replica request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesStartReplicaRequest):
            request = cloud_sql_instances.SqlInstancesStartReplicaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.start_replica]

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

    def stop_replica(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesStopReplicaRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_stop_replica():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesStopReplicaRequest(
                )

                # Make the request
                response = client.stop_replica(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesStopReplicaRequest, dict]):
                The request object. Instance stop replica request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesStopReplicaRequest):
            request = cloud_sql_instances.SqlInstancesStopReplicaRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.stop_replica]

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

    def truncate_log(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesTruncateLogRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_truncate_log():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesTruncateLogRequest(
                )

                # Make the request
                response = client.truncate_log(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesTruncateLogRequest, dict]):
                The request object. Instance truncate log request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesTruncateLogRequest):
            request = cloud_sql_instances.SqlInstancesTruncateLogRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.truncate_log]

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

    def update(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesUpdateRequest, dict]
        ] = None,
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
            from google.cloud import sqladmin_v1

            def sample_update():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesUpdateRequest(
                )

                # Make the request
                response = client.update(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesUpdateRequest, dict]):
                The request object. Instance update request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
                An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesUpdateRequest):
            request = cloud_sql_instances.SqlInstancesUpdateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update]

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

    def create_ephemeral(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_create_ephemeral():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesCreateEphemeralCertRequest(
                )

                # Make the request
                response = client.create_ephemeral(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesCreateEphemeralCertRequest, dict]):
                The request object. Instance create ephemeral certificate
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SslCert:
                SslCerts Resource
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest
        ):
            request = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_ephemeral]

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

    def reschedule_maintenance(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_reschedule_maintenance():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesRescheduleMaintenanceRequest(
                )

                # Make the request
                response = client.reschedule_maintenance(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesRescheduleMaintenanceRequest, dict]):
                The request object. Instance reschedule maintenance
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest
        ):
            request = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reschedule_maintenance]

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

    def verify_external_sync_settings(
        self,
        request: Optional[
            Union[
                cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest, dict
            ]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse:
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
            from google.cloud import sqladmin_v1

            def sample_verify_external_sync_settings():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesVerifyExternalSyncSettingsRequest(
                )

                # Make the request
                response = client.verify_external_sync_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsRequest, dict]):
                The request object. Instance verify external sync
                settings request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SqlInstancesVerifyExternalSyncSettingsResponse:
                Instance verify external sync
                settings response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest
        ):
            request = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.verify_external_sync_settings
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

    def start_external_sync(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesStartExternalSyncRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_start_external_sync():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesStartExternalSyncRequest(
                )

                # Make the request
                response = client.start_external_sync(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesStartExternalSyncRequest, dict]):
                The request object. Instance start external sync request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesStartExternalSyncRequest
        ):
            request = cloud_sql_instances.SqlInstancesStartExternalSyncRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.start_external_sync]

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

    def perform_disk_shrink(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_perform_disk_shrink():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesPerformDiskShrinkRequest(
                )

                # Make the request
                response = client.perform_disk_shrink(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesPerformDiskShrinkRequest, dict]):
                The request object. Instance perform disk shrink request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest
        ):
            request = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.perform_disk_shrink]

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

    def get_disk_shrink_config(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse:
        r"""Get Disk Shrink Config for a given instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1

            def sample_get_disk_shrink_config():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesGetDiskShrinkConfigRequest(
                )

                # Make the request
                response = client.get_disk_shrink_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesGetDiskShrinkConfigRequest, dict]):
                The request object. Instance get disk shrink config
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SqlInstancesGetDiskShrinkConfigResponse:
                Instance get disk shrink config
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest
        ):
            request = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_disk_shrink_config]

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

    def reset_replica_size(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesResetReplicaSizeRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_reset_replica_size():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesResetReplicaSizeRequest(
                )

                # Make the request
                response = client.reset_replica_size(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesResetReplicaSizeRequest, dict]):
                The request object. Instance reset replica size request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesResetReplicaSizeRequest
        ):
            request = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reset_replica_size]

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

    def get_latest_recovery_time(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse:
        r"""Get Latest Recovery Time for a given instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1

            def sample_get_latest_recovery_time():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesGetLatestRecoveryTimeRequest(
                )

                # Make the request
                response = client.get_latest_recovery_time(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesGetLatestRecoveryTimeRequest, dict]):
                The request object. Instance get latest recovery time
                request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SqlInstancesGetLatestRecoveryTimeResponse:
                Instance get latest recovery time
                response.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest
        ):
            request = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_latest_recovery_time]

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

    def execute_sql(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesExecuteSqlRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.SqlInstancesExecuteSqlResponse:
        r"""Execute SQL statements.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import sqladmin_v1

            def sample_execute_sql():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesExecuteSqlRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.execute_sql(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesExecuteSqlRequest, dict]):
                The request object.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SqlInstancesExecuteSqlResponse:

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_sql_instances.SqlInstancesExecuteSqlRequest):
            request = cloud_sql_instances.SqlInstancesExecuteSqlRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.execute_sql]

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

    def acquire_ssrs_lease(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse:
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
            from google.cloud import sqladmin_v1

            def sample_acquire_ssrs_lease():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesAcquireSsrsLeaseRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.acquire_ssrs_lease(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesAcquireSsrsLeaseRequest, dict]):
                The request object. Request to acquire a lease for SSRS.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SqlInstancesAcquireSsrsLeaseResponse:
                Response for the acquire SSRS lease
                request.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest
        ):
            request = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.acquire_ssrs_lease]

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

    def release_ssrs_lease(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse:
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
            from google.cloud import sqladmin_v1

            def sample_release_ssrs_lease():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesReleaseSsrsLeaseRequest(
                    instance="instance_value",
                    project="project_value",
                )

                # Make the request
                response = client.release_ssrs_lease(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesReleaseSsrsLeaseRequest, dict]):
                The request object. Request to release a lease for SSRS.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.SqlInstancesReleaseSsrsLeaseResponse:
                Response for the release SSRS lease
                request.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest
        ):
            request = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.release_ssrs_lease]

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

    def pre_check_major_version_upgrade(
        self,
        request: Optional[
            Union[
                cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest, dict
            ]
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
            from google.cloud import sqladmin_v1

            def sample_pre_check_major_version_upgrade():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                body = sqladmin_v1.InstancesPreCheckMajorVersionUpgradeRequest()
                body.pre_check_major_version_upgrade_context.target_database_version = "SQLSERVER_2025_EXPRESS"

                request = sqladmin_v1.SqlInstancesPreCheckMajorVersionUpgradeRequest(
                    instance="instance_value",
                    project="project_value",
                    body=body,
                )

                # Make the request
                response = client.pre_check_major_version_upgrade(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesPreCheckMajorVersionUpgradeRequest, dict]):
                The request object. Request for Pre-checks for MVU
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest
        ):
            request = (
                cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest(
                    request
                )
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.pre_check_major_version_upgrade
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

    def point_in_time_restore(
        self,
        request: Optional[
            Union[cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest, dict]
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
            from google.cloud import sqladmin_v1

            def sample_point_in_time_restore():
                # Create a client
                client = sqladmin_v1.SqlInstancesServiceClient()

                # Initialize request argument(s)
                request = sqladmin_v1.SqlInstancesPointInTimeRestoreRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.point_in_time_restore(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.sqladmin_v1.types.SqlInstancesPointInTimeRestoreRequest, dict]):
                The request object. Request to perform a point in time
                restore on a Google Cloud Backup and
                Disaster Recovery managed instance.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.sqladmin_v1.types.Operation:
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
            request, cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest
        ):
            request = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.point_in_time_restore]

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

        # Done; return the response.
        return response

    def __enter__(self) -> "SqlInstancesServiceClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

__all__ = ("SqlInstancesServiceClient",)
