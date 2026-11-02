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

from google.cloud.auditmanager_v1 import gapic_version as package_version
from google.cloud.auditmanager_v1._compat import (
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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.auditmanager_v1.services.audit_manager import pagers
from google.cloud.auditmanager_v1.types import auditmanager

from .transports.base import DEFAULT_CLIENT_INFO, AuditManagerTransport
from .transports.grpc import AuditManagerGrpcTransport
from .transports.grpc_asyncio import AuditManagerGrpcAsyncIOTransport
from .transports.rest import AuditManagerRestTransport


class AuditManagerClientMeta(type):
    """Metaclass for the AuditManager client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[AuditManagerTransport]]
    _transport_registry["grpc"] = AuditManagerGrpcTransport
    _transport_registry["grpc_asyncio"] = AuditManagerGrpcAsyncIOTransport
    _transport_registry["rest"] = AuditManagerRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[AuditManagerTransport]:
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


class AuditManagerClient(metaclass=AuditManagerClientMeta):
    """Service describing handlers for resources"""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "auditmanager.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "auditmanager.{UNIVERSE_DOMAIN}"
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
            AuditManagerClient: The constructed client.
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
            AuditManagerClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> AuditManagerTransport:
        """Returns the transport used by the client instance.

        Returns:
            AuditManagerTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def audit_report_path(
        project: str,
        location: str,
        audit_report: str,
    ) -> str:
        """Returns a fully-qualified audit_report string."""
        return "projects/{project}/locations/{location}/auditReports/{audit_report}".format(
            project=project,
            location=location,
            audit_report=audit_report,
        )

    @staticmethod
    def parse_audit_report_path(path: str) -> Dict[str, str]:
        """Parses a audit_report path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/auditReports/(?P<audit_report>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def audit_schedule_path(
        project: str,
        location: str,
        audit_schedule: str,
    ) -> str:
        """Returns a fully-qualified audit_schedule string."""
        return "projects/{project}/locations/{location}/auditSchedules/{audit_schedule}".format(
            project=project,
            location=location,
            audit_schedule=audit_schedule,
        )

    @staticmethod
    def parse_audit_schedule_path(path: str) -> Dict[str, str]:
        """Parses a audit_schedule path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/auditSchedules/(?P<audit_schedule>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def audit_scope_report_path(
        project: str,
        location: str,
        audit_scope_report: str,
    ) -> str:
        """Returns a fully-qualified audit_scope_report string."""
        return "projects/{project}/locations/{location}/auditScopeReports/{audit_scope_report}".format(
            project=project,
            location=location,
            audit_scope_report=audit_scope_report,
        )

    @staticmethod
    def parse_audit_scope_report_path(path: str) -> Dict[str, str]:
        """Parses a audit_scope_report path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/auditScopeReports/(?P<audit_scope_report>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def enrollment_path(
        project: str,
        location: str,
        enrollment: str,
    ) -> str:
        """Returns a fully-qualified enrollment string."""
        return (
            "projects/{project}/locations/{location}/enrollments/{enrollment}".format(
                project=project,
                location=location,
                enrollment=enrollment,
            )
        )

    @staticmethod
    def parse_enrollment_path(path: str) -> Dict[str, str]:
        """Parses a enrollment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/enrollments/(?P<enrollment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def enrollment_status_scope_path(
        folder: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified enrollment_status_scope string."""
        return "folders/{folder}/locations/{location}".format(
            folder=folder,
            location=location,
        )

    @staticmethod
    def parse_enrollment_status_scope_path(path: str) -> Dict[str, str]:
        """Parses a enrollment_status_scope path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def resource_enrollment_status_path(
        folder: str,
        location: str,
        resource_enrollment_status: str,
    ) -> str:
        """Returns a fully-qualified resource_enrollment_status string."""
        return "folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}".format(
            folder=folder,
            location=location,
            resource_enrollment_status=resource_enrollment_status,
        )

    @staticmethod
    def parse_resource_enrollment_status_path(path: str) -> Dict[str, str]:
        """Parses a resource_enrollment_status path into its component segments."""
        m = re.match(
            r"^folders/(?P<folder>.+?)/locations/(?P<location>.+?)/resourceEnrollmentStatuses/(?P<resource_enrollment_status>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def standard_path(
        project: str,
        location: str,
        standard: str,
    ) -> str:
        """Returns a fully-qualified standard string."""
        return "projects/{project}/locations/{location}/standards/{standard}".format(
            project=project,
            location=location,
            standard=standard,
        )

    @staticmethod
    def parse_standard_path(path: str) -> Dict[str, str]:
        """Parses a standard path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/standards/(?P<standard>.+?)$",
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
            Union[str, AuditManagerTransport, Callable[..., AuditManagerTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the audit manager client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AuditManagerTransport,Callable[..., AuditManagerTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AuditManagerTransport constructor.
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
        self._client_cert_source = AuditManagerClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=AuditManagerClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, AuditManagerTransport)
        if transport_provided:
            # transport is a AuditManagerTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(AuditManagerTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=AuditManagerClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=AuditManagerClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=AuditManagerClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[AuditManagerTransport], Callable[..., AuditManagerTransport]
            ] = (
                AuditManagerClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., AuditManagerTransport], transport)
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
                    "Created client `google.cloud.auditmanager_v1.AuditManagerClient`.",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
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
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "credentialsType": None,
                    },
                )

    def create_audit_schedule(
        self,
        request: Optional[Union[auditmanager.CreateAuditScheduleRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        audit_schedule: Optional[auditmanager.AuditSchedule] = None,
        audit_schedule_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditSchedule:
        r"""Creates a new audit schedule in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_create_audit_schedule():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                audit_schedule = auditmanager_v1.AuditSchedule()
                audit_schedule.gcs_uri = "gcs_uri_value"
                audit_schedule.compliance_framework = "compliance_framework_value"
                audit_schedule.report_format = "AUDIT_REPORT_FORMAT_ODF"
                audit_schedule.schedule_config.frequency = "ANNUALLY"

                request = auditmanager_v1.CreateAuditScheduleRequest(
                    parent="parent_value",
                    audit_schedule=audit_schedule,
                    audit_schedule_id="audit_schedule_id_value",
                )

                # Make the request
                response = client.create_audit_schedule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.CreateAuditScheduleRequest, dict]):
                The request object. Request message for
                [CreateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.CreateAuditSchedule].
            parent (str):
                Required. Project or folder that this audit schedule is
                for, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audit_schedule (google.cloud.auditmanager_v1.types.AuditSchedule):
                Required. Audit schedule to create.
                This corresponds to the ``audit_schedule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audit_schedule_id (str):
                Required. ID to use for the audit
                schedule, which becomes the final
                component of the audit schedule's
                resource name.

                This corresponds to the ``audit_schedule_id`` field
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
            google.cloud.auditmanager_v1.types.AuditSchedule:
                An audit schedule, in one of the following formats:

                   - projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
                   - folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, audit_schedule, audit_schedule_id]
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
        if not isinstance(request, auditmanager.CreateAuditScheduleRequest):
            request = auditmanager.CreateAuditScheduleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if audit_schedule is not None:
                request.audit_schedule = audit_schedule
            if audit_schedule_id is not None:
                request.audit_schedule_id = audit_schedule_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_audit_schedule]

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

    def update_audit_schedule(
        self,
        request: Optional[Union[auditmanager.UpdateAuditScheduleRequest, dict]] = None,
        *,
        audit_schedule: Optional[auditmanager.AuditSchedule] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditSchedule:
        r"""Updates an existing audit schedule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_update_audit_schedule():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                audit_schedule = auditmanager_v1.AuditSchedule()
                audit_schedule.gcs_uri = "gcs_uri_value"
                audit_schedule.compliance_framework = "compliance_framework_value"
                audit_schedule.report_format = "AUDIT_REPORT_FORMAT_ODF"
                audit_schedule.schedule_config.frequency = "ANNUALLY"

                request = auditmanager_v1.UpdateAuditScheduleRequest(
                    audit_schedule=audit_schedule,
                )

                # Make the request
                response = client.update_audit_schedule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.UpdateAuditScheduleRequest, dict]):
                The request object. Request message for
                [UpdateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.UpdateAuditSchedule].
            audit_schedule (google.cloud.auditmanager_v1.types.AuditSchedule):
                Required. Audit schedule to update.
                This corresponds to the ``audit_schedule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. List of fields to update.
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
            google.cloud.auditmanager_v1.types.AuditSchedule:
                An audit schedule, in one of the following formats:

                   - projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
                   - folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [audit_schedule, update_mask]
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
        if not isinstance(request, auditmanager.UpdateAuditScheduleRequest):
            request = auditmanager.UpdateAuditScheduleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if audit_schedule is not None:
                request.audit_schedule = audit_schedule
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_audit_schedule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("audit_schedule.name", request.audit_schedule.name),)
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

    def get_audit_schedule(
        self,
        request: Optional[Union[auditmanager.GetAuditScheduleRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditSchedule:
        r"""Gets details of a single audit schedule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_get_audit_schedule():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GetAuditScheduleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_audit_schedule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.GetAuditScheduleRequest, dict]):
                The request object. Request message for
                [GetAuditSchedule][google.cloud.auditmanager.v1.AuditManager.GetAuditSchedule].
            name (str):
                Required. Name of the audit schedule to retrieve, in one
                of the following formats:

                - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule}``

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
            google.cloud.auditmanager_v1.types.AuditSchedule:
                An audit schedule, in one of the following formats:

                   - projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
                   - folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}

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
        if not isinstance(request, auditmanager.GetAuditScheduleRequest):
            request = auditmanager.GetAuditScheduleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_audit_schedule]

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

    def list_audit_schedules(
        self,
        request: Optional[Union[auditmanager.ListAuditSchedulesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuditSchedulesPager:
        r"""Lists audit schedules in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_list_audit_schedules():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListAuditSchedulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audit_schedules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.ListAuditSchedulesRequest, dict]):
                The request object. Request message for
                [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].
            parent (str):
                Required. Parent for the audit schedule, in one of the
                following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

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
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListAuditSchedulesPager:
                Response message for
                   [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].

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
        if not isinstance(request, auditmanager.ListAuditSchedulesRequest):
            request = auditmanager.ListAuditSchedulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_audit_schedules]

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
        response = pagers.ListAuditSchedulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def enroll_resource(
        self,
        request: Optional[Union[auditmanager.EnrollResourceRequest, dict]] = None,
        *,
        scope: Optional[str] = None,
        destinations: Optional[
            MutableSequence[auditmanager.EnrollResourceRequest.EligibleDestination]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.Enrollment:
        r"""Adds your project, folder, or organization to Audit
        Manager. This method creates the Audit Manager service
        agent in your workload and grants required permissions
        to the service agent. If you make this request on a
        workload that's already enrolled, then this method
        overrides the existing set of destinations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_enroll_resource():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                destinations = auditmanager_v1.EligibleDestination()
                destinations.eligible_gcs_bucket = "eligible_gcs_bucket_value"

                request = auditmanager_v1.EnrollResourceRequest(
                    scope="scope_value",
                    destinations=destinations,
                )

                # Make the request
                response = client.enroll_resource(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.EnrollResourceRequest, dict]):
                The request object. Request message for
                [EnrollResource][google.cloud.auditmanager.v1.AuditManager.EnrollResource].
            scope (str):
                Required. Organization, folder, or project to enroll in
                Audit Manager, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            destinations (MutableSequence[google.cloud.auditmanager_v1.types.EnrollResourceRequest.EligibleDestination]):
                Required. Cloud Storage buckets that
                you can upload your audit reports to
                during the audit process.

                When you enroll an organization or
                folder, you can choose a Cloud Storage
                bucket from any project in the
                organization or folder. If you run an
                audit at the project level using the
                service agent at the organization or
                folder level, all the buckets that are
                associated with the service agent are
                available.

                This corresponds to the ``destinations`` field
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
            google.cloud.auditmanager_v1.types.Enrollment:
                Organization, folder, or project to
                enroll for audit reports.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, destinations]
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
        if not isinstance(request, auditmanager.EnrollResourceRequest):
            request = auditmanager.EnrollResourceRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if scope is not None:
                request.scope = scope
            if destinations is not None:
                request.destinations = destinations

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.enroll_resource]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
        )

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

    def generate_audit_scope_report(
        self,
        request: Optional[
            Union[auditmanager.GenerateAuditScopeReportRequest, dict]
        ] = None,
        *,
        scope: Optional[str] = None,
        compliance_standard: Optional[str] = None,
        report_format: Optional[
            auditmanager.GenerateAuditScopeReportRequest.AuditScopeReportFormat
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditScopeReport:
        r"""Generates an audit scope report for the given standard.

        The report includes the following:

        - The technical attributes and constraints that Audit Manager
          uses to verify your compliance with a framework.
        - A list of Google Cloud services and resources that are within
          the scope of the framework.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_generate_audit_scope_report():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GenerateAuditScopeReportRequest(
                    scope="scope_value",
                    report_format="AUDIT_SCOPE_REPORT_FORMAT_ODF",
                    compliance_framework="compliance_framework_value",
                )

                # Make the request
                response = client.generate_audit_scope_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.GenerateAuditScopeReportRequest, dict]):
                The request object. Request message for
                [GenerateAuditScopeReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport].
            scope (str):
                Required. Project or folder that the audit scope report
                is generated for, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            compliance_standard (str):
                Optional. Deprecated. The standard (industry or
                regulatory requirements) that the audit scope report is
                run against.

                Use the ``compliance_framework`` field instead.

                This corresponds to the ``compliance_standard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            report_format (google.cloud.auditmanager_v1.types.GenerateAuditScopeReportRequest.AuditScopeReportFormat):
                Required. Format for the audit scope
                report.

                This corresponds to the ``report_format`` field
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
            google.cloud.auditmanager_v1.types.AuditScopeReport:
                Audit scope report.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, compliance_standard, report_format]
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
        if not isinstance(request, auditmanager.GenerateAuditScopeReportRequest):
            request = auditmanager.GenerateAuditScopeReportRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if scope is not None:
                request.scope = scope
            if compliance_standard is not None:
                request.compliance_standard = compliance_standard
            if report_format is not None:
                request.report_format = report_format

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_audit_scope_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
        )

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

    def generate_audit_report(
        self,
        request: Optional[Union[auditmanager.GenerateAuditReportRequest, dict]] = None,
        *,
        scope: Optional[str] = None,
        gcs_uri: Optional[str] = None,
        compliance_standard: Optional[str] = None,
        report_format: Optional[
            auditmanager.GenerateAuditReportRequest.AuditReportFormat
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Registers audit report generation requests. This
        method returns the operation identifier that you can use
        to track the report generation progress.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_generate_audit_report():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GenerateAuditReportRequest(
                    gcs_uri="gcs_uri_value",
                    scope="scope_value",
                    report_format="AUDIT_REPORT_FORMAT_ODF",
                    compliance_framework="compliance_framework_value",
                )

                # Make the request
                operation = client.generate_audit_report(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.GenerateAuditReportRequest, dict]):
                The request object. Request message for
                [GenerateAuditReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport].
            scope (str):
                Required. Organization, folder, or project that the
                audit applies to, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gcs_uri (str):
                URL for the Cloud Storage bucket
                where the report and evidence is
                uploaded. You must select a bucket that
                was provided during the enrollment
                process.

                This corresponds to the ``gcs_uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            compliance_standard (str):
                Optional. Deprecated. Compliance standard for the audit
                report.

                Use the ``compliance_framework`` field instead.

                This corresponds to the ``compliance_standard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            report_format (google.cloud.auditmanager_v1.types.GenerateAuditReportRequest.AuditReportFormat):
                Required. Format for the audit
                report.

                This corresponds to the ``report_format`` field
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
                :class:`google.cloud.auditmanager_v1.types.AuditReport`
                An audit report.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, gcs_uri, compliance_standard, report_format]
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
        if not isinstance(request, auditmanager.GenerateAuditReportRequest):
            request = auditmanager.GenerateAuditReportRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if scope is not None:
                request.scope = scope
            if gcs_uri is not None:
                request.gcs_uri = gcs_uri
            if compliance_standard is not None:
                request.compliance_standard = compliance_standard
            if report_format is not None:
                request.report_format = report_format

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.generate_audit_report]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
        )

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
            auditmanager.AuditReport,
            metadata_type=auditmanager.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_audit_reports(
        self,
        request: Optional[Union[auditmanager.ListAuditReportsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuditReportsPager:
        r"""Lists the audit reports for the organization, folder,
        or project that you specify as the parent scope.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_list_audit_reports():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListAuditReportsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audit_reports(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.ListAuditReportsRequest, dict]):
                The request object. Request message for
                [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].
            parent (str):
                Required. Parent organization, folder, or project to
                list reports for, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

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
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListAuditReportsPager:
                Response message for
                   [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].

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
        if not isinstance(request, auditmanager.ListAuditReportsRequest):
            request = auditmanager.ListAuditReportsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_audit_reports]

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
        response = pagers.ListAuditReportsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_audit_report(
        self,
        request: Optional[Union[auditmanager.GetAuditReportRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditReport:
        r"""Gets the full metadata and findings for an audit
        report.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_get_audit_report():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GetAuditReportRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_audit_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.GetAuditReportRequest, dict]):
                The request object. Request message for
                [GetAuditReport][google.cloud.auditmanager.v1.AuditManager.GetAuditReport].
            name (str):
                Required. Name of the audit report, in one of the
                following formats:

                - ``projects/{project}/locations/{location}/auditReports/{audit_report}``
                - ``folders/{folder}/locations/{location}/auditReports/{audit_report}``
                - ``organizations/{organization}/locations/{location}/auditReports/{audit_report}``

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
            google.cloud.auditmanager_v1.types.AuditReport:
                An audit report.
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
        if not isinstance(request, auditmanager.GetAuditReportRequest):
            request = auditmanager.GetAuditReportRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_audit_report]

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

    def get_resource_enrollment_status(
        self,
        request: Optional[
            Union[auditmanager.GetResourceEnrollmentStatusRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.ResourceEnrollmentStatus:
        r"""Gets a resource and its enrollment status.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_get_resource_enrollment_status():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GetResourceEnrollmentStatusRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_resource_enrollment_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.GetResourceEnrollmentStatusRequest, dict]):
                The request object. Request message for
                [GetResourceEnrollmentStatus][google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus].
            name (str):
                Required. Name of the resource enrollment status, in one
                of the following formats:

                - ``folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
                - ``projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
                - ``organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``

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
            google.cloud.auditmanager_v1.types.ResourceEnrollmentStatus:
                An organization, folder, or project
                with its enrollment status.

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
        if not isinstance(request, auditmanager.GetResourceEnrollmentStatusRequest):
            request = auditmanager.GetResourceEnrollmentStatusRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_resource_enrollment_status
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

    def list_resource_enrollment_statuses(
        self,
        request: Optional[
            Union[auditmanager.ListResourceEnrollmentStatusesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListResourceEnrollmentStatusesPager:
        r"""Lists all the folders and projects in an organization
        or folder, along with their enrollments.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_list_resource_enrollment_statuses():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListResourceEnrollmentStatusesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_resource_enrollment_statuses(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesRequest, dict]):
                The request object. Request message for
                [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].
            parent (str):
                Required. Parent organization or folder to list
                enrollment statuses for, in one of the following
                formats:

                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

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
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListResourceEnrollmentStatusesPager:
                Response message for
                   [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].

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
        if not isinstance(request, auditmanager.ListResourceEnrollmentStatusesRequest):
            request = auditmanager.ListResourceEnrollmentStatusesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_resource_enrollment_statuses
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
        response = pagers.ListResourceEnrollmentStatusesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_controls(
        self,
        request: Optional[Union[auditmanager.ListControlsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListControlsPager:
        r"""Lists the controls that you must implement to become
        compliant to a regulatory standard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            def sample_list_controls():
                # Create a client
                client = auditmanager_v1.AuditManagerClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListControlsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_controls(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.auditmanager_v1.types.ListControlsRequest, dict]):
                The request object. Request message for
                [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].
            parent (str):
                Required. Standard to list controls for, in one of the
                following formats:

                - ``projects/{project}/locations/{location}/standards/{standard}``
                - ``folders/{folder}/locations/{location}/standards/{standard}``
                - ``organizations/{organization}/locations/{location}/standards/{standard}``

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
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListControlsPager:
                Response message for
                   [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].

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
        if not isinstance(request, auditmanager.ListControlsRequest):
            request = auditmanager.ListControlsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_controls]

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
        response = pagers.ListControlsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "AuditManagerClient":
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

__all__ = ("AuditManagerClient",)
