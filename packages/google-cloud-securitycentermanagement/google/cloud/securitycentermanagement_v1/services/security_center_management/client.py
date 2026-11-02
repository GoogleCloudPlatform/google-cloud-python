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

from google.cloud.securitycentermanagement_v1 import gapic_version as package_version
from google.cloud.securitycentermanagement_v1._compat import (
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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore

from google.cloud.securitycentermanagement_v1.services.security_center_management import (
    pagers,
)
from google.cloud.securitycentermanagement_v1.types import security_center_management

from .transports.base import DEFAULT_CLIENT_INFO, SecurityCenterManagementTransport
from .transports.grpc import SecurityCenterManagementGrpcTransport
from .transports.grpc_asyncio import SecurityCenterManagementGrpcAsyncIOTransport
from .transports.rest import SecurityCenterManagementRestTransport


class SecurityCenterManagementClientMeta(type):
    """Metaclass for the SecurityCenterManagement client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[SecurityCenterManagementTransport]]
    _transport_registry["grpc"] = SecurityCenterManagementGrpcTransport
    _transport_registry["grpc_asyncio"] = SecurityCenterManagementGrpcAsyncIOTransport
    _transport_registry["rest"] = SecurityCenterManagementRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[SecurityCenterManagementTransport]:
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


class SecurityCenterManagementClient(metaclass=SecurityCenterManagementClientMeta):
    """Service describing handlers for resources"""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "securitycentermanagement.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "securitycentermanagement.{UNIVERSE_DOMAIN}"
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
            SecurityCenterManagementClient: The constructed client.
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
            SecurityCenterManagementClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> SecurityCenterManagementTransport:
        """Returns the transport used by the client instance.

        Returns:
            SecurityCenterManagementTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def effective_event_threat_detection_custom_module_path(
        organization: str,
        location: str,
        effective_event_threat_detection_custom_module: str,
    ) -> str:
        """Returns a fully-qualified effective_event_threat_detection_custom_module string."""
        return "organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{effective_event_threat_detection_custom_module}".format(
            organization=organization,
            location=location,
            effective_event_threat_detection_custom_module=effective_event_threat_detection_custom_module,
        )

    @staticmethod
    def parse_effective_event_threat_detection_custom_module_path(
        path: str,
    ) -> Dict[str, str]:
        """Parses a effective_event_threat_detection_custom_module path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/locations/(?P<location>.+?)/effectiveEventThreatDetectionCustomModules/(?P<effective_event_threat_detection_custom_module>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def effective_security_health_analytics_custom_module_path(
        organization: str,
        location: str,
        effective_security_health_analytics_custom_module: str,
    ) -> str:
        """Returns a fully-qualified effective_security_health_analytics_custom_module string."""
        return "organizations/{organization}/locations/{location}/effectiveSecurityHealthAnalyticsCustomModules/{effective_security_health_analytics_custom_module}".format(
            organization=organization,
            location=location,
            effective_security_health_analytics_custom_module=effective_security_health_analytics_custom_module,
        )

    @staticmethod
    def parse_effective_security_health_analytics_custom_module_path(
        path: str,
    ) -> Dict[str, str]:
        """Parses a effective_security_health_analytics_custom_module path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/locations/(?P<location>.+?)/effectiveSecurityHealthAnalyticsCustomModules/(?P<effective_security_health_analytics_custom_module>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def event_threat_detection_custom_module_path(
        organization: str,
        location: str,
        event_threat_detection_custom_module: str,
    ) -> str:
        """Returns a fully-qualified event_threat_detection_custom_module string."""
        return "organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{event_threat_detection_custom_module}".format(
            organization=organization,
            location=location,
            event_threat_detection_custom_module=event_threat_detection_custom_module,
        )

    @staticmethod
    def parse_event_threat_detection_custom_module_path(path: str) -> Dict[str, str]:
        """Parses a event_threat_detection_custom_module path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/locations/(?P<location>.+?)/eventThreatDetectionCustomModules/(?P<event_threat_detection_custom_module>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def finding_path(
        organization: str,
        source: str,
        finding: str,
    ) -> str:
        """Returns a fully-qualified finding string."""
        return (
            "organizations/{organization}/sources/{source}/findings/{finding}".format(
                organization=organization,
                source=source,
                finding=finding,
            )
        )

    @staticmethod
    def parse_finding_path(path: str) -> Dict[str, str]:
        """Parses a finding path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/sources/(?P<source>.+?)/findings/(?P<finding>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def security_center_service_path(
        project: str,
        location: str,
        service: str,
    ) -> str:
        """Returns a fully-qualified security_center_service string."""
        return "projects/{project}/locations/{location}/securityCenterServices/{service}".format(
            project=project,
            location=location,
            service=service,
        )

    @staticmethod
    def parse_security_center_service_path(path: str) -> Dict[str, str]:
        """Parses a security_center_service path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/securityCenterServices/(?P<service>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def security_health_analytics_custom_module_path(
        organization: str,
        location: str,
        security_health_analytics_custom_module: str,
    ) -> str:
        """Returns a fully-qualified security_health_analytics_custom_module string."""
        return "organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{security_health_analytics_custom_module}".format(
            organization=organization,
            location=location,
            security_health_analytics_custom_module=security_health_analytics_custom_module,
        )

    @staticmethod
    def parse_security_health_analytics_custom_module_path(path: str) -> Dict[str, str]:
        """Parses a security_health_analytics_custom_module path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/locations/(?P<location>.+?)/securityHealthAnalyticsCustomModules/(?P<security_health_analytics_custom_module>.+?)$",
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
                SecurityCenterManagementTransport,
                Callable[..., SecurityCenterManagementTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the security center management client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SecurityCenterManagementTransport,Callable[..., SecurityCenterManagementTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SecurityCenterManagementTransport constructor.
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
        self._client_cert_source = (
            SecurityCenterManagementClient._get_client_cert_source(
                self._client_options.client_cert_source, self._use_client_cert
            )
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=SecurityCenterManagementClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, SecurityCenterManagementTransport)
        if transport_provided:
            # transport is a SecurityCenterManagementTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(SecurityCenterManagementTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=SecurityCenterManagementClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=SecurityCenterManagementClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=SecurityCenterManagementClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[SecurityCenterManagementTransport],
                Callable[..., SecurityCenterManagementTransport],
            ] = (
                SecurityCenterManagementClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., SecurityCenterManagementTransport], transport)
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
                    "Created client `google.cloud.securitycentermanagement_v1.SecurityCenterManagementClient`.",
                    extra={
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
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
                        "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                        "credentialsType": None,
                    },
                )

    def list_effective_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesPager:
        r"""Returns a list of all
        [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule]
        resources for the given parent. This includes resident modules
        defined at the scope of the parent, and inherited modules,
        inherited from ancestor organizations, folders, and projects (no
        descendants).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_effective_security_health_analytics_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_effective_security_health_analytics_custom_modules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules].
            parent (str):
                Required. Name of parent to list effective custom
                modules, in one of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesPager:
                Response message for
                   [SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules].

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
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_effective_security_health_analytics_custom_modules
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
        response = pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_effective_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EffectiveSecurityHealthAnalyticsCustomModule:
        r"""Gets details of a single
        [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_get_effective_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_effective_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule].
            name (str):
                Required. The full resource name of the custom module,
                specified in one of the following formats:

                - ``organizations/organization/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}``
                - ``folders/folder/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}``
                - ``projects/project/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}``

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
            google.cloud.securitycentermanagement_v1.types.EffectiveSecurityHealthAnalyticsCustomModule:
                The representation of a Security Health Analytics custom module at a
                   specified level of the resource hierarchy:
                   organization, folder, or project. If a custom module
                   is inherited from an ancestor organization or folder,
                   then the enablement state is set to the value that is
                   effective in the parent, not to INHERITED. For
                   example, if the module is enabled in an organization
                   or folder, then the effective enablement state for
                   the module is ENABLED in all descendant folders or
                   projects.

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
            security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_effective_security_health_analytics_custom_module
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

    def list_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSecurityHealthAnalyticsCustomModulesPager:
        r"""Returns a list of all
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        resources for the given parent. This includes resident modules
        defined at the scope of the parent, and inherited modules,
        inherited from ancestor organizations, folders, and projects (no
        descendants).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_security_health_analytics_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_security_health_analytics_custom_modules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules].
            parent (str):
                Required. Name of the parent organization, folder, or
                project in which to list custom modules, in one of the
                following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityHealthAnalyticsCustomModulesPager:
                Response message for
                   [SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules].

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
            security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_security_health_analytics_custom_modules
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
        response = pagers.ListSecurityHealthAnalyticsCustomModulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_descendant_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDescendantSecurityHealthAnalyticsCustomModulesPager:
        r"""Returns a list of all resident
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        resources under the given organization, folder, or project and
        all of its descendants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_descendant_security_health_analytics_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_descendant_security_health_analytics_custom_modules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules].
            parent (str):
                Required. Name of the parent organization, folder, or
                project in which to list custom modules, in one of the
                following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesPager:
                Response message for
                   [SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules].

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
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_descendant_security_health_analytics_custom_modules
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
        response = pagers.ListDescendantSecurityHealthAnalyticsCustomModulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        r"""Retrieves a
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_get_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule].
            name (str):
                Required. Name of the resource, in the format
                ``projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``.

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
            google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the descendant folders and
                projects.

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
            security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_security_health_analytics_custom_module
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

    def create_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        security_health_analytics_custom_module: Optional[
            security_center_management.SecurityHealthAnalyticsCustomModule
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        r"""Creates a resident
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        at the scope of the given organization, folder, or project, and
        also creates inherited ``SecurityHealthAnalyticsCustomModule``
        resources for all folders and projects that are descendants of
        the given parent. These modules are enabled by default.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_create_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.CreateSecurityHealthAnalyticsCustomModuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule].
            parent (str):
                Required. Name of the parent organization, folder, or
                project of the module, in one of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_health_analytics_custom_module (google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule):
                Required. The resource being created.
                This corresponds to the ``security_health_analytics_custom_module`` field
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
            google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the descendant folders and
                projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, security_health_analytics_custom_module]
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
            security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if security_health_analytics_custom_module is not None:
                request.security_health_analytics_custom_module = (
                    security_health_analytics_custom_module
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_security_health_analytics_custom_module
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

        # Done; return the response.
        return response

    def update_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        security_health_analytics_custom_module: Optional[
            security_center_management.SecurityHealthAnalyticsCustomModule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        r"""Updates the
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        under the given name based on the given update mask. Updating
        the enablement state is supported on both resident and inherited
        modules (though resident modules cannot have an enablement state
        of "inherited"). Updating the display name and custom
        configuration of a module is supported on resident modules only.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_update_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.UpdateSecurityHealthAnalyticsCustomModuleRequest(
                )

                # Make the request
                response = client.update_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule].
            security_health_analytics_custom_module (google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule):
                Required. The resource being updated.
                This corresponds to the ``security_health_analytics_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The fields to update. The following values are
                valid:

                - ``custom_config``
                - ``enablement_state``

                If you omit this field or set it to the wildcard value
                ``*``, then all eligible fields are updated.

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
            google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the descendant folders and
                projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_health_analytics_custom_module, update_mask]
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
            security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_health_analytics_custom_module is not None:
                request.security_health_analytics_custom_module = (
                    security_health_analytics_custom_module
                )
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "security_health_analytics_custom_module.name",
                        request.security_health_analytics_custom_module.name,
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

        # Done; return the response.
        return response

    def delete_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        and all of its descendants in the resource hierarchy. This
        method is only supported for resident custom modules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_delete_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_security_health_analytics_custom_module(request=request)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule].
            name (str):
                Required. The resource name of the SHA custom module, in
                one of the following formats:

                - ``organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``

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
            security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
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

    def simulate_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        custom_config: Optional[security_center_management.CustomConfig] = None,
        resource: Optional[
            security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse:
        r"""Simulates the result of using a
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        to check a resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_simulate_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                resource = securitycentermanagement_v1.SimulatedResource()
                resource.resource_type = "resource_type_value"

                request = securitycentermanagement_v1.SimulateSecurityHealthAnalyticsCustomModuleRequest(
                    parent="parent_value",
                    resource=resource,
                )

                # Make the request
                response = client.simulate_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule].
                The maximum size of the request is 4 MiB.
            parent (str):
                Required. The relative resource name of the
                organization, project, or folder. For more information
                about relative resource names, see `AIP-122: Resource
                names <https://google.aip.dev/122>`__. Example:
                ``organizations/{organization_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            custom_config (google.cloud.securitycentermanagement_v1.types.CustomConfig):
                Required. The custom configuration
                that you need to test.

                This corresponds to the ``custom_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource (google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource):
                Required. Resource data to simulate
                custom module against.

                This corresponds to the ``resource`` field
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
            google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse:
                Response message for
                   [SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, custom_config, resource]
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
            security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if custom_config is not None:
                request.custom_config = custom_config
            if resource is not None:
                request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.simulate_security_health_analytics_custom_module
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

        # Done; return the response.
        return response

    def list_effective_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEffectiveEventThreatDetectionCustomModulesPager:
        r"""Lists all effective Event Threat Detection custom
        modules for the given parent. This includes resident
        modules defined at the scope of the parent along with
        modules inherited from its ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_effective_event_threat_detection_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListEffectiveEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_effective_event_threat_detection_custom_modules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules].
            parent (str):
                Required. Name of parent to list effective custom
                modules, in one of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveEventThreatDetectionCustomModulesPager:
                Response message for
                   [SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules].

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
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
        ):
            request = security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_effective_event_threat_detection_custom_modules
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
        response = pagers.ListEffectiveEventThreatDetectionCustomModulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_effective_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EffectiveEventThreatDetectionCustomModule:
        r"""Gets the effective Event Threat Detection custom module at the
        given level.

        The difference between an
        [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule]
        and an
        [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule]
        is that the fields for an
        ``EffectiveEventThreatDetectionCustomModule`` are computed from
        ancestors if needed. For example, the enablement state for an
        ``EventThreatDetectionCustomModule`` can be ``ENABLED``,
        ``DISABLED``, or ``INHERITED``. In contrast, the enablement
        state for an ``EffectiveEventThreatDetectionCustomModule`` is
        always computed as ``ENABLED`` or ``DISABLED``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_get_effective_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetEffectiveEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_effective_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule].
            name (str):
                Required. The resource name of the Event Threat
                Detection custom module, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}``

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
            google.cloud.securitycentermanagement_v1.types.EffectiveEventThreatDetectionCustomModule:
                The representation of an
                   [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule]
                   at a given level, taking hierarchy into account and
                   resolving various fields accordingly. For example, if
                   the module is enabled at the ancestor level, then
                   effective modules at all descendant levels will have
                   their enablement state set to ENABLED. Similarly, if
                   module.inherited is set, then the effective module's
                   configuration will reflect the ancestor's
                   configuration.

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
            security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_effective_event_threat_detection_custom_module
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

    def list_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListEventThreatDetectionCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEventThreatDetectionCustomModulesPager:
        r"""Lists all Event Threat Detection custom modules for
        the given organization, folder, or project. This
        includes resident modules defined at the scope of the
        parent along with modules inherited from ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_event_threat_detection_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_event_threat_detection_custom_modules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules].
            parent (str):
                Required. Name of parent to list custom modules, in one
                of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEventThreatDetectionCustomModulesPager:
                Response message for
                   [SecurityCenterManagement.ListEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules].

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
            security_center_management.ListEventThreatDetectionCustomModulesRequest,
        ):
            request = (
                security_center_management.ListEventThreatDetectionCustomModulesRequest(
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
            self._transport.list_event_threat_detection_custom_modules
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
        response = pagers.ListEventThreatDetectionCustomModulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_descendant_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDescendantEventThreatDetectionCustomModulesPager:
        r"""Lists all resident Event Threat Detection custom
        modules for the given organization, folder, or project
        and its descendants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_descendant_event_threat_detection_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListDescendantEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_descendant_event_threat_detection_custom_modules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules].
            parent (str):
                Required. Name of parent to list custom modules, in one
                of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantEventThreatDetectionCustomModulesPager:
                Response message for
                   [SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules].

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
            security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
        ):
            request = security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_descendant_event_threat_detection_custom_modules
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
        response = pagers.ListDescendantEventThreatDetectionCustomModulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EventThreatDetectionCustomModule:
        r"""Gets an Event Threat Detection custom module.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_get_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.GetEventThreatDetectionCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.GetEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEventThreatDetectionCustomModule].
            name (str):
                Required. The resource name of the Event Threat
                Detection custom module, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``

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
            google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule:
                A Security Command Center resource
                that contains the configuration and
                enablement state of a custom module,
                which enables Event Threat Detection to
                write certain findings to Security
                Command Center.

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
            security_center_management.GetEventThreatDetectionCustomModuleRequest,
        ):
            request = (
                security_center_management.GetEventThreatDetectionCustomModuleRequest(
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
            self._transport.get_event_threat_detection_custom_module
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

    def create_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.CreateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        event_threat_detection_custom_module: Optional[
            security_center_management.EventThreatDetectionCustomModule
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EventThreatDetectionCustomModule:
        r"""Creates a resident Event Threat Detection custom
        module at the scope of the given organization, folder,
        or project, and creates inherited custom modules for all
        descendants of the given parent. These modules are
        enabled by default.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_create_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.CreateEventThreatDetectionCustomModuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.CreateEventThreatDetectionCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.CreateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateEventThreatDetectionCustomModule].
            parent (str):
                Required. Name of parent for the module, in one of the
                following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            event_threat_detection_custom_module (google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule):
                Required. The module to create. The
                [EventThreatDetectionCustomModule.name][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.name]
                field is ignored; Security Command Center generates the
                name.

                This corresponds to the ``event_threat_detection_custom_module`` field
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
            google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule:
                A Security Command Center resource
                that contains the configuration and
                enablement state of a custom module,
                which enables Event Threat Detection to
                write certain findings to Security
                Command Center.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, event_threat_detection_custom_module]
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
            security_center_management.CreateEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.CreateEventThreatDetectionCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if event_threat_detection_custom_module is not None:
                request.event_threat_detection_custom_module = (
                    event_threat_detection_custom_module
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_event_threat_detection_custom_module
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

        # Done; return the response.
        return response

    def update_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        event_threat_detection_custom_module: Optional[
            security_center_management.EventThreatDetectionCustomModule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EventThreatDetectionCustomModule:
        r"""Updates the Event Threat Detection custom module with
        the given name based on the given update mask. Updating
        the enablement state is supported for both resident and
        inherited modules (though resident modules cannot have
        an enablement state of "inherited"). Updating the
        display name or configuration of a module is supported
        for resident modules only. The type of a module cannot
        be changed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_update_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.UpdateEventThreatDetectionCustomModuleRequest(
                )

                # Make the request
                response = client.update_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.UpdateEventThreatDetectionCustomModuleRequest, dict]):
                The request object. Message for updating a
                EventThreatDetectionCustomModule
            event_threat_detection_custom_module (google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule):
                Required. The module being updated.
                This corresponds to the ``event_threat_detection_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The fields to update. If
                omitted, then all fields are updated.

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
            google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule:
                A Security Command Center resource
                that contains the configuration and
                enablement state of a custom module,
                which enables Event Threat Detection to
                write certain findings to Security
                Command Center.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [event_threat_detection_custom_module, update_mask]
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
            security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.UpdateEventThreatDetectionCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if event_threat_detection_custom_module is not None:
                request.event_threat_detection_custom_module = (
                    event_threat_detection_custom_module
                )
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "event_threat_detection_custom_module.name",
                        request.event_threat_detection_custom_module.name,
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

        # Done; return the response.
        return response

    def delete_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified Event Threat Detection custom
        module and all of its descendants in the resource
        hierarchy. This method is only supported for resident
        custom modules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_delete_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.DeleteEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_event_threat_detection_custom_module(request=request)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.DeleteEventThreatDetectionCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.DeleteEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteEventThreatDetectionCustomModule].
            name (str):
                Required. The resource name of the Event Threat
                Detection custom module, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``

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
            security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.DeleteEventThreatDetectionCustomModuleRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
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

    def validate_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.ValidateEventThreatDetectionCustomModuleResponse:
        r"""Validates the given Event Threat Detection custom
        module.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_validate_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ValidateEventThreatDetectionCustomModuleRequest(
                    parent="parent_value",
                    raw_text="raw_text_value",
                    type_="type__value",
                )

                # Make the request
                response = client.validate_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ValidateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleResponse:
                Response message for
                   [SecurityCenterManagement.ValidateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.ValidateEventThreatDetectionCustomModuleRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.validate_event_threat_detection_custom_module
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

        # Done; return the response.
        return response

    def get_security_center_service(
        self,
        request: Optional[
            Union[security_center_management.GetSecurityCenterServiceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityCenterService:
        r"""Gets service settings for the specified Security
        Command Center service.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_get_security_center_service():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetSecurityCenterServiceRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_security_center_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.GetSecurityCenterServiceRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.GetSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService].
            name (str):
                Required. The Security Command Center service to
                retrieve, in one of the following formats:

                - organizations/{organization}/locations/{location}/securityCenterServices/{service}
                - folders/{folder}/locations/{location}/securityCenterServices/{service}
                - projects/{project}/locations/{location}/securityCenterServices/{service}

                The following values are valid for ``{service}``:

                - ``container-threat-detection``
                - ``event-threat-detection``
                - ``security-health-analytics``
                - ``vm-threat-detection``
                - ``web-security-scanner``

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
            google.cloud.securitycentermanagement_v1.types.SecurityCenterService:
                Represents a particular Security
                Command Center service. This includes
                settings information such as top-level
                enablement in addition to individual
                module settings. Service settings can be
                configured at the organization, folder,
                or project level. Service settings at
                the organization or folder level are
                inherited by those in descendant folders
                and projects.

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
            request, security_center_management.GetSecurityCenterServiceRequest
        ):
            request = security_center_management.GetSecurityCenterServiceRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_security_center_service
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

    def list_security_center_services(
        self,
        request: Optional[
            Union[security_center_management.ListSecurityCenterServicesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSecurityCenterServicesPager:
        r"""Returns a list of all Security Command Center
        services for the given parent.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_list_security_center_services():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListSecurityCenterServicesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_security_center_services(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.ListSecurityCenterServices][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices].
            parent (str):
                Required. The name of the parent to list Security
                Command Center services, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityCenterServicesPager:
                Response message for
                   [SecurityCenterManagement.ListSecurityCenterServices][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices].

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
            request, security_center_management.ListSecurityCenterServicesRequest
        ):
            request = security_center_management.ListSecurityCenterServicesRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_security_center_services
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
        response = pagers.ListSecurityCenterServicesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_security_center_service(
        self,
        request: Optional[
            Union[security_center_management.UpdateSecurityCenterServiceRequest, dict]
        ] = None,
        *,
        security_center_service: Optional[
            security_center_management.SecurityCenterService
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityCenterService:
        r"""Updates a Security Command Center service using the
        given update mask.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            def sample_update_security_center_service():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.UpdateSecurityCenterServiceRequest(
                )

                # Make the request
                response = client.update_security_center_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.securitycentermanagement_v1.types.UpdateSecurityCenterServiceRequest, dict]):
                The request object. Request message for
                [SecurityCenterManagement.UpdateSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityCenterService].
            security_center_service (google.cloud.securitycentermanagement_v1.types.SecurityCenterService):
                Required. The updated service.
                This corresponds to the ``security_center_service`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The fields to update. Accepts the following
                values:

                - ``intended_enablement_state``
                - ``modules``

                If omitted, then all eligible fields are updated.

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
            google.cloud.securitycentermanagement_v1.types.SecurityCenterService:
                Represents a particular Security
                Command Center service. This includes
                settings information such as top-level
                enablement in addition to individual
                module settings. Service settings can be
                configured at the organization, folder,
                or project level. Service settings at
                the organization or folder level are
                inherited by those in descendant folders
                and projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_center_service, update_mask]
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
            request, security_center_management.UpdateSecurityCenterServiceRequest
        ):
            request = security_center_management.UpdateSecurityCenterServiceRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_center_service is not None:
                request.security_center_service = security_center_service
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_security_center_service
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "security_center_service.name",
                        request.security_center_service.name,
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

        # Done; return the response.
        return response

    def __enter__(self) -> "SecurityCenterManagementClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()

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

__all__ = ("SecurityCenterManagementClient",)
