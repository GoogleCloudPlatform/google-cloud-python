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

from google.cloud.osconfig_v1 import gapic_version as package_version
from google.cloud.osconfig_v1._compat import (
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

from google.cloud.osconfig_v1.services.os_config_zonal_service import pagers
from google.cloud.osconfig_v1.types import (
    inventory,
    os_policy,
    os_policy_assignment_reports,
    os_policy_assignments,
    vulnerability,
)

from .transports.base import DEFAULT_CLIENT_INFO, OsConfigZonalServiceTransport
from .transports.grpc import OsConfigZonalServiceGrpcTransport
from .transports.grpc_asyncio import OsConfigZonalServiceGrpcAsyncIOTransport
from .transports.rest import OsConfigZonalServiceRestTransport


class OsConfigZonalServiceClientMeta(type):
    """Metaclass for the OsConfigZonalService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[OsConfigZonalServiceTransport]]
    _transport_registry["grpc"] = OsConfigZonalServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = OsConfigZonalServiceGrpcAsyncIOTransport
    _transport_registry["rest"] = OsConfigZonalServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[OsConfigZonalServiceTransport]:
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


class OsConfigZonalServiceClient(metaclass=OsConfigZonalServiceClientMeta):
    """Zonal OS Config API

    The OS Config service is the server-side component that allows
    users to manage package installations and patch jobs for Compute
    Engine VM instances.
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "osconfig.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "osconfig.{UNIVERSE_DOMAIN}"
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
            OsConfigZonalServiceClient: The constructed client.
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
            OsConfigZonalServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> OsConfigZonalServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            OsConfigZonalServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def instance_path(
        project: str,
        zone: str,
        instance: str,
    ) -> str:
        """Returns a fully-qualified instance string."""
        return "projects/{project}/zones/{zone}/instances/{instance}".format(
            project=project,
            zone=zone,
            instance=instance,
        )

    @staticmethod
    def parse_instance_path(path: str) -> Dict[str, str]:
        """Parses a instance path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/zones/(?P<zone>.+?)/instances/(?P<instance>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def instance_os_policy_assignment_path(
        project: str,
        location: str,
        instance: str,
        assignment: str,
    ) -> str:
        """Returns a fully-qualified instance_os_policy_assignment string."""
        return "projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}".format(
            project=project,
            location=location,
            instance=instance,
            assignment=assignment,
        )

    @staticmethod
    def parse_instance_os_policy_assignment_path(path: str) -> Dict[str, str]:
        """Parses a instance_os_policy_assignment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/instances/(?P<instance>.+?)/osPolicyAssignments/(?P<assignment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def inventory_path(
        project: str,
        location: str,
        instance: str,
    ) -> str:
        """Returns a fully-qualified inventory string."""
        return "projects/{project}/locations/{location}/instances/{instance}/inventory".format(
            project=project,
            location=location,
            instance=instance,
        )

    @staticmethod
    def parse_inventory_path(path: str) -> Dict[str, str]:
        """Parses a inventory path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/instances/(?P<instance>.+?)/inventory$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def os_policy_assignment_path(
        project: str,
        location: str,
        os_policy_assignment: str,
    ) -> str:
        """Returns a fully-qualified os_policy_assignment string."""
        return "projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}".format(
            project=project,
            location=location,
            os_policy_assignment=os_policy_assignment,
        )

    @staticmethod
    def parse_os_policy_assignment_path(path: str) -> Dict[str, str]:
        """Parses a os_policy_assignment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/osPolicyAssignments/(?P<os_policy_assignment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def os_policy_assignment_report_path(
        project: str,
        location: str,
        instance: str,
        assignment: str,
    ) -> str:
        """Returns a fully-qualified os_policy_assignment_report string."""
        return "projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report".format(
            project=project,
            location=location,
            instance=instance,
            assignment=assignment,
        )

    @staticmethod
    def parse_os_policy_assignment_report_path(path: str) -> Dict[str, str]:
        """Parses a os_policy_assignment_report path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/instances/(?P<instance>.+?)/osPolicyAssignments/(?P<assignment>.+?)/report$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def vulnerability_report_path(
        project: str,
        location: str,
        instance: str,
    ) -> str:
        """Returns a fully-qualified vulnerability_report string."""
        return "projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport".format(
            project=project,
            location=location,
            instance=instance,
        )

    @staticmethod
    def parse_vulnerability_report_path(path: str) -> Dict[str, str]:
        """Parses a vulnerability_report path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/instances/(?P<instance>.+?)/vulnerabilityReport$",
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
                OsConfigZonalServiceTransport,
                Callable[..., OsConfigZonalServiceTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the os config zonal service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,OsConfigZonalServiceTransport,Callable[..., OsConfigZonalServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the OsConfigZonalServiceTransport constructor.
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
        self._client_cert_source = OsConfigZonalServiceClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=OsConfigZonalServiceClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, OsConfigZonalServiceTransport)
        if transport_provided:
            # transport is a OsConfigZonalServiceTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(OsConfigZonalServiceTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=OsConfigZonalServiceClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=OsConfigZonalServiceClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=OsConfigZonalServiceClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[OsConfigZonalServiceTransport],
                Callable[..., OsConfigZonalServiceTransport],
            ] = (
                OsConfigZonalServiceClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., OsConfigZonalServiceTransport], transport)
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
                    "Created client `google.cloud.osconfig_v1.OsConfigZonalServiceClient`.",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1.OsConfigZonalService",
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
                        "serviceName": "google.cloud.osconfig.v1.OsConfigZonalService",
                        "credentialsType": None,
                    },
                )

    def create_os_policy_assignment(
        self,
        request: Optional[
            Union[os_policy_assignments.CreateOSPolicyAssignmentRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        os_policy_assignment: Optional[os_policy_assignments.OSPolicyAssignment] = None,
        os_policy_assignment_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Create an OS policy assignment.

        This method also creates the first revision of the OS policy
        assignment.

        This method returns a long running operation (LRO) that contains
        the rollout details. The rollout can be cancelled by cancelling
        the LRO.

        For more information, see `Method:
        projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_create_os_policy_assignment():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                os_policy_assignment = osconfig_v1.OSPolicyAssignment()
                os_policy_assignment.os_policies.id = "id_value"
                os_policy_assignment.os_policies.mode = "ENFORCEMENT"
                os_policy_assignment.os_policies.resource_groups.resources.pkg.apt.name = "name_value"
                os_policy_assignment.os_policies.resource_groups.resources.pkg.desired_state = "REMOVED"
                os_policy_assignment.os_policies.resource_groups.resources.id = "id_value"
                os_policy_assignment.rollout.disruption_budget.fixed = 528

                request = osconfig_v1.CreateOSPolicyAssignmentRequest(
                    parent="parent_value",
                    os_policy_assignment=os_policy_assignment,
                    os_policy_assignment_id="os_policy_assignment_id_value",
                )

                # Make the request
                operation = client.create_os_policy_assignment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.CreateOSPolicyAssignmentRequest, dict]):
                The request object. A request message to create an OS
                policy assignment
            parent (str):
                Required. The parent resource name in
                the form:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            os_policy_assignment (google.cloud.osconfig_v1.types.OSPolicyAssignment):
                Required. The OS policy assignment to
                be created.

                This corresponds to the ``os_policy_assignment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            os_policy_assignment_id (str):
                Required. The logical name of the OS policy assignment
                in the project with the following restrictions:

                - Must contain only lowercase letters, numbers, and
                  hyphens.
                - Must start with a letter.
                - Must be between 1-63 characters.
                - Must end with a number or a letter.
                - Must be unique within the project.

                This corresponds to the ``os_policy_assignment_id`` field
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

                The result type for the operation will be :class:`google.cloud.osconfig_v1.types.OSPolicyAssignment` OS policy assignment is an API resource that is used to
                   apply a set of OS policies to a dynamically targeted
                   group of Compute Engine VM instances.

                   An OS policy is used to define the desired state
                   configuration for a Compute Engine VM instance
                   through a set of configuration resources that provide
                   capabilities such as installing or removing software
                   packages, or executing a script.

                   For more information, see [OS policy and OS policy
                   assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, os_policy_assignment, os_policy_assignment_id]
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
            request, os_policy_assignments.CreateOSPolicyAssignmentRequest
        ):
            request = os_policy_assignments.CreateOSPolicyAssignmentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if os_policy_assignment is not None:
                request.os_policy_assignment = os_policy_assignment
            if os_policy_assignment_id is not None:
                request.os_policy_assignment_id = os_policy_assignment_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_os_policy_assignment
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
            os_policy_assignments.OSPolicyAssignment,
            metadata_type=os_policy_assignments.OSPolicyAssignmentOperationMetadata,
        )

        # Done; return the response.
        return response

    def update_os_policy_assignment(
        self,
        request: Optional[
            Union[os_policy_assignments.UpdateOSPolicyAssignmentRequest, dict]
        ] = None,
        *,
        os_policy_assignment: Optional[os_policy_assignments.OSPolicyAssignment] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Update an existing OS policy assignment.

        This method creates a new revision of the OS policy assignment.

        This method returns a long running operation (LRO) that contains
        the rollout details. The rollout can be cancelled by cancelling
        the LRO.

        For more information, see `Method:
        projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_update_os_policy_assignment():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                os_policy_assignment = osconfig_v1.OSPolicyAssignment()
                os_policy_assignment.os_policies.id = "id_value"
                os_policy_assignment.os_policies.mode = "ENFORCEMENT"
                os_policy_assignment.os_policies.resource_groups.resources.pkg.apt.name = "name_value"
                os_policy_assignment.os_policies.resource_groups.resources.pkg.desired_state = "REMOVED"
                os_policy_assignment.os_policies.resource_groups.resources.id = "id_value"
                os_policy_assignment.rollout.disruption_budget.fixed = 528

                request = osconfig_v1.UpdateOSPolicyAssignmentRequest(
                    os_policy_assignment=os_policy_assignment,
                )

                # Make the request
                operation = client.update_os_policy_assignment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.UpdateOSPolicyAssignmentRequest, dict]):
                The request object. A request message to update an OS
                policy assignment
            os_policy_assignment (google.cloud.osconfig_v1.types.OSPolicyAssignment):
                Required. The updated OS policy
                assignment.

                This corresponds to the ``os_policy_assignment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Field mask that controls
                which fields of the assignment should be
                updated.

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

                The result type for the operation will be :class:`google.cloud.osconfig_v1.types.OSPolicyAssignment` OS policy assignment is an API resource that is used to
                   apply a set of OS policies to a dynamically targeted
                   group of Compute Engine VM instances.

                   An OS policy is used to define the desired state
                   configuration for a Compute Engine VM instance
                   through a set of configuration resources that provide
                   capabilities such as installing or removing software
                   packages, or executing a script.

                   For more information, see [OS policy and OS policy
                   assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [os_policy_assignment, update_mask]
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
            request, os_policy_assignments.UpdateOSPolicyAssignmentRequest
        ):
            request = os_policy_assignments.UpdateOSPolicyAssignmentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if os_policy_assignment is not None:
                request.os_policy_assignment = os_policy_assignment
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_os_policy_assignment
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("os_policy_assignment.name", request.os_policy_assignment.name),)
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
            os_policy_assignments.OSPolicyAssignment,
            metadata_type=os_policy_assignments.OSPolicyAssignmentOperationMetadata,
        )

        # Done; return the response.
        return response

    def get_os_policy_assignment(
        self,
        request: Optional[
            Union[os_policy_assignments.GetOSPolicyAssignmentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> os_policy_assignments.OSPolicyAssignment:
        r"""Retrieve an existing OS policy assignment.

        This method always returns the latest revision. In order to
        retrieve a previous revision of the assignment, also provide the
        revision ID in the ``name`` parameter.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_get_os_policy_assignment():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.GetOSPolicyAssignmentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_os_policy_assignment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.GetOSPolicyAssignmentRequest, dict]):
                The request object. A request message to get an OS policy
                assignment
            name (str):
                Required. The resource name of OS policy assignment.

                Format:
                ``projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}``

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
            google.cloud.osconfig_v1.types.OSPolicyAssignment:
                OS policy assignment is an API resource that is used to
                   apply a set of OS policies to a dynamically targeted
                   group of Compute Engine VM instances.

                   An OS policy is used to define the desired state
                   configuration for a Compute Engine VM instance
                   through a set of configuration resources that provide
                   capabilities such as installing or removing software
                   packages, or executing a script.

                   For more information, see [OS policy and OS policy
                   assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).

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
        if not isinstance(request, os_policy_assignments.GetOSPolicyAssignmentRequest):
            request = os_policy_assignments.GetOSPolicyAssignmentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_os_policy_assignment]

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

    def list_os_policy_assignments(
        self,
        request: Optional[
            Union[os_policy_assignments.ListOSPolicyAssignmentsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOSPolicyAssignmentsPager:
        r"""List the OS policy assignments under the parent
        resource.
        For each OS policy assignment, the latest revision is
        returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_list_os_policy_assignments():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.ListOSPolicyAssignmentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_os_policy_assignments(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsRequest, dict]):
                The request object. A request message to list OS policy
                assignments for a parent resource
            parent (str):
                Required. The parent resource name.
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
            google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentsPager:
                A response message for listing all
                assignments under given parent.
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
            request, os_policy_assignments.ListOSPolicyAssignmentsRequest
        ):
            request = os_policy_assignments.ListOSPolicyAssignmentsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_os_policy_assignments
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
        response = pagers.ListOSPolicyAssignmentsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_os_policy_assignment_revisions(
        self,
        request: Optional[
            Union[os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOSPolicyAssignmentRevisionsPager:
        r"""List the OS policy assignment revisions for a given
        OS policy assignment.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_list_os_policy_assignment_revisions():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.ListOSPolicyAssignmentRevisionsRequest(
                    name="name_value",
                )

                # Make the request
                page_result = client.list_os_policy_assignment_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsRequest, dict]):
                The request object. A request message to list revisions
                for a OS policy assignment
            name (str):
                Required. The name of the OS policy
                assignment to list revisions for.

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
            google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentRevisionsPager:
                A response message for listing all
                revisions for a OS policy assignment.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

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
            request, os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest
        ):
            request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_os_policy_assignment_revisions
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

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListOSPolicyAssignmentRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_os_policy_assignment(
        self,
        request: Optional[
            Union[os_policy_assignments.DeleteOSPolicyAssignmentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Delete the OS policy assignment.

        This method creates a new revision of the OS policy assignment.

        This method returns a long running operation (LRO) that contains
        the rollout details. The rollout can be cancelled by cancelling
        the LRO.

        If the LRO completes and is not cancelled, all revisions
        associated with the OS policy assignment are deleted.

        For more information, see `Method:
        projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_delete_os_policy_assignment():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.DeleteOSPolicyAssignmentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_os_policy_assignment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.DeleteOSPolicyAssignmentRequest, dict]):
                The request object. A request message for deleting a OS
                policy assignment.
            name (str):
                Required. The name of the OS policy
                assignment to be deleted

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
            request, os_policy_assignments.DeleteOSPolicyAssignmentRequest
        ):
            request = os_policy_assignments.DeleteOSPolicyAssignmentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_os_policy_assignment
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
            metadata_type=os_policy_assignments.OSPolicyAssignmentOperationMetadata,
        )

        # Done; return the response.
        return response

    def get_os_policy_assignment_report(
        self,
        request: Optional[
            Union[os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> os_policy_assignment_reports.OSPolicyAssignmentReport:
        r"""Get the OS policy asssignment report for the
        specified Compute Engine VM instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_get_os_policy_assignment_report():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.GetOSPolicyAssignmentReportRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_os_policy_assignment_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.GetOSPolicyAssignmentReportRequest, dict]):
                The request object. Get a report of the OS policy
                assignment for a VM instance.
            name (str):
                Required. API resource name for OS policy assignment
                report.

                Format:
                ``/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report``

                For ``{project}``, either ``project-number`` or
                ``project-id`` can be provided. For ``{instance_id}``,
                either Compute Engine ``instance-id`` or
                ``instance-name`` can be provided. For
                ``{assignment_id}``, the OSPolicyAssignment id must be
                provided.

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
            google.cloud.osconfig_v1.types.OSPolicyAssignmentReport:
                A report of the OS policy assignment
                status for a given instance.

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
            request, os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest
        ):
            request = os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_os_policy_assignment_report
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

    def list_os_policy_assignment_reports(
        self,
        request: Optional[
            Union[
                os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOSPolicyAssignmentReportsPager:
        r"""List OS policy asssignment reports for all Compute
        Engine VM instances in the specified zone.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_list_os_policy_assignment_reports():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.ListOSPolicyAssignmentReportsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_os_policy_assignment_reports(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsRequest, dict]):
                The request object. List the OS policy assignment reports
                for VM instances.
            parent (str):
                Required. The parent resource name.

                Format:
                ``projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports``

                For ``{project}``, either ``project-number`` or
                ``project-id`` can be provided. For ``{instance}``,
                either ``instance-name``, ``instance-id``, or ``-`` can
                be provided. If '-' is provided, the response will
                include OSPolicyAssignmentReports for all instances in
                the project/location. For ``{assignment}``, either
                ``assignment-id`` or ``-`` can be provided. If '-' is
                provided, the response will include
                OSPolicyAssignmentReports for all OSPolicyAssignments in
                the project/location. Either {instance} or {assignment}
                must be ``-``.

                For example:
                ``projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports``
                returns all reports for the instance
                ``projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports``
                returns all the reports for the given assignment across
                all instances.
                ``projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports``
                returns all the reports for all assignments across all
                instances.

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
            google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentReportsPager:
                A response message for listing OS
                Policy assignment reports including the
                page of results and page token.

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
            request, os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest
        ):
            request = os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_os_policy_assignment_reports
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
        response = pagers.ListOSPolicyAssignmentReportsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_inventory(
        self,
        request: Optional[Union[inventory.GetInventoryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> inventory.Inventory:
        r"""Get inventory data for the specified VM instance. If the VM has
        no associated inventory, the message ``NOT_FOUND`` is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_get_inventory():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.GetInventoryRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_inventory(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.GetInventoryRequest, dict]):
                The request object. A request message for getting
                inventory data for the specified VM.
            name (str):
                Required. API resource name for inventory resource.

                Format:
                ``projects/{project}/locations/{location}/instances/{instance}/inventory``

                For ``{project}``, either ``project-number`` or
                ``project-id`` can be provided. For ``{instance}``,
                either Compute Engine ``instance-id`` or
                ``instance-name`` can be provided.

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
            google.cloud.osconfig_v1.types.Inventory:
                This API resource represents the available inventory data for a
                   Compute Engine virtual machine (VM) instance at a
                   given point in time.

                   You can use this API resource to determine the
                   inventory data of your VM.

                   For more information, see [Information provided by OS
                   inventory
                   management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).

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
        if not isinstance(request, inventory.GetInventoryRequest):
            request = inventory.GetInventoryRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_inventory]

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

    def list_inventories(
        self,
        request: Optional[Union[inventory.ListInventoriesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListInventoriesPager:
        r"""List inventory data for all VM instances in the
        specified zone.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_list_inventories():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.ListInventoriesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_inventories(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.ListInventoriesRequest, dict]):
                The request object. A request message for listing
                inventory data for all VMs in the
                specified location.
            parent (str):
                Required. The parent resource name.

                Format:
                ``projects/{project}/locations/{location}/instances/-``

                For ``{project}``, either ``project-number`` or
                ``project-id`` can be provided.

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
            google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListInventoriesPager:
                A response message for listing
                inventory data for all VMs in a
                specified location.

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
        if not isinstance(request, inventory.ListInventoriesRequest):
            request = inventory.ListInventoriesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_inventories]

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
        response = pagers.ListInventoriesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_vulnerability_report(
        self,
        request: Optional[
            Union[vulnerability.GetVulnerabilityReportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vulnerability.VulnerabilityReport:
        r"""Gets the vulnerability report for the specified VM
        instance. Only VMs with inventory data have
        vulnerability reports associated with them.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_get_vulnerability_report():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.GetVulnerabilityReportRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_vulnerability_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.GetVulnerabilityReportRequest, dict]):
                The request object. A request message for getting the
                vulnerability report for the specified
                VM.
            name (str):
                Required. API resource name for vulnerability resource.

                Format:
                ``projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport``

                For ``{project}``, either ``project-number`` or
                ``project-id`` can be provided. For ``{instance}``,
                either Compute Engine ``instance-id`` or
                ``instance-name`` can be provided.

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
            google.cloud.osconfig_v1.types.VulnerabilityReport:
                This API resource represents the vulnerability report for a specified
                   Compute Engine virtual machine (VM) instance at a
                   given point in time.

                   For more information, see [Vulnerability
                   reports](https://cloud.google.com/compute/docs/instances/os-inventory-management#vulnerability-reports).

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
        if not isinstance(request, vulnerability.GetVulnerabilityReportRequest):
            request = vulnerability.GetVulnerabilityReportRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_vulnerability_report]

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

    def list_vulnerability_reports(
        self,
        request: Optional[
            Union[vulnerability.ListVulnerabilityReportsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListVulnerabilityReportsPager:
        r"""List vulnerability reports for all VM instances in
        the specified zone.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import osconfig_v1

            def sample_list_vulnerability_reports():
                # Create a client
                client = osconfig_v1.OsConfigZonalServiceClient()

                # Initialize request argument(s)
                request = osconfig_v1.ListVulnerabilityReportsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_vulnerability_reports(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.osconfig_v1.types.ListVulnerabilityReportsRequest, dict]):
                The request object. A request message for listing
                vulnerability reports for all VM
                instances in the specified location.
            parent (str):
                Required. The parent resource name.

                Format:
                ``projects/{project}/locations/{location}/instances/-``

                For ``{project}``, either ``project-number`` or
                ``project-id`` can be provided.

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
            google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListVulnerabilityReportsPager:
                A response message for listing
                vulnerability reports for all VM
                instances in the specified location.

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
        if not isinstance(request, vulnerability.ListVulnerabilityReportsRequest):
            request = vulnerability.ListVulnerabilityReportsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_vulnerability_reports
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
        response = pagers.ListVulnerabilityReportsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "OsConfigZonalServiceClient":
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

__all__ = ("OsConfigZonalServiceClient",)
