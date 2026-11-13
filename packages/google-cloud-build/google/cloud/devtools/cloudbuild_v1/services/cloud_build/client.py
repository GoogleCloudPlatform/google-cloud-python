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

from google.cloud.devtools.cloudbuild_v1 import gapic_version as package_version
from google.cloud.devtools.cloudbuild_v1._compat import (
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
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.devtools.cloudbuild_v1.services.cloud_build import pagers
from google.cloud.devtools.cloudbuild_v1.types import cloudbuild

from .transports.base import DEFAULT_CLIENT_INFO, CloudBuildTransport
from .transports.grpc import CloudBuildGrpcTransport
from .transports.grpc_asyncio import CloudBuildGrpcAsyncIOTransport
from .transports.rest import CloudBuildRestTransport


class CloudBuildClientMeta(type):
    """Metaclass for the CloudBuild client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[CloudBuildTransport]]
    _transport_registry["grpc"] = CloudBuildGrpcTransport
    _transport_registry["grpc_asyncio"] = CloudBuildGrpcAsyncIOTransport
    _transport_registry["rest"] = CloudBuildRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[CloudBuildTransport]:
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


class CloudBuildClient(metaclass=CloudBuildClientMeta):
    """Creates and manages builds on Google Cloud Platform.

    The main concept used by this API is a ``Build``, which describes
    the location of the source to build, how to build the source, and
    where to store the built artifacts, if any.

    A user can list previously-requested builds or get builds by their
    ID to determine the status of the build.
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "cloudbuild.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "cloudbuild.{UNIVERSE_DOMAIN}"
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
            CloudBuildClient: The constructed client.
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
            CloudBuildClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> CloudBuildTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudBuildTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def build_path(
        project: str,
        build: str,
    ) -> str:
        """Returns a fully-qualified build string."""
        return "projects/{project}/builds/{build}".format(
            project=project,
            build=build,
        )

    @staticmethod
    def parse_build_path(path: str) -> Dict[str, str]:
        """Parses a build path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/builds/(?P<build>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def build_trigger_path(
        project: str,
        trigger: str,
    ) -> str:
        """Returns a fully-qualified build_trigger string."""
        return "projects/{project}/triggers/{trigger}".format(
            project=project,
            trigger=trigger,
        )

    @staticmethod
    def parse_build_trigger_path(path: str) -> Dict[str, str]:
        """Parses a build_trigger path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/triggers/(?P<trigger>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def crypto_key_path(
        project: str,
        location: str,
        keyring: str,
        key: str,
    ) -> str:
        """Returns a fully-qualified crypto_key string."""
        return "projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}".format(
            project=project,
            location=location,
            keyring=keyring,
            key=key,
        )

    @staticmethod
    def parse_crypto_key_path(path: str) -> Dict[str, str]:
        """Parses a crypto_key path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/keyRings/(?P<keyring>.+?)/cryptoKeys/(?P<key>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def default_service_account_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified default_service_account string."""
        return "projects/{project}/locations/{location}/defaultServiceAccount".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_default_service_account_path(path: str) -> Dict[str, str]:
        """Parses a default_service_account path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/defaultServiceAccount$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def github_enterprise_config_path(
        project: str,
        config: str,
    ) -> str:
        """Returns a fully-qualified github_enterprise_config string."""
        return "projects/{project}/githubEnterpriseConfigs/{config}".format(
            project=project,
            config=config,
        )

    @staticmethod
    def parse_github_enterprise_config_path(path: str) -> Dict[str, str]:
        """Parses a github_enterprise_config path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/githubEnterpriseConfigs/(?P<config>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def git_repository_link_path(
        project: str,
        location: str,
        connection: str,
        git_repository_link: str,
    ) -> str:
        """Returns a fully-qualified git_repository_link string."""
        return "projects/{project}/locations/{location}/connections/{connection}/gitRepositoryLinks/{git_repository_link}".format(
            project=project,
            location=location,
            connection=connection,
            git_repository_link=git_repository_link,
        )

    @staticmethod
    def parse_git_repository_link_path(path: str) -> Dict[str, str]:
        """Parses a git_repository_link path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/connections/(?P<connection>.+?)/gitRepositoryLinks/(?P<git_repository_link>.+?)$",
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
        networkattachment: str,
    ) -> str:
        """Returns a fully-qualified network_attachment string."""
        return "projects/{project}/regions/{region}/networkAttachments/{networkattachment}".format(
            project=project,
            region=region,
            networkattachment=networkattachment,
        )

    @staticmethod
    def parse_network_attachment_path(path: str) -> Dict[str, str]:
        """Parses a network_attachment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/regions/(?P<region>.+?)/networkAttachments/(?P<networkattachment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def repository_path(
        project: str,
        location: str,
        connection: str,
        repository: str,
    ) -> str:
        """Returns a fully-qualified repository string."""
        return "projects/{project}/locations/{location}/connections/{connection}/repositories/{repository}".format(
            project=project,
            location=location,
            connection=connection,
            repository=repository,
        )

    @staticmethod
    def parse_repository_path(path: str) -> Dict[str, str]:
        """Parses a repository path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/connections/(?P<connection>.+?)/repositories/(?P<repository>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def secret_version_path(
        project: str,
        secret: str,
        version: str,
    ) -> str:
        """Returns a fully-qualified secret_version string."""
        return "projects/{project}/secrets/{secret}/versions/{version}".format(
            project=project,
            secret=secret,
            version=version,
        )

    @staticmethod
    def parse_secret_version_path(path: str) -> Dict[str, str]:
        """Parses a secret_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/secrets/(?P<secret>.+?)/versions/(?P<version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def service_account_path(
        project: str,
        service_account: str,
    ) -> str:
        """Returns a fully-qualified service_account string."""
        return "projects/{project}/serviceAccounts/{service_account}".format(
            project=project,
            service_account=service_account,
        )

    @staticmethod
    def parse_service_account_path(path: str) -> Dict[str, str]:
        """Parses a service_account path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/serviceAccounts/(?P<service_account>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def subscription_path(
        project: str,
        subscription: str,
    ) -> str:
        """Returns a fully-qualified subscription string."""
        return "projects/{project}/subscriptions/{subscription}".format(
            project=project,
            subscription=subscription,
        )

    @staticmethod
    def parse_subscription_path(path: str) -> Dict[str, str]:
        """Parses a subscription path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/subscriptions/(?P<subscription>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def topic_path(
        project: str,
        topic: str,
    ) -> str:
        """Returns a fully-qualified topic string."""
        return "projects/{project}/topics/{topic}".format(
            project=project,
            topic=topic,
        )

    @staticmethod
    def parse_topic_path(path: str) -> Dict[str, str]:
        """Parses a topic path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/topics/(?P<topic>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def worker_pool_path(
        project: str,
        location: str,
        worker_pool: str,
    ) -> str:
        """Returns a fully-qualified worker_pool string."""
        return (
            "projects/{project}/locations/{location}/workerPools/{worker_pool}".format(
                project=project,
                location=location,
                worker_pool=worker_pool,
            )
        )

    @staticmethod
    def parse_worker_pool_path(path: str) -> Dict[str, str]:
        """Parses a worker_pool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/workerPools/(?P<worker_pool>.+?)$",
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
            Union[str, CloudBuildTransport, Callable[..., CloudBuildTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud build client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CloudBuildTransport,Callable[..., CloudBuildTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CloudBuildTransport constructor.
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
        self._client_cert_source = CloudBuildClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=CloudBuildClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, CloudBuildTransport)
        if transport_provided:
            # transport is a CloudBuildTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(CloudBuildTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=CloudBuildClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=CloudBuildClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=CloudBuildClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[CloudBuildTransport], Callable[..., CloudBuildTransport]
            ] = (
                CloudBuildClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., CloudBuildTransport], transport)
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
                    "Created client `google.devtools.cloudbuild_v1.CloudBuildClient`.",
                    extra={
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
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
                        "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                        "credentialsType": None,
                    },
                )

    def create_build(
        self,
        request: Optional[Union[cloudbuild.CreateBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        build: Optional[cloudbuild.Build] = None,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Starts a build with the specified configuration.

        This method returns a long-running ``Operation``, which includes
        the build ID. Pass the build ID to ``GetBuild`` to determine the
        build status (such as ``SUCCESS`` or ``FAILURE``).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_create_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.CreateBuildRequest(
                    project_id="project_id_value",
                )

                # Make the request
                operation = client.create_build(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.CreateBuildRequest, dict]):
                The request object. Request to create a new build.
            project_id (str):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            build (google.cloud.devtools.cloudbuild_v1.types.Build):
                Required. Build resource to create.
                This corresponds to the ``build`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            parent (str):
                The parent resource where this build will be created.
                Format: ``projects/{project}/locations/{location}``

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, build, parent]
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
        if not isinstance(request, cloudbuild.CreateBuildRequest):
            request = cloudbuild.CreateBuildRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if build is not None:
                request.build = build
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_build]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    def get_build(
        self,
        request: Optional[Union[cloudbuild.GetBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.Build:
        r"""Returns information about a previously requested build.

        The ``Build`` that is returned includes its status (such as
        ``SUCCESS``, ``FAILURE``, or ``WORKING``), and timing
        information.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_get_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetBuildRequest(
                    project_id="project_id_value",
                    id="id_value",
                )

                # Make the request
                response = client.get_build(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.GetBuildRequest, dict]):
                The request object. Request to get a build.
            project_id (str):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (str):
                Required. ID of the build.
                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (str):
                The name of the ``Build`` to retrieve. Format:
                ``projects/{project}/locations/{location}/builds/{build}``

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
            google.cloud.devtools.cloudbuild_v1.types.Build:
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, id, name]
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
        if not isinstance(request, cloudbuild.GetBuildRequest):
            request = cloudbuild.GetBuildRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if id is not None:
                request.id = id
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_build]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def list_builds(
        self,
        request: Optional[Union[cloudbuild.ListBuildsRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBuildsPager:
        r"""Lists previously requested builds.

        Previously requested builds may still be in-progress, or
        may have finished successfully or unsuccessfully.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_list_builds():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ListBuildsRequest(
                    project_id="project_id_value",
                )

                # Make the request
                page_result = client.list_builds(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.ListBuildsRequest, dict]):
                The request object. Request to list builds.
            project_id (str):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (str):
                The raw filter text to constrain the
                results.

                This corresponds to the ``filter`` field
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
            google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsPager:
                Response including listed builds.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, filter]
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
        if not isinstance(request, cloudbuild.ListBuildsRequest):
            request = cloudbuild.ListBuildsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if filter is not None:
                request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_builds]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListBuildsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def cancel_build(
        self,
        request: Optional[Union[cloudbuild.CancelBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.Build:
        r"""Cancels a build in progress.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_cancel_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.CancelBuildRequest(
                    project_id="project_id_value",
                    id="id_value",
                )

                # Make the request
                response = client.cancel_build(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.CancelBuildRequest, dict]):
                The request object. Request to cancel an ongoing build.
            project_id (str):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (str):
                Required. ID of the build.
                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (str):
                The name of the ``Build`` to cancel. Format:
                ``projects/{project}/locations/{location}/builds/{build}``

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
            google.cloud.devtools.cloudbuild_v1.types.Build:
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, id, name]
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
        if not isinstance(request, cloudbuild.CancelBuildRequest):
            request = cloudbuild.CancelBuildRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if id is not None:
                request.id = id
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.cancel_build]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def retry_build(
        self,
        request: Optional[Union[cloudbuild.RetryBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a new build based on the specified build.

        This method creates a new build using the original build
        request, which may or may not result in an identical build.

        For triggered builds:

        - Triggered builds resolve to a precise revision; therefore a
          retry of a triggered build will result in a build that uses
          the same revision.

        For non-triggered builds that specify ``RepoSource``:

        - If the original build built from the tip of a branch, the
          retried build will build from the tip of that branch, which
          may not be the same revision as the original build.
        - If the original build specified a commit sha or revision ID,
          the retried build will use the identical source.

        For builds that specify ``StorageSource``:

        - If the original build pulled source from Cloud Storage without
          specifying the generation of the object, the new build will
          use the current object, which may be different from the
          original build source.
        - If the original build pulled source from Cloud Storage and
          specified the generation of the object, the new build will
          attempt to use the same object, which may or may not be
          available depending on the bucket's lifecycle management
          settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_retry_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.RetryBuildRequest(
                    project_id="project_id_value",
                    id="id_value",
                )

                # Make the request
                operation = client.retry_build(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.RetryBuildRequest, dict]):
                The request object. Specifies a build to retry.
            project_id (str):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (str):
                Required. Build ID of the original
                build.

                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (str):
                The name of the ``Build`` to retry. Format:
                ``projects/{project}/locations/{location}/builds/{build}``

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
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, id, name]
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
        if not isinstance(request, cloudbuild.RetryBuildRequest):
            request = cloudbuild.RetryBuildRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if id is not None:
                request.id = id
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.retry_build]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    def approve_build(
        self,
        request: Optional[Union[cloudbuild.ApproveBuildRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        approval_result: Optional[cloudbuild.ApprovalResult] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Approves or rejects a pending build.

        If approved, the returned long-running operation (LRO)
        will be analogous to the LRO returned from a CreateBuild
        call.

        If rejected, the returned LRO will be immediately done.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_approve_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ApproveBuildRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.approve_build(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.ApproveBuildRequest, dict]):
                The request object. Request to approve or reject a
                pending build.
            name (str):
                Required. Name of the target build. For example:
                "projects/{$project_id}/builds/{$build_id}"

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            approval_result (google.cloud.devtools.cloudbuild_v1.types.ApprovalResult):
                Approval decision and metadata.
                This corresponds to the ``approval_result`` field
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
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, approval_result]
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
        if not isinstance(request, cloudbuild.ApproveBuildRequest):
            request = cloudbuild.ApproveBuildRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if approval_result is not None:
                request.approval_result = approval_result

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.approve_build]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    def create_build_trigger(
        self,
        request: Optional[Union[cloudbuild.CreateBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger: Optional[cloudbuild.BuildTrigger] = None,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.BuildTrigger:
        r"""Creates a new ``BuildTrigger``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_create_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                trigger = cloudbuild_v1.BuildTrigger()
                trigger.autodetect = True

                request = cloudbuild_v1.CreateBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger=trigger,
                )

                # Make the request
                response = client.create_build_trigger(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.CreateBuildTriggerRequest, dict]):
                The request object. Request to create a new ``BuildTrigger``.
            project_id (str):
                Required. ID of the project for which
                to configure automatic builds.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger (google.cloud.devtools.cloudbuild_v1.types.BuildTrigger):
                Required. ``BuildTrigger`` to create.
                This corresponds to the ``trigger`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            parent (str):
                The parent resource where this trigger will be created.
                Format: ``projects/{project}/locations/{location}``

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
            google.cloud.devtools.cloudbuild_v1.types.BuildTrigger:
                Configuration for an automated build
                in response to source repository
                changes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger, parent]
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
        if not isinstance(request, cloudbuild.CreateBuildTriggerRequest):
            request = cloudbuild.CreateBuildTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if trigger is not None:
                request.trigger = trigger
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_build_trigger]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def get_build_trigger(
        self,
        request: Optional[Union[cloudbuild.GetBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.BuildTrigger:
        r"""Returns information about a ``BuildTrigger``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_get_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                )

                # Make the request
                response = client.get_build_trigger(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.GetBuildTriggerRequest, dict]):
                The request object. Returns the ``BuildTrigger`` with the specified ID.
            project_id (str):
                Required. ID of the project that owns
                the trigger.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (str):
                Required. Identifier (``id`` or ``name``) of the
                ``BuildTrigger`` to get.

                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (str):
                The name of the ``Trigger`` to retrieve. Format:
                ``projects/{project}/locations/{location}/triggers/{trigger}``

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
            google.cloud.devtools.cloudbuild_v1.types.BuildTrigger:
                Configuration for an automated build
                in response to source repository
                changes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, name]
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
        if not isinstance(request, cloudbuild.GetBuildTriggerRequest):
            request = cloudbuild.GetBuildTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if trigger_id is not None:
                request.trigger_id = trigger_id
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_build_trigger]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def list_build_triggers(
        self,
        request: Optional[Union[cloudbuild.ListBuildTriggersRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBuildTriggersPager:
        r"""Lists existing ``BuildTrigger``\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_list_build_triggers():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ListBuildTriggersRequest(
                    project_id="project_id_value",
                )

                # Make the request
                page_result = client.list_build_triggers(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersRequest, dict]):
                The request object. Request to list existing ``BuildTriggers``.
            project_id (str):
                Required. ID of the project for which
                to list BuildTriggers.

                This corresponds to the ``project_id`` field
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
            google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersPager:
                Response containing existing BuildTriggers.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id]
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
        if not isinstance(request, cloudbuild.ListBuildTriggersRequest):
            request = cloudbuild.ListBuildTriggersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_build_triggers]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListBuildTriggersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_build_trigger(
        self,
        request: Optional[Union[cloudbuild.DeleteBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a ``BuildTrigger`` by its project ID and trigger ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_delete_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.DeleteBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                )

                # Make the request
                client.delete_build_trigger(request=request)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.DeleteBuildTriggerRequest, dict]):
                The request object. Request to delete a ``BuildTrigger``.
            project_id (str):
                Required. ID of the project that owns
                the trigger.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (str):
                Required. ID of the ``BuildTrigger`` to delete.
                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (str):
                The name of the ``Trigger`` to delete. Format:
                ``projects/{project}/locations/{location}/triggers/{trigger}``

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
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, name]
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
        if not isinstance(request, cloudbuild.DeleteBuildTriggerRequest):
            request = cloudbuild.DeleteBuildTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if trigger_id is not None:
                request.trigger_id = trigger_id
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_build_trigger]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def update_build_trigger(
        self,
        request: Optional[Union[cloudbuild.UpdateBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        trigger: Optional[cloudbuild.BuildTrigger] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.BuildTrigger:
        r"""Updates a ``BuildTrigger`` by its project ID and trigger ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_update_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                trigger = cloudbuild_v1.BuildTrigger()
                trigger.autodetect = True

                request = cloudbuild_v1.UpdateBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                    trigger=trigger,
                )

                # Make the request
                response = client.update_build_trigger(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.UpdateBuildTriggerRequest, dict]):
                The request object. Request to update an existing ``BuildTrigger``.
            project_id (str):
                Required. ID of the project that owns
                the trigger.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (str):
                Required. ID of the ``BuildTrigger`` to update.
                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger (google.cloud.devtools.cloudbuild_v1.types.BuildTrigger):
                Required. ``BuildTrigger`` to update.
                This corresponds to the ``trigger`` field
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
            google.cloud.devtools.cloudbuild_v1.types.BuildTrigger:
                Configuration for an automated build
                in response to source repository
                changes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, trigger]
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
        if not isinstance(request, cloudbuild.UpdateBuildTriggerRequest):
            request = cloudbuild.UpdateBuildTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if trigger_id is not None:
                request.trigger_id = trigger_id
            if trigger is not None:
                request.trigger = trigger

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_build_trigger]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.trigger.resource_name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def run_build_trigger(
        self,
        request: Optional[Union[cloudbuild.RunBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        source: Optional[cloudbuild.RepoSource] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Runs a ``BuildTrigger`` at a particular source revision.

        To run a regional or global trigger, use the POST request that
        includes the location endpoint in the path (ex.
        v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run).
        The POST request that does not include the location endpoint in
        the path can only be used when running global triggers.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_run_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.RunBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                )

                # Make the request
                operation = client.run_build_trigger(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.RunBuildTriggerRequest, dict]):
                The request object. Specifies a build trigger to run and
                the source to use.
            project_id (str):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (str):
                Required. ID of the trigger.
                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            source (google.cloud.devtools.cloudbuild_v1.types.RepoSource):
                Source to build against this trigger.
                Branch and tag names cannot consist of
                regular expressions.

                This corresponds to the ``source`` field
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
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, source]
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
        if not isinstance(request, cloudbuild.RunBuildTriggerRequest):
            request = cloudbuild.RunBuildTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if project_id is not None:
                request.project_id = project_id
            if trigger_id is not None:
                request.trigger_id = trigger_id
            if source is not None:
                request.source = source

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.run_build_trigger]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    def receive_trigger_webhook(
        self,
        request: Optional[Union[cloudbuild.ReceiveTriggerWebhookRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.ReceiveTriggerWebhookResponse:
        r"""ReceiveTriggerWebhook [Experimental] is called when the API
        receives a webhook request targeted at a specific trigger.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_receive_trigger_webhook():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ReceiveTriggerWebhookRequest(
                )

                # Make the request
                response = client.receive_trigger_webhook(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookRequest, dict]):
                The request object. ReceiveTriggerWebhookRequest [Experimental] is the
                request object accepted by the ReceiveTriggerWebhook
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookResponse:
                ReceiveTriggerWebhookResponse [Experimental] is the response object for the
                   ReceiveTriggerWebhook method.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloudbuild.ReceiveTriggerWebhookRequest):
            request = cloudbuild.ReceiveTriggerWebhookRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.receive_trigger_webhook]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project_id", request.project_id),
                    ("trigger", request.trigger),
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

    def create_worker_pool(
        self,
        request: Optional[Union[cloudbuild.CreateWorkerPoolRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        worker_pool: Optional[cloudbuild.WorkerPool] = None,
        worker_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_create_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.CreateWorkerPoolRequest(
                    parent="parent_value",
                    worker_pool_id="worker_pool_id_value",
                )

                # Make the request
                operation = client.create_worker_pool(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolRequest, dict]):
                The request object. Request to create a new ``WorkerPool``.
            parent (str):
                Required. The parent resource where this worker pool
                will be created. Format:
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            worker_pool (google.cloud.devtools.cloudbuild_v1.types.WorkerPool):
                Required. ``WorkerPool`` resource to create.
                This corresponds to the ``worker_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            worker_pool_id (str):
                Required. Immutable. The ID to use for the
                ``WorkerPool``, which will become the final component of
                the resource name.

                This value should be 1-63 characters, and valid
                characters are /[a-z][0-9]-/.

                This corresponds to the ``worker_pool_id`` field
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
                :class:`google.cloud.devtools.cloudbuild_v1.types.WorkerPool`
                Configuration for a WorkerPool.

                   Cloud Build owns and maintains a pool of workers for
                   general use and have no access to a project's private
                   network. By default, builds submitted to Cloud Build
                   will use a worker from this pool.

                   If your build needs access to resources on a private
                   network, create and use a WorkerPool to run your
                   builds. Private \`WorkerPool`s give your builds
                   access to any single VPC network that you administer,
                   including any on-prem resources connected to that VPC
                   network. For an overview of private pools, see
                   [Private pools
                   overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, worker_pool, worker_pool_id]
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
        if not isinstance(request, cloudbuild.CreateWorkerPoolRequest):
            request = cloudbuild.CreateWorkerPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if worker_pool is not None:
                request.worker_pool = worker_pool
            if worker_pool_id is not None:
                request.worker_pool_id = worker_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_worker_pool]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            cloudbuild.WorkerPool,
            metadata_type=cloudbuild.CreateWorkerPoolOperationMetadata,
        )

        # Done; return the response.
        return response

    def get_worker_pool(
        self,
        request: Optional[Union[cloudbuild.GetWorkerPoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.WorkerPool:
        r"""Returns details of a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_get_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetWorkerPoolRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_worker_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.GetWorkerPoolRequest, dict]):
                The request object. Request to get a ``WorkerPool`` with the specified name.
            name (str):
                Required. The name of the ``WorkerPool`` to retrieve.
                Format:
                ``projects/{project}/locations/{location}/workerPools/{workerPool}``.

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
            google.cloud.devtools.cloudbuild_v1.types.WorkerPool:
                Configuration for a WorkerPool.

                   Cloud Build owns and maintains a pool of workers for
                   general use and have no access to a project's private
                   network. By default, builds submitted to Cloud Build
                   will use a worker from this pool.

                   If your build needs access to resources on a private
                   network, create and use a WorkerPool to run your
                   builds. Private \`WorkerPool`s give your builds
                   access to any single VPC network that you administer,
                   including any on-prem resources connected to that VPC
                   network. For an overview of private pools, see
                   [Private pools
                   overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

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
        if not isinstance(request, cloudbuild.GetWorkerPoolRequest):
            request = cloudbuild.GetWorkerPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_worker_pool]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/workerPools/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def delete_worker_pool(
        self,
        request: Optional[Union[cloudbuild.DeleteWorkerPoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_delete_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.DeleteWorkerPoolRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_worker_pool(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolRequest, dict]):
                The request object. Request to delete a ``WorkerPool``.
            name (str):
                Required. The name of the ``WorkerPool`` to delete.
                Format:
                ``projects/{project}/locations/{location}/workerPools/{workerPool}``.

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
        if not isinstance(request, cloudbuild.DeleteWorkerPoolRequest):
            request = cloudbuild.DeleteWorkerPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_worker_pool]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/workerPools/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=cloudbuild.DeleteWorkerPoolOperationMetadata,
        )

        # Done; return the response.
        return response

    def update_worker_pool(
        self,
        request: Optional[Union[cloudbuild.UpdateWorkerPoolRequest, dict]] = None,
        *,
        worker_pool: Optional[cloudbuild.WorkerPool] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_update_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.UpdateWorkerPoolRequest(
                )

                # Make the request
                operation = client.update_worker_pool(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolRequest, dict]):
                The request object. Request to update a ``WorkerPool``.
            worker_pool (google.cloud.devtools.cloudbuild_v1.types.WorkerPool):
                Required. The ``WorkerPool`` to update.

                The ``name`` field is used to identify the
                ``WorkerPool`` to update. Format:
                ``projects/{project}/locations/{location}/workerPools/{workerPool}``.

                This corresponds to the ``worker_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. A mask specifying which fields in
                ``worker_pool`` to update.

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
                :class:`google.cloud.devtools.cloudbuild_v1.types.WorkerPool`
                Configuration for a WorkerPool.

                   Cloud Build owns and maintains a pool of workers for
                   general use and have no access to a project's private
                   network. By default, builds submitted to Cloud Build
                   will use a worker from this pool.

                   If your build needs access to resources on a private
                   network, create and use a WorkerPool to run your
                   builds. Private \`WorkerPool`s give your builds
                   access to any single VPC network that you administer,
                   including any on-prem resources connected to that VPC
                   network. For an overview of private pools, see
                   [Private pools
                   overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [worker_pool, update_mask]
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
        if not isinstance(request, cloudbuild.UpdateWorkerPoolRequest):
            request = cloudbuild.UpdateWorkerPoolRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if worker_pool is not None:
                request.worker_pool = worker_pool
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_worker_pool]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/workerPools/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.worker_pool.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            cloudbuild.WorkerPool,
            metadata_type=cloudbuild.UpdateWorkerPoolOperationMetadata,
        )

        # Done; return the response.
        return response

    def list_worker_pools(
        self,
        request: Optional[Union[cloudbuild.ListWorkerPoolsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListWorkerPoolsPager:
        r"""Lists ``WorkerPool``\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_list_worker_pools():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ListWorkerPoolsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_worker_pools(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsRequest, dict]):
                The request object. Request to list ``WorkerPool``\ s.
            parent (str):
                Required. The parent of the collection of
                ``WorkerPools``. Format:
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
            google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsPager:
                Response containing existing WorkerPools.

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
        if not isinstance(request, cloudbuild.ListWorkerPoolsRequest):
            request = cloudbuild.ListWorkerPoolsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_worker_pools]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListWorkerPoolsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_default_service_account(
        self,
        request: Optional[
            Union[cloudbuild.GetDefaultServiceAccountRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.DefaultServiceAccount:
        r"""Returns the ``DefaultServiceAccount`` used by the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            def sample_get_default_service_account():
                # Create a client
                client = cloudbuild_v1.CloudBuildClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetDefaultServiceAccountRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_default_service_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.devtools.cloudbuild_v1.types.GetDefaultServiceAccountRequest, dict]):
                The request object. Returns the default service account that will be used
                for ``Builds``.
            name (str):
                Required. The name of the ``DefaultServiceAccount`` to
                retrieve. Format:
                ``projects/{project}/locations/{location}/defaultServiceAccount``

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
            google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount:
                The default service account used for Builds.
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
        if not isinstance(request, cloudbuild.GetDefaultServiceAccountRequest):
            request = cloudbuild.GetDefaultServiceAccountRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_default_service_account
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/defaultServiceAccount$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

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

    def __enter__(self) -> "CloudBuildClient":
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

__all__ = ("CloudBuildClient",)
